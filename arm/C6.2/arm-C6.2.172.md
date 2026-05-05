## C6.2.172 HINT

Hint instruction

This instruction is for the instruction set space that is reserved for architectural hint instructions.

Some encodings described here are not allocated in this revision of the architecture, and behave as NOPs. These encodings might be allocated to other hint functionality in future revisions of the architecture and therefore must not be used by software.

<!-- image -->

## Encoding

```
HINT #<imm>
```

## Decode for this encoding

```
SystemHintOp op; boolean stream; case CRm:op2 of when '0000 000' op = SystemHintOp_NOP; when '0000 001' op = SystemHintOp_YIELD; when '0000 010' op = SystemHintOp_WFE; when '0000 011' op = SystemHintOp_WFI; when '0000 100' op = SystemHintOp_SEV; when '0000 101' op = SystemHintOp_SEVL; when '0000 110' if !IsFeatureImplemented(FEAT_DGH) then EndOfDecode(Decode_NOP); op = SystemHintOp_DGH; when '0000 111' SEE "XPACLRI"; when '0001 xxx' case op2 of when '000' SEE "PACIA1716"; when '010' SEE "PACIB1716"; when '100' SEE "AUTIA1716"; when '110' SEE "AUTIB1716"; otherwise EndOfDecode(Decode_NOP); when '0010 000' if !IsFeatureImplemented(FEAT_RAS) then EndOfDecode(Decode_NOP); op = SystemHintOp_ESB; when '0010 001' if !IsFeatureImplemented(FEAT_SPE) then EndOfDecode(Decode_NOP); op = SystemHintOp_PSB; when '0010 010' if !IsFeatureImplemented(FEAT_TRF) then EndOfDecode(Decode_NOP); op = SystemHintOp_TSB; when '0010 011' if !IsFeatureImplemented(FEAT_GCS) then EndOfDecode(Decode_NOP); op = SystemHintOp_GCSB; when '0010 100' op = SystemHintOp_CSDB; when '0010 110' if !IsFeatureImplemented(FEAT_CLRBHB) then EndOfDecode(Decode_NOP); op = SystemHintOp_CLRBHB; when '0011 xxx' case op2 of when '000' SEE "PACIAZ"; when '001' SEE "PACIASP"; when '010' SEE "PACIBZ";
```

```
when '011' SEE "PACIBSP"; when '100' SEE "AUTIAZ"; when '101' SEE "AUTIASP"; when '110' SEE "AUTIBZ"; when '111' SEE "AUTIBSP"; when '0100 xx0' if !IsFeatureImplemented(FEAT_BTI) then EndOfDecode(Decode_NOP); // Check branch target compatibility between BTI instruction and PSTATE.BTYPE SetBTypeCompatible(BTypeCompatible_BTI(op2<2:1>)); op = SystemHintOp_BTI; when '0100 111' SEE "PACM"; when '0101 000' if !IsFeatureImplemented(FEAT_CHK) then EndOfDecode(Decode_NOP); op = SystemHintOp_CHKFEAT; when '0110 00x' if !IsFeatureImplemented(FEAT_PCDPHINT) then EndOfDecode(Decode_NOP); stream = op2<0> == '1'; op = SystemHintOp_STSHH; otherwise EndOfDecode(Decode_NOP);
```

## Assembler Symbols

## &lt;imm&gt;

Is a 7-bit unsigned immediate, in the range 0 to 127, encoded in the 'CRm:op2' field.

The encodings that are allocated to architectural hint functionality are described in the 'Hints' table in the 'Index by Encoding'.

Note

For allocated encodings of 'CRm:op2':

- Adisassembler will disassemble the allocated instruction, rather than the HINT instruction.
- Anassembler may support assembly of allocated encodings using HINT with the corresponding &lt;imm&gt; value, but it is not required to do so.

## Operation

```
case op of when SystemHintOp_YIELD Hint_Yield(); when SystemHintOp_DGH Hint_DGH(); when SystemHintOp_WFE Hint_WFE(); when SystemHintOp_WFI Hint_WFI(); when SystemHintOp_SEV SendEvent(); when SystemHintOp_SEVL SendEventLocal(); when SystemHintOp_ESB SynchronizeErrors(); AArch64.ESBOperation(); if PSTATE.EL IN {EL0, EL1} && EL2Enabled() then AArch64.vESBOperation(); elsif IsFeatureImplemented(FEAT_E3DSE) && PSTATE.EL != EL3 then AArch64.dESBOperation();
```

```
TakeUnmaskedSErrorInterrupts(); when SystemHintOp_PSB if IsFeatureImplemented(FEAT_FGT) && IsFeatureImplemented(FEAT_SPEv1p5) then constant boolean trap_to_el2 = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !IsInHost() && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && HFGITR_EL2.PSBCSYNC == '1'); if trap_to_el2 then ExceptionRecord except = ExceptionSyndrome(Exception_LDST64BTrap); // to be renamed except.syndrome.iss = \texttt{0x3}<24:0>; constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = \texttt{0x0}; AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); ProfilingSynchronizationBarrier(); when SystemHintOp_TSB if IsFeatureImplemented(FEAT_FGT2) && IsFeatureImplemented(FEAT_TRBEv1p1) then constant boolean trap_to_el2 = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !IsInHost() && (!HaveEL(EL3) || SCR_EL3.FGTEn2 == '1') && HFGITR2_EL2.TSBCSYNC == '1'); if trap_to_el2 then ExceptionRecord except = ExceptionSyndrome(Exception_LDST64BTrap); // to be renamed except.syndrome.iss = \texttt{0x4}<24:0>; constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = \texttt{0x0}; AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); TraceSynchronizationBarrier(); when SystemHintOp_GCSB GCSSynchronizationBarrier(); when SystemHintOp_CHKFEAT X[16, 64] = AArch64.ChkFeat(X[16, 64]); when SystemHintOp_CSDB ConsumptionOfSpeculativeDataBarrier(); when SystemHintOp_CLRBHB Hint_CLRBHB(); when SystemHintOp_BTI SetBTypeNext('00'); when SystemHintOp_STSHH Hint_StoreShared(stream); when SystemHintOp_NOP return; // Do nothing otherwise Unreachable();
```
