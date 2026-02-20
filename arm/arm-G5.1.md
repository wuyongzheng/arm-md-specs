## G5.1 About VMSAv8-32

This chapter describes the A-profile VMSA for AArch32 state, VMSAv8-32.

This chapter describes the control of the VMSA by Exception levels that are using AArch32. Security state, Exception levels, and AArch32 execution privilege summarizes how the AArch32 PE modes map onto the Exception levels.

FEAT\_SEL2, if implemented, is not available in AArch32 state and EL2 only executes in Non-secure state.

FEAT\_S2FWB, if implemented, is not available in AArch32 state. If EL2 is executing in AArch64 state 2 stage translations might be affected. For more information, see The AArch64 Virtual Memory System Architecture.

The AArch64 Virtual Memory System Architecture describes the control of the VMSA by Exception levels that are using AArch64.

The main function of the VMSA is to perform address translation, and access permissions and memory attribute determination and checking, for memory accesses made by the PE. Address translation, and permissions and attribute determination and checking, is performed by a stage of address translation.

In VMSAv8-32, the Memory Management Unit (MMU) provides a number of stages of address translation. This chapter describes only the stages that are visible from Exception levels that are using AArch32, which are as follows:

## For operation in Secure state

Asingle stage of address translation, for use when executing at PL1 or EL0. This is the Secure PL1&amp;0 stage 1 address translation stage.

## For operation in Non-secure state

- Asingle stage of address translation for use when executing at EL2. This is the Non-secure EL2 stage 1 address translation stage.
- Two stages of address translation for use when executing at PL1 or EL0. These are:
- -The Non-secure PL1&amp;0 stage 1 address translation stage.
- -The Non-secure PL1&amp;0 stage 2 address translation stage.

The System registers provide independent control of each supported stage of address translation, including a control to disable that stage of translation.

However, if the PE is executing at EL0 using AArch32 when EL1 is using AArch64 then it is using the VMSAv8-64 EL1&amp;0 translation regime, described in The AArch64 Virtual Memory System Architecture.

These features mean the VMSAv8-32 can support a hierarchy of software supervision, for example an Operating System and a hypervisor.

Each stage of address translation uses address translations and associated memory properties held in memory mapped tables called translation tables .

For information about how the MMU features differ if an implementation does not include all of the Exception levels, see About address translation for VMSAv8-32.

The translation tables define the following properties:

## Access to the Secure or Non-secure address map

The translation table entries determine whether an access from Secure state accesses the Secure or the Non-secure address map. Any access from Non-secure state accesses the Non-secure address map.

## Memory access permission control

This controls whether a program is permitted to access a memory region. For instruction and data access, the possible settings are:

- No access.
- Read-only.
- Write-only. This is possible only in a translation regime with two stages of translation.
- Read/write.

For instruction accesses, additional controls determine whether instructions can be fetched and executed from the memory region.

If a PE attempts an access that is not permitted, a memory fault is signaled to the PE.

## Memory region attributes

These describe the properties of a memory region. The top-level attribute, the Memory type, is one of Normal, or a type of Device memory, as follows:

- Both translation table formats support the following Device memory types:

- Device-nGnRnE

- Device-nGnRE

- The Long-descriptor translation table format supports, in addition, the following Device memory types:

- Device-nGRE

- Device-GRE

Note

Armv8 added the Device-nGRE and Device-GRE memory types. Also, in versions of the Arm architecture before Armv8:

- Device-nGnRnE memory is described as Strongly-ordered memory.

- Device-nGnRE memory is described as Device memory.

Normal memory regions can have additional attributes.

For more information, see Memory types and attributes.

## Address translation mappings

An address translation maps an input address to an output address .

Astage 1 translation takes the address of an explicit data access or instruction fetch, a virtual address (VA), as the input address, and translates it to a different output address:

- If only one stage of translation is provided, this output address is the physical address (PA).

- If two stages of address translation are provided, the output address of the stage 1 translation is an intermediate physical address (IPA).

Note

In the Armv8-32 architecture, a software agent, such as an Operating System, that uses or defines stage 1 memory translations, might be unaware of the distinction between IPA and PA.

Astage 2 translation translates the IPA to a PA.

The possible Security states and privilege levels of memory accesses define a set of translation regimes , where a translation regime maps an input V A to the corresponding PA, using one or two stages of translation. See The VMSAv8-32 translation regimes.

System registers control VMSAv8-32, including defining the location of the translation tables, and enabling and configuring the MMU, including enabling and disabling the different address translation stages. Also, they report any faults that occur on a memory access. For more information, see Functional grouping of VMSAv8-32 System registers.

The following sections give an overview of VMSAv8-32, and of the implementation options for VMSAv8-32:

