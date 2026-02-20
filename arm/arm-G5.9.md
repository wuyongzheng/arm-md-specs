## G5.9 TLB maintenance requirements

Translation Lookaside Buffers describes the Arm architectural provision for TLBs. Although the Arm architecture does not specify the form of any TLB structures, it does define the mechanisms by which TLBs can be maintained. The following sections describe the VMSAv8-32 TLB maintenance instructions:

- General TLB maintenance requirements.
- Maintenance requirements on changing System register values.
- Atomicity of register changes on changing virtual machine.
- Synchronization of changes of ASID and TTBR.
- The scope of TLB maintenance instructions.

## G5.9.1 General TLB maintenance requirements

TLB maintenance instructions provide a mechanism to invalidate entries from a TLB. As Translation Lookaside Buffers describes, when address translation is enabled translation table entries can be allocated to a TLB at any time. This means that software must perform TLB maintenance between updating translation table entries that apply in a particular context and accessing memory locations whose translation is determined by those entries in that context.

Note

This requirement applies to any translation table entry at any level of the translation tables, including an entry that points to further levels of the tables, provided that the entry in that level of the tables does not cause a Translation fault, an Address size fault, or an Access flag fault.

The effects of certain System register control fields are permitted to be cached in a TLB. For more information, see TLB maintenance.

Note

For AArch32, use of a single DTLBI or ITLBI instruction when invalidating TLB entries is insufficient, as both data and instruction TLBs must be invalidated. Arm provides a set of TLBI instructions that are intended for this purpose.

In addition to any TLB maintenance requirement, when changing the cacheability attributes of an area of memory, software must ensure that any cached copies of affected locations are removed from the caches. For more information, see Cache maintenance requirement created by changing translation table attributes.

Because a TLB never holds any translation table entry that generates a Translation fault, an Address size fault, or an Access flag fault, a change from a translation table entry that causes a Translation, Address size, or Access flag fault to one that does not fault, does not require any TLB or branch predictor invalidation. However, a Context Synchronization event is required to ensure that instruction fetches are affected by a completed change to translation table entries that, before the change, generated a Translation, Address size, or Access flag fault.

Special considerations apply to translation table updates that change the memory type, cacheability, or output address of an entry, see Using break-before-make when updating translation table entries.

In addition, software must perform TLB maintenance after updating the System registers if the update means that the TLB might hold information that applies to a current translation context, but is no longer valid for that context. Maintenance requirements on changing System register values gives more information about this maintenance requirement.

Each of the translation regimes defined in Figure G5-1 is a different context, and:

- For the Non-secure PL1&amp;0 regime, a change in the VMID or ASID value changes the context.
- For the Secure PL1&amp;0 regime, a change in the ASID value changes the context.

For operation in Non-secure PL1 or EL0 modes, a change of HCR.VM, unless made at the same time as a change of VMID, requires the invalidation of all TLB entries for the Non-secure PL1&amp;0 translation regime that apply to the current VMID. Otherwise, there is no guarantee that the effect of the change of HCR.VM is visible to software executing in the Non-secure PL1 and EL0 modes.

Any TLB maintenance instruction can affect any other TLB entries that are not locked down.

AArch32 state defines { coproc == 0b1111 , CRn == c8 } System instructions for TLB maintenance instructions, and supports the following operations:

- Invalidate all unlocked entries in the TLB.

- Invalidate a single TLB entry, by V A, or V A and ASID for a non-global entry.

- Invalidate all TLB entries that match a specified ASID.

- Invalidate all TLB entries that match a specified V A, regardless of the ASID.

- Operations that apply across multiprocessors in the same Inner Shareable domain.

Note

An address-based TLB maintenance instruction that applies to the Inner Shareable domain does so regardless of the Shareability attributes of the address supplied as an argument to the instruction.

ATLBmaintenance instruction that specifies a VA that would generate any MMU fault, including a VA that is not in the range of VAs that can be translated, does not generate an abort.

EL2 provides additional TLB maintenance instructions for use in AArch32 state at EL2, and has some implications for the effect of the other TLB maintenance instructions, see The scope of TLB maintenance instructions.

In an implementation that includes EL3, the TLB maintenance instructions take account of the current Security state, as part of the address translation required for the TLB maintenance instruction.

Some TLB maintenance instructions are defined as operating only on instruction TLBs, or only on data TLBs. AArch32 state includes these instructions for backward compatibility. However, more recent TLB maintenance instructions do not support this distinction. Arm deprecates any use of Instruction TLB maintenance instructions, or of Data TLB maintenance instructions, and developers must not rely on this distinction being maintained in future revisions of the Arm architecture.

The Arm architecture does not dictate the form in which the TLB stores translation table entries. However, for TLB invalidate instructions, the minimum size of the table entry that is invalidated from the TLB must be at least the size that appears in the translation table entry.

The scope of TLB maintenance instructions describes the TLB maintenance instructions. The following subsections give more information about the general requirements for TLB maintenance:

- Using break-before-make when updating translation table entries.
- The interaction of TLB lockdown with TLB maintenance instructions.
- Ordering and completion of TLB maintenance instructions.
- Use of ASIDs and VMIDs to reduce TLB maintenance requirements.

