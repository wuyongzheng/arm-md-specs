## F5.1.44 DCPS1

Debug Change PE State to EL1 allows the debugger to move the PE into EL1 from EL0 or to a specific mode at the current Exception level.

DCPS1 is UNDEFINED if any of:

- The PE is in Non-debug state.
- EL2 is implemented, EL2 is implemented and enabled in the current Security state, and any of:
- EL2 is using AArch32 and HCR.TGE is set to 1.
- EL2 is using AArch64 and HCR\_EL2.TGE is set to 1.

When the PE executes DCPS1 at EL0, EL1 or EL3:

- If EL3 or EL1 is using AArch32, the PE enters SVC mode and LR\_svc, SPSR\_svc, DLR, and DSPSR become UNKNOWN. If DCPS1 is executed in Monitor mode, SCR.NS is cleared to 0.
- If EL1 is using AArch64, the PE enters EL1 using AArch64, selects SP\_EL1, and ELR\_EL1, ESR\_EL1, SPSR\_EL1, DLR\_EL0 and DSPSR\_EL0 become UNKNOWN.

When the PE executes DCPS1 at EL2 the PE does not change mode, and ELR\_hyp, HSR, SPSR\_hyp, DLR and DSPSR become UNKNOWN.

For more information on the operation of the DCPS&lt;n&gt; instructions, see DCPS.

<!-- image -->

## Encoding

DCPS1

## Decode for this encoding

// No additional

decoding

## Operation

```
if !Halted() then UNDEFINED; end if EL2Enabled() && PSTATE.EL == EL0 then constant bit tge = if ELUsingAArch32(EL2) then HCR.TGE else HCR_EL2.TGE; if tge == '1' then UNDEFINED; end end if PSTATE.EL != EL0 || ELUsingAArch32(EL1) then if PSTATE.M == M32_Monitor then SCR.NS = '0'; end if PSTATE.EL != EL2 then AArch32.WriteMode(M32_Svc); PSTATE.E = SCTLR.EE; if IsFeatureImplemented(FEAT_PAN) && SCTLR.SPAN == '0' then PSTATE.PAN = '1'; end Rmode[14, M32_Svc] = bits(32) UNKNOWN; // LR_svc SPSR_svc = bits(32) UNKNOWN; else PSTATE.E = HSCTLR.EE; ELR_hyp = bits(32) UNKNOWN;
```

required.

Listing F5-25

Listing F5-26

```
HSR = bits(32) UNKNOWN; SPSR_hyp = bits(32) UNKNOWN; end DLR = bits(32) UNKNOWN; DSPSR = bits(32) UNKNOWN; else // Targeting EL1 using AArch64 AArch64.MaybeZeroRegisterUppers(); MaybeZeroSVEUppers(EL1); PSTATE.nRW = '0'; PSTATE.SP = '1'; PSTATE.EL = EL1; if IsFeatureImplemented(FEAT_PAN) && SCTLR_EL1.SPAN == '0' then PSTATE.PAN = '1'; end if IsFeatureImplemented(FEAT_UAO) then PSTATE.UAO = '0'; end ELR_EL1 = bits(64) UNKNOWN; ESR_EL1 = bits(64) UNKNOWN; SPSR_EL1 = bits(64) UNKNOWN; DLR_EL0 = bits(64) UNKNOWN; DSPSR_EL0 = bits(64) UNKNOWN; // SCTLR_EL1.IESB might be ignored in Debug state. if (IsFeatureImplemented(FEAT_IESB) && SCTLR_EL1.IESB == '1' && !ConstrainUnpredictableBool(Unpredictable_IESBinDebug)) then SynchronizeErrors(); end end UpdateEDSCRFields(); // Update EDSCR PE state flags
```