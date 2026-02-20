## C5.6 A64 System instructions for prediction restriction

This section lists the A64 System instructions for prediction restriction.

## C5.6.1 CFP RCTX, Control Flow Prediction Restriction by Context

The CFP RCTX characteristics are:

## Purpose

Control Flow Prediction Restriction by Context applies to all Control Flow Prediction Resources that predict execution based on information gathered within the target execution context or contexts.

Control flow predictions determined by the actions of code in the target execution context or contexts appearing in program order before the instruction cannot exploitatively control speculative execution occurring after the instruction is complete and synchronized.

This instruction is guaranteed to be complete following a DSB that covers both read and write behavior on the same PE as executed the original restriction instruction, and a subsequent context synchronization event is required to ensure that the effect of the completion of the instructions is synchronized to the current execution.

Note

This instruction does not require the invalidation of prediction structures so long as the behavior described for completion of this instruction is met by the implementation.

Onsomeimplementations the instruction is likely to take a significant number of cycles to execute. This instruction is expected to be used very rarely, such as on the roll-over of an ASID or VMID, but should not be used on every context switch.

## Configuration

This system instruction is present only when FEAT\_SPECRES is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CFP RCTX are UNDEFINED.

## Attributes

CFP RCTX is a 64-bit System instruction.

## Field descriptions

<!-- image -->

## Bits [63:49]

Reserved, RES0.

## GVMID, bit [48]

Execution of this instruction applies to all VMIDs or a specified VMID.

| GVMID   | Meaning                                                              |
|---------|----------------------------------------------------------------------|
| 0b0     | Applies to specified VMIDfor an EL0 or EL1 target execution context. |
| 0b1     | Applies to all VMIDs for an EL0 or EL1 target execution context.     |

For target execution contexts other than EL0 or EL1, this field is RES0.

If the instruction is executed at EL0 or EL1, this field has an Effective value of 0.

If EL2 is not implemented or not enabled for the target Security state, this field is RES0.

## VMID, bits [47:32]

Only applies when bit[48] is 0 and the target execution context is either:

- EL1.
- EL0 when the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

Otherwise this field is RES0.

When the instruction is executed at EL1, this field is treated as the current VMID.

When the instruction is executed at EL0 and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, this field is treated as the current VMID.

When the instruction is executed at EL0 and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field is ignored.

If EL2 is not implemented or not enabled for the target Security state, this field is RES0.

If the implementation supports 16 bits of VMID, then the upper 8 bits of the VMID must be written to 0 by software when the context being affected only uses 8 bits.

## Bits [31:28]

Reserved, RES0.

## NSE, bit [27]

## When FEAT\_RME is implemented:

Together with the NS field, selects the Security state.

For a description of the values derived by evaluating NS and NSE together, see CFP\_RCTX.NS.

## Otherwise:

Reserved, RES0.

## NS, bit [26]

## When FEAT\_RME is implemented:

Together with the NSE field, selects the Security state.

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

Some Effective values are determined by the current Security state:

- When executed in Secure state, the Effective value of NSE is 0.
- When executed in Non-secure state, the Effective value of {NSE, NS} is {0, 1}.
- When executed in Realm state, the Effective value of {NSE, NS} is {1, 1}.

This instruction is treated as a NOP when executed at EL3 and either:

- CFP\_RCTX.{NSE, NS} selects a reserved value.
- CFP\_RCTX.{NSE, NS} == {1, 0} and CFP\_RCTX.EL has a value other than 0b11 .

## Otherwise:

Security State.

| NS   | Meaning           |
|------|-------------------|
| 0b0  | Secure state.     |
| 0b1  | Non-secure state. |

When executed in Non-secure state, the Effective value of NS is 1.

## EL, bits [25:24]

Exception Level. Indicates the Exception level of the target execution context.

| EL   | Meaning   | Applies when            |
|------|-----------|-------------------------|
| 0b00 | EL0.      |                         |
| 0b01 | EL1       |                         |
| 0b10 | EL2       | FEAT_EL2 is implemented |
| 0b11 | EL3       | FEAT_EL3 is implemented |

If the instruction is executed at an Exception level lower than the specified level, or is specified to apply to a combination of Exception level and Security state that is not implemented, this instruction is treated as a NOP.

## Bits [23:17]

Reserved, RES0.

## GASID, bit [16]

Execution of this instruction applies to all ASIDs or a specified ASID.

| GASID   | Meaning                                                        |
|---------|----------------------------------------------------------------|
| 0b0     | Applies to specified ASID for an EL0 target execution context. |
| 0b1     | Applies to all ASIDs for an EL0 target execution context.      |

