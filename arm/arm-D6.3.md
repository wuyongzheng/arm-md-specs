## D6.3 Trace buffer Self-hosted mode

| I TSNMY   | When the Trace Buffer Unit is using Self-hosted mode, then:                                                                                                                                                                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FTWWP   | If all of the following apply, then the Effective value of TRBLIMITR_EL1.nVM is 0: • FEAT_TRBEv1p1 is implemented. • Self-hosted trace is enabled. • EL2 is implemented and enabled in the owning Security state. • The owning Exception level is EL1. • The Effective value of TRFCR_EL2.DnVM is 1. |

## D6.3.1 Behavior when address translation is enabled

| R XRNCQ   | If the Effective value of TRBLIMITR_EL1.nVM is 0, then the Base pointer , Limit pointer , and current write pointer are virtual addresses in the stage 1 translation regime of the owning translation regime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R CMDTG   | If the Effective value of TRBLIMITR_EL1.nVM is 0, then the stage 1 translation process for translating virtual addresses and checking for MMUfaults is identical to that for any other virtual address in the owning translation regime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| I GKBYK   | If the Effective value of TRBLIMITR_EL1.nVM is 0, thenR CMDTG means all of the following apply:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|           | • The virtual addresses are translated to stage 1 output addresses by stage 1 translation, and checked for stage 1 MMUfaults. The stage 1 output addresses are: - Physical address in the owning Security state if the owning translation regime has no stage 2 translation. - Intermediate physical addresses (IPAs) in the owning Security state if the owning translation regime has stage 2 translations. • If stage 1 translation is enabled for the owning translation regime, the memory type and, as applicable, Cacheability, Shareability, and Device type attributes, for stage 1 output addresses are defined by the translation table entries for the virtual address being written to. • If stage 1 translation is disabled for the owning translation regime, the memory type of the stage 1 output addresses is Device-nGnRnE, unless overridden by stage 2 controls. |

- RSJFRQ When the Trace Buffer Unit is enabled, the Trace Buffer Unit might prefetch and cache address translations for the translation regime of the owning Exception level, including when the owning Exception level is out-of-context.

IQXJZX

RSJFRQ means that, when the Trace Buffer Unit is enabled and the owning Exception level is a lower Exception level, then the Trace Buffer Unit might make memory accesses to translation table entries from the translation regime of the owning Exception level, using the settings of the System registers associated with that translation regime.

If the PE is not executing in the owning Security state, or the PE is executing at EL3 and SCR\_EL3.{NSE, NS} does not indicate the owning Security state, then the translation regime of the owning Exception level might not be the owning translation regime.

These memory accesses might be observed by other observers, to the extent that those accesses are required to be observed as determined by the Shareability and Cacheability of those translation table entries.

This is an exception to the rules in the section Speculative memory accesses from out-of-context translation regimes. See also Context switching.

## D6.3.2 Behavior when address translation is disabled

RPBZRZ If the Effective value of TRBLIMITR\_EL1.nVM is 1, the Base pointer , Limit pointer , and current write pointer

- Physical addresses in the owning Security state if the owning translation regime has no stage 2 translation.

are:

|         | • Intermediate physical addresses (IPAs) in the owning Security state if the owning translation regime has stage 2 translations. These addresses are output directly by stage 1 without any address translation. Stage 1 translation is disabled for writes to the trace buffer made by the Trace Buffer Unit.                                                                                                                                                   |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FJKLW | If the Effective value of TRBLIMITR_EL1.nVM is 1, then unless overridden by stage 2 controls, TRBMAR_EL1 defines the memory type, and, as applicable, Cacheability, Shareability, and Device type attributes, for the stage 1 output addresses.                                                                                                                                                                                                                  |
| I GLNHS | If the Effective value of TRBLIMITR_EL1.nVM is 1, the values of SCTLR_ELx.{C, M}for the owning translation regime are ignored for the purposes of determining the trace buffer Cacheability attributes.                                                                                                                                                                                                                                                          |
| S ZMPXW | If the Effective value of TRBLIMITR_EL1.nVM is 1 it is possible to generate mismatched attributes for a location from within the same stage 1 translation regime, using TRBMAR_EL1. Software must be aware of the consequences of and permitted behaviors when accessing a memory location with mismatched attributes. For more information, including a full definition of mismatched attributes and the permitted behaviors, see Mismatched memory attributes. |
| R MXRFD | If the Effective value of TRBLIMITR_EL1.nVM is 1 and TRBPTR_EL1[ OAMax : AArch64.PAMax() ] is nonzero, then a stage 1 Address Size fault is generated when the Trace Buffer Unit attempts to write to memory, where: • If FEAT_D128 is implemented, then OAMax is 55. • Otherwise, if FEAT_LPA is implemented or FEAT_LPA2 is implemented , then OAMax is 51. • Otherwise, OAMax is 47.                                                                          |
| R BRRRK | If the Effective value of TRBLIMITR_EL1.nVM is 1 and TRBPTR_EL1[63:( OAMax +1)] is nonzero when the Trace Buffer Unit attempts to write to the trace buffer, then one of the following occurs, and it is CONSTRAINED UNPREDICTABLE which: • Astage 1 Address Size fault is generated. • TRBPTR_EL1[63:( OAMax +1)] are ignored and treated as zero.                                                                                                              |

