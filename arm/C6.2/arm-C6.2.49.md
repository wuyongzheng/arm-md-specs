## C6.2.49 BRK

## Breakpoint instruction

This instruction generates a Breakpoint Instruction exception. The PE records the exception in ESR\_ELx, using the EC value 0x3 c, and captures the value of the immediate argument in ESR\_ELx.ISS.

Within a guarded memory region, while PSTATE.BTYPE != 0b00 , a BRK instruction will not generate a Branch Target exception and will generate a Breakpoint Instruction exception as normal. For more information, see PSTATE.BTYPE.

<!-- image -->

## Encoding

BRK

#&lt;imm&gt;

## Decode for this encoding

```
constant bits(16) comment = imm16; if IsFeatureImplemented(FEAT_BTI) SetBTypeCompatible(TRUE);
```

## Assembler Symbols

## &lt;imm&gt;

Is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm16' field.

## Operation

AArch64.SoftwareBreakpoint(comment);

then