## G5.9.1.1 Using break-before-make when updating translation table entries

To avoid possibly creating multiple TLB entries for the same address, and to avoid the effects of TLB caching possibly breaking coherency, single-copy atomicity properties, ordering guarantees or uniprocessor semantics, or possibly failing to clear the Exclusives monitors, the architecture requires the use of a break-before-make sequence when changing translation table entries whenever multiple threads of execution can use the same translation tables and the change to the translation table entries involves any of:

- Achange of the memory type, including shareability.
- Achange of the cacheability attributes.
- Achange of the output address (OA), if the OA of at least one of the old translation table entries and the new translation table entry is writable.
- Achange to the size of block used by the translation system. This applies both:
- -When changing from a smaller size to a larger size, for example by replacing a table mapping with a block mapping in a stage 2 translation table.
- -When changing from a larger size to a smaller size, for example by replacing a block mapping with a table mapping in a stage 2 translation table.
- Achange of the output address (OA), if the contents of memory at the new OA do not match the contents of memory at the previous OA.
- Creating a global entry when there might be non-global entries in a TLB that overlap with that global entry.

Note

Changes to the output address (OA) include changing between Secure and Non-secure output addresses.

Abreak-before-make sequence on changing from an old translation table entry to a new translation table entry requires the following steps:

1. Replace the old translation table entry with an invalid entry, and execute a DSB instruction.
2. Invalidate the translation table entry with a broadcast TLB invalidation instruction, and execute a DSB instruction to ensure the completion of that invalidation.
3. Write the new translation table entry, and execute a DSB instruction to ensure that the new entry is visible.

This sequence ensures that at no time are both the old and new entries simultaneously visible to different threads of execution, and therefore the problems described at the start of this subsection cannot arise.

## G5.9.1.2 The interaction of TLB lockdown with TLB maintenance instructions

The precise interaction of TLB lockdown with the TLB maintenance instructions is IMPLEMENTATION DEFINED. However, the architecturally-defined TLB maintenance instructions must comply with these rules:

- The effect on locked entry of a TLB invalidate all unlocked entries instruction or a TLB invalidate by V A all ASID instruction that would invalidate that entry if the entry was not locked must be one of the following, and it is IMPLEMENTATION DEFINED which behavior applies:
- -The instructions have no effect on entries that are locked down.
- -The instructions generate an IMPLEMENTATION DEFINED Data Abort exception if an entry is locked down, or might be locked down. For an invalidate instruction performed in AArch32 state, the { coproc == 0b1111 , CRn == c5 } fault status register definitions include a Fault status code for cache and TLB lockdown faults, see Table G5-26 for the codes used with the Short-descriptor translation table formats, or Table G5-27 for the codes used with the Long-descriptor translation table formats. In an implementation that includes EL2, if EL2 is using AArch32 and the value of HCR.TIDCP is 1, any such exceptions taken from a Non-secure PL1 mode are routed to Hyp mode, see HCR.

This permits a usage model for TLB invalidate routines, where the routine invalidates a large range of addresses, without considering whether any entries are locked in the TLB.

- The effect on a locked TLB entry of a TLB invalidate by V A instruction or a TLB invalidate by ASID match instruction that would invalidate that entry if the entry was not locked must be one of the following, and it is IMPLEMENTATION DEFINED which behavior applies:
- -Alocked entry is invalidated in the TLB.
- -The instruction has no effect on a locked entry in the TLB. In the case of the Invalidate single entry by VA, this means the PE treats the instruction as a NOP.
- -The instruction generates an IMPLEMENTATION DEFINED Data Abort exception if it operates on an entry that is locked down, or might be locked down. For an invalidate instruction performed in AArch32 state, the { coproc == 0b1111 , CRn == c5 } fault status register definitions include a Fault status code for cache and TLB lockdown faults, see Table G5-26 and Table G5-27.

Note

Any implementation that uses an abort mechanism for entries that can be locked down but are not actually locked down must:

- Document the IMPLEMENTATION DEFINED instruction sequences that perform the required invalidation on entries that are not locked down.
- Implement one of the other specified alternatives for the locked entries.

Arm recommends that, when possible, such IMPLEMENTATION DEFINED instruction sequences use the architecturally- defined maintenance instructions. This minimizes the number of customized maintenance operations required. In addition, an implementation that uses an abort mechanism for handling TLB maintenance instructions on entries that can be locked down but are not actually locked down must also must provide a mechanism that ensures that no TLB entries are locked.

Similar rules apply to cache lockdown, see The interaction of cache lockdown with cache maintenance instructions.

The architecture does not guarantee that any unlocked entry in the TLB remains in the TLB. This means that, as a side-effect of a TLB maintenance instruction, any unlocked entry in the TLB might be invalidated.

## G5.9.1.3 Ordering and completion of TLB maintenance instructions

The following rules describe the relations between the memory order model and the TLB maintenance instructions:

- ATLBmaintenance instruction executed by a PE, PEe, causes a TLB maintenance operation to be generated on each PE within the shareability domain of PEe that is specified by the instruction.