## D6.3.3 Effect of stage 2 translation

- RJCMKS If the owning translation regime has stage 2 translations, the stage 2 process of translating the stage 1 output intermediate

physical addresses and attributes to a physical address and attributes, and checking for MMU faults, is identical to that for any other intermediate physical address generated by the owning translation regime.

## IZSDMR For example:

- The intermediate physical addresses are translated to physical addresses by stage 2 translation, and checked for stage 2 MMU faults.
- If the Effective value of TRBLIMITR\_EL1.nVM is 1, meaning stage 1 translation is disabled, and the resulting IPA is translated by a stage 2 Block or Page descriptor with the AssuredOnly attribute set to 1, then the access translated by that descriptor generates a stage 2 Permission fault.
- The attributes from stage 1 are combined with the attributes from the stage 2 translation to generate the physical memory attributes.
- If the Effective value of HCR\_EL2.DC in the owning translation regime is 1, then stage 1 translation is disabled and the memory type produced by stage 1 is Normal Non-shareable, Inner Write-Back Cacheable Read-Allocate Write-Allocate, Outer Write-Back Cacheable Read-Allocate Write-Allocate, regardless of the values of SCTLR\_EL1.C and TRBMAR\_EL1.

## D6.3.4 Accesses to the trace buffer

- RJTVDD

Writes to the trace buffer by the Trace Buffer Unit are privileged writes within the owning translation regime.

RLDVQH

If ELx stage 1 translates an address and stage 1 Indirect permissions are used, the Trace Buffer Unit indirectly reads PIR\_ELx. The effect of PSTATE.PAN is not applied to the stage 1 Base permissions.

- RCQPGF If ELx stage 1 translates an address and stage 1 Overlay permissions are used, the effect of stage 1 Overlay permissions apply to the memory access and the Trace Buffer Unit indirectly reads POR\_ELx.
- RBMKDC If stage 2 translates an address and stage 2 Overlay permissions are used, the effect of stage 2 Overlay permissions apply to the memory access and the Trace Buffer Unit indirectly reads S2POR\_EL1.
- ITTKZQ For accesses made by the Trace Buffer Unit, the memory type and, as applicable, Cacheability, Shareability, and Device type attributes are determined by the translation tables or TRBMAR\_EL1. See:
- RCMDTG and IGKBYK, if translation is enabled.
- RFJKLW, if translation is disabled.
- RJCMKS and IZSDMR, if the owning translation regime has stage 2 translations.
- RFBKCC From Armv9.3, hardware management of the Access flag and dirty state for accesses made by the Trace Buffer Unit is controlled in the same way as explicit memory accesses in the trace buffer owning translation regime. Otherwise, it is IMPLEMENTATION DEFINED whether hardware management of the Access flag and dirty state for accesses made by the Trace Buffer Unit is controlled in the same way as explicit memory accesses in the trace buffer owning translation regime. This is discoverable by software using TRBIDR\_EL1.F. See Hardware management of the dirty state and Hardware management of the Access flag.
- RTNLBZ If FEAT\_HAFT is implemented, for an architecturally executed memory access that is translated by a translation stage with Table descriptor Access flag hardware management enabled, the Trace Buffer Unit is required to set the Access flag (AF) to 1 in all Table descriptors accessed during the translation table walk for that access that have the AF set to 0.
- RSHWSL If all of the following apply, the Trace Buffer Unit can speculatively update the translation table descriptor for any Page or Block in the trace buffer before writing data to it:
- Hardware management of dirty state by the Trace Buffer Unit is implemented.
- Hardware management of dirty state is enabled for the owning translation regime.
- The write is otherwise permitted.

