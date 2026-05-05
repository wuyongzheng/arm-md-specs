## C6.2.147 DCPS2

Debug change PE state to EL2

This instruction, when executed in Debug state:

- If executed at EL0 or EL1, changes the current Exception level and SP to EL2 using SP\_EL2.
- Otherwise, if executed at ELx, selects SP\_ELx.

The target Exception level of a DCPS2 instruction is:

- EL2 if the instruction is executed at an Exception level that is not EL3.
- EL3 if the instruction is executed at EL3.

When the target Exception level of a DCPS2 instruction is ELx, on executing this instruction:

- ELR\_ELx becomes UNKNOWN.
- SPSR\_ELx becomes UNKNOWN.
- ESR\_ELx becomes UNKNOWN.
- DLR\_EL0 and DSPSR\_EL0 become UNKNOWN.
- The endianness is set according to SCTLR\_ELx.EE.

This instruction is always UNDEFINED in Non-debug state.

This instruction is UNDEFINED at the following Exception levels:

- All Exception levels if EL2 is not implemented.
- At EL0 and EL1 if EL2 is disabled in the current Security state.

For more information on the operation of the DCPS&lt;n&gt; instructions, see DCPS.

<!-- image -->

## Encoding

```
DCPS2 {#<imm>}
```

## Decode for this encoding

// Empty.

## Assembler Symbols

## &lt;imm&gt;

Is an optional 16-bit unsigned immediate, in the range 0 to 65535, defaulting to 0 and encoded in the 'imm16' field.

## Operation

```
if !Halted() then UNDEFINED;
```

```
DCPSInstruction(EL2);
```