- At EL2 or EL3, or at EL1 when the Effective value of HCRX\_EL2.FnXS is 0, the associated TLB maintenance operations do not have the nXS qualifier.

- At EL1, when the Effective value of HCRX\_EL2.FnXS is 1, the behavior of the associated TLB maintenance operations is the same as described for the AArch64 TLB maintenance instructions with the nXS qualifier. See Ordering and completion of TLB maintenance instructions.

Note

When FEAT\_XS is not implemented, all TLB maintenance instructions do not have the nXS qualifier and the Effective value of HCRX\_EL2 is 0.

- ATLBmaintenance operation generated by a TLB maintenance instruction is finished for a PE when:

- All memory accesses generated by that PE using in-scope old translation information are complete.

- All memory accesses RWx generated by that PE are complete.

RWxis the set of all memory accesses generated by instructions for that PE that appear in program order before an instruction I1 executed by that PE where all of the following apply:

- I1 uses the in-scope old translation information.

- The use of the in-scope old translation information generates a synchronous Data Abort.

- If I1 did not generate an abort from use of the in-scope old translation information, I1 would generate a memory access that RWx would be locally-ordered-before.

In-scope old translation information is any translation information, for addresses that are in the scope of the TLB maintenance instruction, that is not consistent with either:

- The architectural translation information held in the translation tables at the time that the TLB maintenance instruction is executed by PEe.

- Any architecture translation information that is Coherence-after the information held in the translation tables at the time that the TLB maintenance instruction is executed by PEe.

Note

- Old translation information of this type might be held in TLBs or other non-coherent caching structures.

ATLBmaintenance instruction is complete when the TLB maintenance operations specified by the TLB maintenance instruction are finished for all PEs.

After the TLB maintenance instruction is complete, no new memory accesses using the in-scope old translation information will be architecturally performed by any observer that is affected by the TLB maintenance instruction.

Note

Speculative memory accesses can be performed using those entries if it is impossible for software running on any observer to tell that those memory accesses have been performed.

- ATLBmaintenance instruction is only guaranteed to be complete after the execution of a DSB instruction.

- An ISB instruction, or a return from an exception, causes the effect of all completed TLB maintenance instructions that appear in program order before the ISB or return from exception to be visible to all subsequent instructions, including the instruction fetches for those instructions.

- An exception causes all completed TLB maintenance instructions, that appear in the instruction stream before the point where the exception is taken, to be visible to all subsequent instructions, including the instruction fetches for those instructions.

- All TLB maintenance instructions are executed in program order relative to each other.

- The execution of a Data or Unified TLB maintenance instruction is only guaranteed to be visible to a subsequent explicit memory read or write effect instruction after both:

- The execution of a DSB instruction to ensure the completion of the TLB maintenance instruction.

- Execution of a subsequent Context Synchronization event.

- The execution of an Instruction or Unified TLB maintenance instruction is only guaranteed to be visible to a subsequent instruction fetch after both:
- -The execution of a DSB instruction to ensure the completion of the TLB maintenance instruction.
- -Execution of a subsequent Context Synchronization event.

In all cases in this section where a DMB or DSB is referred to, it refers to a DMB or DSB whose required access type is both loads and stores. A DSB NSH is sufficient to ensure completion of TLB maintenance instructions that apply to a single PE. A DSB ISH is sufficient to ensure completion of TLB maintenance instructions that apply to PEs in the same Inner Shareable domain.

The following rules apply when writing translation table entries. They ensure that the updated entries are visible to subsequent accesses and cache maintenance instructions.

For TLB maintenance, the translation table walk is treated as a separate observer. This means:

- Awrite to the translation tables is only guaranteed to be seen by a translation table walk caused by an explicit memory read or write effect after the execution of both a DSB and an ISB .
- However, the architecture guarantees that any writes to the translation tables are not seen by any explicit memory effect that occurs in program order before the write to the translation tables.
- Awrite to the translation tables is only guaranteed to be seen by a translation table walk caused by the instruction fetch of an instruction that follows the write to the translation tables after both a DSB and an ISB .

Therefore, in a uniprocessor system, an example instruction sequence for writing a translation table entry, covering changes to the instruction or data mappings is:

```
STR rx, [Translation table entry] ; write new entry to the translation table DSB ; ensures visibility of the new entry Invalidate TLB entry by VA (and ASID if non-global) [page address] Invalidate BTC DSB ; ensure completion of the Invalidate TLB instruction ISB ; ensure table changes visible to instruction fetch
```

## G5.9.1.4 Use of ASIDs and VMIDs to reduce TLB maintenance requirements

To reduce the need for TLB maintenance on context switches, the lookups from some translation regimes can be associated with an ASID, or with an ASID and a VMID.

Note

The use of ASIDs and VMIDs in VMSAv8-32 is generally similar to their use in VMSAv8-64, see Use of ASIDs and VMIDs to reduce TLB maintenance requirements.

For more information about the use of ASIDs in VMSAv8-32 see Global and process-specific translation table entries.

## G5.9.1.4.1 Common not private translations in VMSAv8-32