This includes the case where a trace buffer management event means the Trace Buffer Unit stops writing data before the Page or Block is written to.

- RBWNRF The access granule for writes to the trace buffer by the Trace Buffer Unit is IMPLEMENTATION DEFINED, up to a maximum of 2KB, and might vary from time to time.
- RCMSNC Writes to any Device memory type by the Trace Buffer Unit occur once.
- RRZTDD Amemory access from the Trace Buffer Unit that crosses a Page or Block boundary to a memory location that has a different memory type or Shareability attribute results in CONSTRAINED UNPREDICTABLE behavior. In this case, the implementation performs one of the following behaviors:
- Each memory access generated by the Trace Buffer Unit uses the memory type and Shareability attribute associated with its own address.
- The access generates an Alignment fault caused by the memory type:
- -If only the stage 1 translation generated the mismatch, or there is only one stage of translation in the owning translation regime, the resulting trace buffer management event is a stage 1 Data Abort.
- -If only the stage 2 translation generated the mismatch, the resulting trace buffer management event is a stage 2 Data Abort.
- -If both stages of translation generate the mismatch, the resulting trace buffer management event is either a stage 1 Data Abort or a stage 2 Data Abort.
- The trace data is discarded and the current write pointer might not be updated.
- RXRQTN Amemory access from the Trace Buffer Unit to Device memory that crosses a boundary corresponding to the smallest translation granule size of the implementation causes CONSTRAINED UNPREDICTABLE behavior. In this case, the implementation performs one of the following behaviors:
- Each memory accesses generated by the Trace Buffer Unit is performed as if the boundary has no effect on the memory accesses.
- Each memory accesses generated by the Trace Buffer Unit is performed as if the boundary has no effect on the memory accesses except that there is no guarantee of ordering between it and other memory accesses.

RSKVWG

- The access generates an Alignment fault caused by the memory type:
- -If only the stage 1 translation causes the boundary to be crossed, or there is only one stage of translation in the owning translation regime, the resulting trace buffer management event is a stage 1 Data Abort.
- -If only the stage 2 translation causes the boundary to be crossed, the resulting trace buffer management event is a stage 2 Data Abort.
- -If both stages of translation cause the boundary to be crossed, the resulting trace buffer management event is either a stage 1 Data Abort or a stage 2 Data Abort.
- The trace data is discarded and the current write pointer might not be updated.

Note: The boundary is between two Device memory regions that are both:

- Of the size of the smallest implemented translation granule.
- Aligned to the size of the smallest implemented translation granule.
- IVKQBR Although the Trace Buffer Unit behaves as if trace data is written a byte at a time, it is not required to do so.

For example, RBWNRF and RCMSNC mean that if the memory type for the trace buffer is Device-nGnRnE, then all of the following apply:

- Writes are not repeated and not reordered.
- Awrite Completes only after it reaches its endpoint in the memory system.
- The access granule size at the endpoint in the memory system is not defined by the architecture. However, a specific implementation might define the granule to permit interoperability with specific devices.

The access granule is not required to be fixed. For example, the Trace Buffer Unit might output a smaller granule when flushing trace data to the trace buffer.

See also IQQKZF.

## D6.3.5 The owning translation regime

RDPGJG The owning translation regime is defined by the owning Security state and the owning Exception level.

## RHBZNT When the Trace Buffer Unit is enabled, the owning Security state is:

- Non-secure state if and only if at least one of the following is true:
- -EL3 is not implemented and the PE executes in Non-secure state.
- -The Effective value of MDCR\_EL3.NSTBE is 0 and MDCR\_EL3.NSTB is either 0b10 or 0b11 .
- Secure state if and only if Secure state is implemented and at least one of the following is true:
- -EL3 is not implemented and the PE executes in Secure state.
- -The Effective value of MDCR\_EL3.NSTBE is 0 and MDCR\_EL3.NSTB is either 0b00 or 0b01 .
- Realm state if and only if FEAT\_RME is implemented, MDCR\_EL3.NSTBE is 1, and MDCR\_EL3.NSTB is either 0b10 or 0b11 .

When the Trace Buffer Unit is enabled, the owning Exception level is:

