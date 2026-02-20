## G4.8 Pseudocode description of general memory System instructions

This section lists the pseudocode describing general memory operations:

- Memory data type definitions.
- Basic memory access.
- Aligned memory access.
- Unaligned memory access.
- Exclusives monitors operations.
- Access permission checking.
- Abort exceptions.
- Memory barriers.

## G4.8.1 Memory data type definitions

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

## G4.8.2 Basic memory access

The PhysMemRead() and PhysMemWrite() functions perform single-copy atomic, aligned, little-endian memory accesses of size bytes to or from the underlying physical memory array of bytes.

The attributes in memaddrdesc.memattrs are used by the memory system to determine caching and ordering behaviors as described in Memory types and attributes, Definition of the memory model, and Atomicity in the Arm architecture.

## G4.8.3 Aligned memory access

The AArch32.MemSingle[] functions make atomic, little-endian accesses of size bytes.

## G4.8.4 Unaligned memory access

See Unaligned data access for details of the SCTLR.A and HSCTLR.A controls on the generation of alignment faults. The HSCTLR control applies to Normal memory accesses from Hyp mode, and the SCTLR control applies to Normal memory accesses from all other modes.

The Mem\_with\_type[] functions make an access of the required type. If that access is naturally aligned, each form of the function performs an atomic access by making a single call to AArch32.MemSingle[] . If that access is not aligned but passes the IsAligned() checks, each form of the function synthesizes the required access from multiple calls to AArch32.MemSingle[] . It also reverses the byte order if the access is big-endian.

## G4.8.5 Exclusives monitors operations

The AArch32.SetExclusiveMonitors() function sets the Exclusives monitors for a Load-Exclusive instruction, for a block of bytes. The size of the blocks is determined by size , at the V A address . The ExclusiveMonitorsPass() function checks whether a Store-Exclusive instruction still has possession of the Exclusives monitors and therefore completes successfully.

The AArch32.ExclusiveMonitorsPass() function checks whether a Store-Exclusive instruction still has possession of the Exclusives monitors, by checking whether the Exclusives monitors are set to include the location of the memory block specified by size , at the virtual address defined by address . The atomic write that follows after the Exclusives monitors have been set must be to the same physical address. It is permitted, but not required, for this function to return FALSE if the virtual address is not the same as that used in the previous call to AArch32.SetExclusiveMonitors() .

The ExclusiveMonitorsStatus() function returns 0 if the previous atomic write was to the same physical memory locations selected by ExclusiveMonitorsPass() and therefore succeeded. Otherwise the function returns 1, indicating that the address translation delivered a different physical address.

The MarkExclusiveGlobal() procedure takes as arguments a FullAddress.paddress , the PE identifier processorid and the size of the transfer. The procedure records that the PE processorid has requested exclusive access covering at least size bytes from address paddress . The size of the location marked as exclusive is IMPLEMENTATION DEFINED, up to a limit of 2KB and no smaller than two words, and aligned in the address space to the size of the location. It is CONSTRAINED UNPREDICTABLE whether this causes any previous request for exclusive access to any other address by the same PE to be cleared.

The MarkExclusiveLocal() procedure takes as arguments a FullAddress paddress , the PE identifier processorid and the size of the transfer. The procedure records in a local record that PE processorid has requested exclusive access to an address covering at least size bytes from address paddress. The size of the location marked as exclusive is IMPLEMENTATION DEFINED, and can at its largest cover the whole of memory but is no smaller than two words, and is aligned in the address space to the size of the location. It is IMPLEMENTATION DEFINED whether this procedure also performs a MarkExclusiveGlobal() using the same parameters.

The IsExclusiveGlobal() function takes as arguments a FullAddress paddress , the PE identifier processorid and the size of the transfer. The function returns TRUE if the PE processorid has marked in a global record an address range as exclusive access requested that covers at least size bytes from address paddress . It is IMPLEMENTATION DEFINED whether it returns TRUE or FALSE if a global record has marked a different address as exclusive access requested. If no address is marked in a global record as exclusive access, IsExclusiveGlobal() returns FALSE.

The IsExclusiveLocal() function takes as arguments a FullAddress paddress , the PE identifier processorid and the size of the transfer. The function returns TRUE if the PE processorid has marked an address range as exclusive access requested that covers at least the size bytes from address paddress . It is IMPLEMENTATION DEFINED whether this function returns TRUE or FALSE if the address marked as exclusive access requested does not cover all of size bytes from address paddress . If no address is marked as exclusive access requested, then this function returns FALSE. It is IMPLEMENTATION DEFINED whether this result is ANDed with the result of IsExclusiveGlobal() with the same parameters.

The ClearExclusiveByAddress() procedure takes as arguments a FullAddress paddress , the PE identifier processorid and the size of the transfer. The procedure clears the global records of all PEs, other than processorid , for which an address region including any of size bytes starting from paddress has had a request for an exclusive access. It is IMPLEMENTATION DEFINED whether the equivalent global record of the PE processorid is also cleared if any of size bytes starting from paddress has had a request for an exclusive access, or if any other address has had a request for an exclusive access.

The ClearExclusiveLocal() procedure takes as arguments the PE identifier processorid . The procedure clears the local record of PE processorid for which an address has had a request for an exclusive access. It is IMPLEMENTATION DEFINED whether this operation also clears the global record of PE processorid that an address has had a request for an exclusive access.

## G4.8.6 Access permission checking

The AArch32.S1LDHasPermissionsFault() , AArch32.S1SDHasPermissionsFault() , and AArch32.S2HasPermissionsFault() functions are used by the architecture to perform access permission checking based on attributes derived from the Translation Table descriptors.

The interpretation of access permission is shown in Memory access control.

## G4.8.7 Abort exceptions

The function AArch32.Abort() generates a Data Abort exception or a Prefetch Abort exception by calling the AArch32.TakeDataAbortException() or AArch32.TakePrefetchAbortException() function.

The FaultRecord type describes a fault. Functions that check for faults return a record of this type appropriate to the type of fault. Pseudocode description of VMSAv8-32 memory system operations provides a number of wrappers to generate a FaultRecord.

The function NoFault() returns a null record that indicates no fault. The IsFault() function tests whether a FaultRecord contains a fault.

## G4.8.8 Memory barriers

The definition for the memory barrier functions is given by the enumerations MBReqDomain and MBReqTypes .

These enumerations define the required Shareability domains and required access types used as arguments for DMB and DSB instructions.

The procedures DataMemoryBarrier() , DataSynchronizationBarrier() , and InstructionSynchronizationBarrier() perform the memory barriers.

## Chapter G5 The AArch32 Virtual Memory System Architecture

This chapter describes the A-profile AArch32 Virtual Memory System Architecture (VMSA). It includes the following sections:

- About VMSA v8-32.

- The effects of disabling address translation stages on VMSAv8-32 behavior.

- Translation tables.

- The VMSAv8-32 Short-descriptor translation table format.

- The VMSAv8-32 Long-descriptor translation table format.

- Memory access control.

- Memory region attributes.

- Translation Lookaside Buffers.

- TLB maintenance requirements.

- Caches in VMSAv8-32.

- VMSAv8-32 memory aborts.

- Exception reporting in a VMSAv8-32 implementation.

- Address translation instructions.

- Pseudocode description of VMSAv8-32 memory system operations.

- About the System registers for VMSAv8-32.

- Functional grouping of VMSAv8-32 System registers.

Note

This chapter must be read with The AArch32 System Level Memory Model.