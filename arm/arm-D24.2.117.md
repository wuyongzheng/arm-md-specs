## D24.2.117 IFSR32\_EL2, Instruction Fault Status Register (EL2)

The IFSR32\_EL2 characteristics are:

## Purpose

Allows access to the AArch32 IFSR register from AArch64 state only. Its value has no effect on execution in AArch64 state.

## Configuration

If EL2 is not implemented but EL3 is implemented, and EL1 is capable of using AArch32, then this register is not RES0.

AArch64 System register IFSR32\_EL2 bits [31:0] are architecturally mapped to AArch32 System register IFSR[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to IFSR32\_EL2 are UNDEFINED.

## Attributes

IFSR32\_EL2 is a 64-bit register.

## Field descriptions

When TTBCR.EAE == '0':

<!-- image -->

## Bits [63:17]

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

External abort type. This bit can be used to provide an IMPLEMENTATION DEFINED classification of External aborts. In an implementation that does not provide any classification of External aborts, this bit is RES0. For aborts other than External aborts this bit always returns 0.

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

## When TTBCR.EAE == '1':

<!-- image -->

## Bits [63:17]

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

| STATUS   | Meaning                                                                              | Applies when                |
|----------|--------------------------------------------------------------------------------------|-----------------------------|
| 0b000111 | Translation fault, level 3.                                                          |                             |
| 0b001001 | Access flag fault, level 1.                                                          |                             |
| 0b001010 | Access flag fault, level 2.                                                          |                             |
| 0b001011 | Access flag fault, level 3.                                                          |                             |
| 0b001101 | Permission fault, level 1.                                                           |                             |
| 0b001110 | Permission fault, level 2.                                                           |                             |
| 0b001111 | Permission fault, level 3.                                                           |                             |
| 0b010000 | Synchronous External abort, not on translation table walk.                           |                             |
| 0b010101 | Synchronous External abort on translation table walk, level 1.                       |                             |
| 0b010110 | Synchronous External abort on translation table walk, level 2.                       |                             |
| 0b010111 | Synchronous External abort on translation table walk, level 3.                       |                             |
| 0b011000 | Synchronous parity or ECC error on memory access, not on translation table walk.     | FEAT_RAS is not implemented |
| 0b011101 | Synchronous parity or ECC error on memory access on translation table walk, level 1. | FEAT_RAS is not implemented |
| 0b011110 | Synchronous parity or ECC error on memory access on translation table walk, level 2. | FEAT_RAS is not implemented |
| 0b011111 | Synchronous parity or ECC error on memory access on translation table walk, level 3. | FEAT_RAS is not implemented |
| 0b100001 | PC alignment fault.                                                                  |                             |
| 0b100010 | Debug exception.                                                                     |                             |
| 0b110000 | TLB conflict abort.                                                                  |                             |

All other values are reserved.

When FEAT\_RAS is implemented, 0b011000 , 0b011101 , 0b011110 , and 0b011111 are reserved.

For more information about the lookup level associated with a fault, see 'The level associated with MMU faults on a Long-descriptor translation table lookup'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing IFSR32\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, IFSR32\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0101 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = IFSR32_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = IFSR32_EL2;
```

MSR IFSR32\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0101 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then IFSR32_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then IFSR32_EL2 = X[t, 64];
```