In an implementation that includes FEAT\_TTCNP, multiple PEs in the same Inner Shareable domain can use the same translation table entries for a given stage of address translation in a particular translation regime. This sharing is enabled by the TTBR.CnP field for the stage of address translation.

When the value of a TTBR.CnP field is 1, translation table entries pointed to by that TTBR are shared with all other PEs in the Inner Shareable domain for which the following conditions are met:

- The corresponding TTBR.CnP field has the value 1.
- That TTBR is using the Long-descriptor translation table format.
- If an ASID applies to the stage of translation corresponding to that TTBR then the current ASID value must be the same for all of the PEs that are sharing entries for any translation table entry that is not global or not leaf level.
- If a VMID applies to the stage of translation corresponding to that TTBR then the current VMID value must be the same for all of the PEs that are sharing entries.

Note

In an implementation that includes EL3, the Secure instances of TTBR0 and TTBR1 relate to the Secure PL1&amp;0 translation regime, and the Non-secure instances of TTBR0 and TTBR1 relate to the Non-secure PL1&amp;0 translation regime.

For a translation regime with both stage 1 and stage 2 translations, where a TLB combines information from stage 1 and stage 2 translation table entries into a single entry, this entry can be shared between different PEs only if the value of the TTBR.CnP bit is 1 for both stage 1 and stage 2 of the translation table walk.

The TTBR.CnP bit can be cached in a TLB.

For a given TTBR, if the value of TTBR.CnP is 1 on multiple PEs in the same Inner Shareable domain, and those PEs meet the other conditions for sharing translation table entries as defined in this section, but those TTBRs do not point to the same translation table entries, then the system is misconfigured, and performing an address translation using that TTBR:

- Might generate multiple hits in the TLB, and as a result generate an exception that is reported using the TLB conflict fault code, see TLB conflict aborts.
- Otherwise, has a CONSTRAINED UNPREDICTABLE result, as described in CONSTRAINED UNPREDICTABLE behaviors due to caching of System register control or data values.

## G5.9.2 Maintenance requirements on changing System register values

The TLB contents can be influenced by control bits in a number of System registers. This means the TLB entries associated with a translation regime affected by these control bits must be invalidated after any changes to these bits, unless the changes are accompanied by a change to the VMID or ASID, if appropriate depending on the translation regime, that defines the context to which the bits apply. The general form of the required invalidation sequence is as follows:

```
; Change control bits in System registers ISB ; Synchronize changes to the control bits ; Perform TLB invalidation of all entries that might be affected by the changed control bits
```

The System register changes that this applies to are:

- Any change to the NMRR, PRRR, MAIR0, MAIR1, HMAIR0 or HMAIR1 registers.
- Any change to the SCTLR.AFE bit, see Changing the Access flag enable.
- Any change to any of the SCTLR.{TRE, WXN, UWXN} bits.
- Any change to the Translation table base 0 address in TTBR0.
- Any change to the Translation table base 1 address in TTBR1.
- Any change to HTTBR.BADDR.
- Any change to VTTBR.BADDR.
- Changing TTBCR.EAE, see Changing the current Translation table format.
- In an implementation that includes EL3, any change to the SCR.SIF bit.
- In an implementation that includes EL2:
- -Any change to the HCR.VM bit.
- -Any change to HCR.PTW bit, see Changing HCR.PTW.
- When using the Short-descriptor translation table format:
- -Any change to the RGN, IRGN, S, or NOS fields in TTBR0 or TTBR1.
- -Any change to the N, EAE, PD0 or PD1 fields in TTBCR.
- When using the Long-descriptor translation table format:
- -Any change to the EAE, T n SZ, ORGN n , IRGN n , SH n , or EPD n fields in the TTBCR, where n is 0 or 1.
- -Any change to the TTBCR2.
- -Any change to the T0SZ, ORGN0, IRGN0, or SH0 fields in the HTCR.
- -Any change to the T0SZ, ORGN0, IRGN0, or SH0 fields in the VTCR.

## G5.9.2.1 Changing the Access flag enable

In a PE that is using the Short-descriptor translation table format, it is CONSTRAINED UNPREDICTABLE whether the TLB caches the effect of the SCTLR.AFE bit on translation tables. This means that, after changing the SCTLR.AFE bit software must invalidate the TLB before it relies on the effect of the new value of the SCTLR.AFE bit, otherwise behavior is CONSTRAINED UNPREDICTABLE, see CONSTRAINED UNPREDICTABLE behaviors due to caching of System register control or data values.

Note

There is no enable bit for use of the Access flag when using the Long-descriptor translation table format.

## G5.9.2.2 Changing HCR.PTW

When EL2 is using AArch32 and the value of the Protected table walk bit, HCR.PTW, is 1, a stage 1 translation table access in the Non-secure PL1&amp;0 translation regime, to an address that is mapped to any type of Device memory by its stage 2 translation, generates a stage 2 Permission fault. A TLB associated with a particular VMID might hold entries that depend on the effect of HCR.PTW. Therefore, if the value of HCR.PTW is changed without a change to the VMID value, all TLB entries associated with the current VMID must be invalidated before executing software in a Non-secure PL1 or EL0 mode. If this is not done, behavior is CONSTRAINED UNPREDICTABLE, see CONSTRAINED UNPREDICTABLE behaviors due to caching of System register control or data values.

