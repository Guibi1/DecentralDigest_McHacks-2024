import * as fcl from "@onflow/fcl";
import { writable } from "svelte/store";

fcl.config({
    "app.detail.icon": "https://decentral-digest-mc-hacks-2024.vercel.app/favicon.png",
    "app.detail.title": "Decentral Digest",
    "flow.network": "testnet",
    "accessNode.api": "https://access-testnet.onflow.org",
    "discovery.wallet": `https://fcl-discovery.onflow.org/testnet/authn`,
});

function createUser() {
    const user = writable({ loggedIn: null });

    fcl.currentUser.subscribe(user.set);

    async function markAsRead(cid: string) {
        const transaction = `
                import StoringCID from 0x914a57b9fb57ef33
                
                transaction {
                    prepare(acct: AuthAccount) {
                        acct.save(<-StoringCID.storeCID(cid: "${cid}"), to: /storage/${cid})
                        acct.link<&StoringCID.CIDStorage>(/public/${cid}, target: /storage/${cid})
                    }
                }
                `;

        const res = await fcl.send([
            fcl.transaction(transaction),
            fcl.payer(fcl.currentUser().authorization),
            fcl.proposer(fcl.currentUser().authorization),
            fcl.authorizations([fcl.currentUser().authorization]),
            fcl.limit(100),
        ]);
        await fcl.tx(res.transactionId).onceSealed();
    }

    async function getReadStatus(cid: string): Promise<boolean> {
        const { addr } = await fcl.currentUser.snapshot();
        if (!addr) return false;

        const script = `
            import StoringCID from 0x914a57b9fb57ef33

            pub fun main(): Bool {
                return StoringCID.checkCID(addr: ${addr}, cid: "${cid}")
            }
        `;

        return await fcl.query({ cadence: script });
    }

    return {
        ...user,
        markAsRead,
        getReadStatus,
        login: fcl.authenticate,
        logout: fcl.unauthenticate,
    };
}

export default createUser();
