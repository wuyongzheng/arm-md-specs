## G5.2 The effects of disabling address translation stages on VMSAv8-32 behavior

About VMSA v8-32 defines the translation regimes and the associated stages of address translation, each of which has its own System registers for control and configuration. VMSAv8-32 includes an enable bit for each stage of address translation, as follows:

- SCTLR.M, in the Secure instance of the register, controls Secure PL1&amp;0 stage 1 address translation.
- SCTLR.M, in the Non-secure instance of the register, controls Non-secure PL1&amp;0 stage 1 address translation.
- HCR.VM controls Non-secure PL1&amp;0 stage 2 address translation.
- HSCTLR.M controls Non-secure EL2 stage 1 address translation.

## Note

- The descriptions throughout this chapter describe address translation as seen by Exception levels that are using AArch32. However, for the Non-secure PL1&amp;0 translation regime, the stage 2 translation:
- -Is controlled by the HCR if EL2 is using AArch32.
- -Is controlled by the HCR\_EL2 if EL2 is using AArch64.

For this reason, links to the HCR link to a table that disambiguates between the AArch32 HCR and the AArch64 HCR\_EL2.

- If EL2 is using AArch64, then the equivalent of the Non-secure EL2 translation regime is described in The AArch64 Virtual Memory System Architecture, not in this chapter.

The following sections describe the effect on VMSAv8-32 behavior of disabling each stage of translation:

- VMSAv8-32 behavior when stage 1 address translation is disabled.
- VMSAv8-32 behavior when stage 2 address translation is disabled.
- Behavior of instruction fetches when all associated address translations are disabled.

Enabling stages of address translation gives more information about each stage of address translation, in particular after a reset on an implementation that includes EL3.

## G5.2.1 VMSAv8-32 behavior when stage 1 address translation is disabled

When stage 1 address translation is disabled, memory accesses that would otherwise be translated by that stage of address translation are treated as follows:

## Non-secure PL1 and EL0 accesses when EL2 is implemented and HCR.DC is set to 1

In an implementation that includes EL2, for an access from a Non-secure PL1 or EL0 mode when HCR.DC is set to 1, the stage 1 translation assigns the Normal Non-shareable, Inner Write-Back Read-Allocate Write-Allocate, Outer Write-Back Read-Allocate Write-Allocate memory attributes.

When FEAT\_XS is implemented and HCR.DC is 1, the XS attribute is set to 0 at stage 1 of the translation. Otherwise, the XS attribute is set to 1 at stage 1 of the translation.

See also Effect of the HCR.DC field.

## All other accesses

For all other accesses, when a stage 1 address translation is disabled, the assigned attributes depend on whether the access is a data access or an instruction access, as follows:

## Data access

The stage 1 translation assigns the Device-nGnRnE memory type.

## Instruction access

The stage 1 translation assigns Normal memory attribute, with the Cacheability and Shareability attributes determined by the value of:

- The Secure instance of SCTLR.I for the Secure PL1&amp;0 translation regime.
- The Non-secure instance of SCTLR.I for the Non-secure PL1&amp;0 translation regime.
- HSCTLR.I for the Non-secure EL2 translation regime.

In these cases, the meaning of the I field is as follows:

## When I is set to 0

The stage 1 translation assigns the attributes Outer Shareable, Non-cacheable.

## When I is set to 1

The stage 1 translation assigns the attributes Inner Write-Through Read-Allocate No Write-Allocate, Outer Write-Through Read-Allocate No Write-Allocate Cacheable.

Note

On some implementations, if the SCTLR.TRE field is set to 0 then this behavior can be changed by the remap settings in the memory remap registers. The details of TEX remap when SCTLR.TRE is set to 0 are IMPLEMENTATION DEFINED, see SCTLR.TRE, SCTLR.M, and the effect of the TEX remap registers.

For this stage of translation, no memory access permission checks are performed, and therefore no MMU Permission faults relating to this stage of translation can be generated.

Note

Alignment checking is performed, and therefore Alignment faults can occur.

For every access, when stage 1 translation is disabled, the output address of the stage 1 translation is equal to the input address. This is called a flat address mapping. If the implementation supports output addresses of more than 32 bits then the output address bits above bit[31] are zero. For example, for a V A to PA translation on an implementation that supports 40-bit PAs, PA[39:32] is 0x00 .

For a Non-secure PL1 or EL0 access, if the PL1&amp;0 stage 2 address translation is enabled, the stage 1 memory attribute assignments and output address can be modified by the stage 2 translation.

See also Behavior of instruction fetches when all associated address translations are disabled.

## G5.2.1.1 Effect of the HCR.DC field

The HCR.DC field determines the default memory attributes assigned for the first stage of the Non-secure PL1&amp;0 translation regime when that stage of translation is disabled.

When executing in a Non-secure PL1 or EL0 mode with HCR.DC set to 1:

- For all purposes other than reading the value of the SCTLR, the PE behaves as if the value of the SCTLR.M field is 0. This means Non-secure PL1&amp;0 stage 1 address translation is disabled.
- For all purposes other than reading the value of the HCR, the PE behaves as if the value of the HCR.VM field is 1. This means Non-secure PL1&amp;0 stage 2 address translation is enabled.

The effect of HCR.DC might be held in TLB entries associated with a particular VMID. Therefore, if software executing at EL2 changes the HCR.DC value without also changing the current VMID, it must also invalidate all TLB entries associated with the current VMID. Otherwise, the behavior of Non-secure software executing at EL1 or EL0 is CONSTRAINED UNPREDICTABLE, see CONSTRAINED UNPREDICTABLE behaviors due to caching of System register control or data values.

## G5.2.1.2 Effect of disabling translation on maintenance and address translation instructions

Cache maintenance instructions act on the target cache whether address translation is enabled or not, and regardless of the values of the memory attributes. However, if a stage of translation is disabled, they use the flat address mapping for that stage, and all mappings are considered global.

TLB invalidate operations act on the target TLB whether address translation is enabled or not.

When the Non-secure PL1&amp;0 stage 1 address translation is disabled, any ATS1C** or ATS12NSO** address translation instruction that accesses the Non-secure state translation reflects the effect of the HCR.DC field.

## G5.2.2 VMSAv8-32 behavior when stage 2 address translation is disabled

When stage 2 address translation is disabled:

- The IPA output from the stage 1 translation maps flat to the PA.
- The memory attributes and permissions from the stage 1 translation apply to the PA.

If the stage 1 address translation and the stage 2 address translation are both disabled, see Behavior of instruction fetches when all associated address translations are disabled.

## G5.2.3 Behavior of instruction fetches when all associated address translations are disabled

The information in this section applies to memory accesses:

- From Secure PL1 and EL0 modes, when the Secure PL1&amp;0 stage 1 address translation is disabled.

- From Hyp mode, when the Non-secure EL2 stage 1 address translation is disabled.

- From Non-secure PL1 and EL0 modes, when all of the following apply:

- The Non-secure PL1&amp;0 stage 1 address translation is disabled.

- The Non-secure PL1&amp;0 stage 2 address translation is disabled.

- HCR.DC is set to 0.

In these cases, when execution is in AArch32 state a memory location might be accessed as a result of an instruction fetch if either:

- The memory location is in the same 4KB block of memory, aligned to 4KB, as an instruction which a simple sequential execution of the program either requires to be fetched now or has required to be fetched since the last reset, or is in the 4KB block immediately following such a block.

- The memory location is the target of a direct branch that a simple sequential execution of the program would have taken since the most recent of:

- The last reset.

- If the branch predictor is architecturally invisible, the last synchronization of instruction cache maintenance targeting the address of the branch instruction.

- If the branch predictor is not architecturally invisible, the last synchronization of branch predictor maintenance targeting the address of the branch instruction.

These accesses can be caused by speculative instruction fetches, regardless of whether the prefetched instruction is committed for execution.

Note

To ensure architectural compliance, software must ensure that both of the following apply:

- Instructions that will be executed when address translation is disabled are located in 4KB blocks of the address space that contain only memory that is tolerant to speculative accesses.

- Each 4KB block of the address space that immediately follows a 4KB block that holds instructions that will be executed when address translation is disabled also contains only memory that is tolerant to speculative accesses.

## G5.2.4 Enabling stages of address translation

On powerup or Warm reset, only the SCTLR.M field for the Exception level and Security state entered on reset is reset to 0, disabling address translation for the initial state of the PE. All other SCTLR.M and HSCTLR.M fields that are implemented are UNKNOWN after the reset.

This means, on powerup or reset:

- On an implementation that includes EL3, where EL3 is using AArch32:
- -The PL1&amp;0 stage 1 address translation enable bit, SCTLR.M, is banked, meaning there are separate enables for operation in Secure and Non-secure state.
- -If EL3 is using AArch32, only the Secure instance of the SCTLR.M field resets to 0, disabling the Secure state PL1&amp;0 stage 1 address translation. The reset value of the Non-secure instance of SCTLR.M is UNKNOWN.
- On an implementation that includes EL2, where EL2 is using AArch32, the HSCTLR.M field, that controls the Non-secure EL2 stage 1 address translation:
- -If the implementation does not include EL3, resets to 0.
- -Otherwise, is UNKNOWN.
- On an implementation that does not include either EL2 or EL3, there is a single stage of translation. This is controlled by SCTLR.M, that resets to 0.

Note

If, for the software that enables or disables a stage of address translation, the input address of a stage 1 translation differs from the output address of that stage 1 translation, and the software is running in translation regime that is affected by that stage of translation, then the requirement to synchronize changes to the System registers means it is uncertain where in the instruction stream the change of the translation takes place. For this reason, Arm strongly recommends that the input address and the output address are identical in this situation.