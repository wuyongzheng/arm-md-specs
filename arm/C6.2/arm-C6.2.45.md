## C6.2.45 BLRAA, BLRAAZ, BLRAB, BLRABZ

Branch with link to register, with pointer authentication

This instruction authenticates the address in the general-purpose register that is specified by &lt;Xn&gt; , using a modifier and the specified key, and calls a subroutine at the authenticated address, setting register X30 to PC+4.

The modifier is:

- In the general-purpose register or stack pointer that is specified by &lt;Xm|SP&gt; , for BLRAA and BLRAB .
- The value zero, for BLRAAZ and BLRABZ .

Key A is used for BLRAA and BLRAAZ . Key B is used for BLRAB and BLRABZ .

If the authentication passes, the PE continues execution at the target of the branch. For information on behavior if the authentication fails, see Faulting on pointer authentication.

The authenticated address is not written back to the general-purpose register.

This instruction provides a hint that this is a subroutine call.

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the Key A, register modifier variant

Applies when

BLRAA

&lt;Xn&gt;,

(Z == 1

&lt;Xm|SP&gt;

## Encoding for the Key A, zero modifier variant

```
Applies when (Z == 0 && M == 0 && Rm == 11111)
```

BLRAAZ

&lt;Xn&gt;

## Encoding for the Key B, register modifier variant

```
Applies when (Z == 1 && M == 1)
```

BLRAB

&lt;Xn&gt;,

&lt;Xm|SP&gt;

## Encoding for the Key B, zero modifier variant

```
Applies when (Z == 0 && M == 1 && Rm == 11111)
```

```
BLRABZ <Xn>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_PAuth) then if Z == '0' && Rm != '11111' then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean use_key_a = (M == '0'); constant boolean source_is_sp = ((Z == '1') && (m == 31)); constant boolean auth_then_branch = TRUE;
```

&amp;&amp;

M

==

0)

## Assembler Symbols

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose register holding the address to be branched to, encoded in the 'Rn' field.

## &lt;Xm|SP&gt;

Is the 64-bit name of the general-purpose source register or stack pointer holding the modifier, encoded in the 'Rm' field.

## Operation

```
bits(64) target = X[n, 64]; constant bits(64) modifier = if source_is_sp then SP[64] else if use_key_a then target = AuthIA(target, modifier, auth_then_branch); else target = AuthIB(target, modifier, auth_then_branch); if IsFeatureImplemented(FEAT_GCS) && GCSPCREnabled(PSTATE.EL) then AddGCSRecord(PC64 + 4); // Value in BTypeNext will be used to set PSTATE.BTYPE BTypeNext = '10'; X[30, 64] = PC64 + 4; constant boolean branch_conditional = FALSE; BranchTo(target, BranchType_INDCALL, branch_conditional);
```

```
X[m, 64];
```