## G5.9.2.3 Changing the current Translation table format

The effect of changing TTBCR.EAE when executing in the translation regime affected by TTBCR.EAE with any stage of address translation for that translation regime enabled is CONSTRAINED UNPREDICTABLE. This means that, when TTBCR.EAE is changed for a given context, the TLB must be invalidated before resuming execution in that context, otherwise the effect is CONSTRAINED UNPREDICTABLE, see CONSTRAINED UNPREDICTABLE behaviors due to caching of System register control or data values.

## G5.9.3 Atomicity of register changes on changing virtual machine

From the viewpoint of software executing in a Non-secure PL1 or EL0 mode, when there is a switch from one virtual machine to another, the registers that control or affect address translation must be changed atomically. This applies to the registers for:

- Non-secure PL1&amp;0 stage 1 address translations. This means that all of the following registers must change atomically:
- -PRRR and NMRR, if using the Short-descriptor translation table format.
- -MAIR0 and MAIR1, if using the Long-descriptor translation table format.
- -TTBR0, TTBR1, TTBCR, TTBCR2, DACR, and CONTEXTIDR.
- -The SCTLR.
- Non-secure PL1&amp;0 stage 2 address translations. When EL2 is using AArch32, this means that all of the following registers and register fields must change atomically:
- -VTTBR and VTCR.
- -HMAIR0 and HMAIR1.
- -The HSCTLR.

Note

Only some bits of SCTLR affect the stage 1 translation, and only some bits of HSCTLR affect the stage 2 translation. However, in each case, changing these bits requires a write to the register, and that write must be atomic with the other register updates.

These registers apply to execution in Non-secure PL1&amp;0 modes. However, when updated as part of a switch of virtual machines they are updated by software executing in Hyp mode. This means the registers are out of context when they are updated, and no synchronization precautions are required.

Note

By contrast, a translation table change associated with a change of ASID, made by software executing at PL1, can require changes to registers that are in context . Synchronization of changes of ASID and TTBR describes appropriate precautions for such a change.

Software executing in Hyp mode, or in Secure state, must not use the registers associated with the Non-secure PL1&amp;0 translation regime for speculative memory accesses.

## G5.9.4 Synchronization of changes of ASID and TTBR

Acommon virtual memory management requirement is to change the ASID and TTBR together to associate the new ASID with different translation tables, without any change to the current translation regime. When using the Short-descriptor translation table format, different registers hold the ASID and the translation table base address, meaning these two values cannot be updated atomically. Since a PE can perform a speculative memory access at any time, this lack of atomicity is a problem that software must address. Such a change is complicated by:

- The depth of speculative fetch being IMPLEMENTATION DEFINED.
- The use of branch prediction.

When using the Short-descriptor translation table format, the virtual memory management operations must ensure the synchronization of changes of the ContextID and the translation table registers. For example, some or all of the TLBs, branch predictors, and other caching of ASID and translation information might become corrupt with invalid translations. Synchronization is required to avoid either:

- The old ASID being associated with translation table walks from the new translation tables.
- The new ASID being associated with translation table walks from the old translation tables.

There are a number of possible solutions to this problem, and the most appropriate approach depends on the system. Example G5-3, Example G5-4, and Example G5-5 describe three possible approaches.

Note

Another instance of the synchronization problem occurs if a branch is encountered between changing the ASID and performing the synchronization. In this case the value in the branch predictor might be associated with the incorrect ASID. Software can address this possibility using any of these approaches, but instead software might be written in a way that avoids such branches.

## Example G5-3 Using a reserved ASID to synchronize ASID and TTBR changes

In this approach, a particular ASID value is reserved for use by the operating system, and is used only for the synchronization of the ASID and TTBR. This example uses the value of 0 for this purpose, but any value could be used.

This approach can be used only when the size of the mapping for any given VA is the same in the old and new translation tables.

The maintenance software uses the following sequence, which must be executed from memory marked as global:

```
Change ASID to 0 ISB Change TTBR ISB Change ASID
```

```
to new value
```

This approach ensures that any non-global pages fetched at a time when it is uncertain whether the old or new translation tables are being accessed are associated with the unused ASID value of 0. Since the ASID value of 0 is not used for any normal operations these entries cannot cause corruption of execution.

Example G5-4 Using translation tables containing only global mappings when changing the ASID

A second approach involves switching the translation tables to a set of translation tables that only contain global mappings while switching the ASID.

The maintenance software uses the following sequence, which must be executed from memory marked as global:

```
Change TTBR to the global-only mappings ISB Change ASID to new value ISB
```

This approach ensures that no non-global pages can be fetched at a time when it is uncertain whether the old or new ASID value will be used.

This approach works without the need for TLB invalidations in systems that have caching of intermediate levels of translation tables, as described in General TLB maintenance requirements, provided that the translation tables containing only global mappings have only level 1 translation table entries of the following kinds:

- Entries that are global.
- Pointers to level 2 tables that hold only global entries, and that are the same level 2 tables that are used for accessing global entries by both:
- -The set of translation tables that were used under the old ASID value.
- -The set of translation tables that will be used with the new ASID value.
- Invalid level 1 entries.

