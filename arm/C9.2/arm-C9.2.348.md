## C9.2.348 ZERO (table)

Zero ZT0

This instruction zeroes all bytes of the ZT0 register.

This instruction does not require the PE to be in Streaming SVE mode, and it is expected that this instruction will not experience a significant slowdown due to contention with other PEs that are executing in Streaming SVE mode.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

ZERO

{ ZT0

}

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_SME2) then EndOfDecode(Decode\_UNDEF);

## Operation

```
CheckSMEEnabled(); CheckSMEZT0Enabled(); ZT0[512] = Zeros(512);
```