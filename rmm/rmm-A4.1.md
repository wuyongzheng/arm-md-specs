## A4.1 Exception model overview

- DHCGWL A Realm entry is a transfer of control to a Realm.
- DRMGWJ A Realm exit is a transition of control from a Realm.
- ISMPWB When executing in a Realm, an exception taken to R-EL2 or EL3 results in a Realm exit.
- DXSNZP A REC entry is a Realm entry due to execution of RMI\_REC\_ENTER.

IFQZJG The Host provides the address of a REC as an input to the RMI\_REC\_ENTER command.

- IMDQWG In this chapter, both rec and 'the target REC' refer to the REC object which is provided to the RMI\_REC\_ENTER command.

DBLJGY A RecRun object is a data structure used to pass values between the RMM and the Host on REC entry and on REC exit.

- IVCCFV A RecRun object is stored in Non-secure memory.
- IWBHYZ The Host provides the address of a RecRun object as an input to the RMI\_REC\_ENTER command.

IHMSQM An implementation is permitted to return RMI\_SUCCESS from RMI\_REC\_ENTER without performing a REC entry. For example, on observing a pending interrupt, the implementation can generate a REC exit due to IRQ without entering the target REC.

DTJCGH A REC exit is return from an execution of RMI\_REC\_ENTER which caused a REC entry.

IHPWVY The following diagram summarises the possible control flows that result from a Realm exit.

Figure A4.1: Realm exit paths

<!-- image -->

- a. The exception is taken to EL3. The Monitor handles the exception and returns control to the Realm.
- b. The exception is taken to EL3. The Monitor pre-empts Realm Security state and passes control to the Secure Security state. This may be for example due to an FIQ.
- c. The exception is taken to EL2. The RMM decides to perform a REC exit. The RMM executes an SMC instruction, requesting the Monitor to pass control to the Non-secure Security state.
- d. The exception is taken to EL2. The RMM executes an SMC instruction, requesting the Monitor to perform an operation, then returns control to the Realm.
- e. The exception is taken to EL2. The RMM handles the exception and returns control to the Realm.

Chapter A4. Realm exception model

See also:

- A4.2 REC entry
- A4.3 REC exit
- B4.3.14 RMI\_REC\_ENTER command
- B4.4.20 RmiRecRun type