In addition, all sets of translation tables in this example should have the same Shareability and Cacheability attributes, as held in the TTBR0.{ORGN, IRGN} or TTBR1.{ORGN, IRGN} fields.

If these rules are not followed, then the implementation might cache level 1 translation table entries that require explicit invalidation.

## Example G5-5 Disabling non-global mappings when changing the ASID

In systems where only the translation tables indexed by TTBR0 hold non-global mappings, maintenance software can use the TTBCR.PD0 field to disable use of TTBR0 during the change of ASID. This means the system does not require a set of global-only mappings.

The maintenance software uses the following sequence, which must be executed from a memory region with a translation that is accessed using the base address in the TTBR1 register, and is marked as global:

```
Set TTBCR.PD0 = 1 ISB Change ASID to new value Change TTBR to new value ISB Set TTBCR.PD0 = 0
```

This approach ensures that no non-global pages can be fetched at a time when it is uncertain whether the old or new ASID value will be used.

When using the Long-descriptor translation table format, TTBCR.A1 holds the number, 0 or 1, of the TTBR that holds the current ASID. This means the current TTBR can also hold the current ASID, and the current translation table base address and ASID can be updated atomically when:

- TTBR0 is the only TTBR being used. TTBCR.A1 must be set to 0.
- TTBR0 points to the only translation tables that hold non-global entries, and TTBCR.A1 is set to 0.
- TTBR1 points to the only translation tables that hold non-global entries, and TTBCR.A1 is set to 1.

In these cases, software can update the current translation table base address and ASID atomically, by updating the appropriate TTBR, and does not require a specific routine to ensure synchronization of the change of ASID and base address.

However, in all other cases using the Long-descriptor format, the synchronization requirements are identical to those when using the Short-descriptor formats, and the examples in this section indicate how synchronization might be achieved.

Note

When using the Long-descriptor translation table format, CONTEXTIDR.ASID has no significance for address translation, and is only an extension of the Context ID value.

## G5.9.5 The scope of TLB maintenance instructions

TLB maintenance instructions provide a mechanism for invalidating entries from TLB caching structures, to ensure that changes to the translation tables are reflected correctly in the TLB caching structures. To support TLB maintenance in multiprocessor systems, there are maintenance operations that apply to the TLBs of all PEs in the same Inner Shareable domain.

The architecture permits the caching of any translation table entry that has been returned from memory without a fault and that does not, itself, cause a Translation Fault, an Address size fault, or an Access Flag fault. This means the TLB:

- Cannot hold an entry that, when used for a translation table lookup, causes a Translation fault, an Address size fault, or an Access Flag fault.
- Can hold an entry for a translation table lookup for a translation that causes a Translation Fault, an Address size fault, or an Access Flag fault at a subsequent level of translation table lookup. For example, it can hold an entry for the level 1 lookup of a translation that causes a Translation fault, an Address size fault, or an Access Flag fault at level 2 or level 3 of lookup.

This means that entries cached in the TLB can include:

- Translation table entries that point to a subsequent table to be used in the current stage of translation.

- In an implementation that includes EL2:

- Stage 2 translation table entries that are used as part of a stage 1 translation table walk.

- Stage 2 translation table entries for translating the output address of a stage 1 translation.

Such entries might be held in intermediate TLB caching structures that are used during a translation table walk and that are distinct from the data caches in that they are not required to be invalidated as the result of writes of the data. The architecture makes no restriction on the form of these intermediate TLB caching structures when these caches are indexed by their input address. The architecture does not restrict having either:

- Translation table entry caching that is indexed by the physical address of the location holding the translation table entry.
- Translation table entry caching that is used for stage 1 translations and is indexed by the intermediate physical address of the location holding the translation table entry. However, FEAT\_nTLBPA allows software discoverability of whether such caches exist, such that if FEAT\_nTLBPA is implemented, such caching is not implemented.

If all of the following are true, a TLB maintenance instruction will ensure that any physical address or intermediate physical address indexed cached copies of translation table entries are invalidated for a PE:

- The TLB maintenance instruction applies to that PE with the context information that is relevant to translation table entry caching that is either:
- -Indexed by the physical address of the location holding the translation table entry.
- -Stage 1 translation information that is indexed by the intermediate physical address of the location holding the translation table entry.
- FEAT\_nTLBPA is not implemented.

Note

Any TLB caching based on the physical address or intermediate physical address obeys the other rules regarding the caching to TLB entries described in this manner, including restrictions on types of entries that cannot be held in a TLB, and a requirement that entries held in a TLB are distinguished by context information such as translation regime, VMID, and ASID.

The architecture does not intend to restrict the form of TLB caching structures used for holding translation table entries. In particular for translation regimes that involve two stages of translation, it recognizes that such caching structures might contain:

- At any level of the translation table walk, entries containing information from stage 1 translation table entries.
- In an implementation that includes EL2:
- -At any level of the translation table walk, entries containing information from stage 2 translation table entries.
- -At any level of the translation table walk, entries combining information from both stage 1 and stage 2 translation table entries.

