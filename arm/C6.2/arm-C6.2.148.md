## C6.2.148 DCPS3

Debug change PE state to EL3

This instruction, when executed in Debug state:

- If executed at EL3, selects SP\_EL3.
- Otherwise, changes the current Exception level and SP to EL3 using SP\_EL3.

The target Exception level of a DCPS3 instruction is EL3.

On executing a DCPS3 instruction:

- ELR\_EL3 becomes UNKNOWN.
- SPSR\_EL3 becomes UNKNOWN.
- ESR\_EL3 becomes UNKNOWN.
- DLR\_EL0 and DSPSR\_EL0 become UNKNOWN.
- The endianness is set according to SCTLR\_EL3.EE.

This instruction is always UNDEFINED in Non-debug state.

This instruction is UNDEFINED at all Exception levels if either:

- EDSCR.SDD == 1.
- EL3 is not implemented.

For more information on the operation of the DCPS&lt;n&gt; instructions, see DCPS.

<!-- image -->

## Encoding

```
DCPS3 {#<imm>}
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
DCPSInstruction(EL3);
```
