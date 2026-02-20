## G8.2.47 DFSR, Data Fault Status Register

The DFSR characteristics are:

## Purpose

Holds status information about the last data fault.

## Configuration

The current translation table format determines which format of the register is used.

AArch32 System register DFSR bits [31:0] are architecturally mapped to AArch64 System register ESR\_EL1[31:0].

This register is banked between DFSR and DFSR\_S and DFSR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DFSR are UNDEFINED.

## Attributes

DFSR is a 32-bit register.

This register has the following instances:

- DFSR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- DFSR\_S, when FEAT\_AA32EL3 is implemented.
- DFSR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

When TTBCR.EAE == '0':

<!-- image -->

## Bits [31:17]

Reserved, RES0.

## FnV, bit [16]

FAR not Valid, for a synchronous External abort other than a synchronous External abort on a translation table walk.

| FnV   | Meaning                                        |
|-------|------------------------------------------------|
| 0b0   | DFAR is valid.                                 |
| 0b1   | DFAR is not valid, and holds an UNKNOWN value. |

This field is valid only for a synchronous External abort other than a synchronous External abort on a translation table walk. It is RES0 for all other Data Abort exceptions.

The reset behavior of this field is:

LPAE

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## AET, bits [15:14]

## When FEAT\_RAS is implemented:

Asynchronous Error Type. When DFSC is 0b010001 , describes the PE error state after taking the SError exception. Possible values are:

| AET   | Meaning                    |
|-------|----------------------------|
| 0b00  | Uncontainable (UC).        |
| 0b01  | Unrecoverable state (UEU). |
| 0b10  | Restartable state (UEO).   |
| 0b11  | Recoverable state (UER).   |

This field is valid only if the DFSC code is 0b010001 . It is RES0 for all other aborts.

In the event of multiple errors taken as a single SError exception, the overall PE error state is reported.

Note

Software can use this information to determine what recovery might be possible. The recovery software must also examine any implemented fault records to determine the location and extent of the error.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CM, bit [13]

Cache maintenance fault. For synchronous faults, this bit indicates whether a cache maintenance instruction generated the fault.

| CM   | Meaning                                                                                     |
|------|---------------------------------------------------------------------------------------------|
| 0b0  | Abort not caused by execution of a cache maintenance instruction.                           |
| 0b1  | Abort caused by execution of a cache maintenance instruction, or on an address translation. |

On a synchronous Data Abort exception on a translation table walk, this bit is UNKNOWN.

On an asynchronous fault, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ExT, bit [12]

External abort type.

In an implementation that does not provide any classification of External aborts, this bit is RES0.

For aborts other than External aborts this bit always returns 0.

This bit can be used to provide an IMPLEMENTATION DEFINED classification of External aborts.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## WnR, bit [11]

Write not Read bit. Indicates whether the abort was caused by a write or a read instruction.

| WnR   | Meaning                              |
|-------|--------------------------------------|
| 0b0   | Abort caused by a read instruction.  |
| 0b1   | Abort caused by a write instruction. |

For faults on the cache maintenance and address translation System instructions in the (coproc== 0b1111 ) encoding space this bit always returns a value of 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## FS, bits [10, 3:0]

Fault status bits. Possible values of FS[4:0] are:

| FS      | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b00001 | Alignment fault.                                                |
| 0b00010 | Debug exception.                                                |
| 0b00011 | Access flag fault, level 1.                                     |
| 0b00100 | Fault on instruction cache maintenance.                         |
| 0b00101 | Translation fault, level 1.                                     |
| 0b00110 | Access flag fault, level 2.                                     |
| 0b00111 | Translation fault, level 2.                                     |
| 0b01000 | Synchronous External abort, not on translation table walk.      |
| 0b01001 | Domain fault, level 1.                                          |
| 0b01011 | Domain fault, level 2.                                          |
| 0b01100 | Synchronous External abort, on translation table walk, level 1. |
| 0b01101 | Permission fault, level 1.                                      |
| 0b01110 | Synchronous External abort, on translation table walk, level 2. |
| 0b01111 | Permission fault, level 2.                                      |
| 0b10000 | TLB conflict abort.                                             |
| 0b10100 | IMPLEMENTATION DEFINED fault (Lockdown fault).                  |