- The VMSAv8-32 translation regimes.

- Address types used in a VMSAv8-32 description.

- Address spaces in VMSAv8-32.

- About address translation for VMSAv8-32.

The remainder of the chapter fully describes the VMSA, including the different implementation options, as summarized in Organization of the remainder of this chapter.

## G5.1.1 The VMSAv8-32 translation regimes

As introduced in Address translation mappings, a translation regime maps an input V A to the corresponding PA, using one or two stages of translation. Figure G5-1 shows the VMSAv8-32 translation regimes, and their associated translation stages and the Exception levels from which they are controlled.

Figure G5-1 VMSAv8-32 translation regimes, and associated control

Note

Conceptually, a translation regime that has only a stage 1 address translation is equivalent to a regime with a fixed, flat stage 2 mapping from IPA to PA.

Limited use of Privilege level in AArch32 state describes the mapping between the PE modes and the Privilege levels (PLs).

## G5.1.1.1 Alternative descriptions of the PL1&amp;0 translation regime

The PL1&amp;0 is described in terms of Privilege level because of the way the AArch32 PE modes map onto the Exception levels, as described in Limited use of Privilege level in AArch32 state. The description of this translation regime in terms of the Exception levels using depends on the current state of the PE, as follows:

- In Non-secure state, PL1 always maps to EL1, and therefore the Non-secure PL1&amp;0 translation regime could be described as the Non-secure EL1&amp;0 translation regime.

- In Secure state:

- When EL3 is using AArch32, PL1 maps to EL3, and therefore under these conditions the Secure PL1&amp;0 translation regime could be described as the Secure EL3&amp;0 translation regime,

- When EL3 is using AArch64, Secure PL1 maps to Secure EL1, and therefore under these conditions the Secure PL1&amp;0 translation regime could be described as the Secure EL1&amp;0 translation regime,

However, these descriptions all refer to the same translation regime, with the same System registers associated with its stage 1 translations. Therefore, the regime is generally referred to as the PL1&amp;0 translation regime.

Note

As Figure G5-1 shows, stage 2 translation is supported only in Non-secure state.

## G5.1.2 Address types used in a VMSAv8-32 description

Adescription of VMSAv8-32 refers to the following address types.

Note

These descriptions relate to a VMSAv8-32 description and therefore sometimes differ from the generic definitions given in the Glossary.

Virtual address (VA)

An address used in an instruction, as a data or instruction address, is a Virtual Address (V A).

An address held in the PC, LR, or SP, is a V A.

The VA map runs from zero to the size of the V A space. For AArch32 state, the maximum V A space is 4GB, giving a maximum VA range of 0x0000\_0000 -0xFFFF\_FFFF .

## Intermediate physical address (IPA)

In a translation regime that provides two stages of address translation, the IPA is the address after the stage 1 translation, and is the input address for the stage 2 translation.

In a translation regime that provides only one stage of address translation, the IPA is identical to the PA.

AVMSAv8-32 implementation provides only one stage of address translation:

- If the implementation does not include EL2.
- When executing in Secure state.
- When executing in Hyp mode.

## Physical address (PA)

The address of a location in the Secure or Non-secure memory map. That is, an output address from the PE to the memory system.

## G5.1.3 Address spaces in VMSAv8-32

For execution in AArch32 state, the architecture supports:

- AVAspace of up to 32 bits. The actual width is IMPLEMENTATION DEFINED.
- An IPA space of up to 40 bits. The translation tables and associated System registers define the width of the implemented address space.

Note

AArch32 defines two translation table formats. The Long-descriptor format gives access to the full 40-bit IPA or PA space at a granularity of 4KB. The Short-descriptor format:

- Gives access to a 32-bit PA space at 4KB granularity.
- Gives access to a 40-bit PA space, but only at 16MB granularity, by the use of Supersections.

If an implementation includes EL3, the address maps are defined independently for Secure and Non-secure operation, providing two independent 40-bit address spaces, where:

- AVAaccessed from Non-secure state can only be translated to the Non-secure address map.
- AVAaccessed from Secure state can be translated to either the Secure or the Non-secure address map.

## G5.1.4 About address translation for VMSAv8-32

Address translation is the process of mapping one address type to another, for example, mapping V As to IPAs, or mapping VAs to PAs. A translation table defines the mapping from one address type to another, and a Translation table base register (TTBR) indicates the start of a translation table. Each implemented stage of address translation shown in Figure G5-1 requires its own translation tables.

For PL1&amp;0 stage 1 translations, the mapping can be split between two tables, one controlling the lower part of the V A space, and the other controlling the upper part of the V A space. This can be used, for example, so that:

- One table defines the mapping for operating system and I/O addresses, that do not change on a context switch.
- Asecond table defines the mapping for application-specific addresses, and therefore might require updating on a context switch.

The VMSAv8-32 implementation options determine the supported address translation stages. The following descriptions apply when all implemented Exception levels are using AArch32:

## VMSAv8-32 without EL2 or EL3

Supports only a single PL1&amp;0 stage 1 address translation. Translation of this stage of address translation can be split between two sets of translation tables, with base addresses defined by TTBR0 and TTBR1, and controlled by TTBCR.

## VMSAv8-32 with EL3 but without EL2

Supports only the Secure PL1&amp;0 stage 1 address translation and the Non-secure PL1&amp;0 stage 1 address translation. In each Security state, this stage of translation can be split between two sets of translation tables, with base addresses defined by the Secure and Non-secure copies of TTBR0 and TTBR1, and controlled by the Secure and Non-secure copies of TTBCR.

## VMSAv8-32 with EL2 but without EL3

The implementation supports the following stages of address translation:

## Non-secure EL2 stage 1 address translation

The HTTBR defines the base address of the translation table for this stage of address translation, controlled by HTCR.

## Non-secure PL1&amp;0 stage 1 address translation

Translation of this stage of address translation can be split between two sets of translation tables, with base addresses defined by the Non-secure copies of TTBR0 and TTBR1 and controlled by the Non-secure instance of TTBCR.

## Non-secure PL1&amp;0 stage 2 address translation

The VTTBR defines the base address of the translation table for this stage of address translation, controlled by VTCR.

## VMSAv8-32 with EL2 and EL3

The implementation supports all of the stages of address translation, as follows:

## Secure PL1&amp;0 stage 1 address translation

Translation of this stage of address translation can be split between two sets of translation tables, with base addresses defined by the Secure copies of TTBR0 and TTBR1, and controlled by the Secure instance of TTBCR.

## Non-secure EL2 stage 1 address translation

The HTTBR defines the base address of the translation table for this stage of address translation, controlled by HTCR.

## Non-secure PL1&amp;0 stage 1 address translation

Translation of this stage of address translation can be split between two sets of translation tables, with base addresses defined by the Non-secure copies of TTBR0 and TTBR1 and controlled by the Non-secure instance of TTBCR.

## Non-secure PL1&amp;0 stage 2 address translation

The VTTBR defines the base address of the translation table for this stage of address translation, controlled by VTCR.

Figure G5-2 shows the translation regimes and stages in a VMSAv8-32 implementation that includes all of the Exception levels, and indicates the PE mode that, typically, defines each set of translation tables, if that stage of address translation is controlled by a Privilege level that is using AArch32:

## Figure G5-2 VMSAv8-32 address translation summary

Note

The term Typically configured is used in Figure G5-2 to indicate the expected software usage. However, stages of address translation used in AArch32 state can also be configured:

- From an Exception level higher than the Exception level of the configuring PE mode shown in Figure G5-2, regardless of whether that Exception level is using AArch32 or is using AArch64, except that a Non-secure Exception level can never configure a stage of address translation that is used in Secure state.

- From an Exception level that is using AArch64 and is higher than the level at which the translation stage is being used. For example, if Non-secure EL0 is the only Non-secure Exception level that is using AArch32, then the Non-secure PL1&amp;0 stage of address translation is configured from Non-secure EL1, that is using AArch64.

In general:

- The translation from V A to PA can require multiple stages of address translation, as Figure G5-2 shows.

- Asingle stage of address translation takes an input address and translates it to an output address.

Afull translation table lookup is called a translation table walk . It is performed automatically by hardware, and can have a significant cost in execution time. To support fine granularity of the V A to PA mapping, a single input address to output address translation can require multiple accesses to the translation tables, with each access giving finer granularity. Each access is described as a level of address lookup. The final level of the lookup defines:

- The required output address.

- The attributes and access permissions of the addressed memory.

Translation Lookaside Buffers (TLBs) reduce the average cost of a memory access by caching the results of translation table walks. TLBs behave as caches of the translation table information, and VMSAv8-32 provides TLB maintenance instructions for the management of TLB contents.

Note

The Arm architecture permits TLBs to hold any translation table entry that does not directly cause a Translation fault, an Address size fault, or an Access flag fault.

To reduce the software overhead of TLB maintenance, for the PL1&amp;0 translation regimes VMSAv8-32 distinguishes between Global pages and Process-specific pages . The ASID identifies pages associated with a specific process and provides a mechanism for changing process-specific tables without having to maintain the TLB structures.

If an implementation includes EL2, the VMID identifies the current virtual machine, with its own independent ASID space. The TLB entries include this VMID information, meaning TLBs do not require explicit invalidation when