- EL1 if and only if at least one of the following is true:
- -EL2 is not implemented in the owning Security state.
- -EL2 is disabled in the owning Security state.
- -MDCR\_EL2.E2TB is either 0b10 or 0b11 .
- EL2 if and only if all of the following is true:
- -EL2 is implemented and enabled in the owning Security state.
- -MDCR\_EL2.E2TB is 0b00 .

RXWDZV When the Trace Buffer Unit is enabled and the owning Exception level is EL1, all of the following apply:

- The owning translation regime is EL1&amp;0.
- If the Effective value of TRBLIMITR\_EL1.nVM is 0, the trace buffer pointer addresses are virtual addresses in the EL1&amp;0 translation regime using the current ASID from TTBRx\_EL1.
- If the Effective value of TRBLIMITR\_EL1.nVM is 1, the trace buffer pointer addresses are intermediate physical addresses.
- Intermediate physical addresses (whether from the output of stage 1, or the pointers, as applicable) are subject to stage 2 translation using the current VMID if EL2 is implemented and enabled and HCR\_EL2.VM is 1.
- If the Trace Buffer Unit is using Self-hosted mode, then the following are prohibited trace regions:

RSHXTV

IQCKVZ

- -EL3.
- -EL2.
- -EL0, if EL2 is implemented and enabled and HCR\_EL2.TGE is 1.

When the Trace Buffer Unit is enabled and the owning Exception level is EL2, all of the following apply:

- If the Effective value of HCR\_EL2.E2H is 0, the owning translation regime is EL2.
- If the Effective value of HCR\_EL2.E2H is 1, the owning translation regime is EL2&amp;0.
- If the Effective value of HCR\_EL2.E2H is 0 and the Effective value of TRBLIMITR\_EL1.nVM is 0, the trace buffer pointer addresses are virtual addresses in the EL2 translation regime.
- If the Effective value of HCR\_EL2.E2H is 1 and the Effective value of TRBLIMITR\_EL1.nVM is 0, the trace buffer pointer addresses are virtual addresses in the EL2&amp;0 translation regime using the current ASID from TTBRx\_EL2.
- If the Effective value of TRBLIMITR\_EL1.nVM is 1, the trace buffer pointer addresses are physical addresses.
- If the Trace Buffer Unit is using Self-hosted mode, then EL3 is a prohibited trace region.

Table D6-2 summarizes the owning translation regime. In this table:

Enabled

is the value of the function TraceBufferEnabled() .

NSTBE

is the Effective value of MDCR\_EL3.NSTBE.

NSTB

is the Effective value of MDCR\_EL3.NSTB.

E2TB

is the Effective value of MDCR\_EL2.E2TB.

EEL2

is the Effective value of SCR\_EL3.EEL2.

E2H

is the Effective value of HCR\_EL2.E2H.

The pseudocode function TraceBufferOwner describes this.

Table D6-2 Summary of owning translation regime (for all Exception levels using AArch64 state)

| Enabled   | NSTBE   | NSTB   | E2TB   | EEL2   | E2H   | Owning translation regime   |
|-----------|---------|--------|--------|--------|-------|-----------------------------|
| FALSE     | x       | x      | x      | x      | x     | Disabled                    |
| TRUE      | 0b0     | 0b0x   | x      | 0b0    | x     | Secure EL1&0                |
| TRUE      | 0b0     | 0b0x   | 0b00   | 0b1    | 0b0   | Secure EL2                  |
| TRUE      | 0b0     | 0b0x   | 0b00   | 0b1    | 0b1   | Secure EL2&0                |
| TRUE      | 0b0     | 0b0x   | 0b1x   | 0b1    | x     | Secure EL1&0                |
| TRUE      | 0b0     | 0b1x   | 0b00   | x      | 0b0   | Non-secure EL2              |
| TRUE      | 0b0     | 0b1x   | 0b00   | x      | 0b1   | Non-secure EL2&0            |
| TRUE      | 0b0     | 0b1x   | 0b1x   | x      | x     | Non-secure EL1&0            |
| TRUE      | 0b1     | 0b1x   | 0b00   | x      | 0b0   | Realm EL2                   |
| TRUE      | 0b1     | 0b1x   | 0b00   | x      | 0b1   | Realm EL2&0                 |
| TRUE      | 0b1     | 0b1x   | 0b1x   | x      | x     | Realm EL1&0                 |

RMFFGX

When the Trace Buffer Unit is enabled and the owning Security state is Non-secure state, Secure state and Realm state are prohibited trace regions.