Note

For the purpose of TLB maintenance, the term TLB entry denotes any structure, including temporary working registers in translation table walk hardware, that holds a translation table entry.

For the TLB maintenance instructions:

- If a TLB maintenance instruction is required to apply to stage 1 entries then it must apply to any cached entry in the caching structures that includes any stage 1 information that would be used to translate the address being invalidated, including any entry that combines information from both stage 1 and stage 2 translation table entries.

Note

- -Where stage 1 information has been cached in multiple TLB entries, as could occur from splintering a page when caching in the TLB, then the invalidation must apply to each cached entry containing stage 1 information from the page that is used to translate the address being invalidated, regardless of whether or not that cached entry would be used to translate the address being invalidated.
- -As stated in Global and process-specific translation table entries, translation table entries from levels of translation other than the final level are treated as being non-global. Arm expects that, in at least some implementations, cached copies of levels of the translation table walk other than the last level are tagged with their ASID, regardless of whether the final level is global. This means that TLB invalidations that involve the ASID require the ASID to match such entries to perform the required invalidation.
- If a TLB maintenance instruction is required to apply to stage 2 entries only, then:
- -It is not required to apply to caching structures that combine stage 1 and stage 2 translation table entries.
- -It must apply to caching structures that contain information only from stage 2 translation table entries.
- If a TLB maintenance instruction is required to apply to both stage 1 and stage 2 entries, then it must apply to any entry in the caching structures that includes information from either a stage 1 translation table entry or a stage 2 translation table entry, including any entry that combines information from both stage 1 and stage 2 translation table entries.

Table G5-23 summarizes the required effect of the AArch32 TLB maintenance instructions, that operate only on TLBs on the PE that executes the instruction. Additional TLB maintenance instructions that:

- Apply across all PEs in the same Inner Shareable domain. Each instruction shown in the table has an Inner Shareable equivalent, identified by an IS suffix. For example, the Inner Shareable equivalent of TLBIALL is TLBIALLIS. See also EL2 forced broadcasting of TLB maintenance instructions.
- Can apply to separate Instruction or Data TLBs. These instructions are indicated by a footnote to the table. Arm deprecates any use of these instructions.

## Note

- The architecture permits a TLB invalidation instruction to affect any unlocked entry in the TLB. Table G5-23 defines only the entries that each instruction must invalidate.
- All TLB instructions, including those that operate on a V A match, operate as described regardless of the value of SCTLR.M.

When interpreting the table:

Related operations Each instruction description applies also to any equivalent instruction that either:

- Applies to all PEs in the same Inner Shareable domain.
- Applies only to a data TLB, or only to an instruction TLB.

So, for example, the TLBIALL instruction description applies also to TLBIALLIS, ITLBIALL, and DTLBIALL.

TLB maintenance system instructions lists all of the TLB maintenance instructions.

Matches the VA Means the VA argument for the instruction must match the V A value in the TLB entry.

Matches the ASID Means the ASID argument for the instruction must match the ASID in use when the TLB entry was assigned.

## Matches the current VMID

Means the current VMID must match the VMID in use when the TLB entry was assigned.

The dependency on the VMID applies even when the value of HCR.VM is 0, including situations where there is no use of virtualization. However, VTTBR.VMID resets to zero, meaning there is a valid VMID from reset.

Execution at EL2 Descriptions of operations at EL2 apply only to implementations that include EL2.

For the definitions of the translation regimes referred to in the table see About VMSA v8-32.

## Table G5-23 Effect of the TLB maintenance instructions

| Instruction   | Executed from   | Executed from   | Effect, must invalidate any entry that matches all stated conditions a                                           |
|---------------|-----------------|-----------------|------------------------------------------------------------------------------------------------------------------|
|               | State           | Mode            |                                                                                                                  |
| TLBIALL b     | Secure          | PL1             | All entries for the Secure PL1&0 translation regime. That is, all entries that were allocated in Secure state.   |
|               | Non-secure      | PL1             | All entries for stage 1 of the Non-secure PL1&0 translation regime that match the current VMID.                  |
|               |                 | Hyp             | All entries for stage 1 or stage 2 of the Non-secure PL1&0 translation regime that match the current VMID.       |
| TLBIMVA b     | Secure          | PL1             | Any entry for the Secure PL1&0 translation regime that both:                                                     |
|               |                 |                 | • Matches the VA argument.                                                                                       |
|               |                 |                 | • Matches the ASID argument, or is global.                                                                       |
|               | Non-secure      | PL1 or Hyp      | Any entry for stage 1 of the Non-secure PL1&0 translation regime to which all of the following apply. The entry: |
|               |                 |                 | • Matches the VA argument.                                                                                       |
|               |                 |                 | • Matches the ASID argument, or is global.                                                                       |
|               |                 |                 | • Matches the current VMID.                                                                                      |

