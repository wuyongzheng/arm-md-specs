## D7.8 Pseudocode description of general memory System instructions

This section lists the pseudocode describing general memory operations:

- Memory data type definitions.
- Basic memory access.
- Aligned memory access.
- Unaligned memory access.
- Exclusives monitors operations.
- Access permission checking.
- Abort exceptions.
- Memory barriers.

## D7.8.1 Memory data type definitions

This section lists the memory data types.

The memory data types are:

- Address descriptor, defined by the AddressDescriptor type.
- Full address, defined by the FullAddress type.
- Memory attributes, defined by the MemoryAttributes type.
- Memory type, defined by the MemType enumeration.
- Device memory type, defined by the DeviceType enumeration.
- Normal memory attributes, defined by the MemAttrHints type.
- Cacheability attributes, defined by the MemAttr\_NC , MemAttr\_WT , and MemAttr\_WB constants.
- Allocation hints, defined by the MemHint\_No , MemHint\_WA , MemHint\_RA , and MemHint\_RWA constants.
- Access permissions, defined by the Permissions type.

These types are defined in A-profile Architecture Pseudocode.

## D7.8.2 Basic memory access

The PhysMemRead() and PhysMemWrite() functions perform single-copy atomic, aligned, little-endian memory accesses of size bytes to or from the underlying physical memory array of bytes.

The attributes in memaddrdesc.memattrs are used by the memory system to determine caching and ordering behaviors as described in Memory types and attributes, Ordering relations, and Atomicity in the Arm architecture.

## D7.8.3 Aligned memory access

The two MemSingle[] accessors, non-assignment (memory read) AArch64.MemSingle[] and assignment (memory write) AArch64.MemSingle[], make atomic, little-endian accesses of size bytes.

## D7.8.4 Unaligned memory access

The two Mem[] accessors, Non-assignment (memory read) Mem[] and Assignment (memory write) Mem[] , make accesses of the required type. If an access is not architecturally defined to be atomic, Mem[] synthesizes accesses from multiple calls to AArch64.MemSingle[] . It also reverses the byte order if the access is big-endian.

The IsAligned() function checks the alignment of memory accesses.

## D7.8.5 Exclusives monitors operations

The AArch64.SetExclusiveMonitors() function sets the Exclusives monitors for a block of bytes, the size of which is determined by size , at the virtual address defined by address .

The AArch64.ExclusiveMonitorsPass() function checks whether the Exclusives monitors are set to include the location of a number of bytes specified by size , at the virtual address defined by address . The atomic write that follows after the Exclusives monitors have been set must be to the same physical address. It is permitted, but not required, for this function to return FALSE if the virtual address is not the same as that used in the previous call to AArch64.SetExclusiveMonitors() .

The ExclusiveMonitorsStatus() function returns 0 if the previous atomic write was to the same physical memory locations selected by AArch64.ExclusiveMonitorsPass() and therefore succeeded. Otherwise the function returns 1, indicating that the address translation delivered a different physical address.

The MarkExclusiveGlobal() procedure takes as arguments a FullAddress paddress , the PE identifier processorid and the size of the transfer. The procedure records that the PE processorid has requested exclusive access covering at least size bytes from address paddress . The size of the location marked as exclusive is IMPLEMENTATION DEFINED, up to a limit of 2KB and no smaller than two words, and aligned in the address space to the size of the location. It is CONSTRAINED UNPREDICTABLE whether this causes any previous request for exclusive access to any other address by the same PE to be cleared.

The MarkExclusiveLocal() procedure takes as arguments a FullAddress paddress , the PE identifier processorid and the size of the transfer. The procedure records in a local record that PE processorid has requested exclusive access to an address covering at least size bytes from address paddress. The size of the location marked as exclusive is IMPLEMENTATION DEFINED, and can at its largest cover the whole of memory but is no smaller than two words, and is aligned in the address space to the size of the location. It is IMPLEMENTATION DEFINED whether this procedure also performs a MarkExclusiveGlobal() using the same parameters.