For target execution contexts other than EL0, this field is RES0.

If the instruction is executed at EL0, this field has an Effective value of 0.

## ASID, bits [15:0]

Only applies for an EL0 target execution context and when bit[16] is 0.

Otherwise, this field is RES0.

When the instruction is executed at EL0, this field is treated as the current ASID.

If the implementation supports 16 bits of ASID, then the upper 8 bits of the ASID must be written to 0 by software when the context being affected only uses 8 bits.

## Executing CFP RCTX

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

CFP RCTX, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b011 | 0b0111 | 0b0011 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_SPECRES) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && SCTLR_EL1.EnRCTX == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGITR_EL2.CFPRCTX == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.EnRCTX == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.RestrictPrediction(X[t, 64], RestrictType_ControlFlow); elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.CFPRCTX == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.RestrictPrediction(X[t, 64], RestrictType_ControlFlow); elsif PSTATE.EL == EL2 then AArch64.RestrictPrediction(X[t, 64], RestrictType_ControlFlow); elsif PSTATE.EL == EL3 then AArch64.RestrictPrediction(X[t, 64], RestrictType_ControlFlow);
```

## C5.6.2 COSP RCTX, Clear Other Speculative Prediction Restriction by Context

The COSP RCTX characteristics are:

## Purpose

Clear Other Speculative Prediction Restriction by Context applies to all prediction resources not managed by other speculation restriction System instructions.

The actions of code in the target execution context or contexts appearing in program order before the instruction cannot exploitatively control any predictions occurring after the instruction is complete and synchronized.

This instruction applies to all speculative access except:

- Cache Prefetch predictions.
- Control Flow predictions.
- Data Value predictions.

This instruction is guaranteed to be complete following a DSB that covers both read and write behavior on the PE that executed the original restriction instruction, and a subsequent Context Synchronization event is required to ensure that the effect of the completion of the instructions is synchronized to the current execution.

Note

This instruction does not require the invalidation of Cache Allocation Resources so long as the behavior described for completion of this instruction is met by the implementation.

Onsomeimplementations, the instruction is likely to take a significant number of cycles to execute. This instruction is expected to be used rarely, such as on the roll-over of an ASID or VMID, but should not be used on every context switch.

This instruction applies to speculative accesses resulting from address predictions.

## Configuration

This system instruction is present only when FEAT\_SPECRES2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to COSP RCTX are UNDEFINED.

## Attributes

COSP RCTX is a 64-bit System instruction.

## Field descriptions

<!-- image -->

## Bits [63:49]

Reserved, RES0.

## GVMID, bit [48]

Execution of this instruction applies to all VMIDs or a specified VMID.

| GVMID   | Meaning                                                              |
|---------|----------------------------------------------------------------------|
| 0b0     | Applies to specified VMIDfor an EL0 or EL1 target execution context. |
| 0b1     | Applies to all VMIDs for an EL0 or EL1 target execution context.     |

For target execution contexts other than EL0 and EL1, this field is RES0.

If the instruction is executed at EL0 or EL1, this field has an Effective value of 0.

If EL2 is not implemented or not enabled for the target Security state, this field is RES0.

## VMID, bits [47:32]

Only applies when bit[48] is 0 and the target execution context is either:

- EL1.
- EL0 when the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

Otherwise this field is RES0.

When the instruction is executed at EL1, this field is treated as the current VMID.

When the instruction is executed at EL0 and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, this field is treated as the current VMID.

When the instruction is executed at EL0 and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field is ignored.

If EL2 is not implemented or not enabled for the target Security state, this field is RES0.

If the implementation supports 16 bits of VMID, then the upper 8 bits of the VMID must be written to 0 by software when the context being affected only uses 8 bits.

## Bits [31:28]

Reserved, RES0.

## NSE, bit [27]

## When FEAT\_RME is implemented:

Together with the NS field, selects the Security state.

For a description of the values derived by evaluating NS and NSE together, see COSP\_RCTX.NS.

## Otherwise:

Reserved, RES0.

## NS, bit [26]

## When FEAT\_RME is implemented:

Together with the NSE field, selects the Security state.

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

Some Effective values are determined by the current Security state:

- When executed in Secure state, the Effective value of NSE is 0.
- When executed in Non-secure state, the Effective value of {NSE, NS} is {0, 1}.
- When executed in Realm state, the Effective value of {NSE, NS} is {1, 1}.

This instruction is treated as a NOP when executed at EL3 and either:

- COSP\_RCTX.{NSE, NS} selects a reserved value.
- COSP\_RCTX.{NSE, NS} == {1, 0} and COSP\_RCTX.EL has a value other than 0b11 .

## Otherwise:

Security State.

| NS   | Meaning           |
|------|-------------------|
| 0b0  | Secure state.     |
| 0b1  | Non-secure state. |

When executed in Non-secure state, the Effective value of NS is 1.

## EL, bits [25:24]

Exception Level. Indicates the Exception level of the target execution context.

| EL   | Meaning   | Applies when            |
|------|-----------|-------------------------|
| 0b00 | EL0.      |                         |
| 0b01 | EL1       |                         |
| 0b10 | EL2       | FEAT_EL2 is implemented |
| 0b11 | EL3       | FEAT_EL3 is implemented |

If the instruction is executed at an Exception level lower than the specified level, or is specified to apply to a combination of Exception level and Security state that is not implemented, this instruction is treated as a NOP.

## Bits [23:17]

Reserved, RES0.

## GASID, bit [16]

Execution of this instruction applies to all ASIDs, or a specified ASID.

| GASID   | Meaning                                                        |
|---------|----------------------------------------------------------------|
| 0b0     | Applies to specified ASID for an EL0 target execution context. |
| 0b1     | Applies to all ASIDs for an EL0 target execution context.      |

For target execution contexts other than EL0, this field is RES0.

If the instruction is executed at EL0, this field has an Effective value of 0.

## ASID, bits [15:0]

Only applies to an EL0 target execution context and when bit[16] is 0.

Otherwise, this field is RES0.

When the instruction is executed at EL0, this field is treated as the current ASID.

If the implementation supports 16 bits of ASID, then the upper 8 bits of the ASID must be written to 0 by software when the context being affected only uses 8 bits.

## Executing COSP RCTX

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

COSP RCTX, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b011 | 0b0111 | 0b0011 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_SPECRES2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && SCTLR_EL1.EnRCTX == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGITR_EL2.COSPRCTX == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.EnRCTX == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.RestrictPrediction(X[t, 64], RestrictType_Other); elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.COSPRCTX == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.RestrictPrediction(X[t, 64], RestrictType_Other); elsif PSTATE.EL == EL2 then AArch64.RestrictPrediction(X[t, 64], RestrictType_Other); elsif PSTATE.EL == EL3 then AArch64.RestrictPrediction(X[t, 64], RestrictType_Other);
```

