## G8.2.24 CCSIDR, Current Cache Size ID Register

The CCSIDR characteristics are:

## Purpose

Provides information about the architecture of the currently selected cache.

When FEAT\_CCIDX is implemented, this register is used in conjunction with CCSIDR2.

## Configuration

The implementation includes one CCSIDR for each cache that it can access. CSSELR and the Security state select which Cache Size ID Register is accessible.

AArch32 System register CCSIDR bits [31:0] are architecturally mapped to AArch64 System register CCSIDR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to CCSIDR are UNDEFINED.

## Attributes

CCSIDR is a 32-bit register.

## Field descriptions

When FEAT\_CCIDX is implemented:

<!-- image -->

| 31   | 24 23         | 3 2 0    |
|------|---------------|----------|
| RES0 | Associativity | LineSize |

Note

The parameters NumSets, Associativity, and LineSize in these registers define the architecturally visible parameters that are required for the cache maintenance by Set/Way instructions. They are not guaranteed to represent the actual microarchitectural features of a design. You cannot make any inference about the actual sizes of caches based on these parameters.

## Bits [31:24]

Reserved, RES0.

## Associativity, bits [23:3]

(Associativity of cache) - 1, therefore a value of 0 indicates an associativity of 1. The associativity does not have to be a power of 2.

## LineSize, bits [2:0]

(Log2(Number of bytes in cache line)) - 4. For example:

For a line length of 16 bytes: Log2(16) = 4, LineSize entry = 0. This is the minimum line length.

For a line length of 32 bytes: Log2(32) = 5, LineSize entry = 1.

Note

The C++ 17 specification has two defined parameters relating to the granularity of memory that does not interfere. For generic software and tools, Arm will set the hardware\_destructive\_interference\_size parameter to 256 bytes and the hardware\_constructive\_interference\_size parameter to 64 bytes.

## Otherwise:

<!-- image -->

| 31      | 28 27   | 13 12         | 3 2 0    |
|---------|---------|---------------|----------|
| UNKNOWN | NumSets | Associativity | LineSize |

Note

The parameters NumSets, Associativity, and LineSize in these registers define the architecturally visible parameters that are required for the cache maintenance by Set/Way instructions. They are not guaranteed to represent the actual microarchitectural features of a design. You cannot make any inference about the actual sizes of caches based on these parameters.

## Bits [31:28]

Reserved, UNKNOWN.

## NumSets, bits [27:13]

(Number of sets in cache) - 1, therefore a value of 0 indicates 1 set in the cache. The number of sets does not have to be a power of 2.

## Associativity, bits [12:3]

(Associativity of cache) - 1, therefore a value of 0 indicates an associativity of 1. The associativity does not have to be a power of 2.

## LineSize, bits [2:0]

(Log2(Number of bytes in cache line)) - 4. For example:

For a line length of 16 bytes: Log2(16) = 4, LineSize entry = 0. This is the minimum line length.

For a line length of 32 bytes: Log2(32) = 5, LineSize entry = 1.

Note

The C++ 17 specification has two defined parameters relating to the granularity of memory that does not interfere. For generic software and tools, Arm will set the hardware\_destructive\_interference\_size parameter to 256 bytes and the hardware\_constructive\_interference\_size parameter to 64 bytes.

## Accessing CCSIDR

If CSSELR.{Level, InD} is programmed to a cache level that is not implemented, then on a read of the CCSIDR the behavior is CONSTRAINED UNPREDICTABLE, and can be one of the following:

- The CCSIDR read is treated as NOP.
- The CCSIDR read is UNDEFINED.
- The CCSIDR read returns an UNKNOWN value.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b001  | 0b0000 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID2 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_EVT) && HCR_EL2.TID4 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_EVT) && HCR2.TID4 == '1' then AArch32.TakeHypTrapException(0x03); else R[t] = CCSIDR; elsif PSTATE.EL == EL2 then R[t] = CCSIDR; elsif PSTATE.EL == EL3 then R[t] = CCSIDR;
```