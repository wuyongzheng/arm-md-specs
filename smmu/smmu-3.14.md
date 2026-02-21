## 3.14 Speculative accesses

An implementation might allow incoming transactions to be marked as speculative in an IMPLEMENTATION DEFINED manner. Only read transactions are allowed to be marked as speculative. The behavior of a write transaction that is marked as speculative is always to terminate the transaction with an abort, and no event is recorded to software.

The behavior of a read transaction that is marked as speculative depends on two things:

1. If the translation occurs successfully without faulting, the read transaction continues into the system and returns data. Otherwise if any kind of fault or configuration error occurs, the transaction is terminated with an abort; no event is recorded to software for any speculative transaction. The determination of a fault is no different to non-speculative read transactions, including Access flag faults.
2. If HTTU is enabled and translation succeeds without fault, the read transaction updates the Access flags of relevant translation table descriptors.

The SMMU HTTU rules match those set out for Armv8.1-A [2], with respect to hardware update of Access flag and dirty state, including update of stage 2 translation table flags for both speculative accesses made at stage 1 and writes of stage 1 descriptors due to the setting of Access flags.

An implementation might provide translation services to a client device, and might support speculatively-issued Translation Requests. An IMPLEMENTATION DEFINED mechanism must be used to differentiate speculative Translation Requests from non-speculative Translation Requests.

Note: This mechanism might arise as an IMPLEMENTATION SPECIFIC service provided to another device. PCIe ATS Translation Requests are always non-speculative.

If a received Translation Request is marked as speculative, behavior is dependent on the read/write property of the request:

- Translation Requests for an address to be written grant write in the response only if the translation table descriptors that translate the address are all marked writable-dirty. In this case, if hardware management of the Access flag is enabled, the request updates AF. If hardware management of dirty state is enabled, speculative Write Translation Requests do not mark any writable-clean descriptor in the first or only stage of translation as writable-dirty. If the descriptor is marked writable-clean, the response does not grant write access.
- Translation Requests for an address to be read return a successful response, if appropriate, and if hardware management of the Access flag is enabled updates AF.
- In both cases, if hardware management of Access flag and dirty state is enabled in a nested translation then an update of a stage 1 descriptor to set AF or the Dirty state of the page might cause the stage 2 descriptors related to the updated stage 1 descriptor to be marked as Dirty as required.

The response to a Translation Request indicates whether a translation request was denied because of a page fault or otherwise missing translation, or whether a valid translation existed but the request failed because the translation was writable-clean.

Note: A device might use this information to determine whether to stop making requests or whether to subsequently try again with a non-speculative write.

For speculative accesses of SMMU structures and translations, see section 3.21.1 Translation tables and TLB invalidation completion behavior and 3.21.3 Configuration structures and configuration invalidation completion .