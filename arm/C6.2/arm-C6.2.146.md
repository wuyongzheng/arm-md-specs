## C6.2.146 DCPS1

Debug change PE state to EL1

This instruction, when executed in Debug state:

- If executed at EL0, changes the current Exception level and SP to EL1 using SP\_EL1.
- Otherwise, if executed at ELx, selects SP\_ELx.

The target Exception level of a DCPS1 instruction is:

- EL1 if the instruction is executed at EL0.
- Otherwise, the Exception level at which the instruction is executed.

When the target Exception level of a DCPS1 instruction is ELx, on executing this instruction:

- ELR\_ELx becomes UNKNOWN.
- SPSR\_ELx becomes UNKNOWN.
- ESR\_ELx becomes UNKNOWN.
- DLR\_EL0 and DSPSR\_EL0 become UNKNOWN.
- The endianness is set according to SCTLR\_ELx.EE.

This instruction is always UNDEFINED in Non-debug state.

This instruction is UNDEFINED at EL0 if EL2 is implemented and enabled in the current Security state and HCR\_EL2.TGE == 1.

For more information on the operation of the DCPS&lt;n&gt; instructions, see DCPS.

<!-- image -->

## Encoding

```
DCPS1 {#<imm>}
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
DCPSInstruction(EL1);
```
