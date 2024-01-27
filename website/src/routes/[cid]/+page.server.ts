import type { PageServerLoad } from "./$types";

export const load = (async ({ params, fetch }) => {
    const res = await fetch(`https://ipfs.io/ipfs/${params.cid}`);
    if (!res.ok) throw new Error("Not found");

    return { test: await res.json() };
}) satisfies PageServerLoad;