changing from one virtual machine to another, if the virtual machines have different VMIDs. For stage 2 translations, all translations are associated with the current VMID. There is no mechanism to associate a particular stage 2 translation with multiple virtual machines.

## G5.1.4.1 Atomicity of register changes on changing virtual machine

From the viewpoint of software executing at Non-secure PL1 or EL0, when there is a switch from one virtual machine to another, the registers that control or affect address translation must be changed atomically. This applies to the registers for the Non-secure PL1&amp;0 translation regime. This means that all of the following registers must change atomically:

- The registers associated with the stage 1 translations:
- -MAIR0, MAIR1, AMAIR0, and AMAIR1.
- -TTBR0, TTBR1, TTBCR, TTBCR2, and CONTEXTIDR.
- -SCTLR.
- The registers associated with the stage 2 translations:
- -VTTBR and VTCR.
- -HSCTLR.

Note

Only some fields of SCTLR affect the stage 1 translation, and only some fields of HSCTLR affect the stage 2 translation. However, in each case, changing these fields requires a write to the register, and that write must be atomic with the other register updates.

These registers apply to execution using the Non-secure PL1&amp;0 translation regime. However, when updated as part of a switch of virtual machines they are updated by software executing at EL2. This means the registers are out of context when they are updated, and no synchronization precautions are required.

## G5.1.4.2 Use of out-of-context translation regimes

The architecture requires that:

- When executing at EL3 or EL2, the PE must not use the registers associated with the Non-secure PL1&amp;0 translation regime for speculative memory accesses.
- When executing at EL3 the PE must not use the registers associated with the EL2 translation regime for speculative memory accesses.
- When executing at EL3, EL2, or Non-secure EL1, the PE must not use the registers associated with the Secure PL1&amp;0 translation regime for speculative memory accesses.

If the Statistical Profiling Unit (SPU) is not in use for a lower Exception level when entering an Exception level on completion of a DSB instruction, then no new memory accesses using any translation table entries from a translation regime of an Exception level lower than the Exception level that has been entered will be observed by any observers to the extent that those accesses are required to be observed, as determined by the Shareability and Cacheability of those translation table entries.

If the SPU is in use for a lower Exception level when entering an Exception level on completion of a PSB CSYNC and a subsequent DSB instruction, then no new memory accesses using any translation table entries from a translation regime of an Exception level lower than the Exception level that has been entered will be observed by any observers, to the extent that those accesses are required to be observed, as determined by the Shareability and Cacheability of those translation table entries.

Note

- This does not require that speculative memory accesses cannot be performed using those entries if it is impossible to tell that those memory accesses have been observed by the observers.
- This requirement does not imply that, on taking an exception to a higher Exception level, any translation table walks started before the exception was taken will be completed by the time the higher Exception level is entered, and therefore memory accesses required for such a translation table walk might, in effect, be performed speculatively. However, the execution of a DSB on entry to the higher Exception level ensures that these accesses are complete.

## G5.1.5 Organization of the remainder of this chapter

The remainder of this chapter is organized as follows.

The next part of the chapter describes address translation and the associated memory properties held in the translation table entries, in the following sections:

- The effects of disabling address translation stages on VMSAv8-32 behavior.
- Translation tables.
- Secure and Non-secure address spaces.
- The VMSAv8-32 Short-descriptor translation table format.
- The VMSAv8-32 Long-descriptor translation table format.
- Memory access control.
- Memory region attributes.
- Translation Lookaside Buffers.
- TLB maintenance requirements.

Caches in VMSAv8-32 describes VMSAv8-32-specific cache requirements.

The following sections then describe aborts on VMSAv8-32 memory accesses, and how these and other faults are reported:

- VMSAv8-32 memory aborts.
- Exception reporting in a VMSAv8-32 implementation.

Address translation instructions then describes these operations, and how they relate to address translation.

Anumber of sections then describe the System registers for VMSAv8-32. The following sections give general information about the System registers, and the organization of the registers in the primary encoding spaces, ( coproc == 0b1110 ) and ( coproc == 0b1111 ) for these registers:

- About the System registers for VMSAv8-32.
- Functional grouping of VMSAv8-32 System registers.

Note

The System registers in the ( coproc == 0b1110 ) encoding space provide the following functionality:

- Self-hosted debug. These registers are described in Debug registers.
- The System register interface to a trace unit. These registers are not described in this manual.
- Jazelle registers. These registers are summarized in Legacy feature registers and system instructions.

Therefore, there is no summary of these registers by functional groups.

Pseudocode description of VMSAv8-32 memory system operations then summarizes the pseudocode functions that describe many features of VMSAv8-32 operation.