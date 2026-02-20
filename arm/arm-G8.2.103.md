## G8.2.103 IFSR, Instruction Fault Status Register

The IFSR characteristics are:

## Purpose

Holds status information about the last instruction fault.

## Configuration

The current translation table format determines which format of the register is used.

AArch32 System register IFSR bits [31:0] are architecturally mapped to AArch64 System register IFSR32\_EL2[31:0].

This register is banked between IFSR and IFSR\_S and IFSR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to IFSR are UNDEFINED.

## Attributes

IFSR is a 32-bit register.

This register has the following instances:

- IFSR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- IFSR\_S, when FEAT\_AA32EL3 is implemented.
- IFSR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

When TTBCR.EAE == '0':

<!-- image -->

## Bits [31:17]

Reserved, RES0.

## FnV, bit [16]

FAR not Valid, for a synchronous External abort other than a synchronous External abort on a translation table walk.

| FnV   | Meaning                                        |
|-------|------------------------------------------------|
| 0b0   | IFAR is valid.                                 |
| 0b1   | IFAR is not valid, and holds an UNKNOWN value. |

This field is valid only for a synchronous External abort other than a synchronous External abort on a translation table walk. It is RES0 for all other Prefetch Abort exceptions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [15:13]

Reserved, RES0.

## ExT, bit [12]

External abort type. This bit can be used to provide an IMPLEMENTATION DEFINED classification of External aborts.

In an implementation that does not provide any classification of External aborts, this bit is RES0.

For aborts other than External aborts this bit always returns 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [11]

Reserved, RES0.

## FS, bits [10, 3:0]

Fault Status bits. Bits [10] and [3:0] are interpreted together.

| FS      | Meaning                                                                          | Applies when                |
|---------|----------------------------------------------------------------------------------|-----------------------------|
| 0b00001 | PC alignment fault.                                                              |                             |
| 0b00010 | Debug exception.                                                                 |                             |
| 0b00011 | Access flag fault, level 1.                                                      |                             |
| 0b00101 | Translation fault, level 1.                                                      |                             |
| 0b00110 | Access flag fault, level 2.                                                      |                             |
| 0b00111 | Translation fault, level 2.                                                      |                             |
| 0b01000 | Synchronous External abort, not on translation table walk.                       |                             |
| 0b01001 | Domain fault, level 1.                                                           |                             |
| 0b01011 | Domain fault, level 2.                                                           |                             |
| 0b01100 | Synchronous External abort, on translation table walk, level 1.                  |                             |
| 0b01101 | Permission fault, level 1.                                                       |                             |
| 0b01110 | Synchronous External abort, on translation table walk, level 2.                  |                             |
| 0b01111 | Permission fault, level 2.                                                       |                             |
| 0b10000 | TLB conflict abort.                                                              |                             |
| 0b10100 | IMPLEMENTATION DEFINED fault (Lockdown fault).                                   |                             |
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

## Bits [8:4]

Reserved, RES0.

When TTBCR.EAE == '1':

<!-- image -->

## Bits [31:17]

Reserved, RES0.

## FnV, bit [16]

FAR not Valid, for a synchronous External abort other than a synchronous External abort on a translation table walk.

| FnV   | Meaning                                        |
|-------|------------------------------------------------|
| 0b0   | IFAR is valid.                                 |
| 0b1   | IFAR is not valid, and holds an UNKNOWN value. |

This field is valid only for a synchronous External abort other than a synchronous External abort on a translation table walk. It is RES0 for all other Prefetch Abort exceptions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [15:13]

Reserved, RES0.

## ExT, bit [12]

External abort type. This bit can be used to provide an IMPLEMENTATION DEFINED classification of External aborts.

In an implementation that does not provide any classification of External aborts, this bit is RES0.

For aborts other than External aborts this bit always returns 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:10]

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

| STATUS   | Meaning                                                | Applies when   |
|----------|--------------------------------------------------------|----------------|
| 0b000000 | Address size fault in translation table base register. |                |
| 0b000001 | Address size fault, level 1.                           |                |
| 0b000010 | Address size fault, level 2.                           |                |
| 0b000011 | Address size fault, level 3.                           |                |
| 0b000101 | Translation fault, level 1.                            |                |
| 0b000110 | Translation fault, level 2.                            |                |

| STATUS   | Meaning                                                                              | Applies when                                                   |
|----------|--------------------------------------------------------------------------------------|----------------------------------------------------------------|
| 0b000111 | Translation fault, level 3.                                                          | Translation fault, level 3.                                    |
| 0b001001 | Access flag fault, level 1.                                                          | Access flag fault, level 1.                                    |
| 0b001010 | Access flag fault, level 2.                                                          | Access flag fault, level 2.                                    |
| 0b001011 | Access flag fault, level 3.                                                          | Access flag fault, level 3.                                    |
| 0b001101 | Permission fault, level 1.                                                           | Permission fault, level 1.                                     |
| 0b001110 | Permission fault, level 2.                                                           | Permission fault, level 2.                                     |
| 0b001111 | Permission fault, level 3.                                                           | Permission fault, level 3.                                     |
| 0b010000 | Synchronous External abort, not on translation table walk.                           | Synchronous External abort, not on translation table walk.     |
| 0b010101 | Synchronous External abort on translation table walk, level 1.                       | Synchronous External abort on translation table walk, level 1. |
| 0b010110 | Synchronous External abort on translation table walk, level 2.                       | Synchronous External abort on translation table walk, level 2. |
| 0b010111 | Synchronous External abort on translation table walk, level 3.                       | Synchronous External abort on translation table walk, level 3. |
| 0b011000 | Synchronous parity or ECC error on memory access, not on translation table walk.     | FEAT_RAS is not implemented                                    |
| 0b011101 | Synchronous parity or ECC error on memory access on translation table walk, level 1. | FEAT_RAS is not implemented                                    |
| 0b011110 | Synchronous parity or ECC error on memory access on translation table walk, level 2. | FEAT_RAS is not implemented                                    |
| 0b011111 | Synchronous parity or ECC error on memory access on translation table walk, level 3. | FEAT_RAS is not implemented                                    |
| 0b100001 | PC alignment fault.                                                                  | PC alignment fault.                                            |
| 0b100010 | Debug exception.                                                                     | Debug exception.                                               |
| 0b110000 | TLB conflict abort.                                                                  | TLB conflict abort.                                            |

All other values are reserved.

When FEAT\_RAS is implemented, 0b011000 , 0b011101 , 0b011110 , and 0b011111 are reserved.

For more information about the lookup level associated with a fault, see 'The level associated with MMU faults on a Long-descriptor translation table lookup'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing IFSR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0000 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = IFSR_NS; else R[t] = IFSR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = IFSR_NS; else R[t] = IFSR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = IFSR_S; else R[t] = IFSR_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0101 | 0b0000 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then IFSR_NS = R[t]; else IFSR = R[t]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && IFSR_NS = R[t]; else IFSR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then IFSR_S = R[t]; else IFSR_NS = R[t];
```

```
ELUsingAArch32(EL3) then
```