## C5.6.3 CPP RCTX, Cache Prefetch Prediction Restriction by Context

The CPP RCTX characteristics are:

## Purpose

Cache Prefetch Prediction Restriction by Context applies to all Cache Allocation Resources that predict cache allocations based on information gathered within the target execution context or contexts.

The actions of code in the target execution context or contexts appearing in program order before the instruction cannot exploitatively control cache prefetch predictions occurring after the instruction is complete and synchronized.

This instruction applies to all:

- Instruction caches.
- Data caches.
- TLB prefetching hardware used by the executing PE that applies to the supplied context or contexts.

This instruction is guaranteed to be complete following a DSB that covers both read and write behavior on the same PE as executed the original restriction instruction, and a subsequent context synchronization event is required to ensure that the effect of the completion of the instructions is synchronized to the current execution.

Note

This instruction does not require the invalidation of Cache Allocation Resources so long as the behavior described for completion of this instruction is met by the implementation.

Onsomeimplementations the instruction is likely to take a significant number of cycles to execute. This instruction is expected to be used very rarely, such as on the roll-over of an ASID or VMID, but should not be used on every context switch.

## Configuration

This system instruction is present only when FEAT\_SPECRES is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CPP RCTX are UNDEFINED.

## Attributes

CPP RCTX is a 64-bit System instruction.

## Field descriptions

<!-- image -->

## Bits [63:49]

Reserved, RES0.

## GVMID, bit [48]

Execution of this instruction applies to all VMIDs or a specified VMID.

| GVMID   | Meaning                                                              |
|---------|----------------------------------------------------------------------|
| 0b0     | Applies to specified VMIDfor an EL0 or EL1 target execution context. |
| 0b1     | Applies to all VMIDs for an EL0 or EL1 target execution context.     |

For target execution contexts other than EL0 and EL1, this field is RES0.

If the instruction is executed at EL0 or EL1, this field has an Effective value of 0.

If EL2 is not implemented or not enabled for the target Security state, this field is RES0.

## VMID, bits [47:32]

Only applies when bit[48] is 0 and the target execution context is either:

- EL1.
- EL0 when the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

Otherwise this field is RES0.

When the instruction is executed at EL1, this field is treated as the current VMID.

When the instruction is executed at EL0 and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, this field is treated as the current VMID.