RVGWJN

When the Trace Buffer Unit is enabled and the owning Security state is Secure state, Non-secure state and Realm state are prohibited trace regions.

RRRBFN

IDCRYN

When the Trace Buffer Unit is enabled and the owning Security state is Realm state, Non-secure state and Secure state are prohibited trace regions.

FEAT\_TRF provides additional controls to define Trace Prohibited regions.

The following table summarizes the Trace Prohibited regions, by Exception level and state, when all of the following apply:

- TraceBufferEnabled() is TRUE.
- EL3, Non-secure EL2, and Secure EL2 are all implemented.
- EL3 is using AArch64.
- FEAT\_RME is implemented.

In this table:

NSE

is the Effective value of SCR\_EL3.NSE.

NS

is the Effective value of SCR\_EL3.NS.

RLTE

is the Effective value of MDCR\_EL3.RLTE.

STE

is the Effective value of MDCR\_EL3.STE.

NSTBE

is the Effective value of MDCR\_EL3.NSTBE.

NSTB

is the Effective value of MDCR\_EL3.NSTB.

E2TB

is the Effective value of MDCR\_EL2.E2TB.

EEL2

is the Effective value of SCR\_EL3.EEL2.

TGE

is the Effective value of HCR\_EL2.TGE.

Reserved values are not shown in the table.

The EL3, EL2, EL1, EL0 columns show which control, if any, enables tracing at the Exception level. In these columns:

P

means tracing is prohibited.

E2TRE

means tracing is allowed if TRFCR\_EL2.E2TRE is 1 and prohibited otherwise.

E1TRE

means tracing is allowed if TRFCR\_EL1.E1TRE is 1 and prohibited otherwise.

E0HTRE

means tracing is allowed if TRFCR\_EL2.E0HTRE is 1 and prohibited otherwise.

E0TRE

means tracing is allowed if TRFCR\_EL1.E0TRE is 1 and prohibited otherwise.

The pseudocode function TraceAllowed describes this.

| NSE   | NS   | RLTE   | STE   | NSTBE   | NSTB   | E2TB   | EEL2   | TGE   | EL3   | EL2   | EL1   | EL0    |
|-------|------|--------|-------|---------|--------|--------|--------|-------|-------|-------|-------|--------|
| 0b0   | 0b0  | x      | 0b0   | x       | x      | x      | x      | x     | P     | P     | P     | P      |
| 0b0   | 0b0  | x      | 0b1   | 0b0     | 0b0x   | x      | 0b0    | x     | P     | n/a   | E1TRE | E0TRE  |
| 0b0   | 0b0  | x      | 0b1   | 0b0     | 0b0x   | 0b00   | 0b1    | 0b0   | P     | E2TRE | E1TRE | E0TRE  |
| 0b0   | 0b0  | x      | 0b1   | 0b0     | 0b0x   | 0b00   | 0b1    | 0b1   | P     | E2TRE | n/a   | E0HTRE |

| NSE   | NS   | RLTE   | STE   | NSTBE   | NSTB   | E2TB   | EEL2   | TGE   | EL3   | EL2   | EL1   | EL0    |
|-------|------|--------|-------|---------|--------|--------|--------|-------|-------|-------|-------|--------|
| 0b0   | 0b0  | x      | 0b1   | 0b0     | 0b0x   | 0b1x   | 0b1    | 0b0   | P     | P     | E1TRE | E0TRE  |
| 0b0   | 0b0  | x      | 0b1   | 0b0     | 0b0x   | 0b1x   | 0b1    | 0b1   | P     | P     | n/a   | P      |
| 0b0   | 0b0  | x      | 0b1   | x       | 0b1x   | x      | x      | x     | P     | P     | P     | P      |
| 0b0   | 0b1  | x      | x     | 0b0     | 0b0x   | x      | x      | x     | P     | P     | P     | P      |
| 0b0   | 0b1  | x      | x     | 0b0     | 0b1x   | 0b00   | x      | 0b0   | P     | E2TRE | E1TRE | E0TRE  |
| 0b0   | 0b1  | x      | x     | 0b0     | 0b1x   | 0b00   | x      | 0b1   | P     | E2TRE | n/a   | E0HTRE |
| 0b0   | 0b1  | x      | x     | 0b0     | 0b1x   | 0b1x   | x      | 0b0   | P     | P     | E1TRE | E0TRE  |
| 0b0   | 0b1  | x      | x     | 0b0     | 0b1x   | 0b1x   | x      | 0b1   | P     | P     | n/a   | P      |
| 0b0   | 0b1  | x      | x     | 0b1     | 0b1x   | x      | x      | x     | P     | P     | P     | P      |
| 0b1   | 0b1  | 0b0    | x     | x       | x      | x      | x      | x     | P     | P     | P     | P      |
| 0b1   | 0b1  | 0b1    | x     | 0b0     | x      | x      | x      | x     | P     | P     | P     | P      |
| 0b1   | 0b1  | 0b1    | x     | 0b1     | 0b1    | 0b00   | x      | 0b0   | P     | E2TRE | E1TRE | E0TRE  |
| 0b1   | 0b1  | 0b1    | x     | 0b1     | 0b1    | 0b00   | x      | 0b1   | P     | E2TRE | n/a   | E0HTRE |
| 0b1   | 0b1  | 0b1    | x     | 0b1     | 0b1    | 0b1x   | x      | 0b0   | P     | P     | E1TRE | E0TRE  |
| 0b1   | 0b1  | 0b1    | x     | 0b1     | 0b1    | 0b1x   | x      | 0b1   | P     | P     | n/a   | P      |

