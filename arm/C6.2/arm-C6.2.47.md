## C6.2.47 BRAA, BRAAZ, BRAB, BRABZ

Branch to register, with pointer authentication

This instruction authenticates the address in the general-purpose register that is specified by &lt;Xn&gt; , using a modifier and the specified key, and branches to the authenticated address.

The modifier is:

- In the general-purpose register or stack pointer that is specified by &lt;Xm|SP&gt; , for BRAA and BRAB .
- The value zero, for BRAAZ and BRABZ .

Key A is used for BRAA and BRAAZ . Key B is used for BRAB and BRABZ .

If the authentication passes, the PE continues execution at the target of the branch. For information on behavior if the authentication fails, see Faulting on pointer authentication.

The authenticated address is not written back to the general-purpose register.

This instruction provides a hint that this is not a subroutine call or return.

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the Key A, register modifier variant

Applies when

BRAA

(Z == 1

&lt;Xn&gt;, &lt;Xm|SP&gt;

## Encoding for the Key A, zero modifier variant

```
Applies when (Z == 0 && M == 0 && Rm == 11111)
```

BRAAZ

&lt;Xn&gt;

## Encoding for the Key B, register modifier variant

```
Applies when (Z == 1 && M == 1)
```

BRAB

&lt;Xn&gt;, &lt;Xm|SP&gt;

## Encoding for the Key B, zero modifier variant

```
Applies when (Z == 0 && M == 1 && Rm == 11111)
```

BRABZ

&lt;Xn&gt;

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
bits(64) target = X[n, 64]; constant bits(64) modifier = if source_is_sp then SP[64] else if use_key_a then target = AuthIA(target, modifier, auth_then_branch); else target = AuthIB(target, modifier, auth_then_branch); // Value in BTypeNext will be used to set PSTATE.BTYPE if InGuardedPage then if n == 16 || n == 17 then BTypeNext = '01'; else BTypeNext = '11'; else BTypeNext = '01'; constant boolean branch_conditional = FALSE; BranchTo(target, BranchType_INDIR, branch_conditional);
```

```
X[m, 64];
```