When the instruction is executed at EL0 and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field is ignored.

If EL2 is not implemented or not enabled for the target Security state, this field is RES0.

If the implementation supports 16 bits of VMID, then the upper 8 bits of the VMID must be written to 0 by software when the context being affected only uses 8 bits.

## Bits [31:28]

Reserved, RES0.

## NSE, bit [27]

## When FEAT\_RME is implemented:

Together with the NS field, selects the Security state.

For a description of the values derived by evaluating NS and NSE together, see CPP\_RCTX.NS.

## Otherwise:

Reserved, RES0.

## NS, bit [26]

## When FEAT\_RME is implemented:

Together with the NSE field, selects the Security state.

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

Some Effective values are determined by the current Security state:

- When executed in Secure state, the Effective value of NSE is 0.
- When executed in Non-secure state, the Effective value of {NSE, NS} is {0, 1}.
- When executed in Realm state, the Effective value of {NSE, NS} is {1, 1}.

This instruction is treated as a NOP when executed at EL3 and either:

- CPP\_RCTX.{NSE, NS} selects a reserved value.
- CPP\_RCTX.{NSE, NS} == {1, 0} and CPP\_RCTX.EL has a value other than 0b11 .

## Otherwise:

Security State.

| NS   | Meaning           |
|------|-------------------|
| 0b0  | Secure state.     |
| 0b1  | Non-secure state. |

When executed in Non-secure state, the Effective value of NS is 1.

## EL, bits [25:24]

Exception Level. Indicates the Exception level of the target execution context.

| EL   | Meaning   | Applies when            |
|------|-----------|-------------------------|
| 0b00 | EL0.      |                         |
| 0b01 | EL1       |                         |
| 0b10 | EL2       | FEAT_EL2 is implemented |
| 0b11 | EL3       | FEAT_EL3 is implemented |

If the instruction is executed at an Exception level lower than the specified level, or is specified to apply to a combination of Exception level and Security state that is not implemented, this instruction is treated as a NOP.

## Bits [23:17]

Reserved, RES0.

## GASID, bit [16]

Execution of this instruction applies to all ASIDs or a specified ASID.

| GASID   | Meaning                                                        |
|---------|----------------------------------------------------------------|
| 0b0     | Applies to specified ASID for an EL0 target execution context. |
| 0b1     | Applies to all ASIDs for an EL0 target execution context.      |

For target execution contexts other than EL0, this field is RES0.

If the instruction is executed at EL0, this field has an Effective value of 0.

## ASID, bits [15:0]

Only applies for an EL0 target execution context and when bit[16] is 0.

Otherwise, this field is RES0.

When the instruction is executed at EL0, this field is treated as the current ASID.

If the implementation supports 16 bits of ASID, then the upper 8 bits of the ASID must be written to 0 by software when the context being affected only uses 8 bits.

## Executing CPP RCTX

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