RMCYDC

When the Trace Buffer Unit is disabled or not using Self-hosted mode, the owning translation regime, owning Security state, and owning Exception level are not defined.

## D6.3.6 Cache and TLB operations

- IWYVXK Translations used by the Trace Buffer Unit might be cached in a TLB.
- RGQJMC TLB maintenance operations that affect the TLB of the PE also affect any TLB caching translations for the Trace Buffer Unit of that PE.
- RRNPNM The PE is permitted, but not required, to cache all translations used by the Trace Buffer Unit in TLB caching structures that combine stage 1 and stage 2 of the translation. This includes when the Effective value of TRBLIMITR\_EL1.nVM is 1 and the owning translation regime has stage 2 translations.

SLSZDR

RDNFWB

When the Effective value of TRBLIMITR\_EL1.nVM is 1 and the owning translation regime has stage 2 translations, the Trace Buffer Unit uses intermediate physical addresses (IPAs). RRNPNM permits, but does not require, such translations to be cached in a TLB in such a way that an IPAS2 TLB maintenance operation is not sufficient to invalidate the cached copies. In this case, there is no V A for the translation.

If the Effective value of TRBLIMITR\_EL1.nVM is 1 and the owning translation regime has stage 2 translations, then the following code executed at EL2 or above is sufficient to invalidate all cached copies of the stage 2 translations used by the Trace Buffer Unit of the IPA held in Xt for the current VMID:

```
TLBI IPAS2E1, Xt DSB TLBI VMALLE1
```

Equivalent architectural requirements apply to the IPAS2L instruction, except that the only TLB entries that must be invalidated by an IPAS2L instruction are those that come from the final level of the translation table lookup.

Equivalent sequences guaranteed to invalidate all entries invalidated by the above code sequence can be used, such as TLBI ALL or TLBI VMALLS1S2 .

Cache maintenance operations that affect the caches of the PE also affect data caching by the Trace Buffer Unit of that PE.

IMZQPT

RGQJMC and RDNFWB mean that the completion of any cache or TLB maintenance instruction includes its completion on all Trace Buffer Units for PEs that are affected by both the instruction and the DSB operation that is required to guarantee visibility of the maintenance instruction. See Synchronization litmus tests for more information.

## D6.3.7 Self-hosted mode and MEC

RRKSNW

If FEAT\_MEC is implemented and the Trace Buffer Unit is using Self-hosted mode, accesses made by the Trace Buffer Unit to the trace buffer are associated with a MECID that is determined by the owning translation regime, owning Security state, and owning Exception level. For more information, see Memory Encryption Contexts.

## D6.3.8 Self-hosted mode and MPAM

RWXSYG

If FEAT\_MPAM is implemented and the Trace Buffer Unit is using Self-hosted mode, then the MPAM information for accesses made by the Trace Buffer Unit to the trace buffer use the MPAM values of the owning Exception level and owning Security state .

IXLNWD

For example, if the owning Exception level is EL2 the trace buffer writes use MPAM2\_EL2.PARTID\_D, MPAM2\_EL2.PMG\_D, with MPAM\_NS or MPAM\_SP reflecting the owning Security state. See also About MPAM.