| Instruction            | Executed from                       | Executed from           | Effect, must invalidate any entry that matches all stated conditions                                                                                                                                                                                                                                                          |
|------------------------|-------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Instruction            | State                               | Mode                    | Effect, must invalidate any entry that matches all stated conditions                                                                                                                                                                                                                                                          |
| TLBIASID b             | Secure Non-secure                   | PL1 PL1 or Hyp          | Any entry for the Secure PL1&0 translation regime that matches the specified ASID and either: • Is from a level of lookup above the final level. • Is a non-global entry from the final level of lookup. Any entry for stage 1 of the Non-secure PL1&0 translation regime that both: • Matches the specified ASID and either: |
| TLBIMVAA               | Secure                              | PL1                     | Any entry for the Secure PL1&0 translation regime that matches theVA argument.                                                                                                                                                                                                                                                |
|                        | Non-secure                          | PL1 or Hyp              | Any entry for stage 1 of the Non-secure PL1&0 translation regime that both: • Matches the VA argument. • Matches the current VMID.                                                                                                                                                                                            |
| TLBIALLNSNH c          | Secure Non-secure                   | Monitor Hyp             | All entries for stage 1 or stage 2 of the Non-secure PL1&0 translation regime, regardless of the associated VMID.                                                                                                                                                                                                             |
| TLBIALLH c             | Secure Non-secure                   | Monitor Hyp             | All entries for the Non-secure EL2 translation regime. That is, any entry that was allocated in Non-secure state from Hyp mode.                                                                                                                                                                                               |
| TLBIMVAL               | Secure                              | PL1                     | Any entry for stage 1 of the Secure PL1&0 translation regime that is from the last level of the translation table walk and both: • Matches the VA argument.                                                                                                                                                                   |
|                        | Non-secure                          | PL1 or Hyp              | • Matches the ASID argument, or is global. Any entry for stage 1 of the Non-secure PL1&0 translation regime that is from the last level of the translation table walk and to which all of the following apply. The entry: • Matches the VA argument. • Matches the ASID argument, or is global.                               |
| TLBIMVAAL              | Secure                              | PL1                     | • Matches the current VMID. Any entry for stage 1 of the Secure PL1&0 translation regime that is from the last level of the translation table walk and matches the VAargument.                                                                                                                                                |
|                        | Non-secure                          |                         | Any entry for stage 1 of the Non-secure PL1&0 translation regime that is from the last level of the translation table walk and both: • Matches the VA argument.                                                                                                                                                               |
|                        |                                     | PL1 or Hyp              | • Matches the current VMID. Any entry for the Non-secure EL2 translation regime that matches theVA argument.                                                                                                                                                                                                                  |
| TLBIMVAH c TLBIMVALH c | Secure Non-secure Secure Non-secure | Monitor Hyp Monitor Hyp | Any entry for the Non-secure EL2 translation regime that is from the last level of the translation table walk and matches the VA argument.                                                                                                                                                                                    |

| Instruction     | Executed from   | Executed from   | Effect, must invalidate any entry that matches all stated conditions a                                                                 |
|-----------------|-----------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|
|                 | State           | Mode            |                                                                                                                                        |
| TLBIIPAS2 c, d  | Secure          | Monitor e       | Any entry for stage 2 of the PL1&0 translation regime that both: • Matches the IPA argument. • Matches the current VMID.               |
|                 | Non-secure      | Hyp             |                                                                                                                                        |
| TLBIIPAS2L c, d | Secure          | Monitor e       | Any entry for stage 2 of the PL1&0 translation regime that is from the last level of translation and both: • Matches the IPA argument. |
|                 | Non-secure      | Hyp             | • Matches the current VMID.                                                                                                            |

- b. The architecture defines variants of these instructions that apply only to instruction TLBs, and only to data TLBs. Arm deprecates any use of these variants. For more information, see the referenced description of the operation.
- c. Available only in an implementation that includes EL2. See also EL2 forced broadcasting of TLB maintenance instructions.
- d. This instruction is CONSTRAINED UNPREDICTABLE if executed in any AArch32 Secure privileged mode.
- e. This instruction executes as a NOP when SCR.NS == 0.

## G5.9.5.1 EL2 forced broadcasting of TLB maintenance instructions

In an implementation that includes EL2, when the value of HCR.FB is 1, the TLB maintenance instructions that are not broadcast across the Inner Shareable domain are forced to operate across the Inner Shareable domain when executed in a Non-secure PL1 mode. For example, when the value of HCR.FB is 1, a TLBIMVA instruction executed in a Non-secure PL1 mode performs the same invalidation as the invalidation performed by a TLBIMVAIS instruction.

## G5.9.5.2 TLB maintenance with different translation granule sizes

If a TLB maintenance instruction specifying a V A affecting the EL2 translation regime is broadcast from a PE using AArch32 to a PE using AArch64 using a translation granule size that is different from the AArch32 translation granule size for that same translation regime, the TLB maintenance instruction is not required to perform any invalidation on the recipient PE.

If a TLB maintenance instruction specifying a V A affecting the PL1 translation regime is broadcast from a PE using AArch32 using one translation granule size for that translation regime for a particular ASID, VMID (if applicable), and Security state, to a PE using AArch64 where EL1 for the same ASID, VMID (if applicable), and Security state, is using a translation granule size that is different from the AArch32 translation granule size, the TLB maintenance instruction is not required to perform any invalidation on the recipient PE.