CPP RCTX, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b011 | 0b0111 | 0b0011 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_SPECRES) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && SCTLR_EL1.EnRCTX == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGITR_EL2.CPPRCTX == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.EnRCTX == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.RestrictPrediction(X[t, 64], RestrictType_CachePrefetch); elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.CPPRCTX == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.RestrictPrediction(X[t, 64], RestrictType_CachePrefetch); elsif PSTATE.EL == EL2 then AArch64.RestrictPrediction(X[t, 64], RestrictType_CachePrefetch); elsif PSTATE.EL == EL3 then AArch64.RestrictPrediction(X[t, 64], RestrictType_CachePrefetch);
```

## C5.6.4 DVP RCTX, Data Value Prediction Restriction by Context

The DVP RCTX characteristics are:

## Purpose

Data Value Prediction Restriction by Context applies to all Data Value Prediction Resources that predict execution based on information gathered within the target execution context or contexts.

Note

The prediction of the PSTATE.{N,Z,C,V} values is not considered a data value for this purpose.

Data value predictions determined by the actions of code in the target execution context or contexts appearing in program order before the instruction cannot exploitatively control speculative execution occurring after the instruction is complete and synchronized.

This instruction is guaranteed to be complete following a DSB that covers both read and write behavior on the same PE as executed the original restriction instruction, and a subsequent context synchronization event is required to ensure that the effect of the completion of the instructions is synchronized to the current execution.

<!-- image -->

This instruction does not require the invalidation of prediction structures so long as the behavior described for completion of this instruction is met by the implementation.

Onsomeimplementations the instruction is likely to take a significant number of cycles to execute. This instruction is expected to be used very rarely, such as on the roll-over of an ASID or VMID, but should not be used on every context switch.

## Configuration

This system instruction is present only when FEAT\_SPECRES is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to DVP RCTX are UNDEFINED.

## Attributes

DVPRCTXis a 64-bit System instruction.

## Field descriptions

<!-- image -->

## Bits [63:49]

Reserved, RES0.

## GVMID, bit [48]

Execution of this instruction applies to all VMIDs or a specified VMID.

| GVMID   | Meaning                                                              |
|---------|----------------------------------------------------------------------|
| 0b0     | Applies to specified VMIDfor an EL0 or EL1 target execution context. |
| 0b1     | Applies to all VMIDs for an EL0 or EL1 target execution context.     |

For target execution contexts other than EL0 or EL1, this field is RES0.

If the instruction is executed at EL0 or EL1, then this field has an Effective value of 0.

If EL2 is not implemented or not enabled for the target Security state, this field is RES0.

## VMID, bits [47:32]

Only applies when bit[48] is 0 and the target execution context is either:

- EL1.
- EL0 when the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

Otherwise this field is RES0.

When the instruction is executed at EL1, this field is treated as the current VMID.

When the instruction is executed at EL0 and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, this field is treated as the current VMID.

When the instruction is executed at EL0 and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field is ignored.

If EL2 is not implemented or not enabled for the target Security state, this field is RES0.

If the implementation supports 16 bits of VMID, then the upper 8 bits of the VMID must be written to 0 by software when the context being affected only uses 8 bits.

## Bits [31:28]

Reserved, RES0.

## NSE, bit [27]

## When FEAT\_RME is implemented:

Together with the NS field, selects the Security state.

For a description of the values derived by evaluating NS and NSE together, see DVP\_RCTX.NS.

## Otherwise:

Reserved, RES0.

## NS, bit [26]

## When FEAT\_RME is implemented:

Together with the NSE field, selects the Security state.

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

Some Effective values are determined by the current Security state:

- When executed in Secure state, the Effective value of NSE is 0.
- When executed in Non-secure state, the Effective value of {NSE, NS} is {0, 1}.
- When executed in Realm state, the Effective value of {NSE, NS} is {1, 1}.

This instruction is treated as a NOP when executed at EL3 and either:

- DVP\_RCTX.{NSE, NS} selects a reserved value.
- DVP\_RCTX.{NSE, NS} == {1, 0} and DVP\_RCTX.EL has a value other than 0b11 .

## Otherwise:

Security State.

| NS   | Meaning           |
|------|-------------------|
| 0b0  | Secure state.     |
| 0b1  | Non-secure state. |

When executed in Non-secure state, the Effective value of NS is 1.

## EL, bits [25:24]

Exception Level. Indicates the Exception level of the target execution context.

| EL   | Meaning   | Applies when            |
|------|-----------|-------------------------|
| 0b00 | EL0.      |                         |
| 0b01 | EL1       |                         |
| 0b10 | EL2       | FEAT_EL2 is implemented |
| 0b11 | EL3       | FEAT_EL3 is implemented |

If the instruction is executed at an Exception level lower than the specified level, or is specified to apply to a combination of Exception level and Security state that is not implemented, this instruction is treated as a NOP.

## Bits [23:17]

Reserved, RES0.

## GASID, bit [16]

Execution of this instruction applies to all ASIDs or a specified ASID.

| GASID   | Meaning                                                        |
|---------|----------------------------------------------------------------|
| 0b0     | Applies to specified ASID for an EL0 target execution context. |
| 0b1     | Applies to all ASIDs for an EL0 target execution context.      |

For target execution contexts other than EL0, this field is RES0.

If the instruction is executed at EL0, this field has an Effective value of 0.

## ASID, bits [15:0]

Only applies for an EL0 target execution context and when bit[16] is 0.

Otherwise this field is RES0.

When the instruction is executed at EL0, this field is treated as the current ASID.

If the implementation supports 16 bits of ASID, then the upper 8 bits of the ASID must be written to 0 by software when the context being affected only uses 8 bits.

## Executing DVP RCTX

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

DVP RCTX, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b011 | 0b0111 | 0b0011 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_SPECRES) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && SCTLR_EL1.EnRCTX == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGITR_EL2.DVPRCTX == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.EnRCTX == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.RestrictPrediction(X[t, 64], RestrictType_DataValue); elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.DVPRCTX == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.RestrictPrediction(X[t, 64], RestrictType_DataValue); elsif PSTATE.EL == EL2 then AArch64.RestrictPrediction(X[t, 64], RestrictType_DataValue); elsif PSTATE.EL == EL3 then AArch64.RestrictPrediction(X[t, 64], RestrictType_DataValue);
```