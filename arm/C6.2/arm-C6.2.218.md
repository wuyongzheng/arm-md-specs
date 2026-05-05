## C6.2.218 LDRAA, LDRAB

Load register, with pointer authentication

This instruction authenticates an address from a base register using a modifier of zero and the specified key, adds an immediate offset to the authenticated address, and loads a 64-bit doubleword from memory at this resulting address into a register.

Key A is used for LDRAA . Key B is used for LDRAB .

If the authentication passes, the PE behaves the same as for an LDR instruction. For information on behavior if the authentication fails, see Faulting on pointer authentication.

The authenticated address is not written back to the base register, unless the pre-indexed variant of the instruction is used. In this case, the address that is written back to the base register does not include the pointer authentication code.

For information about addressing modes, see Load/Store addressing modes.

## PAC

(FEAT\_PAuth)

<!-- image -->

## Encoding for the Key A, offset variant

```
Applies when (M == 0 && W == 0) LDRAA <Xt>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the Key A, pre-indexed variant

```
Applies when (M == 0 && W == 1) LDRAA <Xt>, [<Xn|SP>{, #<simm>}]!
```

## Encoding for the Key B, offset variant

```
0)
```

```
Applies when (M == 1 && W == LDRAB <Xt>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the Key B, pre-indexed variant

```
Applies when (M == 1 && W == 1) LDRAB <Xt>, [<Xn|SP>{, #<simm>}]!
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); boolean wback = W == '1'; constant boolean use_key_a = M == '0'; constant bits(10) S10 = S:imm9; constant bits(64) offset = LSL(SignExtend(S10, 64), 3); constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

```
boolean wb_unknown = FALSE; if wback && n == t && n != 31 then constant Constraint c = ConstrainUnpredictable(Unpredictable_WBOVERLAPLD); assert c IN {Constraint_WBSUPPRESS, Constraint_UNKNOWN, Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_WBSUPPRESS wback = FALSE; // writeback is suppressed when Constraint_UNKNOWN wb_unknown = TRUE; // writeback is UNKNOWN when Constraint_UNDEF EndOfDecode(Decode_UNDEF); when Constraint_NOP EndOfDecode(Decode_NOP);
```

## Assembler Symbols

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the optional signed immediate byte offset, a multiple of 8 in the range -4096 to 4088, defaulting to 0 and encoded in the 'S:imm9' field as &lt;simm&gt;/8.

## Operation

```
bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant boolean auth_then_branch = TRUE; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked, t); if n == 31 then address = SP[64]; else address = X[n, 64]; if use_key_a then address = AuthDA(address, X[31, 64], auth_then_branch); else address = AuthDB(address, X[31, 64], auth_then_branch); if n == 31 then CheckSPAlignment(); address = AddressAdd(address, offset, accdesc); X[t, 64] = Mem[address, 8, accdesc]; if wback then if wb_unknown then address = bits(64) UNKNOWN; if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