| FS      | Meaning                                                                          | Applies when                |
|---------|----------------------------------------------------------------------------------|-----------------------------|
| 0b10101 | IMPLEMENTATION DEFINED fault (Unsupported Exclusive access fault).               |                             |
| 0b10110 | SError exception.                                                                |                             |
| 0b11000 | SError exception, from a parity or ECC error on memory access.                   | FEAT_RAS is not implemented |
| 0b11001 | Synchronous parity or ECC error on memory access, not on translation table walk. | FEAT_RAS is not implemented |
| 0b11100 | Synchronous parity or ECC error on translation table walk, level 1.              | FEAT_RAS is not implemented |
| 0b11110 | Synchronous parity or ECC error on translation table walk, level 2.              | FEAT_RAS is not implemented |

All other values are reserved.

For more information about the lookup level associated with a fault, see 'The level associated with MMU faults on a Short-descriptor translation table lookup'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## LPAE, bit [9]

On taking a Data Abort exception, this bit is set as follows:

| LPAE   | Meaning                                               |
|--------|-------------------------------------------------------|
| 0b0    | Using the Short-descriptor translation table formats. |
| 0b1    | Using the Long-descriptor translation table formats.  |

Hardware does not interpret this bit to determine the behavior of the memory system, and therefore software can set this bit to 0 or 1 without affecting operation.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [8]

Reserved, RES0.

## Domain, bits [7:4]

The domain of the fault address.

Arm deprecates any use of this field, see 'The Domain field in the DFSR'.

This field is UNKNOWN for certain faults where the DFSR is updated and reported using the Short-descriptor FSR encodings, see 'Validity of Domain field on faults that update the DFSR when using the Short-descriptor encodings'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When TTBCR.EAE == '1':

<!-- image -->

## Bits [31:17]

Reserved, RES0.

## FnV, bit [16]

FAR not Valid, for a synchronous External abort other than a synchronous External abort on a translation table walk.

| FnV   | Meaning                                        |
|-------|------------------------------------------------|
| 0b0   | DFAR is valid.                                 |
| 0b1   | DFAR is not valid, and holds an UNKNOWN value. |

This field is valid only for a synchronous External abort other than a synchronous External abort on a translation table walk. It is RES0 for all other Data Abort exceptions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## AET, bits [15:14]

## When FEAT\_RAS is implemented:

Asynchronous Error Type. When DFSC is 0b010001 , describes the PE error state after taking the SError exception. Possible values are:

| AET   | Meaning                    |
|-------|----------------------------|
| 0b00  | Uncontainable (UC).        |
| 0b01  | Unrecoverable state (UEU). |
| 0b10  | Restartable state (UEO).   |
| 0b11  | Recoverable state (UER).   |

This field is valid only if the DFSC code is 0b010001 . It is RES0 for all other aborts.

In the event of multiple errors taken as a single SError exception, the overall PE error state is reported.

<!-- image -->

Software can use this information to determine what recovery might be possible. The recovery software must also examine any implemented fault records to determine the location and extent of the error.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CM, bit [13]

Cache maintenance fault. For synchronous faults, this bit indicates whether a cache maintenance instruction generated the fault.

| CM   | Meaning                                                           |
|------|-------------------------------------------------------------------|
| 0b0  | Abort not caused by execution of a cache maintenance instruction. |
| 0b1  | Abort caused by execution of a cache maintenance instruction.     |

On a synchronous Data Abort exception on a translation table walk, this bit is UNKNOWN.

On an asynchronous fault, this bit is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ExT, bit [12]

External abort type.

In an implementation that does not provide any classification of External aborts, this bit is RES0.

For aborts other than External aborts this bit always returns 0.

This bit can be used to provide an IMPLEMENTATION DEFINED classification of External aborts.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## WnR, bit [11]

