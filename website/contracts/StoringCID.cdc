pub contract StoringCID {
    pub resource CIDStorage {
        pub let cid: String

        init(cid: String) {
            self.cid = cid
        }
    }

    pub fun storeCID(cid: String): @CIDStorage {
        return <-create CIDStorage(cid: cid)
    }

    pub fun checkCID(addr: Address, cid: String): Bool {
        let path = PublicPath(identifier: cid)
        if path == nil {
            return false
        }

        let cidStorageRef = getAccount(addr).getCapability<&CIDStorage>(path!).borrow()
        let storedCid = cidStorageRef?.cid
        if storedCid == cid {
            return true
        } else {
            return false
        }
    }
}
