## C6.2.488 UDF

## Permanently undefined

This instruction generates an Undefined Instruction exception (ESR\_ELx.EC = 0b000000 ). The encodings for UDF used in this section are defined as permanently UNDEFINED.

<!-- image -->

## Encoding

UDF

#&lt;imm&gt;

## Decode for this encoding

```
// The imm16 field is ignored by hardware. EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;imm&gt;

is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm16' field. The PE ignores the value of this constant.

## Operation

// No operation.