The IsExclusiveGlobal() function takes as arguments a FullAddress paddress , the PE identifier processorid and the size of the transfer. The function returns TRUE if the PE processorid has marked in a global record an address range as exclusive access requested that covers at least size bytes from address paddress . It is IMPLEMENTATION DEFINED whether it returns TRUE or FALSE if a global record has marked a different address as exclusive access requested. If no address is marked in a global record as exclusive access, IsExclusiveGlobal() returns FALSE.

The IsExclusiveLocal() function takes as arguments a FullAddress paddress , the PE identifier processorid and the size of the transfer. The function returns TRUE if the PE processorid has marked an address range as exclusive access requested that covers at least the size bytes from address paddress . It is IMPLEMENTATION DEFINED whether this function returns TRUE or FALSE if the address marked as exclusive access requested does not cover all of size bytes from address paddress . If no address is marked as exclusive access requested, then this function returns FALSE. It is IMPLEMENTATION DEFINED whether this result is ANDed with the result of IsExclusiveGlobal() with the same parameters.

The ClearExclusiveByAddress() procedure takes as arguments a FullAddress paddress , the PE identifier processorid and the size of the transfer. The procedure clears the global records of all PEs, other than processorid , for which an address region including any of size bytes starting from paddress has had a request for an exclusive access. It is IMPLEMENTATION DEFINED whether the equivalent global record of the PE processorid is also cleared if any of size bytes starting from paddress has had a request for an exclusive access, or if any other address has had a request for an exclusive access.

The ClearExclusiveLocal() procedure takes as arguments the PE identifier processorid . The procedure clears the local record of PE processorid for which an address has had a request for an exclusive access. It is IMPLEMENTATION DEFINED whether this operation also clears the global record of PE processorid that an address has had a request for an exclusive access.

## D7.8.6 Access permission checking

The AArch64.S1CheckPermissions () and AArch64.S2CheckPermissions () functions are used by the architecture to perform access permission checking based on attributes derived from the Translation Tables descriptors.

The interpretation of access permission is shown in Memory access control.

## D7.8.7 Abort exceptions

The AArch64.Abort() function generates either a Data Abort or an Instruction Abort exception by calling AArch64.DataAbort() or AArch64.InstructionAbort() . It also can generate a debug exception for debug

related faults, see AArch64 Self-hosted Debug.

The AArch64.DataAbort() function generates a Data Abort exception, routes the exception to EL2 or EL3, and records the information required for the Exception Syndrome registers, ESR\_ELx. See ISS encoding for an exception from a Data Abort. A second stage abort might also record the intermediate physical address, IPA, but this depends on the type of the abort.

For a synchronous abort, AArch64.DataAbort() also sets the FAR to the V A of the abort.

The AArch64.InstructionAbort() function generates an Instruction Abort exception, routes the exception to EL2 or EL3, and records the information required for the Exception Syndrome registers, ESR\_ELx, see ISS encoding for an exception from an Instruction Abort. A second stage abort might also record the intermediate physical address, IPA, but this depends on the type of the abort.

For a synchronous abort, AArch64.InstructionAbort() also sets the FAR to the V A of the abort.

The FaultRecord type describes a fault. Functions that check for faults return a record of this type appropriate to the type of fault.

The function NoFault() returns a null record that indicates no fault. The IsFault() function tests whether a FaultRecord contains a fault.

## D7.8.8 Memory barriers

The definition for the memory barrier functions is given by the enumerations MBReqDomain and MBReqTypes .

These enumerations define the required shareability domains and required access types used as arguments for DMB and DSB instructions.

The procedures DataMemoryBarrier , DataSynchronizationBarrier , and InstructionSynchronizationBarrier perform the memory barriers.

## Chapter D8 The AArch64 Virtual Memory System Architecture

This chapter provides a system level view of the AArch64 Virtual Memory System Architecture (VMSA), the memory system architecture of an A-profile implementation that is executing in AArch64 state. It contains the following sections:

- Address translation.
- Translation process.
- Translation table descriptor formats.
- Memory access control.
- Memory region attributes.
- Other descriptor fields.
- Address tagging.
- Pointer authentication.
- Memory Encryption Contexts extension.
- Virtualization Host Extensions.
- Nested virtualization.
- Memory aborts.
- Translation Lookaside Buffers.
- TLB maintenance.
- Caches.
- Pseudocode description of VMSA address translation.