Write not Read bit. Indicates whether the abort was caused by a write or a read instruction.

| WnR   | Meaning                              |
|-------|--------------------------------------|
| 0b0   | Abort caused by a read instruction.  |
| 0b1   | Abort caused by a write instruction. |

For faults on the cache maintenance and address translation System instructions in the (coproc== 0b1111 ) encoding space this bit always returns a value of 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [10]

Reserved, RES0.

## LPAE, bit [9]

On taking a Data Abort exception, this bit is set as follows:

| LPAE   | Meaning                                               |
|--------|-------------------------------------------------------|
| 0b0    | Using the Short-descriptor translation table formats. |
| 0b1    | Using the Long-descriptor translation table formats.  |

Hardware does not interpret this bit to determine the behavior of the memory system, and therefore software can set this bit to 0 or 1 without affecting operation.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [8:6]

Reserved, RES0.

## STATUS, bits [5:0]

Fault status bits. Possible values of this field are:

| STATUS   | Meaning Applies when                                                                                         |
|----------|--------------------------------------------------------------------------------------------------------------|
| 0b000000 | Address size fault in translation table base register.                                                       |
| 0b000001 | Address size fault, level 1.                                                                                 |
| 0b000010 | Address size fault, level 2.                                                                                 |
| 0b000011 | Address size fault, level 3.                                                                                 |
| 0b000101 | Translation fault, level 1.                                                                                  |
| 0b000110 | Translation fault, level 2.                                                                                  |
| 0b000111 | Translation fault, level 3.                                                                                  |
| 0b001001 | Access flag fault, level 1.                                                                                  |
| 0b001010 | Access flag fault, level 2.                                                                                  |
| 0b001011 | Access flag fault, level 3.                                                                                  |
| 0b001101 | Permission fault, level 1.                                                                                   |
| 0b001110 | Permission fault, level 2.                                                                                   |
| 0b001111 | Permission fault, level 3.                                                                                   |
| 0b010000 | Synchronous External abort, not on translation table walk.                                                   |
| 0b010001 | Asynchronous SError exception.                                                                               |
| 0b010101 | Synchronous External abort on translation table walk, level 1.                                               |
| 0b010110 | Synchronous External abort on translation table walk, level 2.                                               |
| 0b010111 | Synchronous External abort on translation table walk, level 3.                                               |
| 0b011000 | Synchronous parity or ECC error on memory access, not on translation table walk. FEAT_RAS is not implemented |

| STATUS   | Meaning                                                                              | Applies when                |
|----------|--------------------------------------------------------------------------------------|-----------------------------|
| 0b011001 | Asynchronous SError exception, from a parity or ECC error on memory access.          | FEAT_RAS is not implemented |
| 0b011101 | Synchronous parity or ECC error on memory access on translation table walk, level 1. | FEAT_RAS is not implemented |
| 0b011110 | Synchronous parity or ECC error on memory access on translation table walk, level 2. | FEAT_RAS is not implemented |
| 0b011111 | Synchronous parity or ECC error on memory access on translation table walk, level 3. | FEAT_RAS is not implemented |
| 0b100001 | Alignment fault.                                                                     |                             |
| 0b100010 | Debug exception.                                                                     |                             |
| 0b110000 | TLB conflict abort.                                                                  |                             |
| 0b110100 | IMPLEMENTATION DEFINED fault (Lockdown).                                             |                             |
| 0b110101 | IMPLEMENTATION DEFINED fault (Unsupported Exclusive access).                         |                             |

All other values are reserved.

For more information about the lookup level associated with a fault, see 'The level associated with MMU faults on a Long-descriptor translation table lookup'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing DFSR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = DFSR_NS; else
```

```
R[t] = DFSR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = DFSR_NS; else R[t] = DFSR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = DFSR_S; else R[t] = DFSR_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then DFSR_NS = R[t]; else DFSR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then DFSR_NS = R[t]; else DFSR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then DFSR_S = R[t]; else DFSR_NS = R[t];
```