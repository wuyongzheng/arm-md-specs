## C6.2.173 HLT

Halt instruction

This instruction can generate a Halt Instruction debug event, which causes entry into Debug state.

Within a guarded memory region, while PSTATE.BTYPE != 0b00 , an HLT instruction that would cause entry into Debug state will not generate a Branch Target exception and will cause entry into Debug state as normal. For more information, see PSTATE.BTYPE.

<!-- image -->

## Encoding

```
HLT #<imm>
```

## Decode for this encoding

```
if EDSCR.HDE == '0' || !HaltingAllowed() then EndOfDecode(Decode_UNDEF); elsif IsFeatureImplemented(FEAT_BTI) then SetBTypeCompatible(TRUE);
```

## Assembler Symbols

## &lt;imm&gt;

Is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm16' field.

## Operation

```
constant boolean is_async = FALSE; constant FaultRecord fault = NoFault();
```

```
Halt(DebugHalt_HaltInstruction, is_async, fault);
```
