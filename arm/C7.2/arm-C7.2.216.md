## C7.2.216 LDAP1 (SIMD&amp;FP)

Load-acquire RCpc one single-element structure to one lane of one register

This instruction loads a single-element structure from memory and writes the result to the specified lane of the SIMD&amp;FP register without affecting the other bits of the register.

The instruction has memory ordering semantics, as described in Load-Acquire, Load-AcquirePC, and Store-Release, except that:

- There is no ordering requirement, separate from the requirements of a Load-AcquirePC or a Store-Release, created by having a Store-Release followed by a Load-AcquirePC instruction.
- The reading of a value written by a Store-Release by a Load-AcquirePC instruction by the same observer does not make the write of the Store-Release globally observed.

This difference in memory ordering is not described in the pseudocode.

For information about addressing modes, see Load/Store addressing modes.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## 64-bit

(FEAT\_AdvSIMD &amp;&amp; FEAT\_LRCPC3)

<!-- image -->

## Encoding

```
LDAP1 { <Vt>.D
```

```
}[<index>], [<Xn|SP>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_LRCPC3) then EndOfDecode(Decode_UNDEF); integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = integer UNKNOWN; constant boolean wback = FALSE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Assembler Symbols

&lt;Vt&gt;

Is the name of the first or only SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## &lt;index&gt;

Is the element index, encoded in 'Q'.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Shared Decode

```
bits(2) scale = opcode<2:1>; constant integer selem = UInt(opcode<0>:R) + 1; boolean replicate = FALSE; integer index; case scale of when '11' // load and replicate if L == '0' || S == '1' then scale = size; replicate = TRUE; when '00' index = UInt(Q:S:size); // B[0-15] when '01' if size<0> == '1' then EndOfDecode(Decode_UNDEF); end index = UInt(Q:S:size<1>); // H[0-7] when '10' if size<1> == '1' then EndOfDecode(Decode_UNDEF); end if size<0> == '0' then index = UInt(Q:S); // S[0-3] else if S == '1' then EndOfDecode(Decode_UNDEF); end index = UInt(Q); // D[0-1] scale = '11'; end end constant integer{} datasize = 64 << UInt(Q); constant integer{} esize = 8 << UInt(scale);
```

```
AArch64.CheckFPAdvSIMDEnabled(); bits(64) address; bits(64) eaddr; bits(64) offs; bits(128) rval; bits(esize) element; constant integer ebytes = esize DIV 8; constant AccessDescriptor accdesc = if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; offs = Zeros(64); if replicate then // load and replicate to all elements for s = 0 to selem-1 eaddr = AddressIncrement(address, offs, accdesc); element = Mem[eaddr, ebytes, accdesc]; // replicate to fill 128or 64-bit register V[t, datasize] = Replicate(element, datasize DIV esize); offs = offs + ebytes; t = (t + 1) MOD 32; else // load/store one element per register for s = 0 to selem-1 rval = V[t, 128];
```

```
EndOfDecode(Decode_UNDEF); end Operation CreateAccDescASIMDAcqRel(MemOp_LOAD, tagchecked);
```

```
eaddr = AddressIncrement(address, offs, accdesc); Elem[rval, index, esize] = Mem[eaddr, ebytes, accdesc]; V[t, 128] = rval; offs = offs + ebytes; t = ( t + 1 ) MOD 32; if wback then if m != 31 then offs = X[m, 64]; address = AddressAdd(address, offs, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
