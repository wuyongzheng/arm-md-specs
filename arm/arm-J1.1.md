## J1.1 Pseudocode for AArch64 operation

This section holds the pseudocode for execution in AArch64 state. Functions that are listed in this section are identified as AArch64.FunctionName . Some of these functions have an equivalent AArch32 function, AArch32.FunctionName . This section is organized by functional groups, with the functional groups being indicated by hierarchical path names, for example aarch64/debug/breakpoint .

The top-level sections of the AArch64 pseudocode hierarchy are:

- aarch64/debug.
- aarch64/exceptions.
- aarch64/functions.
- aarch64/translation.

## J1.1.1 aarch64/debug

This section includes the following pseudocode functions:

- BRBCycleCountingEnabled
- BRBEBranch
- BRBEBranchOnISB
- BRBEDebugStateEntry
- BRBEDebugStateExit
- BRBEException
- BRBEExceptionReturn
- BRBEFreeze
- BRBEISB
- BRBEMispredictAllowed
- BRBETimeStamp
- BRB\_IALL
- BRB\_INJ
- BranchEncCycleCount
- BranchMispredict
- BranchRawCycleCount
- BranchRecordAllowed
- Contents
- FilterBranchRecord
- FirstBranchAfterProhibited
- GetBRBENumRecords
- Getter
- ShouldBRBEFreeze
- UpdateBranchRecordBuffer
- AArch64.BreakpointMatch
- AArch64.BreakpointValueMatch
- AArch64.ReservedBreakpointType
- AArch64.StateMatch
- DebugAddrTop
- EffectiveMDSELR\_EL1\_BANK
- IsBreakpointEnabled
- SelfHostedExtendedBPWPEnabled

- CheckForPMUException
- EffectivePMEE
- ExceptionReturnPPEND
- IsSupportingPMUSynchronousMode
- PMUExceptionEnabled
- PMUExceptionMasked
- PMUInterruptEnabled
- inst\_addr\_executed
- sync\_counter\_overflowed
- AArch64.GenerateDebugExceptions
- AArch64.GenerateDebugExceptionsFrom
- AArch64.TRCIT
- TraceInstrumentation
- AArch64.IncrementCycleCounter
- AArch64.IncrementEventCounter
- AArch64.PMUCycle
- TakeProfilingException
- CheckForSPEException
- CheckMDCR\_EL3\_NSPBTrap
- CollectContextIDR1
- CollectContextIDR2
- CollectPhysicalAddress
- CollectTimeStamp
- DefaultSPEEvent
- EffectiveMDCR\_EL3\_NSPB
- EffectivePMBLIMITR\_EL1\_nVM
- EffectivePMSCR\_EL1\_EE
- EffectivePMSCR\_EL2\_EE
- GetPMBSR\_EL1\_FSC
- GetPMBSR\_EL2\_FSC
- GetPMBSR\_EL3\_FSC
- OtherSPEManagementEvent
- PMBSR\_EL
- ProfilingBufferEnabled
- ProfilingBufferOwner
- ProfilingSynchronizationBarrier
- ReportSPEEvent
- SPE
- SPEAddByteToRecord
- SPEAddPacketToRecord
- SPEBranch
- SPEBufferIsFull
- SPECollectRecord
- SPECompleteSample
- SPEConstructClass
- SPEConstructRecord
- SPECycle

- SPEEmptyRecord
- SPEEncodeETS
- SPEEncodeEVL
- SPEEvent
- SPEFilterByDataSource
- SPEFilterByEvents
- SPEFilterByLatency
- SPEFilterByType
- SPEFreezeOnEvent
- SPEGetDataSource
- SPEGetDataSourcePayloadSize
- SPEGetEventsPayloadSize
- SPEGetRandomBoolean
- SPEGetRandomInterval
- SPEISB
- SPEInterruptEnabled
- SPELDSTType
- SPEMultiAccessSample
- SPEOpAttr
- SPEOpType
- SPEProfilingStopped
- SPEResetSampleCounter
- SPEResetSampleStorage
- SPESampleAddAddressPCVirtual
- SPESampleAddContext
- SPESampleAddTimeStamp
- SPESampleCollision
- SPESampleExtendedLoadStore
- SPESampleGCSSS2
- SPESampleGeneralPurposeLoadStore
- SPESampleLoadStore
- SPESampleMemCopy
- SPESampleMemSet
- SPESampleOnSharedResource
- SPESampleOpOther
- SPESampleOpSMEArrayOther
- SPESampleOpSVEOther
- SPESampleOpSVESMELoadStore
- SPESampleSIMDFPLoadStore
- SPESetDataPhysicalAddress
- SPESetDataVirtualAddress
- SPEStartCounter
- SPEStartSample
- SPEStopCounter
- SPEToCollectSample
- SPEWriteToBuffer
- StatisticalProfilingEnabled

- TimeStamp
- AArch64.TakeExceptionInDebugState
- AArch64.WatchpointByteMatch
- AArch64.WatchpointMatch
- IsWatchpointEnabled

## J1.1.1.1 BRBCycleCountingEnabled

```
is allowed, FALSE;
```

```
// BRBCycleCountingEnabled() // ========================= // Returns TRUE if the recording of cycle counts // FALSE otherwise. boolean BRBCycleCountingEnabled() if HaveEL(EL2) && BRBCR_EL2.CC == '0' then return if BRBCR_EL1.CC == '0' then return FALSE; return TRUE;
```

## J1.1.1.2 BRBEBranch

```
// BRBEBranch() // ============ // Called to write branch record for the following branches when BRBE is active: // direct branches, // indirect branches, // direct branches with link, // indirect branches with link, // returns from subroutines. BRBEBranch(BranchType br_type, boolean cond, bits(64) target_address) if BranchRecordAllowed(PSTATE.EL) && FilterBranchRecord(br_type, cond) then bits(6) branch_type; case br_type of when BranchType_DIR branch_type = if cond then '001000' else '000000'; when BranchType_INDIR branch_type = '000001'; when BranchType_DIRCALL branch_type = '000010'; when BranchType_INDCALL branch_type = '000011'; when BranchType_RET branch_type = '000101'; otherwise Unreachable(); bit ccu; bits(14) cc; (ccu, cc) = BranchEncCycleCount(); constant bits(2) el = PSTATE.EL; constant bit mispredict = (if BRBEMispredictAllowed() && BranchMispredict() then '1' else '0'); UpdateBranchRecordBuffer(ccu, cc, branch_type, el, mispredict, '11', PC64, target_address); PMUEvent(PMU_EVENT_BRB_FILTRATE);
```

return;

## J1.1.1.3 BRBEBranchOnISB

```
// BRBEBranchOnISB() // ================= // Returns TRUE if ISBs generate Branch records, and FALSE otherwise. boolean BRBEBranchOnISB() return boolean IMPLEMENTATION_DEFINED "ISB generates Branch records";
```

## J1.1.1.4 BRBEDebugStateEntry

```
// BRBEDebugStateEntry() // ===================== // Called to write Debug state entry branch record when BRBE is active. BRBEDebugStateEntry(bits(64) source_address) if BranchRecordAllowed(PSTATE.EL) then constant bits(6) branch_type = '100001'; bit ccu; bits(14) cc; (ccu, cc) = BranchEncCycleCount(); constant bits(2) el = '00'; constant bit mispredict = '0'; // Debug state is a prohibited region, therefore target_address=0 UpdateBranchRecordBuffer(ccu, cc, branch_type, el, mispredict, '10', source_address, Zeros(64)); PMUEvent(PMU_EVENT_BRB_FILTRATE); return;
```

## J1.1.1.5 BRBEDebugStateExit

```
// BRBEDebugStateExit() // ==================== // Called to write Debug state exit branch record when BRBE is active. BRBEDebugStateExit(bits(64) target_address) if BranchRecordAllowed(PSTATE.EL) then // Debug state is a prohibited region, therefore ccu=1, cc=0, source_address=0 constant bits(6) branch_type = '111001'; constant bit ccu = '1'; constant bits(14) cc = Zeros(14); constant bits(2) el = PSTATE.EL; constant bit mispredict = '0'; UpdateBranchRecordBuffer(ccu, cc, branch_type, el, mispredict, '01', Zeros(64), target_address); PMUEvent(PMU_EVENT_BRB_FILTRATE); return;
```

## J1.1.1.6 BRBEException

```
// BRBEException() // =============== // Called to write exception branch record when BRBE is active. BRBEException(ExceptionRecord erec, boolean source_valid, bits(64) source_address_in,
```

```
bits(64) target_address_in, bits(2) target_el, boolean trappedsyscallinst) bits(64) target_address = target_address_in; constant Exception except = erec.exceptype; constant bits(25) iss = erec.syndrome.iss; case target_el of when EL3 if !IsFeatureImplemented(FEAT_BRBEv1p1) || (MDCR_EL3.E3BREC == MDCR_EL3.E3BREW) then return; when EL2 if BRBCR_EL2.EXCEPTION == '0' then return; when EL1 if BRBCR_EL1.EXCEPTION == '0' then return; constant boolean target_valid = BranchRecordAllowed(target_el); if source_valid || target_valid then bits(6) branch_type; case except of when Exception_Uncategorized branch_type = '100011'; // Trap when Exception_WFxTrap branch_type = '100011'; // Trap when Exception_CP15RTTrap branch_type = '100011'; // Trap when Exception_CP15RRTTrap branch_type = '100011'; // Trap when Exception_CP14RTTrap branch_type = '100011'; // Trap when Exception_CP14DTTrap branch_type = '100011'; // Trap when Exception_AdvSIMDFPAccessTrap branch_type = '100011'; // Trap when Exception_FPIDTrap branch_type = '100011'; // Trap when Exception_PACTrap branch_type = '100011'; // Trap when Exception_CP14RRTTrap branch_type = '100011'; // Trap when Exception_LDST64BTrap branch_type = '100011'; // Trap when Exception_BranchTarget branch_type = '101011'; // Inst Fault when Exception_IllegalState branch_type = '100011'; // Trap when Exception_SupervisorCall if !trappedsyscallinst then branch_type = '100010'; // Call else branch_type = '100011'; // Trap when Exception_HypervisorCall branch_type = '100010'; // Call when Exception_MonitorCall if !trappedsyscallinst then branch_type = '100010'; // Call else branch_type = '100011'; // Trap when Exception_SystemRegisterTrap branch_type = '100011'; // Trap when Exception_SystemRegister128Trap branch_type = '100011'; // Trap when Exception_SVEAccessTrap branch_type = '100011'; // Trap when Exception_SMEAccessTrap branch_type = '100011'; // Trap when Exception_ERetTrap branch_type = '100011'; // Trap when Exception_PACFail branch_type = '101100'; // Data Fault when Exception_InstructionAbort branch_type = '101011'; // Inst Fault when Exception_PCAlignment branch_type = '101010'; // Alignment when Exception_DataAbort branch_type = '101100'; // Data Fault when Exception_NV2DataAbort branch_type = '101100'; // Data Fault when Exception_SPAlignment branch_type = '101010'; // Alignment when Exception_FPTrappedException branch_type = '100011'; // Trap when Exception_SError branch_type = '100100'; // System Error when Exception_Breakpoint branch_type = '100110'; // Inst debug when Exception_SoftwareStep branch_type = '100110'; // Inst debug when Exception_Watchpoint branch_type = '100111'; // Data debug when Exception_NV2Watchpoint branch_type = '100111'; // Data debug when Exception_SoftwareBreakpoint branch_type = '100110'; // Inst debug when Exception_IRQ branch_type = '101110'; // IRQ when Exception_FIQ branch_type = '101111'; // FIQ when Exception_MemCpyMemSet branch_type = '100011'; // Trap when Exception_GCSFail if iss<23:20> == '0000' then branch_type = '101100'; // Data Fault elsif iss<23:20> == '0001' then branch_type = '101011'; // Inst Fault elsif iss<23:20> == '0010' then branch_type = '100011'; // Trap else Unreachable(); when Exception_Profiling branch_type = '100110'; // Inst debug when Exception_GPC if iss<20> == '1' then branch_type = '101011'; // Inst fault
```

```
else branch_type = '101100'; // Data fault otherwise Unreachable(); bit ccu; bits(14) cc; (ccu, cc) = BranchEncCycleCount(); constant bits(2) el = if target_valid then target_el else '00'; constant bit mispredict = '0'; constant bit sv = if source_valid then '1' else '0'; constant bit tv = if target_valid then '1' else '0'; constant bits(64) source_address = if source_valid then source_address_in else Zeros(64); if !target_valid then target_address = Zeros(64); else target_address = AArch64.BranchAddr(target_address, target_el); UpdateBranchRecordBuffer(ccu, cc, branch_type, el, mispredict, sv:tv, source_address, target_address); PMUEvent(PMU_EVENT_BRB_FILTRATE);
```

```
return; BRBEExceptionReturn
```

## J1.1.1.7

```
// BRBEExceptionReturn() // ===================== // Called to write exception return branch record when BRBE is active. BRBEExceptionReturn(bits(64) target_address_in, bits(2) source_el, boolean source_valid, bits(64) source_address_in) bits(64) target_address = target_address_in; case source_el of when EL3 if !IsFeatureImplemented(FEAT_BRBEv1p1) || (MDCR_EL3.E3BREC == MDCR_EL3.E3BREW) then return; when EL2 if BRBCR_EL2.ERTN == '0' then return; when EL1 if BRBCR_EL1.ERTN == '0' then return; constant boolean target_valid = BranchRecordAllowed(PSTATE.EL); if source_valid || target_valid then constant bits(6) branch_type = '000111'; bit ccu; bits(14) cc; (ccu, cc) = BranchEncCycleCount(); constant bits(2) el = if target_valid then PSTATE.EL else '00'; constant bit mispredict = (if source_valid && BRBEMispredictAllowed() && BranchMispredict() then '1' else '0'); constant bit sv = if source_valid then '1' else '0'; constant bit tv = if target_valid then '1' else '0'; constant bits(64) source_address = if source_valid then source_address_in else Zeros(64); if !target_valid then target_address = Zeros(64); UpdateBranchRecordBuffer(ccu, cc, branch_type, el, mispredict, sv:tv, source_address, target_address); PMUEvent(PMU_EVENT_BRB_FILTRATE); return;
```

## J1.1.1.8 BRBEFreeze

```
// BRBEFreeze() // ============ // Generates BRBE freeze event. BRBEFreeze() BRBFCR_EL1.PAUSED = '1';
```

## BRBTS\_EL1 = GetTimestamp(BRBETimeStamp()); J1.1.1.9 BRBEISB // BRBEISB() // ========= // Handles ISB instruction for BRBE. BRBEISB() constant boolean branch\_conditional = FALSE; BRBEBranch(BranchType\_DIR, branch\_conditional, PC64 + 4); J1.1.1.10 BRBEMispredictAllowed // BRBEMispredictAllowed() // ======================= // Returns TRUE if the recording of branch misprediction is allowed, // FALSE otherwise. boolean BRBEMispredictAllowed() if HaveEL(EL2) &amp;&amp; BRBCR\_EL2.MPRED == '0' then return FALSE; if BRBCR\_EL1.MPRED == '0' then return FALSE; return TRUE; J1.1.1.11 BRBETimeStamp ConstrainUnpredictableBits

```
// BRBETimeStamp() // =============== // Returns captured timestamp. TimeStamp BRBETimeStamp() if HaveEL(EL2) then TS_el2 = BRBCR_EL2.TS; if !IsFeatureImplemented(FEAT_ECV) && TS_el2 == '10' then // Reserved value (-, TS_el2) = ConstrainUnpredictableBits(Unpredictable_EL2TIMESTAMP, 2); case TS_el2 of when '00' // Falls out to check BRBCR_EL1.TS when '01' return TimeStamp_Virtual; when '10' assert IsFeatureImplemented(FEAT_ECV); // Otherwise // removes this case return TimeStamp_OffsetPhysical; when '11' return TimeStamp_Physical; TS_el1 = BRBCR_EL1.TS; if TS_el1 == '00' || (!IsFeatureImplemented(FEAT_ECV) && TS_el1 == '10') then // Reserved value (-, TS_el1) = ConstrainUnpredictableBits(Unpredictable_EL1TIMESTAMP, 2); case TS_el1 of
```

```
when '01' return TimeStamp_Virtual; when '10' return TimeStamp_OffsetPhysical; when '11' return TimeStamp_Physical; otherwise Unreachable(); // ConstrainUnpredictableBits removes this case
```

## J1.1.1.12 BRB\_IALL

```
// BRB_IALL() // ========== // Called to perform invalidation of branch records BRB_IALL() constant integer nbrberecords for i = 0 to nbrberecords - 1 Records_SRC[i] = Zeros(64); Records_TGT[i] = Zeros(64); Records_INF[i] = Zeros(64);
```

## J1.1.1.13 BRB\_INJ

```
// BRB_INJ() // ========= // Called to perform manual injection of branch records. BRB_INJ() UpdateBranchRecordBuffer(BRBINFINJ_EL1.CCU, BRBINFINJ_EL1.CC, BRBINFINJ_EL1.TYPE, BRBINFINJ_EL1.EL, BRBINFINJ_EL1.MPRED, BRBINFINJ_EL1.VALID, BRBSRCINJ_EL1.ADDRESS, BRBTGTINJ_EL1.ADDRESS); BRBINFINJ_EL1 = bits(64) UNKNOWN; BRBSRCINJ_EL1 = bits(64) UNKNOWN; BRBTGTINJ_EL1 = bits(64) UNKNOWN; if ConstrainUnpredictableBool(Unpredictable_BRBFILTRATE) then PMUEvent(PMU_EVENT_BRB_FILTRATE);
```

## J1.1.1.14 BranchEncCycleCount

```
// BranchEncCycleCount() // ===================== // The first return result is '1' if either of the following is true, and '0' otherwise: // -This is the first Branch record after the PE exited a Prohibited Region. // -This is the first Branch record after cycle counting has been enabled. // If the first return return is '0', the second return result is the encoded cycle count // since the last branch. // The format of this field uses a mantissa and exponent to express the cycle count value. // -bits[7:0] indicate the mantissa M. // -bits[13:8] indicate the exponent E. // The cycle count is expressed using the following function: // cycle_count = (if IsZero(E) then UInt(M) else UInt('1':M:Zeros(UInt(E)-1))) // A value of all ones in both the mantissa and exponent indicates the cycle count value // exceeded the size of the cycle counter. // If the cycle count is not known, the second return result is zero. (bit, bits(14)) BranchEncCycleCount() cc = BranchRawCycleCount();
```

```
= GetBRBENumRecords();
```

## if !BRBCycleCountingEnabled() || FirstBranchAfterProhibited() then return ('1', Zeros(14)); // The format of this field uses a mantissa and exponent to express the cycle count value. // -bits[7:0] indicate the mantissa M. // -bits[13:8] indicate the exponent E. // The cycle count is expressed using the following function: // cycle\_count = IsZero(E) ? UInt(M) : UInt('1':M:Zeros(UInt(E)-1)) // A value of all ones in both the mantissa and exponent indicates the cycle count value // exceeded the size of the cycle counter. bits(6) E; bits(8) M; if cc &lt; 2^8 then E = Zeros(6); M = cc&lt;7:0&gt;; elsif cc &gt;= 2^20 then E = Ones(6); M = Ones(8); else E = 1&lt;5:0&gt;; while cc &gt;= 2^9 do E = E + 1; cc = cc DIV 2; M = cc&lt;7:0&gt;; return ('0', E:M); J1.1.1.15 BranchMispredict // BranchMispredict() // ================== // Returns TRUE if the branch being executed was mispredicted, FALSE otherwise. boolean BranchMispredict(); J1.1.1.16 BranchRawCycleCount // BranchRawCycleCount() // ===================== // If the cycle count is known, the return result is the cycle count since the last branch. integer BranchRawCycleCount(); J1.1.1.17 BranchRecordAllowed otherwise.

```
// BranchRecordAllowed() // ===================== // Returns TRUE if branch recording is allowed, FALSE boolean BranchRecordAllowed(bits(2) el) if ELUsingAArch32(el) then return FALSE; if BRBFCR_EL1.PAUSED == '1' then return FALSE; if el == EL3 && IsFeatureImplemented(FEAT_BRBEv1p1) then return (MDCR_EL3.E3BREC != MDCR_EL3.E3BREW);
```

```
if HaveEL(EL3) && (MDCR_EL3.SBRBE == '00' || (CurrentSecurityState() == SS_Secure && MDCR_EL3.SBRBE == '01')) then return FALSE; case el of when EL3 return FALSE; // FEAT_BRBEv1p1 not implemented when EL2 return BRBCR_EL2.E2BRE == '1'; when EL1 return BRBCR_EL1.E1BRE == '1'; when EL0 if EL2Enabled() && HCR_EL2.TGE == '1' then return BRBCR_EL2.E0HBRE == '1'; else return BRBCR_EL1.E0BRE == '1';
```

## J1.1.1.18 Contents

```
// Contents of the Branch Record Buffer //===================================== array [0..63] of BRBSRC_EL1_Type Records_SRC; array [0..63] of BRBTGT_EL1_Type Records_TGT; array [0..63] of BRBINF_EL1_Type Records_INF;
```

## J1.1.1.19 FilterBranchRecord

```
// FilterBranchRecord() // ==================== // Returns TRUE if the branch record is not filtered out, FALSE otherwise. boolean FilterBranchRecord(BranchType br, boolean cond) case br of when BranchType_DIRCALL return BRBFCR_EL1.DIRCALL != BRBFCR_EL1.EnI; when BranchType_INDCALL return BRBFCR_EL1.INDCALL != BRBFCR_EL1.EnI; when BranchType_RET return BRBFCR_EL1.RTN != BRBFCR_EL1.EnI; when BranchType_DIR if cond then return BRBFCR_EL1.CONDDIR != BRBFCR_EL1.EnI; else return BRBFCR_EL1.DIRECT != BRBFCR_EL1.EnI; when BranchType_INDIR return BRBFCR_EL1.INDIRECT != BRBFCR_EL1.EnI; otherwise Unreachable(); return FALSE;
```

## J1.1.1.20 FirstBranchAfterProhibited

```
// FirstBranchAfterProhibited() // ============================ // Returns TRUE if branch recorded is the first branch after a prohibited // FALSE otherwise. boolean FirstBranchAfterProhibited();
```

```
region,
```

## J1.1.1.21 GetBRBENumRecords

```
// GetBRBENumRecords() // =================== // Returns the number of branch records implemented. integer GetBRBENumRecords() assert UInt(BRBIDR0_EL1.NUMREC) IN {0x08, 0x10, 0x20, 0x40}; return integer IMPLEMENTATION_DEFINED "Number of BRBE Branch records";
```

## J1.1.1.22 Getter

```
// Getter functions for branch records // =================================== // Functions used by MRS instructions that access branch records BRBSRC_EL1_Type BRBSRC_EL1[integer n] assert n IN {0..31}; constant integer record_index = UInt(BRBFCR_EL1.BANK:n<4:0>); if record_index < GetBRBENumRecords() then return Records_SRC[record_index]; else return Zeros(64); BRBTGT_EL1_Type BRBTGT_EL1[integer n] assert n IN {0..31}; constant integer record_index = UInt(BRBFCR_EL1.BANK:n<4:0>); if record_index < GetBRBENumRecords() then return Records_TGT[record_index]; else return Zeros(64); BRBINF_EL1_Type BRBINF_EL1[integer n] assert n IN {0..31}; constant integer record_index = UInt(BRBFCR_EL1.BANK:n<4:0>); if record_index < GetBRBENumRecords() then return Records_INF[record_index]; else return Zeros(64);
```

## J1.1.1.23 ShouldBRBEFreeze

```
// ShouldBRBEFreeze() // ================== // Returns TRUE if the BRBE freeze event conditions have been met, and FALSE otherwise. boolean ShouldBRBEFreeze() if !BranchRecordAllowed(PSTATE.EL) then return FALSE; boolean include_r1; boolean include_r2; constant boolean include_r3 = FALSE; if HaveEL(EL2) then include_r1 = (BRBCR_EL1.FZP == '1'); include_r2 = (BRBCR_EL2.FZP == '1'); else include_r1 = TRUE; include_r2 = TRUE; return CheckPMUOverflowCondition(PMUOverflowCondition_BRBEFreeze, include_r1, include_r2, include_r3);
```

## J1.1.1.24 UpdateBranchRecordBuffer

```
// UpdateBranchRecordBuffer() // ========================== // Add a new Branch record to the buffer. UpdateBranchRecordBuffer(bit ccu, bits(14) cc, bits(6) branch_type, bits(2) el, bit mispredict, bits(2) valid, bits(64) source_address, bits(64) target_address) // Shift the Branch Records in the buffer constant integer nbrberecords = GetBRBENumRecords(); for i = nbrberecords - 1 downto 1 Records_SRC[i] = Records_SRC[i - 1]; Records_TGT[i] = Records_TGT[i - 1]; Records_INF[i] = Records_INF[i - 1]; Records_INF[0].CCU = ccu; Records_INF[0].CC = cc; Records_INF[0].EL = el; Records_INF[0].VALID = valid; Records_INF[0].MPRED = mispredict; Records_INF[0].TYPE = branch_type; Records_SRC[0] = source_address; Records_TGT[0] = target_address; return;
```

## J1.1.1.25 AArch64.BreakpointMatch

```
// AArch64.BreakpointMatch() // ========================= // Breakpoint matching in an AArch64 translation regime. // Returns BreakpointInfo structure that contains breakpoint type, a boolean to indicate the // type of breakpoint, matched address and whether the breakpoint is active and matched // successfully. For Address Mismatch breakpoints, the returned boolean is the inverted result. BreakpointInfo AArch64.BreakpointMatch(integer n, bits(64) vaddress, AccessDescriptor accdesc, integer size) assert !ELUsingAArch32(S1TranslationRegime()); assert n < NumBreakpointsImplemented(); BreakpointInfo brkptinfo; linking_enabled = (DBGBCR_EL1[n].BT IN {'0x11', '1xx1'} || (IsFeatureImplemented(FEAT_ABLE) && DBGBCR_EL1[n].BT2 == '1')); // A breakpoint that has linking enabled does not generate debug events in isolation if linking_enabled then brkptinfo.bptype = BreakpointType_Inactive; brkptinfo.match = FALSE; return brkptinfo; enabled = IsBreakpointEnabled(n); linked = DBGBCR_EL1[n].BT == '0x01'; isbreakpnt = TRUE; linked_to = FALSE; from_linking_enabled = FALSE; lbnx = if IsFeatureImplemented(FEAT_Debugv8p9) then DBGBCR_EL1[n].LBNX else '00'; linked_n = UInt(lbnx : DBGBCR_EL1[n].LBN); ssce = if IsFeatureImplemented(FEAT_RME) then DBGBCR_EL1[n].SSCE else '0'; state_match = AArch64.StateMatch(DBGBCR_EL1[n].SSC, ssce, DBGBCR_EL1[n].HMC, DBGBCR_EL1[n].PMC, linked, linked_n, isbreakpnt, vaddress, accdesc);
```

```
(bp_type, value_match) = AArch64.BreakpointValueMatch(n, vaddress, linked_to, isbreakpnt, from_linking_enabled); if HaveAArch32() && size == 4 then // Check second halfword // If the breakpoint address and BAS of an Address breakpoint match the address of the // second halfword of an instruction, but not the address of the first halfword, it is // CONSTRAINED UNPREDICTABLE whether or not this breakpoint generates a Breakpoint debug // event. (-, match_i) = AArch64.BreakpointValueMatch(n, vaddress + 2, linked_to, isbreakpnt, from_linking_enabled); if !value_match && match_i then value_match = ConstrainUnpredictableBool(Unpredictable_BPMATCHHALF); if vaddress<1> == '1' && DBGBCR_EL1[n].BAS == '1111' then // The above notwithstanding, if DBGBCR_EL1[n].BAS == '1111', then it is CONSTRAINED // UNPREDICTABLE whether or not a Breakpoint debug event is generated for an instruction // at the address DBGBVR_EL1[n]+2. if value_match then value_match = ConstrainUnpredictableBool(Unpredictable_BPMATCHHALF); if !(state_match && enabled) then brkptinfo.bptype = BreakpointType_Inactive; brkptinfo.match = FALSE; else brkptinfo.bptype = bp_type; brkptinfo.match = value_match; return brkptinfo;
```

## J1.1.1.26 AArch64.BreakpointValueMatch

```
// AArch64.BreakpointValueMatch() // ============================== // Returns breakpoint type to indicate the type of breakpoint and a boolean to indicate // whether the breakpoint matched successfully. For Address Mismatch breakpoints, the // returned boolean is the inverted result. If the breakpoint type return value is Inactive, // then the boolean result is FALSE. (BreakpointType, boolean) AArch64.BreakpointValueMatch(integer n_in, bits(64) vaddress, boolean linked_to, boolean isbreakpnt, boolean from_linking_enabled) // "n_in" is the identity of the breakpoint unit to match against. // "vaddress" is the current instruction address, ignored if linked_to is TRUE and for Context // matching breakpoints. // "linked_to" is TRUE if this is a call from StateMatch for linking. // "isbreakpnt" TRUE is this is a call from BreakpointMatch or from StateMatch for a // linked breakpoint or from BreakpointValueMatch for a linked breakpoint with linking enabled. // "from_linking_enabled" is TRUE if this is a call from BreakpointValueMatch for a linked // breakpoint with linking enabled. integer n = n_in; Constraint c; bits(5) dbgtype; // If a non-existent breakpoint then it is CONSTRAINED UNPREDICTABLE whether this gives // no match or the breakpoint is mapped to another UNKNOWN implemented breakpoint. if n >= NumBreakpointsImplemented() then (c, n) = ConstrainUnpredictableInteger(0, NumBreakpointsImplemented() - 1, Unpredictable_BPNOTIMPL); assert c IN {Constraint_DISABLED, Constraint_UNKNOWN}; if c == Constraint_DISABLED then return (BreakpointType_Inactive, FALSE); // If this breakpoint is not enabled, it cannot generate a match. // (This could also happen on a call from StateMatch for linking). if !IsBreakpointEnabled(n) then return (BreakpointType_Inactive, FALSE);
```

```
// If BT is set to a reserved type, behaves either as disabled or as a not-reserved type. if IsFeatureImplemented(FEAT_ABLE) then dbgtype = DBGBCR_EL1[n].<BT2,BT>; else dbgtype = '0' : DBGBCR_EL1[n].BT; (c, dbgtype) = AArch64.ReservedBreakpointType(n, dbgtype); if c == Constraint_DISABLED then return (BreakpointType_Inactive, FALSE); // Otherwise the value returned by ConstrainUnpredictableBits must be a not-reserved value // Determine what to compare against. match_addr = (dbgtype == 'x0x0x'); mismatch = (dbgtype == 'x010x'); match_vmid = (dbgtype == 'x10xx'); match_cid = (dbgtype == 'x001x'); match_cid1 = (dbgtype IN {'x101x', 'xx11x'}); match_cid2 = (dbgtype == 'x11xx'); linking_enabled = (dbgtype IN {'xxx11', 'x1xx1', '1xxxx'}); // If this is a call from StateMatch, return FALSE if the breakpoint is not // programmed with linking enabled. if linked_to && !linking_enabled then return (BreakpointType_Inactive, FALSE); // If called from BreakpointMatch return FALSE for breakpoint with linking enabled. if !linked_to && linking_enabled then return (BreakpointType_Inactive, FALSE); constant boolean linked = (dbgtype == 'x0x01'); if from_linking_enabled then // A breakpoint with linking enabled has called this function. assert linked_to && isbreakpnt; if linked then // A breakpoint with linking enabled is linked to a linked breakpoint. This is // architecturally UNPREDICTABLE, but treated as disabled in the pseudo code to // avoid potential recursion in BreakpointValueMatch(). return (BreakpointType_Inactive, FALSE); // If a linked breakpoint is linked to an address matching breakpoint, // the behavior is CONSTRAINED UNPREDICTABLE. if linked_to && match_addr && isbreakpnt then if !ConstrainUnpredictableBool(Unpredictable_BPLINKEDADDRMATCH) then return (BreakpointType_Inactive, FALSE); // A breakpoint programmed for address mismatch does not match in AArch32 state. if mismatch && UsingAArch32() then return (BreakpointType_Inactive, FALSE); boolean bvr_match = FALSE; boolean bxvr_match = FALSE; BreakpointType bp_type; integer mask; if IsFeatureImplemented(FEAT_BWE) then mask = UInt(DBGBCR_EL1[n].MASK); // If the mask is set to a reserved value, the behavior is CONSTRAINED UNPREDICTABLE. if mask IN {1, 2} then (c, mask) = ConstrainUnpredictableInteger(3, 31, Unpredictable_RESBPMASK); assert c IN {Constraint_DISABLED, Constraint_NONE, Constraint_UNKNOWN}; case c of when Constraint_DISABLED return (BreakpointType_Inactive, FALSE); // Disabled when Constraint_NONE mask = 0; // No masking // Otherwise the value returned by ConstrainUnpredictableBits must // be a not-reserved value. if mask != 0 then
```

```
// When DBGBCR_EL1[n].MASK is a valid nonzero value, the behavior is // CONSTRAINED UNPREDICTABLE if any of the following are true: // - DBGBCR_EL1[n].<BT2,BT> is programmed for a Context matching breakpoint. // - DBGBCR_EL1[n].BAS is not '1111' and AArch32 is supported at EL0. if ((match_cid || match_cid1 || match_cid2) || (DBGBCR_EL1[n].BAS != '1111' && HaveAArch32())) then if !ConstrainUnpredictableBool(Unpredictable_BPMASK) then return (BreakpointType_Inactive, FALSE); else // A stand-alone mismatch of a single address is not supported. if mismatch then return (BreakpointType_Inactive, FALSE); else mask = 0; // Do the comparison. if match_addr then boolean byte_select_match; constant integer byte = UInt(vaddress<1:0>); if HaveAArch32() then // T32 instructions can be executed at EL0 in an AArch64 translation regime. assert byte IN {0,2}; // "vaddress" is halfword aligned byte_select_match = (DBGBCR_EL1[n].BAS<byte> == '1'); else assert byte == 0; // "vaddress" is word aligned byte_select_match = TRUE; // DBGBCR_EL1[n].BAS<byte> is RES1 // When FEAT_LVA3 is not implemented, if the DBGBVR_EL1[n].RESS field bits are not a // sign extension of the MSB of DBGBVR_EL1[n].VA, it is UNPREDICTABLE whether they // appear to be included in the match. // If 'vaddress' is outside of the current virtual address space, then the access // generates a Translation fault. constant AddressSize dbgtop = DebugAddrTop(); constant boolean unpredictable_ress = (dbgtop < 55 && !IsOnes(DBGBVR_EL1[n]<63:dbgtop>) && !IsZero(DBGBVR_EL1[n]<63:dbgtop>) && ConstrainUnpredictableBool(Unpredictable_DBGxVR_RESS)); constant integer cmpmsb = if unpredictable_ress then 63 else dbgtop; constant integer cmplsb = if mask > 2 then mask else 2; bvr_match = ((vaddress<cmpmsb:cmplsb> == DBGBVR_EL1[n]<cmpmsb:cmplsb>) && byte_select_match); if mask > 2 then // If masked bits of DBGBVR_EL1[n] are not zero, the behavior // is CONSTRAINED UNPREDICTABLE. constant integer masktop = mask - 1; if bvr_match && !IsZero(DBGBVR_EL1[n]<masktop:2>) then bvr_match = ConstrainUnpredictableBool(Unpredictable_BPMASKEDBITS); elsif match_cid then if IsInHost() then bvr_match = (CONTEXTIDR_EL2<31:0> == DBGBVR_EL1[n]<31:0>); else bvr_match = (PSTATE.EL IN {EL0, EL1} && CONTEXTIDR_EL1<31:0> == DBGBVR_EL1[n]<31:0>); elsif match_cid1 then bvr_match = (PSTATE.EL IN {EL0, EL1} && !IsInHost() && CONTEXTIDR_EL1<31:0> == DBGBVR_EL1[n]<31:0>); if match_vmid then bits(16) vmid; bits(16) bvr_vmid; if !IsFeatureImplemented(FEAT_VMID16) || VTCR_EL2.VS == '0' then vmid = ZeroExtend(VTTBR_EL2.VMID<7:0>, 16); bvr_vmid = ZeroExtend(DBGBVR_EL1[n]<39:32>, 16);
```

```
else vmid = VTTBR_EL2.VMID; bvr_vmid = DBGBVR_EL1[n]<47:32>; bxvr_match = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !IsInHost() && vmid == bvr_vmid); elsif match_cid2 then bxvr_match = (PSTATE.EL != EL3 && EL2Enabled() && DBGBVR_EL1[n]<63:32> == CONTEXTIDR_EL2<31:0>); bvr_match_valid = (match_addr || match_cid || match_cid1); bxvr_match_valid = (match_vmid || match_cid2); value_match = (!bxvr_match_valid || bxvr_match) && (!bvr_match_valid || bvr_match); // A watchpoint might be linked to a linked address matching breakpoint with linking enabled, // which is in turn linked to a context matching breakpoint. if linked_to && linked then // If called from StateMatch and breakpoint is a linked breakpoint then it must be a // watchpoint that is linked to an address matching breakpoint which is linked to a // context matching breakpoint. assert !isbreakpnt && match_addr && IsFeatureImplemented(FEAT_ABLE); lbnx = if IsFeatureImplemented(FEAT_Debugv8p9) then DBGBCR_EL1[n].LBNX else '00'; linked_linked_n = UInt(lbnx : DBGBCR_EL1[n].LBN); boolean linked_value_match; linked_vaddress = bits(64) UNKNOWN; linked_linked_to = TRUE; linked_isbreakpnt = TRUE; linked_from_linking_enabled = TRUE; (bp_type, linked_value_match) = AArch64.BreakpointValueMatch(linked_linked_n, linked_vaddress, linked_linked_to, linked_isbreakpnt, linked_from_linking_enabled); value_match = value_match && linked_value_match; if match_addr && !mismatch then bp_type = BreakpointType_AddrMatch; elsif match_addr && mismatch then bp_type = BreakpointType_AddrMismatch; elsif match_vmid || match_cid || match_cid1 || match_cid2 then bp_type = BreakpointType_CtxtMatch; else Unreachable(); return (bp_type, value_match);
```

## J1.1.1.27 AArch64.ReservedBreakpointType // AArch64.ReservedBreakpointType() // ================================ // Checks if the given DBGBCR&lt;n&gt;\_EL1.{BT2,BT} values are reserved and will // generate Constrained Unpredictable behavior, otherwise returns Constraint\_NONE. (Constraint, bits(5)) AArch64.ReservedBreakpointType(integer n, bits(5) bt\_in) bits(5) bt = bt\_in; boolean reserved = FALSE; context\_aware = IsContextAwareBreakpoint(n); if bt&lt;4&gt; == '0' then // Context matching if bt != '00x0x' &amp;&amp; !context\_aware then reserved = TRUE; // EL2 extension

```
if bt == '01xxx' && !HaveEL(EL2) then reserved = TRUE; // Context matching if (bt IN {'0011x','011xx'} && !IsFeatureImplemented(FEAT_VHE) && !IsFeatureImplemented(FEAT_Debugv8p2)) then reserved = TRUE; // Reserved if bt == '0010x' && !IsFeatureImplemented(FEAT_BWE) && !HaveAArch32EL(EL1) then reserved = TRUE; else // Reserved if bt != '10x0x' then reserved = TRUE; if reserved then Constraint c; (c, bt) = ConstrainUnpredictableBits(Unpredictable_RESBPTYPE, 5); assert c IN {Constraint_DISABLED, Constraint_UNKNOWN}; if c == Constraint_DISABLED then return (c, bits(5) UNKNOWN); // Otherwise the value returned by ConstrainUnpredictableBits must be a not-reserved value return (Constraint_NONE, bt);
```

```
J1.1.1.28 AArch64.StateMatch // AArch64.StateMatch() // ==================== // Determine whether a breakpoint or watchpoint is enabled in the current mode and state. boolean AArch64.StateMatch(bits(2) ssc_in, bit ssce_in, bit hmc_in, bits(2) pxc_in, boolean linked_in, integer linked_n_in, boolean isbreakpnt, bits(64) vaddress, AccessDescriptor accdesc) if !IsFeatureImplemented(FEAT_RME) then assert ssce_in == '0'; // "ssc_in","ssce_in","hmc_in","pxc_in" are the control fields from // the DBGBCR_EL1[n] or DBGWCR_EL1[n] register. // "linked_in" is TRUE if this is a linked breakpoint/watchpoint type. // "linked_n_in" is the linked breakpoint number from the DBGBCR_EL1[n] or // DBGWCR_EL1[n] register. // "isbreakpnt" is TRUE for breakpoints, FALSE for watchpoints. // "vaddress" is the program counter for a linked watchpoint or the same value passed to // AArch64.CheckBreakpoint for a linked breakpoint. // "accdesc" describes the properties of the access being matched. bits(2) ssc = ssc_in; bit ssce = ssce_in; bit hmc = hmc_in; bits(2) pxc = pxc_in; boolean linked = linked_in; integer linked_n = linked_n_in; // If parameters are set to a reserved type, behaves as either disabled or a defined type Constraint c; (c, ssc, ssce, hmc, pxc) = CheckValidStateMatch(ssc, ssce, hmc, pxc, isbreakpnt); if c == Constraint_DISABLED then return FALSE; // Otherwise the hmc,ssc,ssce,pxc values are either valid or the values returned by // CheckValidStateMatch are valid. EL3_match = HaveEL(EL3) && hmc == '1' && ssc<0> == '0'; EL2_match = HaveEL(EL2) && ((hmc == '1' && (ssc:pxc != '1000')) || ssc == '11'); EL1_match = pxc<0> == '1'; EL0_match = pxc<1> == '1';
```

```
boolean priv_match; case accdesc.el of when EL3 priv_match = EL3_match; when EL2 priv_match = EL2_match; when EL1 priv_match = EL1_match; when EL0 priv_match = EL0_match; // Security state match boolean ss_match; case ssce:ssc of when '000' ss_match = hmc == '1' || accdesc.ss != SS_Root; when '001' ss_match = accdesc.ss == SS_NonSecure; when '010' ss_match = (hmc == '1' && accdesc.ss == SS_Root) || accdesc.ss == SS_Secure; when '011' ss_match = (hmc == '1' && accdesc.ss != SS_Root) || accdesc.ss == SS_Secure; when '101' ss_match = accdesc.ss == SS_Realm; boolean linked_match = FALSE; if linked then // "linked_n" must be an enabled context-aware breakpoint unit. If it is not context-aware // then it is CONSTRAINED UNPREDICTABLE whether this gives no match, gives a match without // linking, or linked_n is mapped to some UNKNOWN breakpoint that is context-aware. if !IsContextAwareBreakpoint(linked_n) then (first_ctx_cmp, last_ctx_cmp) = ContextAwareBreakpointRange(); (c, linked_n) = ConstrainUnpredictableInteger(first_ctx_cmp, last_ctx_cmp, Unpredictable_BPNOTCTXCMP); assert c IN {Constraint_DISABLED, Constraint_NONE, Constraint_UNKNOWN}; case c of when Constraint_DISABLED return FALSE; // Disabled when Constraint_NONE linked = FALSE; // No linking // Otherwise ConstrainUnpredictableInteger returned a context-aware breakpoint if linked then linked_to = TRUE; BreakpointType bp_type; from_linking_enabled = FALSE; (bp_type, linked_match) = AArch64.BreakpointValueMatch(linked_n, vaddress, linked_to, isbreakpnt, from_linking_enabled); if bp_type == BreakpointType_AddrMismatch then linked_match = !linked_match; return priv_match && ss_match && (!linked || linked_match);
```

## J1.1.1.29 DebugAddrTop

```
// DebugAddrTop() // ============== // Returns the value for the top bit used in Breakpoint and Watchpoint address AddressSize DebugAddrTop() if IsFeatureImplemented(FEAT_LVA3) then return 55; elsif IsFeatureImplemented(FEAT_LVA) then return 52; else return 48;
```

## J1.1.1.30 EffectiveMDSELR\_EL1\_BANK

```
// EffectiveMDSELR_EL1_BANK() // ==========================
```

```
comparisons.
```

```
// Return the effective value of MDSELR_EL1.BANK. bits(2) EffectiveMDSELR_EL1_BANK() // If 16 or fewer breakpoints and 16 or fewer watchpoints are implemented, // then the field is RES0. constant integer num_bp = NumBreakpointsImplemented(); constant integer num_wp = NumWatchpointsImplemented(); if num_bp <= 16 && num_wp <= 16 then return '00'; // At EL3, the Effective value of this field is zero if MDCR_EL3.EBWE is 0. // At EL2, the Effective value is zero if the Effective value of MDCR_EL2.EBWE is 0. // That is, if either MDCR_EL3.EBWE is 0 or MDCR_EL2.EBWE is 0. // At EL1, the Effective value is zero if the Effective value of MDSCR_EL2.EMBWE // That is, if any of MDCR_EL3.EBWE, MDCR_EL2.EBWE, or MDSCR_EL1.EMBWE is 0. if ((HaveEL(EL3) && MDCR_EL3.EBWE == '0') || (PSTATE.EL != EL3 && EL2Enabled() && MDCR_EL2.EBWE == '0') || (PSTATE.EL == EL1 && MDSCR_EL1.EMBWE == '0')) then return '00'; bits(2) bank = MDSELR_EL1.BANK; // Values are reserved depending on the number of breakpoints or watchpoints // implemented. if ((bank == '11' && num_bp <= 48 && num_wp <= 48) || (bank == '10' && num_bp <= 32 && num_wp <= 32)) then // Reserved value (-, bank) = ConstrainUnpredictableBits(Unpredictable_RESMDSELR, 2); // The value returned by ConstrainUnpredictableBits must be a not-reserved value return bank;
```

## is 0. J1.1.1.31 IsBreakpointEnabled // IsBreakpointEnabled() // ===================== // Returns TRUE if the effective value of DBGBCR\_EL1[n].E is '1', and FALSE otherwise. boolean IsBreakpointEnabled(integer n) if (n &gt; 15 &amp;&amp; ((!HaltOnBreakpointOrWatchpoint() &amp;&amp; !SelfHostedExtendedBPWPEnabled()) || (HaltOnBreakpointOrWatchpoint() &amp;&amp; EDSCR2.EHBWE == '0'))) then return FALSE; return DBGBCR\_EL1[n].E == '1'; J1.1.1.32 SelfHostedExtendedBPWPEnabled

```
// SelfHostedExtendedBPWPEnabled() // =============================== // Returns TRUE if the extended breakpoints and watchpoints are enabled, and FALSE otherwise // from a self-hosted debug perspective. boolean SelfHostedExtendedBPWPEnabled() if NumBreakpointsImplemented() <= 16 && NumWatchpointsImplemented() <= 16 then return FALSE; if ((HaveEL(EL3) && MDCR_EL3.EBWE == '0') || (EL2Enabled() && MDCR_EL2.EBWE == '0')) then return FALSE; return MDSCR_EL1.EMBWE == '1';
```

## J1.1.1.33 CheckForPMUException

```
// CheckForPMUException() // ====================== // Take a PMU exception if enabled, permitted, and unmasked. CheckForPMUException() boolean enabled; bits(2) target_el; boolean pmu_exception; boolean synchronous; (enabled, target_el) = PMUExceptionEnabled(); if !enabled || PMUExceptionMasked(target_el, PSTATE.EL, PSTATE.PM) then pmu_exception = FALSE; elsif IsFeatureImplemented(FEAT_SEBEP) && PSTATE.PPEND == '1' then pmu_exception = TRUE; synchronous = TRUE; else constant boolean include_r1 = TRUE; constant boolean include_r2 = TRUE; constant boolean include_r3 = TRUE; pmu_exception = CheckPMUOverflowCondition(PMUOverflowCondition_PMUException, include_r1, include_r2, include_r3); synchronous = FALSE; if pmu_exception then constant bits(5) fsc = '00000'; TakeProfilingException(target_el, fsc, synchronous);
```

## J1.1.1.34 EffectivePMEE // EffectivePMEE() // =============== // Return the Effective value of PMEE from MDCR\_ELx or PMECR\_EL1, handling reserved encodings: // '10' (MDCR\_ELx), '10' and '01' (PMECR\_EL1). bits(2) EffectivePMEE(bits(2) el, boolean for\_interrupt) bits(2) val; case el of when EL1 val = PMECR\_EL1.PMEE; when EL2 val = MDCR\_EL2.PMEE; when EL3 val = MDCR\_EL3.PMEE; otherwise Unreachable(); if (val == '10' || (el == EL1 &amp;&amp; val == '01')) then Constraint c; (c, val) = ConstrainUnpredictableBits(Unpredictable\_RESPMEE, 2); assert c IN {Constraint\_DISABLED, Constraint\_UNKNOWN}; if c == Constraint\_DISABLED then val = if for\_interrupt then '11' else '00'; // Otherwise the value returned by ConstrainUnpredictableBits must be // a non-reserved value return val; J1.1.1.35 ExceptionReturnPPEND level.

```
// ExceptionReturnPPEND() // ====================== // Sets ShouldSetPPEND to the value to write to PSTATE.PPEND // on an exception return. // This function is called before any change in Exception ExceptionReturnPPEND(bits(64) spsr) boolean enabled_at_source;
```

```
boolean masked_at_source; if spsr<33> == '1' then // SPSR.PPEND bits(2) target_except; (enabled_at_source, target_except) = PMUExceptionEnabled(); if Restarting() then masked_at_source = TRUE; else masked_at_source = PMUExceptionMasked(target_except, PSTATE.EL, PSTATE.PM); bits(2) target_eret; if IllegalExceptionReturn(spsr) then target_eret = PSTATE.EL; else boolean valid; (valid, target_eret) = ELFromSPSR(spsr); assert valid; constant bit target_pm = spsr<32>; // SPSR.PM constant boolean masked_at_dest = PMUExceptionMasked(target_except, target_eret, target_pm); if enabled_at_source && masked_at_source && !masked_at_dest then PSTATE.PPEND = '1'; ShouldSetPPEND = FALSE; // PSTATE.PPEND will not be changed again by this instruction. // If PSTATE.PPEND has not been set by this function, ShouldSetPPEND is // unchanged, meaning PSTATE.PPEND might either be set by the current instruction // causing a counter overflow, or cleared to zero at the end of instruction. return;
```

```
J1.1.1.36 IsSupportingPMUSynchronousMode // IsSupportingPMUSynchronousMode() // ================================ // Returns TRUE if the event support synchronous mode, // and FALSE otherwise. boolean IsSupportingPMUSynchronousMode(bits(16) pmuevent); J1.1.1.37 PMUExceptionEnabled // PMUExceptionEnabled() // ===================== // The first return value is TRUE if the PMU exception is enabled, and FALSE otherwise. // The second return value is the target Exception level for an enabled PMU exception. (boolean, bits(2)) PMUExceptionEnabled() if !IsFeatureImplemented(FEAT_EBEP) then return (FALSE, bits(2) UNKNOWN); boolean enabled; bits(2) target = bits(2) UNKNOWN; constant boolean for_interrupt = FALSE; constant bits(2) pmee_el3 = EffectivePMEE(EL3, for_interrupt); constant bits(2) pmee_el2 = EffectivePMEE(EL2, for_interrupt); constant bits(2) pmee_el1 = EffectivePMEE(EL1, for_interrupt); if HaveEL(EL3) && pmee_el3 != '01' then enabled = pmee_el3 == '11'; if enabled then target = EL3; elsif EL2Enabled() && pmee_el2 != '01' then
```

```
enabled = pmee_el2 == '11'; if enabled then target = EL2; else enabled = pmee_el1 == '11'; if enabled then target = if EL2Enabled() && HCR_EL2.TGE == '1' then EL2 else EL1; return (enabled, target);
```

## J1.1.1.38 PMUExceptionMasked

```
// PMUExceptionMasked() // ==================== // Return TRUE if the PMU Exception is masked at the specified target Exception level // relative to the specified source Exception level, and by the value of PSTATE.PM, // and FALSE otherwise. boolean PMUExceptionMasked(bits(2) target_el, bits(2) from_el, bit pm) assert IsFeatureImplemented(FEAT_EBEP); constant boolean for_interrupt = FALSE; if Halted() then return TRUE; elsif UInt(target_el) < UInt(from_el) then return TRUE; elsif (from_el == EL2 && target_el == EL2 && EffectivePMEE(EL2, for_interrupt) != '11') then return TRUE; elsif target_el == from_el && (PMECR_EL1.KPME == '0' || pm == '1') then return TRUE; return FALSE;
```

## J1.1.1.39 PMUInterruptEnabled

```
// PMUInterruptEnabled() // ===================== // Return TRUE if the PMU interrupt request (PMUIRQ) is enabled, FALSE otherwise. boolean PMUInterruptEnabled() if !IsFeatureImplemented(FEAT_EBEP) then return TRUE; boolean enabled; constant boolean for_interrupt = TRUE; constant bits(2) pmee_el3 = EffectivePMEE(EL3, for_interrupt); constant bits(2) pmee_el2 = EffectivePMEE(EL2, for_interrupt); constant bits(2) pmee_el1 = EffectivePMEE(EL1, for_interrupt); if HaveEL(EL3) && pmee_el3 != '01' then enabled = pmee_el3 == '00'; elsif EL2Enabled() && pmee_el2 != '01' then enabled = pmee_el2 == '00'; else enabled = pmee_el1 == '00'; return enabled;
```

## J1.1.1.40 inst\_addr\_executed

bits(64) inst\_addr\_executed;

## J1.1.1.41 sync\_counter\_overflowed

boolean sync\_counter\_overflowed;

## J1.1.1.42 AArch64.GenerateDebugExceptions

```
// AArch64.GenerateDebugExceptions() // ================================= boolean AArch64.GenerateDebugExceptions() ss = CurrentSecurityState(); return AArch64.GenerateDebugExceptionsFrom(PSTATE.EL, ss, PSTATE.D);
```

## J1.1.1.43 AArch64.GenerateDebugExceptionsFrom

```
// AArch64.GenerateDebugExceptionsFrom() // ===================================== boolean AArch64.GenerateDebugExceptionsFrom(bits(2) from_el, SecurityState from_state, bit mask) if OSLSR_EL1.OSLK == '1' || DoubleLockStatus() || Halted() then return FALSE; route_to_el2 = (HaveEL(EL2) && (from_state != SS_Secure || IsSecureEL2Enabled()) && (HCR_EL2.TGE == '1' || MDCR_EL2.TDE == '1')); target = (if route_to_el2 then EL2 else EL1); boolean enabled; if HaveEL(EL3) && from_state == SS_Secure then enabled = MDCR_EL3.SDD == '0'; if from_el == EL0 && ELUsingAArch32(EL1) then enabled = enabled || SDER32_EL3.SUIDEN == '1'; else enabled = TRUE; if from_el == target then enabled = enabled && MDSCR_EL1.KDE == '1' && mask == '0'; else enabled = enabled && UInt(target) > UInt(from_el); return enabled;
```

## J1.1.1.44 AArch64.TRCIT

```
// AArch64.TRCIT() // =============== // Determines whether an Instrumentation trace packet should // be generated and then generates an instrumentation trace // containing the value of the register passed as an argument AArch64.TRCIT(bits(64) Xt) ss = CurrentSecurityState(); if TraceInstrumentationAllowed(ss, PSTATE.EL) then TraceInstrumentation(Xt);
```

```
packet
```

## J1.1.1.45 TraceInstrumentation

```
// TraceInstrumentation() // ====================== // Generates an instrumentation trace packet // containing the value of the register passed as an argument TraceInstrumentation(bits(64) Xt);
```

## J1.1.1.46 AArch64.IncrementCycleCounter

```
// AArch64.IncrementCycleCounter() // =============================== // Increment the cycle counter and possibly set overflow bits. AArch64.IncrementCycleCounter() if !CountPMUEvents(CYCLE_COUNTER_ID) then return; bit d = PMCR_EL0.D; // Check divide-by-64 bit lc = PMCR_EL0.LC; boolean lc_enabled; (lc_enabled, -) = PMUExceptionEnabled(); lc = if lc_enabled then '1' else lc; // Effective value of 'D' bit is 0 when Effective value of LC is '1' if lc == '1' then d = '0'; if d == '1' && !HasElapsed64Cycles() then return; constant integer old_value = UInt(PMCCNTR_EL0); constant integer new_value = old_value + 1; PMCCNTR_EL0 = new_value<63:0>; constant integer ovflw = if HaveAArch32() && lc == '0' then 32 else 64; if old_value<64:ovflw> != new_value<64:ovflw> then PMOVSSET_EL0.C = '1'; return;
```

## J1.1.1.47 AArch64.IncrementEventCounter

```
// AArch64.IncrementEventCounter() // =============================== // Increment the specified event counter 'idx' by the specified amount 'increment'. // 'Vm' is the value event counter 'idx-1' is being incremented by if 'idx' is odd, // zero otherwise. // Returns the amount the counter was incremented by. integer AArch64.IncrementEventCounter(integer idx, integer increment_in, integer Vm) integer old_value; integer new_value; old_value = UInt(PMEVCNTR_EL0[idx]); constant integer increment = PMUCountValue(idx, increment_in, Vm); new_value = old_value + increment; bit lp; if IsFeatureImplemented(FEAT_PMUv3p5) then PMEVCNTR_EL0[idx] = new_value<63:0>; boolean pmuexception_enabled; (pmuexception_enabled, -) = PMUExceptionEnabled(); if pmuexception_enabled then lp = '1'; else case GetPMUCounterRange(idx) of
```

```
when PMUCounterRange_R1 lp = PMCR_EL0.LP; when PMUCounterRange_R2 lp = MDCR_EL2.HLP; when PMUCounterRange_R3 lp = '1'; otherwise Unreachable(); else lp = '0'; PMEVCNTR_EL0[idx] = ZeroExtend(new_value<31:0>, 64); constant integer ovflw = if lp == '1' then 64 else 32; if old_value<64:ovflw> != new_value<64:ovflw> then PMOVSSET_EL0<idx> = '1'; // Check for the CHAIN event from an even counter if (idx<0> == '0' && idx + 1 < NUM_PMU_COUNTERS && lp == '0' && (GetPMUCounterRange(idx) == GetPMUCounterRange(idx+1) || ConstrainUnpredictableBool(Unpredictable_COUNT_CHAIN))) then // If PMU counters idx and idx+1 are not in same range, // it is CONSTRAINED UNPREDICTABLE if CHAIN event is counted PMUEvent(PMU_EVENT_CHAIN, 1, idx + 1); if (IsFeatureImplemented(FEAT_SEBEP) && IsSupportingPMUSynchronousMode(PMEVTYPER_EL0[idx].evtCount) && PMINTENSET_EL1<idx> == '1' && PMOVSSET_EL0<idx> == '1' && increment != 0) then SyncCounterOverflowed = TRUE; return increment;
```

## J1.1.1.48 AArch64.PMUCycle // AArch64.PMUCycle() // ================== // Called at the end of each cycle to increment event counters and // check for PMU overflow. In pseudocode, a cycle ends after the // execution of the operational pseudocode. AArch64.PMUCycle() if !IsFeatureImplemented(FEAT\_PMUv3) then return; PMUEvent(PMU\_EVENT\_CPU\_CYCLES); constant integer counters = NUM\_PMU\_COUNTERS; integer Vm = 0; if counters != 0 then for idx = 0 to counters - 1 if CountPMUEvents(idx) then constant integer accumulated = PMUEventAccumulator[idx]; if (idx MOD 2) == 0 then Vm = 0; Vm = AArch64.IncrementEventCounter(idx, accumulated, Vm); PMUEventAccumulator[idx] = 0; AArch64.IncrementCycleCounter(); CheckForPMUOverflow(); J1.1.1.49 TakeProfilingException boolean synchronous)

```
// TakeProfilingException() // ======================== // Takes a Profiling exception. TakeProfilingException(bits(2) target_el, bits(5) fsc, ExceptionRecord except = ExceptionSyndrome(Exception_Profiling); except.syndrome.iss<5:1> = fsc; if synchronous then except.syndrome.iss<0> = '1';
```

```
constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = 0x0; AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.1.50 CheckForSPEException

```
// CheckForSPEException() // ====================== // Take an SPE Profiling exception if pending, permitted, and unmasked. CheckForSPEException() if !IsFeatureImplemented(FEAT_SPE_EXC) then return; if Halted() || Restarting() then return; boolean route_to_el3 = FALSE; boolean route_to_el2 = FALSE; boolean route_to_el1 = FALSE; if HaveEL(EL3) && MDCR_EL3.PMSEE == '1x' then constant boolean pending = PMBSR_EL3.S == '1'; constant boolean masked = PSTATE.EL == EL3; route_to_el3 = pending && !masked; SecurityState owning_ss; bits(2) owning_el; (owning_ss, owning_el) = ProfilingBufferOwner(); constant boolean in_owning_ss = IsCurrentSecurityState(owning_ss); if EffectivePMSCR_EL2_EE() == '1x' then constant boolean pending = PMBSR_EL2.S == '1'; constant boolean masked = (!in_owning_ss || PSTATE.EL == EL3 || (PSTATE.EL == EL2 && (PMSCR_EL2.EE != '11' || PMSCR_EL2.KE == '0' || PSTATE.PM == '1'))); route_to_el2 = pending && !masked; if EffectivePMSCR_EL1_EE() == '11' then constant boolean pending = PMBSR_EL1.S == '1'; constant boolean masked = (!in_owning_ss || PSTATE.EL IN {EL3, EL2} || (PSTATE.EL == EL1 && (PMSCR_EL1.KE == '0' || PSTATE.PM == '1'))); if EffectiveTGE() == '1' then route_to_el2 = route_to_el2 || (pending && !masked); else route_to_el1 = pending && !masked; constant bits(5) fsc = '00001'; // SPE exception constant boolean synchronous = FALSE; // The relative priorities of the following checks is IMPLEMENTATION DEFINED if route_to_el3 then TakeProfilingException(EL3, fsc, synchronous); if route_to_el2 then TakeProfilingException(EL2, fsc, synchronous); if route_to_el1 then TakeProfilingException(EL1, fsc, synchronous);
```

## J1.1.1.51 CheckMDCR\_EL3\_NSPBTrap

```
// CheckMDCR_EL3_NSPBTrap() // ========================
```

```
// Check if the register access is trappable by MDCR_EL3.<NSPBE, NSPB> boolean CheckMDCR_EL3_NSPBTrap() bits(3) state_bits; boolean reserved; (state_bits, reserved) = EffectiveMDCR_EL3_NSPB(); return ((reserved && state_bits[0] == '0' || state_bits[1] != SCR_EL3.NS || (IsFeatureImplemented(FEAT_RME) && state_bits[2] != SCR_EL3.NSE));
```

```
// CollectTimeStamp() // ================== TimeStamp CollectTimeStamp() if !StatisticalProfilingEnabled() then return (-, owning_el) = ProfilingBufferOwner(); if owning_el == EL2 then if PMSCR_EL2.TS == '0' then return TimeStamp_None; else if PMSCR_EL1.TS == '0' then return TimeStamp_None; bits(2) PCT_el1; if !IsFeatureImplemented(FEAT_ECV) then
```

## ConstrainUnpredictableBool(Unpredictable\_RESERVEDNSxB\_Trap)) || J1.1.1.52 CollectContextIDR1 // CollectContextIDR1() // ==================== boolean CollectContextIDR1() if !StatisticalProfilingEnabled() then return FALSE; if PSTATE.EL == EL2 then return FALSE; if EL2Enabled() &amp;&amp; HCR\_EL2.TGE == '1' then return FALSE; return PMSCR\_EL1.CX == '1'; J1.1.1.53 CollectContextIDR2 // CollectContextIDR2() // ==================== boolean CollectContextIDR2() if !StatisticalProfilingEnabled() then return FALSE; if !EL2Enabled() then return FALSE; return PMSCR\_EL2.CX == '1'; J1.1.1.54 CollectPhysicalAddress // CollectPhysicalAddress() // ======================== boolean CollectPhysicalAddress() if !StatisticalProfilingEnabled() then return FALSE; (owning\_ss, owning\_el) = ProfilingBufferOwner(); if HaveEL(EL2) &amp;&amp; (owning\_ss != SS\_Secure || IsSecureEL2Enabled()) then return PMSCR\_EL2.PA == '1' &amp;&amp; (owning\_el == EL2 || PMSCR\_EL1.PA == '1'); else return PMSCR\_EL1.PA == '1'; J1.1.1.55 CollectTimeStamp TimeStamp\_None;

```
PCT_el1 = '0':PMSCR_EL1.PCT<0>; // PCT<1> is RES0 else PCT_el1 = PMSCR_EL1.PCT; if PCT_el1 == '10' then // Reserved value (-, PCT_el1) = ConstrainUnpredictableBits(Unpredictable_PMSCR_PCT, 2); if EL2Enabled() then bits(2) PCT_el2; if !IsFeatureImplemented(FEAT_ECV) then PCT_el2 = '0':PMSCR_EL2.PCT<0>; // PCT<1> is RES0 else PCT_el2 = PMSCR_EL2.PCT; if PCT_el2 == '10' then // Reserved value (-, PCT_el2) = ConstrainUnpredictableBits(Unpredictable_PMSCR_PCT, 2); case PCT_el2 of when '00' return if IsInHost() then TimeStamp_Physical else TimeStamp_Virtual; when '01' if owning_el == EL2 then return TimeStamp_Physical; when '11' assert IsFeatureImplemented(FEAT_ECV); // FEAT_ECV must be implemented if owning_el == EL1 && PCT_el1 == '00' then return if IsInHost() then TimeStamp_Physical else TimeStamp_Virtual; else return TimeStamp_OffsetPhysical; otherwise Unreachable(); case PCT_el1 of when '00' return if IsInHost() then TimeStamp_Physical else TimeStamp_Virtual; when '01' return TimeStamp_Physical; when '11' assert IsFeatureImplemented(FEAT_ECV); // FEAT_ECV must be implemented return TimeStamp_OffsetPhysical; otherwise Unreachable();
```

```
J1.1.1.56 DefaultSPEEvent // DefaultSPEEvent() // ================= // Return the target ELx for an indirect write to PMBSR_ELx for an Other buffer management // event or anything other than a buffer management event. bits(2) DefaultSPEEvent() return ReportSPEEvent(Zeros(6), bits(6) UNKNOWN); J1.1.1.57 EffectiveMDCR_EL3_NSPB
```

```
// EffectiveMDCR_EL3_NSPB() // ======================== // Return the Effective value of MDCR_EL3.{NSPBE, NSPB} field and whether it is a reserved value. (bits(3), boolean) EffectiveMDCR_EL3_NSPB() bits(3) state_bits; boolean reserved = FALSE; if IsFeatureImplemented(FEAT_RME) then state_bits = MDCR_EL3.<NSPBE, NSPB>; if state_bits == '10x' || (!IsFeatureImplemented(FEAT_Secure) && state_bits == '00x') then // Reserved value reserved = TRUE; (-, state_bits) = ConstrainUnpredictableBits(Unpredictable_RESERVEDNSxB, 3);
```

```
else state_bits = '0' : MDCR_EL3.NSPB; return (state_bits, reserved);
```

## J1.1.1.58 EffectivePMBLIMITR\_EL1\_nVM

```
// EffectivePMBLIMITR_EL1_nVM() // ============================ bit EffectivePMBLIMITR_EL1_nVM() if !IsFeatureImplemented(FEAT_SPE_nVM) then return '0'; if HaveEL(EL2) then (owning_ss, owning_el) = ProfilingBufferOwner(); if ((owning_ss != SS_Secure || IsSecureEL2Enabled()) && owning_el == EL1 && PMSCR_EL2.EnVM == '0') then return '0'; return PMBLIMITR_EL1.nVM;
```

## J1.1.1.59 EffectivePMSCR\_EL1\_EE

```
// EffectivePMSCR_EL1_EE() // ======================= // Return the Effective value of PMSCR_EL1.EE for the purpose of controlling the // SPE Profiling exception. bits(2) EffectivePMSCR_EL1_EE() if EffectivePMSCR_EL2_EE() == '00' then return '00'; bits(2) ee = PMSCR_EL1.EE; if ee IN {'01', '10'} then // Reserved value if IsFeatureImplemented(FEAT_NV) then ee<0> = ee<1>; else Constraint c; (c, ee) = ConstrainUnpredictableBits(Unpredictable_RESPMSEE, 2); assert c IN {Constraint_DISABLED, Constraint_UNKNOWN}; if c == Constraint_DISABLED then ee = '00'; // Otherwise the value returned by ConstrainUnpredictableBits must be // a non-reserved value return ee;
```

## J1.1.1.60 EffectivePMSCR\_EL2\_EE

```
// EffectivePMSCR_EL2_EE() // ======================= // Return the Effective value of PMSCR_EL2.EE. bits(2) EffectivePMSCR_EL2_EE() if !IsFeatureImplemented(FEAT_SPE_EXC) then return '00'; if HaveEL(EL3) && MDCR_EL3.PMSEE == '00' then return '00'; constant boolean check_el2 = HaveEL(EL2) && (EffectiveSCR_EL3_NS() == IsSecureEL2Enabled()); return if check_el2 then PMSCR_EL2.EE else '01';
```

```
'1' ||
```

## J1.1.1.61 GetPMBSR\_EL1\_FSC

```
// GetPMBSR_EL1_FSC() // ================== // Query the PMBSR_EL1.FSC field. bits(6) GetPMBSR_EL1_FSC() bits(6) FSC; FSC = PMBSR_EL1<5:0>; return FSC;
```

## J1.1.1.62 GetPMBSR\_EL2\_FSC

```
// GetPMBSR_EL2_FSC() // ================== // Query the PMBSR_EL2.FSC field. bits(6) GetPMBSR_EL2_FSC() bits(6) FSC; FSC = PMBSR_EL2<5:0>; return FSC;
```

## J1.1.1.63 GetPMBSR\_EL3\_FSC

```
// GetPMBSR_EL3_FSC() // ================== // Query the PMBSR_EL3.FSC field. bits(6) GetPMBSR_EL3_FSC() bits(6) FSC; FSC = PMBSR_EL3<5:0>; return FSC;
```

## J1.1.1.64 OtherSPEManagementEvent

```
// OtherSPEManagementEvent() // ========================= // Report an Other buffer management event, with the status code 'bsc' OtherSPEManagementEvent(bits(6) bsc) constant bits(2) target_el = DefaultSPEEvent(); if PMBSR_EL[target_el].S == '0' then PMBSR_EL[target_el].S = '1'; // Assert interrupt or exception PMBSR_EL[target_el].EC = '000000'; // Other buffer management event PMBSR_EL[target_el].MSS = ZeroExtend(bsc, 16); PMBSR_EL[target_el].MSS2 = Zeros(24);
```

## J1.1.1.65 PMBSR\_EL

```
// PMBSR_EL - setter // ================= PMBSRType PMBSR_EL[bits(2) el] bits(64) r; case el of when EL1 r = PMBSR_EL1;
```

```
when EL2 r = PMBSR_EL2; when EL3 r = PMBSR_EL3; otherwise Unreachable(); return r; // PMBSR_EL - getter // ================= PMBSR_EL[bits(2) el] = bits(64) value constant bits(64) r = value; case el of when EL1 PMBSR_EL1 = r; when EL2 PMBSR_EL2 = r; when EL3 PMBSR_EL3 = r; otherwise Unreachable(); return;
```

## J1.1.1.66 ProfilingBufferEnabled

```
// ProfilingBufferEnabled() // ======================== boolean ProfilingBufferEnabled() if !IsFeatureImplemented(FEAT_SPE) || Halted() then return FALSE; (owning_ss, owning_el) = ProfilingBufferOwner(); constant bits(2) state_bits = EffectiveSCR_EL3_NSE() : boolean state_match; case owning_ss of when SS_Secure state_match = state_bits == '00'; when SS_NonSecure state_match = state_bits == '01'; when SS_Realm state_match = state_bits == '11'; constant boolean stopped = SPEProfilingStopped(); return (!ELUsingAArch32(owning_el) && state_match && PMBLIMITR_EL1.E == '1' && !stopped);
```

## J1.1.1.67 ProfilingBufferOwner

```
// ProfilingBufferOwner() // ====================== (SecurityState, bits(2)) ProfilingBufferOwner() SecurityState owning_ss; bits(3) state_bits; if HaveEL(EL3) then (state_bits, -) = EffectiveMDCR_EL3_NSPB(); else state_bits = if SecureOnlyImplementation() then '001' else '011'; case state_bits of when '00x' owning_ss = SS_Secure; when '01x' owning_ss = SS_NonSecure; when '11x' owning_ss = SS_Realm; bits(2) owning_el; if HaveEL(EL2) && (owning_ss != SS_Secure || IsSecureEL2Enabled()) then owning_el = if MDCR_EL2.E2PB == '00' then EL2 else EL1; else
```

```
EffectiveSCR_EL3_NS();
```

```
owning_el = EL1; return (owning_ss, owning_el);
```

## J1.1.1.68 ProfilingSynchronizationBarrier

```
// ProfilingSynchronizationBarrier() // ================================= // Barrier to ensure that all existing profiling data has been formatted, and profiling buffer // addresses have been translated such that writes to the profiling buffer have been // A following DSB completes when writes to the profiling buffer have completed.
```

```
initiated. ProfilingSynchronizationBarrier();
```

## J1.1.1.69 ReportSPEEvent

```
// ReportSPEEvent() // ================ // Return the target ELx for an indirect write to PMBSR_ELx. // When the indirect write is due to a buffer management event: // 'ec_bits' is the Event Class for the management event. // 'fsc_bits' is the Fault Status Code when this is a fault, ignored otherwise. // Otherwise, 'ec_bits' should be Zeros(). bits(2) ReportSPEEvent(bits(6) ec_bits, bits(6) fsc_bits) bits(2) target_el; boolean route_to_el3 = FALSE; boolean route_to_el2 = FALSE; if IsFeatureImplemented(FEAT_SPE_EXC) then constant boolean s1fault = (ec_bits == '100100'); // Stage 1 fault constant boolean s2fault = (ec_bits == '100101'); // Stage 2 fault boolean gpcfault, gpfault; if IsFeatureImplemented(FEAT_RME) then // Granule Protection Check fault, other than GPF. That is, a GPT address size fault, // GPT walk fault, or synchronous External abort on GPT fetch. gpcfault = (ec_bits == '011110'); // Other Granule Protection Fault, reported as Stage 1 or Stage 2 fault. gpfault = ((s1fault || s2fault) && fsc_bits IN {'10001x', '1001xx', '101000'}); else gpcfault = FALSE; gpfault = FALSE; constant boolean sync_ext_abort = ((s1fault || s2fault) && fsc_bits IN {'010000', '01001x', '0101xx', '011011'}); SecurityState owning_ss; bits(2) owning_el; (owning_ss, owning_el) = ProfilingBufferOwner(); if HaveEL(EL3) && MDCR_EL3.PMSEE == '1x' then route_to_el3 = (MDCR_EL3.PMSEE == '11' || gpcfault || (gpfault && SCR_EL3.GPF == '1') || (sync_ext_abort && EffectiveEA() == '1')); if EffectivePMSCR_EL2_EE() == '1x' then route_to_el2 = (PMSCR_EL2.EE == '11' || (s1fault && owning_el == EL2) || s2fault || gpcfault || (gpfault && HCR_EL2.GPF == '1') || (sync_ext_abort && EffectiveHCR_TEA() == '1')); if route_to_el3 then target_el = EL3; elsif route_to_el2 then
```

```
target_el = EL2; else target_el = EL1; return target_el;
```

## J1.1.1.70 SPE

```
// SPE Implementation Constants // ============================ constant integer SPEMaxAddrs = 32; constant integer SPEMaxCounters = 32; constant integer SPEMaxRecordSize = 2048;
```

## J1.1.1.71 SPEAddByteToRecord

```
// SPEAddByteToRecord() // ==================== // Add one byte to a record and increase size property appropriately. SPEAddByteToRecord(bits(8) b) assert SPERecordSize < SPEMaxRecordSize; SPERecordData[SPERecordSize] = b; SPERecordSize = SPERecordSize + 1;
```

## J1.1.1.72 SPEAddPacketToRecord

```
// SPEAddPacketToRecord() // ====================== // Add passed header and payload data to the record. // Payload must be a multiple of 8. SPEAddPacketToRecord(bits(2) header_hi, bits(4) header_lo, bits(N) payload) assert N MOD 8 == 0; bits(2) sz; case N of when 8 sz = '00'; when 16 sz = '01'; when 32 sz = '10'; when 64 sz = '11'; otherwise Unreachable(); constant bits(8) header = header_hi:sz:header_lo; SPEAddByteToRecord(header); for i = 0 to (N DIV 8)-1 SPEAddByteToRecord(Elem[payload, i, 8]);
```

## J1.1.1.73 SPEBranch

```
// SPEBranch() // =========== // Called on every branch if SPE is present. Maintains previous branch target // and branch related SPE functionality. SPEBranch(bits(N) target, BranchType branch_type, boolean conditional, boolean taken_flag) constant boolean is_isb = FALSE; SPEBranch(target, branch_type, conditional, taken_flag, is_isb);
```

```
SPEBranch(bits(N) target, BranchType branch_type, boolean conditional, boolean taken_flag, boolean is_isb) // If the PE implements branch prediction, data about (mis)prediction is collected // through the PMU events. boolean collect_prev_br; constant boolean collect_prev_br_eret = boolean IMPLEMENTATION_DEFINED "SPE prev br on eret"; constant boolean collect_prev_br_exception = (boolean IMPLEMENTATION_DEFINED "SPE prev br on exception"); constant boolean collect_prev_br_isb = boolean IMPLEMENTATION_DEFINED "SPE prev br on isb"; case branch_type of when BranchType_EXCEPTION collect_prev_br = collect_prev_br_exception; when BranchType_ERET collect_prev_br = collect_prev_br_eret; otherwise collect_prev_br = !is_isb || collect_prev_br_isb; // Implements previous branch target functionality if (taken_flag && IsFeatureImplemented(FEAT_SPE_PBT) && StatisticalProfilingEnabled() && collect_prev_br) then if SPESampleInFlight then constant bits(64) previous_target = SPESamplePreviousBranchAddress; SPESampleAddress[SPEAddrPosPrevBranchTarget]<63:0> = previous_target<63:0>; constant boolean previous_branch_valid = SPESamplePreviousBranchAddressValid; SPESampleAddressValid[SPEAddrPosPrevBranchTarget] = previous_branch_valid; // Save the target address for it to be added to a future record. SPESamplePreviousBranchAddress<55:0> = target<55:0>; bit ns; bit nse; case CurrentSecurityState() of when SS_Secure ns = '0'; nse = '0'; when SS_NonSecure ns = '1'; nse = '0'; when SS_Realm ns = '1'; nse = '1'; otherwise Unreachable(); SPESamplePreviousBranchAddress<63> = ns; SPESamplePreviousBranchAddress<60> = nse; SPESamplePreviousBranchAddress<62:61> = PSTATE.EL; SPESamplePreviousBranchAddressValid = TRUE; if !StatisticalProfilingEnabled() then if taken_flag then // Invalidate previous branch address, if profiling is disabled // or prohibited. SPESamplePreviousBranchAddressValid = FALSE; return; if SPESampleInFlight then SPESampleOpAttr.branch_is_direct = branch_type IN {BranchType_DIR, BranchType_DIRCALL}; SPESampleOpAttr.branch_has_link = branch_type IN {BranchType_DIRCALL, BranchType_INDCALL}; SPESampleOpAttr.procedure_return = branch_type == BranchType_RET; SPESampleOpAttr.op_type = SPEOpType_Branch; SPESampleOpAttr.is_conditional = conditional; SPESampleOpAttr.cond_pass = taken_flag; // Save the target address. if taken_flag then
```

```
bit ns; bit nse; case CurrentSecurityState() of when SS_Secure ns = '0'; nse = '0'; when SS_NonSecure ns = '1'; nse = '0'; when SS_Realm ns = '1'; nse = '1'; otherwise Unreachable(); constant bits(2) el = PSTATE.EL; SPESampleAddress[SPEAddrPosBranchTarget]<55:0> = target<55:0>; SPESampleAddress[SPEAddrPosBranchTarget]<63:56> = ns:el:nse:Zeros(4); SPESampleAddressValid[SPEAddrPosBranchTarget] = TRUE;
```

## J1.1.1.74 SPEBufferIsFull

```
// SPEBufferIsFull() // ================= // Return true if another full size sample record would not fit in the // profiling buffer. boolean SPEBufferIsFull() constant integer write_pointer_limit = UInt(PMBLIMITR_EL1.LIMIT:Zeros(12)); constant integer current_write_pointer = UInt(PMBPTR_EL1); constant integer record_max_size = 1<<UInt(PMSIDR_EL1.MaxSize); return current_write_pointer > (write_pointer_limit - record_max_size);
```

## J1.1.1.75 SPECollectRecord

```
// SPECollectRecord() // ================== // Returns TRUE if the sampled class of instructions or operations, as // determined by PMSFCR_EL1, are recorded and FALSE otherwise. boolean SPECollectRecord(bits(64) events, integer total_latency, SPEOpType optype) // Filtering by events boolean is_rejected_event; boolean is_rejected_nevent; (is_rejected_event, is_rejected_nevent) = SPEFilterByEvents(events); // Filtering by type constant boolean is_rejected_type = SPEFilterByType(SPESampleOpAttr); // Filtering by latency constant boolean is_rejected_latency = SPEFilterByLatency(total_latency); constant boolean is_rejected_data_source = SPEFilterByDataSource(optype); boolean return_value; return_value = !(is_rejected_nevent || is_rejected_event || is_rejected_type || is_rejected_latency || is_rejected_data_source); if return_value then PMUEvent(PMU_EVENT_SAMPLE_FILTRATE); return return_value;
```

## J1.1.1.76 SPECompleteSample

```
// Order of addresses in sample storage and architectural index values constant integer SPEAddrPosPCVirtual = 0; constant integer SPEAddrPosBranchTarget = 1; constant integer SPEAddrPosDataVirtual = 2; constant integer SPEAddrPosDataPhysical = 3; constant integer SPEAddrPosPrevBranchTarget = 4; // Order of counters in sample storage and architectural index values constant integer SPECounterPosTotalLatency = 0; constant integer SPECounterPosIssueLatency = 1; constant integer SPECounterPosTranslationLatency = 2; constant integer SPECounterPosAltIssueLatency = 4; // Sample in-flight flag boolean SPESampleInFlight = FALSE; // Globally declared variables which store data about the sample. // Context storage bits(32) SPESampleContextEL1; boolean SPESampleContextEL1Valid; bits(32) SPESampleContextEL2; boolean SPESampleContextEL2Valid; bits(64) SPESamplePreviousBranchAddress; boolean SPESamplePreviousBranchAddressValid; // Data source storage bits(16) SPESampleDataSource; boolean SPESampleDataSourceValid; // OpAttr storage SPEOpAttr SPESampleOpAttr; // Timestamp storage bits(64) SPESampleTimestamp; boolean SPESampleTimestampValid; // Event storage bits(64) SPESampleEvents; // SPECompleteSample() // =================== // Called to complete the sampling process. SPECompleteSample() assert SPESampleInFlight; PMUEvent(PMU_EVENT_SAMPLE_FEED); // Stop any pending counters for counter_index = 0 to (SPEMaxCounters - 1) if SPESampleCounterPending[counter_index] then SPEStopCounter(counter_index); // Record any IMPLEMENTATION DEFINED events constant bits(64) impdef_events = bits(64) IMPLEMENTATION_DEFINED "SPE EVENTS"; SPESampleEvents<63:48> = impdef_events<63:48>; // The number of bits available for IMPLEMENTATION DEFINED events // is reduced by FEAT_SPEv1p4 if !IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<31:24> = impdef_events<31:24>; SPESampleEvents<15:12> = impdef_events<15:12>; // Bit 24 encodes whether the sample was collected in Streaming SVE mode. if IsFeatureImplemented(FEAT_SPE_SME) then SPESampleEvents<24> = PSTATE.SM; SPESampleEvents<6> = if (SPESampleOpAttr.is_conditional && !SPESampleOpAttr.cond_pass) then '1' else '0'; boolean collect_record; collect_record = SPECollectRecord(SPESampleEvents, SPESampleCounter[SPECounterPosTotalLatency],
```

```
SPESampleOpAttr.op_type); boolean discard = FALSE; if IsFeatureImplemented(FEAT_SPEv1p2) then discard = PMBLIMITR_EL1.FM == '10'; if collect_record && !discard then SPEConstructRecord(); if SPEBufferIsFull() then constant bits(6) bsc = '000001'; // Buffer full OtherSPEManagementEvent(bsc); PMUEvent(PMU_EVENT_SAMPLE_BUFFER_FULL); SPESampleInFlight = FALSE; SPEResetSampleStorage(); // Counter storage array [0..SPEMaxCounters-1] of integer SPESampleCounter; array [0..SPEMaxCounters-1] of boolean SPESampleCounterValid; array [0..SPEMaxCounters-1] of boolean SPESampleCounterPending; // Address storage array [0..SPEMaxAddrs-1] of bits(64) SPESampleAddress; array [0..SPEMaxAddrs-1] of boolean SPESampleAddressValid;
```

```
// SPEConstructClass() // =================== // Constructs the encodings for the class and subclass fields. (bits(2), bits(8)) SPEConstructClass() bits(2) op_class; bits(8) op_subclass; constant bit cond = if SPESampleOpAttr.is_conditional then '1' else '0'; constant bit fp = if SPESampleOpAttr.is_floating_point then '1' else '0'; constant bit ldst = if SPESampleOpAttr.op_type == SPEOpType_Store then '1' else '0'; constant bit ar = if SPESampleOpAttr.is_acquire_release then '1' else '0'; constant bit excl = if SPESampleOpAttr.is_exclusive then '1' else '0'; constant bit at = if SPESampleOpAttr.at then '1' else '0'; constant bit indirect = if SPESampleOpAttr.branch_is_direct then '0' else '1'; constant bit pred = if SPESampleOpAttr.is_predicated then '1' else '0'; constant bit sg = if SPESampleOpAttr.is_gather_scatter then '1' else '0'; constant bits(3) evl = SPESampleOpAttr.evl; constant bit simd = if SPESampleOpAttr.is_simd then '1' else '0'; constant bits(4) ets = SPESampleOpAttr.ets; // Since this implementation of SPE samples instruction instead of micro-operations, a // Branch with link or Procedure return instruction will never be recorded as a // GCS" format Operation Type packet. Therefore the COMMON bit is hard-wired to '1'. constant bit common = '1'; if SPESampleOpAttr.op_type == SPEOpType_Other then op_class = '00'; op_subclass = Zeros(5):simd:fp:cond; elsif SPESampleOpAttr.op_type == SPEOpType_OtherSVE then op_class = '00'; op_subclass = '0':evl:'1':pred:fp:'0'; elsif SPESampleOpAttr.op_type == SPEOpType_OtherSME then op_class = '00'; op_subclass = '1':ets<3:1>:'1':ets<0>:fp:'0'; elsif SPESampleOpAttr.op_type == SPEOpType_Branch then op_class = '10'; bits(2) cr = '00'; bit gcs = '0';
```

```
event J1.1.1.77 SPEConstructClass "Load/store,
```

```
if IsFeatureImplemented(FEAT_SPE_CRR) then if SPESampleOpAttr.branch_has_link then cr = '01'; elsif SPESampleOpAttr.procedure_return then cr = '10'; else cr = '11'; if IsFeatureImplemented(FEAT_GCS) then if (SPESampleOpAttr.ldst_type == SPELDSTType_GCS && (SPESampleOpAttr.branch_has_link || SPESampleOpAttr.procedure_return)) then gcs = '1'; op_subclass = Zeros(3):cr:gcs:indirect:cond; elsif SPESampleOpAttr.op_type IN {SPEOpType_Load, SPEOpType_Store, SPEOpType_LoadAtomic} then op_class = '01'; case SPESampleOpAttr.ldst_type of when SPELDSTType_NV2 op_subclass = '0011000':ldst; when SPELDSTType_Extended op_subclass = '000':ar:excl:at:'1':ldst; when SPELDSTType_General op_subclass = Zeros(7):ldst; when SPELDSTType_SIMDFP op_subclass = '0000010':ldst; when SPELDSTType_SVESME op_subclass = sg:evl:'1':pred:'0':ldst; when SPELDSTType_Unspecified op_subclass = '0001000':ldst; when SPELDSTType_Tags op_subclass = '0001010':ldst; when SPELDSTType_MemCopy op_subclass = '0010000':ldst; when SPELDSTType_MemSet op_subclass = '00100101'; when SPELDSTType_GCS op_subclass = '01000':common:'0':ldst; when SPELDSTType_GCSSS2 // GCSSS2 is converted to GCS, should not appear here Unreachable(); otherwise Unreachable(); else Unreachable(); return (op_class, op_subclass);
```

```
J1.1.1.78 SPEConstructRecord data.
```

```
// SPEConstructRecord() // ==================== // Create new record and populate it with packets using sample storage // This is an example implementation, packets may appear in // any order as long as the record ends with an End or Timestamp packet. SPEConstructRecord() // Empty the record. SPEEmptyRecord(); // Add contextEL1 if available if SPESampleContextEL1Valid then SPEAddPacketToRecord('01', '0100', SPESampleContextEL1); // Add contextEL2 if available if SPESampleContextEL2Valid then SPEAddPacketToRecord('01', '0101', SPESampleContextEL2); // Add valid counters
```

```
for counter_index = 0 to (SPEMaxCounters - 1) if SPESampleCounterValid[counter_index] then if counter_index >= 8 then // Need extended format SPEAddByteToRecord('001000':counter_index<4:3>); // Check for overflow constant boolean large_counters = boolean IMPLEMENTATION_DEFINED "SPE 16bit counters"; if large_counters then if SPESampleCounter[counter_index] > 0xFFFF then SPESampleCounter[counter_index] = 0xFFFF; else if SPESampleCounter[counter_index] > 0xFFF then SPESampleCounter[counter_index] = 0xFFF; // Add byte0 for short format (byte1 for extended format) SPEAddPacketToRecord('10', '1':counter_index<2:0>, SPESampleCounter[counter_index]<15:0>); // Add valid addresses if IsFeatureImplemented(FEAT_SPE_PBT) then // Under the some conditions, it is IMPLEMENTATION_DEFINED whether // previous branch packet is present. constant boolean include_prev_br = (boolean IMPLEMENTATION_DEFINED "SPE get prev br if not br"); if SPESampleOpAttr.op_type != SPEOpType_Branch && !include_prev_br then SPESampleAddressValid[SPEAddrPosPrevBranchTarget] = FALSE; // Data Virtual address should not be collected if this was an NV2 access and Statistical // Profiling is disabled at EL2. if !StatisticalProfilingEnabled(EL2) && SPESampleOpAttr.ldst_type == SPELDSTType_NV2 then SPESampleAddressValid[SPEAddrPosDataVirtual] = FALSE; for address_index = 0 to (SPEMaxAddrs - 1) if SPESampleAddressValid[address_index] then if address_index >= 8 then // Need extended format SPEAddByteToRecord('001000':address_index<4:3>); // Add byte0 for short format (byte1 for extended format) SPEAddPacketToRecord('10', '0':address_index<2:0>, SPESampleAddress[address_index]); // Add Data Source if SPESampleDataSourceValid then constant integer ds_payload_size = SPEGetDataSourcePayloadSize(); SPEAddPacketToRecord('01', '0011', SPESampleDataSource<8*ds_payload_size-1:0>); bits(2) op_class; bits(8) op_subclass; (op_class, op_subclass) = SPEConstructClass(); // Add operation details SPEAddPacketToRecord('01', '10':op_class, op_subclass); // Add events // Get size of payload in bytes. constant integer payload_size = SPEGetEventsPayloadSize(); SPEAddPacketToRecord('01', '0010', SPESampleEvents<8*payload_size-1:0>); // Add Timestamp to end the record if one is available. // Otherwise end with an End packet. if SPESampleTimestampValid then SPEAddPacketToRecord('01', '0001', SPESampleTimestamp); else SPEAddByteToRecord('00000001'); // Add padding while SPERecordSize MOD (1<<UInt(PMBIDR_EL1.Align)) != 0 do
```

```
SPEAddByteToRecord(Zeros(8)); SPEWriteToBuffer(); CTI_SignalEvent(CrossTriggerIn_SPESample);
```

## J1.1.1.79 SPECycle

```
// SPECycle() // ========== // Function called at the end of every cycle. Responsible for asserting interrupts // and advancing counters. SPECycle() if !IsFeatureImplemented(FEAT_SPE) then return; // Increment pending counters if SPESampleInFlight then for i = 0 to (SPEMaxCounters - 1) if SPESampleCounterPending[i] then SPESampleCounter[i] = SPESampleCounter[i] + 1; // Assert PMBIRQ if appropriate. if SPEInterruptEnabled() && PMBSR_EL1.S == '1' then SetInterruptRequestLevel(InterruptID_PMBIRQ, HIGH); else SetInterruptRequestLevel(InterruptID_PMBIRQ, LOW);
```

## J1.1.1.80 SPEEmptyRecord

```
// SPEEmptyRecord() // ================ // Reset record data. SPEEmptyRecord() SPERecordSize = 0; for i = 0 to (SPEMaxRecordSize - 1) SPERecordData[i] = Zeros(8);
```

## J1.1.1.81 SPEEncodeETS

```
// SPEEncodeETS() // ============== // Encodes an integer tile size length into the ets field for the SPE operation type packet. bits(4) SPEEncodeETS(integer size) bits(4) ets; if size <= 128 then ets = '0000'; elsif size <= 256 then ets = '0001'; elsif size <= 512 then ets = '0010'; elsif size <= 1024 then ets = '0011'; elsif size <= 2048 then ets = '0100'; elsif size <= 4096 then ets = '0101'; elsif size <= 8192 then ets = '0110'; elsif size <= 16384 then
```

```
ets = '0111'; elsif size <= 32768 then ets = '1000'; elsif size <= 65536 then ets = '1001'; elsif size <= 131072 then ets = '1010'; elsif size <= 262144 then ets = '1011'; else ets = '1111'; return ets;
```

## J1.1.1.82 SPEEncodeEVL

```
// SPEEncodeEVL() // ============== // Encodes an integer vector length into the evl field for the SPE operation type packet. bits(3) SPEEncodeEVL(integer vl) bits(3) evl; if vl <= 32 then evl = '000'; elsif vl <= 64 then evl = '001'; elsif vl <= 128 then evl = '010'; elsif vl <= 256 then evl = '011'; elsif vl <= 512 then evl = '100'; elsif vl <= 1024 then evl = '101'; elsif vl <= 2048 then evl = '110'; else if IsFeatureImplemented(FEAT_SPE_SME) then evl = '111'; else Unreachable(); return evl;
```

## J1.1.1.83 SPEEvent

```
// SPEEvent() // ========== // Called when a PMU event is generated by the sampled structure. // Sets appropriate bit in SPESampleStorage.events. SPEEvent(bits(16) pmuevent) if !SPESampleInFlight then return; case pmuevent of when PMU_EVENT_DSNP_HIT_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<23> = '1'; // Snoop hit when PMU_EVENT_L1D_LFB_HIT_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<22> = '1'; // Recent fetch when PMU_EVENT_L2D_LFB_HIT_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<22> = '1'; // Recent fetch when PMU_EVENT_L3D_LFB_HIT_RD
```

```
if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<22> = '1'; // Recent fetch when PMU_EVENT_LL_LFB_HIT_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<22> = '1'; // Recent fetch when PMU_EVENT_L1D_CACHE_HITM_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<21> = '1'; // Modified when PMU_EVENT_L2D_CACHE_HITM_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<21> = '1'; // Modified when PMU_EVENT_L3D_CACHE_HITM_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<21> = '1'; // Modified when PMU_EVENT_LL_CACHE_HITM_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<21> = '1'; // Modified when PMU_EVENT_L2D_CACHE_LMISS_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<20> = '1'; // L2 miss when PMU_EVENT_L2D_CACHE_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<19> = '1'; // L2 access when PMU_EVENT_SVE_PRED_EMPTY_SPEC if IsFeatureImplemented(FEAT_SPEv1p1) then SPESampleEvents<18> = '1'; // Empty predicate when PMU_EVENT_SVE_PRED_NOT_FULL_SPEC if IsFeatureImplemented(FEAT_SPEv1p1) then SPESampleEvents<17> = '1'; // Partial predicate when PMU_EVENT_LDST_ALIGN_LAT if IsFeatureImplemented(FEAT_SPEv1p1) then SPESampleEvents<11> = '1'; // Misaligned when PMU_EVENT_REMOTE_ACCESS SPESampleEvents<10> = '1'; // Remote access when PMU_EVENT_LL_CACHE_MISS SPESampleEvents<9> = '1'; // LLC miss when PMU_EVENT_LL_CACHE SPESampleEvents<8> = '1'; // LLC access when PMU_EVENT_BR_MIS_PRED SPESampleEvents<7> = '1'; // Mispredicted when PMU_EVENT_BR_MIS_PRED_RETIRED SPESampleEvents<7> = '1'; // Not taken when PMU_EVENT_DTLB_WALK SPESampleEvents<5> = '1'; // TLB walk when PMU_EVENT_L1D_TLB SPESampleEvents<4> = '1'; // TLB access when PMU_EVENT_L1D_CACHE_REFILL if !IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<3> = '1'; // L1 refill when PMU_EVENT_L1D_CACHE_LMISS_RD if IsFeatureImplemented(FEAT_SPEv1p4) then SPESampleEvents<3> = '1'; // L1 miss when PMU_EVENT_L1D_CACHE SPESampleEvents<2> = '1'; // L1 access when PMU_EVENT_INST_RETIRED SPESampleEvents<1> = '1'; // Retire when PMU_EVENT_EXC_TAKEN SPESampleEvents<0> = '1'; // Exception otherwise return; return;
```

## J1.1.1.84 SPEFilterByDataSource

```
// SPEFilterByDataSource() // ======================= // Carry out filtering by data source. boolean SPEFilterByDataSource(SPEOpType optype) // Filtering by Data Source boolean is_rejected_data_source = FALSE; if (IsFeatureImplemented(FEAT_SPE_FDS) && SPESampleDataSourceValid && (optype IN {SPEOpType_Load, SPEOpType_LoadAtomic})) then constant bits(16) data_source = SPESampleDataSource; constant integer index = UInt(data_source<5:0>); constant boolean is_ds = PMSDSFR_EL1<index> == '1';
```

```
if is_ds then PMUEvent(PMU_EVENT_SAMPLE_FEED_DS); if PMSFCR_EL1.FDS == '1' then // Filtering by Data Source is enabled is_rejected_data_source = !is_ds; return is_rejected_data_source;
```

## J1.1.1.85 SPEFilterByEvents

```
// SPEFilterByEvents() // =================== // Carries out filtering by the event bits. (boolean, boolean) SPEFilterByEvents(bits(64) events) // "mask" defines which Events packet bits are checked by the filter bits(64) mask = Zeros(64); constant bits(64) impdef_mask = bits(64) IMPLEMENTATION_DEFINED "SPE mask"; mask<63:48> = impdef_mask<63:48>; if IsFeatureImplemented(FEAT_SPE_SME) && IsFeatureImplemented(FEAT_SPEv1p4) then mask<25:24> = '11'; // Streaming mode, SMCU if IsFeatureImplemented(FEAT_SPEv1p4) then mask<23:19> = '11111'; // Snoop hit, recent fetch, modified, // L2 miss, L2 access else mask<31:24> = impdef_mask<31:24>; if IsFeatureImplemented(FEAT_SPEv1p1) && IsFeatureImplemented(FEAT_SVE) then mask<18:17> = '11'; // Predicates mask<15:12> = impdef_mask<15:12>; if IsFeatureImplemented(FEAT_SPEv1p1) then mask<11> = '1'; // Data alignment if IsFeatureImplemented(FEAT_SPEv1p4) then mask<10:8> = '111'; // Remote access, LLC access, LLC miss else mask<10:8> = impdef_mask<10:8>; mask<7> = '1'; // Mispredicted if IsFeatureImplemented(FEAT_SPE_FnE) then mask<6> = '1'; // Not taken mask<5,3,1> = '111'; // TLB walk, L1 miss, retired if IsFeatureImplemented(FEAT_SPEv1p4) then mask<4,2> = '11'; // TLB access, L1 access else mask<4,2> = impdef_mask<4,2>; constant bits(64) e = events AND mask; // Filtering by event constant bits(64) evfr = PMSEVFR_EL1 AND mask; boolean is_rejected_event = FALSE; constant boolean is_evt = IsZero(NOT(e) AND evfr); if PMSFCR_EL1.FE == '1' then // Filtering by event is enabled if !IsZero(evfr) then // Not a CONSTRAINED UNPREDICTABLE case is_rejected_event = !is_evt; else is_rejected_event = ConstrainUnpredictableBool(Unpredictable_BADPMSFCR); // Filtering by inverse event boolean is_rejected_nevent = FALSE; boolean is_nevt; if IsFeatureImplemented(FEAT_SPE_FnE) then constant bits(64) nevfr = PMSNEVFR_EL1 AND mask; is_nevt = IsZero(e AND nevfr); if PMSFCR_EL1.FnE == '1' then // Inverse filtering by event is enabled
```

```
if !IsZero(nevfr) then // Not a CONSTRAINED UNPREDICTABLE case is_rejected_nevent = !is_nevt; else is_rejected_nevent else is_nevt = TRUE; // not implemented if is_evt && is_nevt then PMUEvent(PMU_EVENT_SAMPLE_FEED_EVENT); if (IsFeatureImplemented(FEAT_SPE_FnE) && PMSFCR_EL1.<FnE,FE> == '11' && !IsZero(PMSEVFR_EL1 AND PMSNEVFR_EL1 AND mask)) then // CONSTRAINED UNPREDICTABLE case due to combination of filter and inverse is_rejected_nevent = ConstrainUnpredictableBool(Unpredictable_BADPMSFCR); is_rejected_event = ConstrainUnpredictableBool(Unpredictable_BADPMSFCR); return (is_rejected_event, is_rejected_nevent);
```

```
// SPEFilterByType() // ================= // Returns TRUE if the operation is to be discarded because of its OpAttrs, and FALSE boolean SPEFilterByType(SPEOpAttr opattr) // Bit positions in the PMSFCR_EL1.{TYPE, TYPEm} fields constant integer B = 0; constant integer LD = 1; constant integer ST = 2; constant integer FP = 3; constant integer SIMD = 4; bits(5) flags = Zeros(5); bits(5) ctrl = Zeros(5); // With GCS, Branch Link and Procedure Return instructions write and read the GCS. // BL and RET instructions with GCS enabled call SPESampleLoadStore() before // branch/packet construction, setting ldst_type to indicate a GCS access. constant boolean is_gcs_ldst = (opattr.op_type == SPEOpType_Branch && opattr.ldst_type == SPELDSTType_GCS); constant boolean is_load = (opattr.op_type IN {SPEOpType_Load, SPEOpType_LoadAtomic} || (is_gcs_ldst && opattr.procedure_return)); constant boolean is_store = (opattr.op_type IN {SPEOpType_Store, SPEOpType_LoadAtomic}
```

## = ConstrainUnpredictableBool(Unpredictable\_BADPMSFCR); filter J1.1.1.86 SPEFilterByLatency // SPEFilterByLatency() // ==================== // Carries out filtering by latency. boolean SPEFilterByLatency(integer total\_latency) constant boolean is\_lat = (total\_latency &gt;= UInt(PMSLATFR\_EL1.MINLAT)); if is\_lat then PMUEvent(PMU\_EVENT\_SAMPLE\_FEED\_LAT); boolean is\_rejected\_latency = FALSE; if PMSFCR\_EL1.FL == '1' then // Filtering by latency is enabled if !IsZero(PMSLATFR\_EL1.MINLAT) then // Not a CONSTRAINED UNPREDICTABLE case is\_rejected\_latency = is\_rejected\_latency || !is\_lat; else is\_rejected\_latency = ConstrainUnpredictableBool(Unpredictable\_BADPMSFCR); return is\_rejected\_latency; J1.1.1.87 SPEFilterByType otherwise.

```
|| (is_gcs_ldst && opattr.branch_has_link)); flags<B> = (if opattr.op_type == SPEOpType_Branch then '1' else '0'); flags<LD> = (if is_load then '1' else '0'); flags<ST> = (if is_store then '1' else '0'); flags<FP> = (if opattr.is_floating_point then '1' else '0'); flags<SIMD> = (if opattr.is_simd then '1' else '0'); ctrl<2:0> = PMSFCR_EL1.TYPE<2:0>; bits(5) mask = Zeros(5); if IsFeatureImplemented(FEAT_SPE_EFT) then ctrl<4:3> = PMSFCR_EL1.TYPE<4:3>; mask<4:0> = PMSFCR_EL1.TYPEm; constant bits(5) ctrl_or = (ctrl AND (NOT mask)); constant bits(5) ctrl_and = (ctrl AND mask); constant boolean is_op = ((IsZero(ctrl_or) || !IsZero(flags AND ctrl_or)) && ((flags AND mask) == ctrl_and)); if flags<B> == '1' then PMUEvent(PMU_EVENT_SAMPLE_FEED_BR); if flags<LD> == '1' then PMUEvent(PMU_EVENT_SAMPLE_FEED_LD); if flags<ST> == '1' then PMUEvent(PMU_EVENT_SAMPLE_FEED_ST); if flags<FP> == '1' then PMUEvent(PMU_EVENT_SAMPLE_FEED_FP); if flags<SIMD> == '1' then PMUEvent(PMU_EVENT_SAMPLE_FEED_SIMD); boolean is_rejected_type = FALSE; if PMSFCR_EL1.FT == '1' then // Filtering by type is enabled if IsFeatureImplemented(FEAT_SPE_EFT) || !IsZero(ctrl) then is_rejected_type = !is_op; else is_rejected_type = ConstrainUnpredictableBool(Unpredictable_BADPMSFCR); if is_op return is_rejected_type;
```

```
// SPEFreezeOnEvent() // ================== // Returns TRUE if PMU event counter idx should be frozen due to an SPE event, and FALSE boolean SPEFreezeOnEvent(integer idx) constant integer counters = NUM_PMU_COUNTERS; assert (idx >= 0 && (idx < counters || idx == CYCLE_COUNTER_ID || (idx == INSTRUCTION_COUNTER_ID && IsFeatureImplemented(FEAT_PMUv3_ICNTR)))); if !IsFeatureImplemented(FEAT_SPEv1p2) || !IsFeatureImplemented(FEAT_PMUv3p7) then return FALSE; if idx == CYCLE_COUNTER_ID && !IsFeatureImplemented(FEAT_SPE_DPFZS) then // FZS does not affect the cycle counter when FEAT_SPE_DPFZS is not implemented return FALSE; constant boolean freeze_on_event = PMBLIMITR_EL1.<E,PMFZ> == '11'; constant boolean stopped = SPEProfilingStopped(); case GetPMUCounterRange(idx) of when PMUCounterRange_R1 return freeze_on_event && stopped && PMCR_EL0.FZS == '1'; when PMUCounterRange_R2 return freeze_on_event && stopped && MDCR_EL2.HPMFZS == '1'; otherwise return FALSE;
```

```
&& (!IsZero(ctrl) || !IsZero(mask)) then PMUEvent(PMU_EVENT_SAMPLE_FEED_OP); J1.1.1.88 SPEFreezeOnEvent otherwise.
```

## J1.1.1.89 SPEGetDataSource

```
// SPEGetDataSource() // ================== // Returns a tuple indicating the data source for an access passed to SPESampleLoadStore, and // whether the data source is valid. (boolean, bits(16)) SPEGetDataSource(boolean is_load, AccessDescriptor accdesc, AddressDescriptor addrdesc);
```

```
J1.1.1.90 SPEGetDataSourcePayloadSize // SPEGetDataSourcePayloadSize() // ============================= // Returns the size of the Data Source payload in bytes. integer SPEGetDataSourcePayloadSize() return integer IMPLEMENTATION_DEFINED "SPE Data Source packet payload size"; J1.1.1.91 SPEGetEventsPayloadSize // SPEGetEventsPayloadSize() // ========================= // Returns the size in bytes of the Events packet payload as an integer. integer SPEGetEventsPayloadSize() return integer IMPLEMENTATION_DEFINED "SPE Events packet payload size"; J1.1.1.92 SPEGetRandomBoolean // SPEGetRandomBoolean() // ===================== // Returns a random or pseudo-random boolean value. boolean SPEGetRandomBoolean(); J1.1.1.93 SPEGetRandomInterval // SPEGetRandomInterval() // ====================== // Returns a random or pseudo-random byte for resetting COUNT or ECOUNT. bits(8) SPEGetRandomInterval(); J1.1.1.94 SPEISB branches.
```

```
// SPEISB() // ======== // Called by ISB instruction, correctly calls SPEBranch to save previous SPEISB() constant bits(64) address = PC64 + 4; constant BranchType branch_type = BranchType_DIR; constant boolean branch_conditional = FALSE; constant boolean taken = FALSE; constant boolean is_isb = TRUE; SPEBranch(address, branch_type, branch_conditional, taken, is_isb);
```

## J1.1.1.95 SPEInterruptEnabled

```
// SPEInterruptEnabled() // ===================== // Return TRUE if the SPE interrupt request (PMBIRQ) is enabled, FALSE boolean SPEInterruptEnabled() return EffectivePMSCR_EL1_EE() == '00';
```

## J1.1.1.96 SPELDSTType

```
// SPELDSTType // =========== // Type of a load or store enumeration SPELDSTType { SPELDSTType_NV2, SPELDSTType_Extended, SPELDSTType_General, SPELDSTType_SIMDFP, SPELDSTType_SVESME, SPELDSTType_Tags, SPELDSTType_MemCopy, SPELDSTType_MemSet, SPELDSTType_GCS, SPELDSTType_GCSSS2, SPELDSTType_Unspecified };
```

```
operation.
```

## J1.1.1.97 SPEMultiAccessSample

```
// SPEMultiAccessSample() // ====================== // Called by instructions which make at least one store and one load access, where the configuration // of the operation type filter affects which access is sampled. boolean SPEMultiAccessSample() // If loads or stores are filtered out, the other should be recorded. // If neither or both are filtered out, pick one in an unbiased way. // Bit positions in the PMSFCR.{TYPE, TYPEm} fields. constant integer LD = 1; constant integer ST = 2; // Are loads allowed by filter? constant boolean loads_pass_filter = PMSFCR_EL1.FT == '1' && PMSFCR_EL1.TYPE<LD> == '1'; // Are stores allowed by filter? constant boolean stores_pass_filter = PMSFCR_EL1.FT == '1' && PMSFCR_EL1.TYPE<ST> == '1'; boolean record_load; if loads_pass_filter && !stores_pass_filter then // Only loads pass filter record_load = TRUE; elsif !loads_pass_filter && stores_pass_filter then // Only stores pass filter record_load = FALSE; else // Both loads and stores pass the filter or neither pass the filter. // Pick between the load or the store access (pseudo-)randomly. record_load = SPEGetRandomBoolean(); return record_load;
```

```
otherwise.
```

## J1.1.1.98 SPEOpAttr

```
// SPEOpAttr // ========= // Attributes of sampled operation filtered by SPECollectRecord(). type SPEOpAttr is ( SPEOpType op_type, SPELDSTType ldst_type, boolean branch_is_direct, boolean branch_has_link, boolean procedure_return, boolean is_conditional, boolean is_floating_point, boolean is_simd, boolean cond_pass, boolean at, boolean is_acquire_release, boolean is_predicated, bits(3) evl, boolean is_gather_scatter, boolean is_exclusive, bits(4) ets, boolean addr_valid )
```

## J1.1.1.99

```
SPEOpType
```

```
// SPEOpType // ========= // Types of operation filtered by SPECollectRecord(). enumeration SPEOpType { SPEOpType_Load, // Any memory-read operation other than atomics, compare-and-swap, // and swap SPEOpType_Store, // Any memory-write operation, including atomics without return SPEOpType_LoadAtomic, // Atomics with return, compare-and-swap and swap SPEOpType_Branch, // Software write to the PC SPEOpType_OtherSVE, // Other SVE operation SPEOpType_OtherSME, // Other SME operation SPEOpType_Other, // Any other class of operation SPEOpType_Invalid };
```

## J1.1.1.100 SPEProfilingStopped

```
// SPEProfilingStopped() // ===================== boolean SPEProfilingStopped() boolean stopped = (PMBSR_EL1.S == '1'); if IsFeatureImplemented(FEAT_SPE_EXC) then if HaveEL(EL3) && MDCR_EL3.PMSEE == '1x' then stopped = stopped || (PMBSR_EL3.S == '1'); if EffectivePMSCR_EL2_EE() == '1x' then stopped = stopped || (PMBSR_EL2.S == '1'); return stopped;
```

## J1.1.1.101 SPEResetSampleCounter

```
// SPEResetSampleCounter() // ======================= // Reset PMSICR_EL1.Counter SPEResetSampleCounter() PMSICR_EL1.COUNT<31:8> = PMSIRR_EL1.INTERVAL; if PMSIRR_EL1.RND == '1' && !IsFeatureImplemented(FEAT_SPE_ERnd) then PMSICR_EL1.COUNT<7:0> = SPEGetRandomInterval(); else PMSICR_EL1.COUNT<7:0> = Zeros(8);
```

## J1.1.1.102 SPEResetSampleStorage

```
integer SPERecordSize; // SPEResetSampleStorage() // ======================= // Reset all variables inside sample storage. SPEResetSampleStorage() // Context values SPESampleContextEL1 = Zeros(32); SPESampleContextEL1Valid = FALSE; SPESampleContextEL2 = Zeros(32); SPESampleContextEL2Valid = FALSE; // Counter values for i = 0 to (SPEMaxCounters - 1) SPESampleCounter[i] = 0; SPESampleCounterValid[i] = FALSE; SPESampleCounterPending[i] = FALSE; // Address values for i = 0 to (SPEMaxAddrs - 1) SPESampleAddressValid[i] = FALSE; SPESampleAddress[i] = Zeros(64); // Data source values SPESampleDataSource = Zeros(16); SPESampleDataSourceValid = FALSE; // Timestamp values SPESampleTimestamp = Zeros(64); SPESampleTimestampValid = FALSE; // Event values SPESampleEvents = Zeros(64); // Operation attributes SPESampleOpAttr.op_type = SPEOpType_Invalid; SPESampleOpAttr.ldst_type = SPELDSTType_Unspecified; SPESampleOpAttr.branch_is_direct = FALSE; SPESampleOpAttr.branch_has_link = FALSE; SPESampleOpAttr.procedure_return = FALSE; SPESampleOpAttr.is_conditional = FALSE; SPESampleOpAttr.is_floating_point = FALSE; SPESampleOpAttr.is_simd = FALSE; SPESampleOpAttr.cond_pass = FALSE; SPESampleOpAttr.at = FALSE; SPESampleOpAttr.is_acquire_release = FALSE; SPESampleOpAttr.is_exclusive = FALSE; SPESampleOpAttr.is_predicated = FALSE;
```

```
SPESampleOpAttr.evl = '000'; SPESampleOpAttr.is_gather_scatter = FALSE; SPESampleOpAttr.addr_valid = FALSE; array [0..SPEMaxRecordSize-1] of bits(8) SPERecordData;
```

## J1.1.1.103 SPESampleAddAddressPCVirtual

```
// SPESampleAddAddressPCVirtual() // ============================== // Save the current PC address to sample storage. SPESampleAddAddressPCVirtual() bit ns; bit nse; case CurrentSecurityState() of when SS_Secure ns = '0'; nse = '0'; when SS_NonSecure ns = '1'; nse = '0'; when SS_Realm ns = '1'; nse = '1'; otherwise Unreachable(); constant bits(2) el = PSTATE.EL; constant bits(64) pc = ThisInstrAddr(64); SPESampleAddress[SPEAddrPosPCVirtual]<55:0> = pc<55:0>; SPESampleAddress[SPEAddrPosPCVirtual]<63:56> = ns:el:nse:Zeros(4); SPESampleAddressValid[SPEAddrPosPCVirtual] = TRUE;
```

## J1.1.1.104 SPESampleAddContext

```
// SPESampleAddContext() // ===================== // Save contexts to sample storage if appropriate. SPESampleAddContext() if CollectContextIDR1() then SPESampleContextEL1 = CONTEXTIDR_EL1<31:0>; SPESampleContextEL1Valid = TRUE; if CollectContextIDR2() then SPESampleContextEL2 = CONTEXTIDR_EL2<31:0>; SPESampleContextEL2Valid = TRUE;
```

## J1.1.1.105 SPESampleAddTimeStamp

```
// SPESampleAddTimeStamp() // ======================= // Save the appropriate type of timestamp to sample storage. SPESampleAddTimeStamp() constant TimeStamp timestamp = CollectTimeStamp(); case timestamp of when TimeStamp_None SPESampleTimestampValid = FALSE; otherwise SPESampleTimestampValid = TRUE; SPESampleTimestamp = GetTimestamp(timestamp);
```

## J1.1.1.106 SPESampleCollision

```
// SPESampleCollision() // ==================== // Called when there is an SPE sample collision. SPESampleCollision() // Sample collision with the previous sample PMUEvent(PMU_EVENT_SAMPLE_COLLISION); constant bits(2) target_el = DefaultSPEEvent(); PMBSR_EL[target_el].COLL = '1';
```

## J1.1.1.107 SPESampleExtendedLoadStore

```
// SPESampleExtendedLoadStore() // ============================ // Sets the subclass of the operation type packet for // extended load/store operations. SPESampleExtendedLoadStore(boolean ar, boolean excl, boolean at, boolean is_load) SPESampleOpAttr.is_acquire_release = ar; SPESampleOpAttr.is_exclusive = excl; SPESampleOpAttr.ldst_type = SPELDSTType_Extended; SPESampleOpAttr.at = at; if is_load then if at then SPESampleOpAttr.op_type = SPEOpType_LoadAtomic; else SPESampleOpAttr.op_type = SPEOpType_Load; else SPESampleOpAttr.op_type = SPEOpType_Store;
```

## J1.1.1.108 SPESampleGCSSS2

```
// SPESampleGCSSS2() // ================= // Sets the subclass of the operation type packet for GCSSS2 load/store operations. SPESampleGCSSS2() // GCSSS2 does a read and a write. constant boolean record_load = SPEMultiAccessSample(); SPESampleOpAttr.op_type = if record_load then SPEOpType_Load else SPEOpType_Store; SPESampleOpAttr.ldst_type = SPELDSTType_GCSSS2;
```

## J1.1.1.109 SPESampleGeneralPurposeLoadStore

```
// SPESampleGeneralPurposeLoadStore() // ================================== // Sets the subclass of the operation type packet for general // purpose load/store operations. SPESampleGeneralPurposeLoadStore(boolean is_load) SPESampleOpAttr.ldst_type = SPELDSTType_General; SPESampleOpAttr.op_type = if is_load then SPEOpType_Load
```

```
else SPEOpType_Store;
```

## J1.1.1.110 SPESampleLoadStore

```
// SPESampleLoadStore() // ==================== // Called if a sample is in flight when writing or reading memory, // indicating that the operation being sampled is in the Load, Store or atomic category. SPESampleLoadStore(boolean is_load, AccessDescriptor accdesc, AddressDescriptor addrdesc) // Check if this access type is suitable to be sampled. // This implementation of SPE always samples the first access made by a suitable instruction. // FEAT_MOPS instructions are an exception, where the first load or first store access may be // selected based on the configuration of the sample filters. if accdesc.acctype IN {AccessType_SPE, AccessType_IFETCH, AccessType_TRBE, AccessType_DC, AccessType_TTW, AccessType_AT} then return; boolean sample_access = FALSE; // For FEAT_MOPS and FEAT_GCS GCSSS2 instructions which perform both loads and stores, the // filter configuration will influence which part of the access is chosen to be sampled. if (SPESampleOpAttr.ldst_type IN {SPELDSTType_MemCopy, SPELDSTType_MemSet, SPELDSTType_GCSSS2}) then // SPEMultiAccessSample() will have been called before this function, and chooses whether to // sample a load or a store. boolean sample_load; sample_load = SPESampleOpAttr.op_type IN {SPEOpType_Load, SPEOpType_LoadAtomic}; // If no valid data has been collected, and this operation is acceptable for sampling. if !SPESampleOpAttr.addr_valid && (is_load == sample_load) then sample_access = TRUE; else if !SPESampleOpAttr.addr_valid then sample_access = TRUE; if sample_access then // Data access virtual address SPESetDataVirtualAddress(addrdesc.vaddress); // Data access physical address if CollectPhysicalAddress() then SPESetDataPhysicalAddress(addrdesc, accdesc); SPESampleOpAttr.addr_valid = TRUE; if SPESampleOpAttr.op_type == SPEOpType_Invalid then // Set as unspecified load/store by default, instructions will overwrite this if it does not // apply to them. SPESampleOpAttr.op_type = if is_load then SPEOpType_Load else SPEOpType_Store; if accdesc.acctype == AccessType_NV2 then // NV2 register load/store SPESampleOpAttr.ldst_type = SPELDSTType_NV2; // Set SPELDSTType to GCS for all GCS instruction, overwriting type GCSSS2. // After selection of which operation of a GCSSS2 instruction to sample, GCSSS2 is treated the // same as other GCS instructions. if accdesc.acctype == AccessType_GCS then SPESampleOpAttr.ldst_type = SPELDSTType_GCS; // If the GCS access is from a BL or RET, this will get overwritten to SPEOpType_Branch. SPESampleOpAttr.op_type = if is_load then SPEOpType_Load else SPEOpType_Store; (SPESampleDataSourceValid, SPESampleDataSource) = SPEGetDataSource(is_load, accdesc, addrdesc);
```

## J1.1.1.111 SPESampleMemCopy

```
// SPESampleMemCopy() // ================== // Sets the subclass of the operation type packet for Memory Copy load/store // operations. SPESampleMemCopy() // MemCopy does a read and a write. constant boolean record_load = SPEMultiAccessSample(); SPESampleOpAttr.op_type = if record_load then SPEOpType_Load else SPEOpType_Store; SPESampleOpAttr.ldst_type = SPELDSTType_MemCopy;
```

## J1.1.1.112 SPESampleMemSet

```
// SPESampleMemSet() // ================= // Callback used by memory set instructions to pass data back to the SPU. SPESampleMemSet() SPESampleOpAttr.op_type = SPEOpType_Store; SPESampleOpAttr.ldst_type = SPELDSTType_MemSet;
```

## J1.1.1.113 SPESampleOnSharedResource

```
// SPESampleOnSharedResource() // =========================== // Called when the sampled instruction is executed on an SMCU or other shared resource, sets bit 25 // of the events packet to 0b1. SPESampleOnSharedResource() SPESampleEvents<25> = '1';
```

## J1.1.1.114 SPESampleOpOther

```
// SPESampleOpOther() // ================== // Add other operation to sample storage. SPESampleOpOther(boolean conditional, boolean cond_pass, boolean is_fp, boolean is_simd) SPESampleOpAttr.is_simd = is_simd; SPESampleOpOther(conditional, cond_pass, is_fp); SPESampleOpOther(boolean conditional, boolean cond_pass, boolean is_fp) SPESampleOpAttr.cond_pass = cond_pass; SPESampleOpAttr.is_floating_point = is_fp; SPESampleOpOther(conditional); SPESampleOpOther(boolean conditional) SPESampleOpAttr.is_conditional = conditional; SPESampleOpAttr.op_type = SPEOpType_Other;
```

## J1.1.1.115 SPESampleOpSMEArrayOther

```
// SPESampleOpSMEArrayOther() // ========================== // Sets the subclass of the operation type packet to Other, SME array. SPESampleOpSMEArrayOther(boolean floating_point, integer size)
```

```
// If the sampled effective vector or tile size is not a power of two, or is less than 128 bits, // the value is rounded up before it is encoded in the ets field. SPESampleOpAttr.is_floating_point = floating_point; SPESampleOpAttr.ets = SPEEncodeETS(size); SPESampleOpAttr.op_type = SPEOpType_OtherSME; SPESampleOpAttr.is_simd = TRUE;
```

## J1.1.1.116 SPESampleOpSVEOther

```
// SPESampleOpSVEOther() // ===================== // Callback used by SVE, Other operations to pass data back to the SPU. SPESampleOpSVEOther(integer vl, boolean predicated, boolean SPESampleOpAttr.is_predicated = predicated; SPESampleOpAttr.is_floating_point = floating_point; SPESampleOpAttr.evl = SPEEncodeEVL(vl); SPESampleOpAttr.op_type = SPEOpType_OtherSVE;
```

## floating\_point) J1.1.1.117 SPESampleOpSVESMELoadStore // SPESampleOpSVESMELoadStore() // ============================ // Callback used by SVE or SME loads and stores to pass data to SPE. SPESampleOpSVESMELoadStore(boolean is\_gather\_scatter, integer vl, boolean predicated, boolean is\_load) SPESampleOpAttr.is\_gather\_scatter = is\_gather\_scatter; SPESampleOpAttr.is\_predicated = predicated; SPESampleOpAttr.evl = SPEEncodeEVL(vl); assert SPESampleOpAttr.evl != '111'; SPESampleOpAttr.op\_type = if is\_load then SPEOpType\_Load else SPEOpType\_Store; SPESampleOpAttr.ldst\_type = SPELDSTType\_SVESME; J1.1.1.118 SPESampleSIMDFPLoadStore // SPESampleSIMDFPLoadStore() // ========================== // Sets the subclass of the operation type packet for SIMD &amp; FP // load store operations. SPESampleSIMDFPLoadStore(boolean is\_load, boolean scalar) SPESampleOpAttr.ldst\_type = SPELDSTType\_SIMDFP; SPESampleOpAttr.op\_type = if is\_load then SPEOpType\_Load else SPEOpType\_Store; SPESampleOpAttr.is\_simd = !scalar; // Scalar operations in SIMD&amp;FP are treated as floating point. SPESampleOpAttr.is\_floating\_point = scalar; J1.1.1.119 SPESetDataPhysicalAddress // SPESetDataPhysicalAddress() // =========================== // Called from SampleLoadStore() to save data physical packet. SPESetDataPhysicalAddress(AddressDescriptor addrdesc, AccessDescriptor accdesc) bit ns; bit nse; bit ch; bits(4) lat;

```
case addrdesc.paddress.paspace of when PAS_Secure ns = '0'; nse = '0'; when PAS_NonSecure ns = '1'; nse = '0'; when PAS_Realm ns = '1'; nse = '1'; otherwise Unreachable(); if IsFeatureImplemented(FEAT_MTE2) then if accdesc.tagchecked then ch = '1'; lat = AArch64.LogicalAddressTag(addrdesc.vaddress); else ch = '0'; // If the access is Unchecked, this is an IMPLEMENTATION_DEFINED choice // between 0b0000 and the Logical Address Tag boolean zero_unchecked; zero_unchecked = boolean IMPLEMENTATION_DEFINED "SPE PAT for tag unchecked access zero"; if !zero_unchecked then lat = AArch64.LogicalAddressTag(addrdesc.vaddress); else lat = Zeros(4); else ch = '0'; lat = '0000'; constant bits(56) paddr = addrdesc.paddress.address; SPESampleAddress[SPEAddrPosDataPhysical]<55:0> = ZeroExtend(paddr, 56); SPESampleAddress[SPEAddrPosDataPhysical]<63:56> = ns:ch:'0':nse:lat; SPESampleAddressValid[SPEAddrPosDataPhysical] = TRUE;
```

```
J1.1.1.120 SPESetDataVirtualAddress // SPESetDataVirtualAddress() // ========================== // Called from SampleLoadStore() to save data virtual packet. // Also used by exclusive load/stores to save virtual addresses if exclusive monitor is lost // before a read/write is completed. SPESetDataVirtualAddress(bits(64) vaddress) bit tbi; tbi = EffectiveTBI(vaddress, FALSE, PSTATE.EL); boolean non_tbi_is_zeros; non_tbi_is_zeros = boolean IMPLEMENTATION_DEFINED "SPE non-tbi tag is zero"; if tbi == '1' || !non_tbi_is_zeros then SPESampleAddress[SPEAddrPosDataVirtual]<63:0> = vaddress<63:0>; else SPESampleAddress[SPEAddrPosDataVirtual]<55:0> = vaddress<55:0>; SPESampleAddress[SPEAddrPosDataVirtual]<63:56> = Zeros(8); SPESampleAddressValid[SPEAddrPosDataVirtual] = TRUE; J1.1.1.121 SPEStartCounter is called.
```

```
// SPEStartCounter() // ================= // Enables incrementing of the counter at the passed index when SPECycle SPEStartCounter(integer counter_index) assert counter_index < SPEMaxCounters;
```

## J1.1.1.122 SPEStartSample

```
// SPEStartSample() // ================ // Called to start the sampling process. Returns TRUE if a new sample is to be collected, and // FALSE otherwise. boolean SPEStartSample() if !StatisticalProfilingEnabled() then return FALSE; PMUEvent(PMU_EVENT_SAMPLE_POP); if !SPEToCollectSample() then return FALSE; if SPESampleInFlight then SPESampleCollision(); return FALSE; SPESampleInFlight = TRUE; SPEStartCounter(SPECounterPosTotalLatency); SPEStartCounter(SPECounterPosIssueLatency); SPESampleAddAddressPCVirtual(); // Many operations are type other and not conditional, can save footprint // and overhead by having this as the default and not calling SPESampleOpOther // if conditional == FALSE SPESampleOpOther(FALSE); SPESampleAddContext(); // Timestamp may be collected at any point in the sampling operation. // Collecting prior to execution is one possible choice. // This choice is IMPLEMENTATION DEFINED. SPESampleAddTimeStamp(); return TRUE;
```

```
J1.1.1.123 SPEStopCounter // SPEStopCounter() // ================ // Disables incrementing of the counter at the passed index when SPECycle is called. SPEStopCounter(integer counter_index) SPESampleCounterValid[counter_index] = TRUE; SPESampleCounterPending[counter_index] = FALSE; J1.1.1.124 SPEToCollectSample // SPEToCollectSample() // ==================== // Returns TRUE if the instruction which is about the executed should be sampled, and FALSE // otherwise. boolean SPEToCollectSample() if IsZero(PMSICR_EL1.COUNT) then SPEResetSampleCounter(); else
```

```
PMSICR_EL1.COUNT = PMSICR_EL1.COUNT - 1; if IsZero(PMSICR_EL1.COUNT) then if PMSIRR_EL1.RND == '1' && IsFeatureImplemented(FEAT_SPE_ERnd) then PMSICR_EL1.ECOUNT = SPEGetRandomInterval(); return IsZero(PMSICR_EL1.ECOUNT); else return TRUE; if (PMSIRR_EL1.RND == '1' && IsFeatureImplemented(FEAT_SPE_ERnd) && !IsZero(PMSICR_EL1.ECOUNT)) then PMSICR_EL1.ECOUNT = PMSICR_EL1.ECOUNT - 1; if IsZero(PMSICR_EL1.ECOUNT) then return TRUE; return FALSE; J1.1.1.125 SPEWriteToBuffer
```

```
// SPEWriteToBuffer() // ================== // Write the active record to the Profiling Buffer. SPEWriteToBuffer() assert ProfilingBufferEnabled(); // Check alignment constant integer align = UInt(PMBIDR_EL1.Align); constant boolean aligned = IsAlignedP2(PMBPTR_EL1.PTR, align); constant boolean ttw_abort_as_fault = (boolean IMPLEMENTATION_DEFINED "Report SPE ExtAbort on TTW as fault"); SecurityState owning_ss; bits(2) owning_el; (owning_ss, owning_el) = ProfilingBufferOwner(); constant AccessDescriptor accdesc = CreateAccDescSPE(owning_ss, owning_el); constant bits(64) start_vaddr = PMBPTR_EL1; for i = 0 to SPERecordSize - 1 // If a previous write did not cause an issue if !SPEProfilingStopped() then constant bits(64) address = PMBPTR_EL1; PhysMemRetStatus memstatus; AddressDescriptor addrdesc; (memstatus, addrdesc) = DebugMemWrite(address, accdesc, aligned, SPERecordData[i]); constant FaultRecord fault = addrdesc.fault; constant boolean ttw_abort = fault.statuscode IN {Fault_SyncExternalOnWalk, Fault_SyncParityOnWalk}; if IsFault(fault.statuscode) && (!ttw_abort || ttw_abort_as_fault) then DebugWriteFault(address, fault); elsif IsFault(memstatus) || (ttw_abort && !ttw_abort_as_fault) then DebugWriteExternalAbort(memstatus, addrdesc, start_vaddr); // Move pointer if no Buffer Management Event has been caused. if !SPEProfilingStopped() then PMBPTR_EL1 = PMBPTR_EL1 + 1; return;
```

## J1.1.1.126 StatisticalProfilingEnabled

```
// StatisticalProfilingEnabled() // ============================= // Return TRUE if Statistical Profiling is Enabled in the current EL, FALSE otherwise. boolean StatisticalProfilingEnabled() return StatisticalProfilingEnabled(PSTATE.EL); // StatisticalProfilingEnabled() // ============================= // Return TRUE if Statistical Profiling is Enabled in the specified EL, FALSE otherwise. boolean StatisticalProfilingEnabled(bits(2) el) if !IsFeatureImplemented(FEAT_SPE) || UsingAArch32() || !ProfilingBufferEnabled() then return FALSE; tge_set = EL2Enabled() && HCR_EL2.TGE == '1'; (owning_ss, owning_el) = ProfilingBufferOwner(); if (UInt(owning_el) < UInt(el) || (tge_set && owning_el == EL1) || owning_ss != SecurityStateAtEL(el)) then return FALSE; bit spe_bit; case el of when EL3 Unreachable(); when EL2 spe_bit = PMSCR_EL2.E2SPE; when EL1 spe_bit = PMSCR_EL1.E1SPE; when EL0 spe_bit = (if tge_set then PMSCR_EL2.E0HSPE else PMSCR_EL1.E0SPE); return spe_bit == '1';
```

## J1.1.1.127 TimeStamp // TimeStamp // ========= enumeration TimeStamp { TimeStamp\_None, // No timestamp TimeStamp\_CoreSight, // CoreSight time (IMPLEMENTATION DEFINED) TimeStamp\_Physical, // Physical counter value with no offset TimeStamp\_OffsetPhysical, // Physical counter value minus CNTPOFF\_EL2 TimeStamp\_Virtual }; // Physical counter value minus CNTVOFF\_EL2 J1.1.1.128 AArch64.TakeExceptionInDebugState UInt(PSTATE.EL);

```
// AArch64.TakeExceptionInDebugState() // =================================== // Take an exception in Debug state to an Exception level using AArch64. AArch64.TakeExceptionInDebugState(bits(2) target_el, ExceptionRecord exception_in) assert HaveEL(target_el) && !ELUsingAArch32(target_el) && UInt(target_el) >= assert target_el != EL3 || EDSCR.SDD == '0'; ExceptionRecord except = exception_in; boolean sync_errors; if IsFeatureImplemented(FEAT_IESB) then sync_errors = SCTLR_EL[target_el].IESB == '1'; if IsFeatureImplemented(FEAT_DoubleFault) then sync_errors = sync_errors || (SCR_EL3.<EA,NMEA> == '11' && target_el == EL3); // The Effective value of SCTLR[].IESB might be zero in Debug state. if !ConstrainUnpredictableBool(Unpredictable_IESBinDebug) then sync_errors = FALSE; else sync_errors = FALSE;
```

```
if !IsFeatureImplemented(FEAT_ExS) || SCTLR_EL[target_el].EIS == '1' then // Synchronize the context, including Instruction Fetch Barrier effect SynchronizeContext(); // If coming from AArch32 state, the top parts of the X[] registers might be set to zero from_32 = UsingAArch32(); if from_32 then AArch64.MaybeZeroRegisterUppers(); if from_32 && IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' then ResetSVEState(); else MaybeZeroSVEUppers(target_el); AArch64.ReportException(except, target_el); if IsFeatureImplemented(FEAT_GCS) then PSTATE.EXLOCK = '0'; // Effective value of GCSCR_ELx.EXLOCKEN is 0 in Debug state PSTATE.EL = target_el; PSTATE.nRW = '0'; PSTATE.SP = '1'; SPSR_ELx[] = bits(64) UNKNOWN; ELR_ELx[] = bits(64) UNKNOWN; // PSTATE.{SS,D,A,I,F} are not observable and ignored in Debug state, so behave as if UNKNOWN. PSTATE.<SS,D,A,I,F> = bits(5) UNKNOWN; if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = bit UNKNOWN; if IsFeatureImplemented(FEAT_EBEP) then PSTATE.PM = bit UNKNOWN; if IsFeatureImplemented(FEAT_SEBEP) then PSTATE.PPEND = '0'; if IsFeatureImplemented(FEAT_MTE) then PSTATE.TCO = '1'; PSTATE.IL = '0'; if IsFeatureImplemented(FEAT_UAO) then PSTATE.UAO = '0'; if IsFeatureImplemented(FEAT_UINJ) then PSTATE.UINJ = '0'; if IsFeatureImplemented(FEAT_PAuth_LR) then PSTATE.PACM = '0'; if (IsFeatureImplemented(FEAT_PAN) && (PSTATE.EL == EL1 || (PSTATE.EL == EL2 && ELIsInHost(EL0))) && SCTLR_ELx[].SPAN == '0') then PSTATE.PAN = '1'; if from_32 then // Coming from AArch32 PSTATE.IT = '00000000'; PSTATE.T = '0'; // PSTATE.J is RES0 if IsFeatureImplemented(FEAT_BTI) then PSTATE.BTYPE = '00'; DLR_EL0 = bits(64) UNKNOWN; DSPSR_EL0 = bits(64) UNKNOWN; EDSCR.ERR = '1'; UpdateEDSCRFields(); // Update EDSCR PE state flags. if sync_errors then SynchronizeErrors(); EndOfInstruction();
```

## J1.1.1.129 AArch64.WatchpointByteMatch

```
// AArch64.WatchpointByteMatch() // ============================= boolean AArch64.WatchpointByteMatch(integer n, bits(64) vaddress) constant AddressSize dbgtop = DebugAddrTop(); constant integer cmpbottom = if DBGWVR_EL1[n]<2> == '1' then 2 else 3; // Word or doubleword bottom = cmpbottom; constant integer select = UInt(vaddress<cmpbottom-1:0>); byte_select_match = (DBGWCR_EL1[n].BAS<select> != '0'); mask = UInt(DBGWCR_EL1[n].MASK);
```

```
// If DBGWCR_EL1[n].MASK is a nonzero value and DBGWCR_EL1[n].BAS is not set to '11111111', or // DBGWCR_EL1[n].BAS specifies a non-contiguous set of bytes behavior is CONSTRAINED // UNPREDICTABLE. if mask > 0 && !IsOnes(DBGWCR_EL1[n].BAS) then byte_select_match = ConstrainUnpredictableBool(Unpredictable_WPMASKANDBAS); else LSB = (DBGWCR_EL1[n].BAS AND NOT(DBGWCR_EL1[n].BAS - 1)); MSB = (DBGWCR_EL1[n].BAS + LSB); if !IsZero(MSB AND (MSB - 1)) then // Not contiguous byte_select_match = ConstrainUnpredictableBool(Unpredictable_WPBASCONTIGUOUS); bottom = 3; // For the whole doubleword // If the address mask is set to a reserved value, the behavior is CONSTRAINED UNPREDICTABLE. if mask > 0 && mask <= 2 then Constraint c; (c, mask) = ConstrainUnpredictableInteger(3, 31, Unpredictable_RESWPMASK); assert c IN {Constraint_DISABLED, Constraint_NONE, Constraint_UNKNOWN}; case c of when Constraint_DISABLED return FALSE; // Disabled when Constraint_NONE mask = 0; // No masking // Otherwise the value returned by ConstrainUnpredictableInteger is a not-reserved value // When FEAT_LVA3 is not implemented, if the DBGWVR_EL1[n].RESS field bits are not a // sign extension of the MSB of DBGWVR_EL1[n].VA, it is UNPREDICTABLE whether they // appear to be included in the match. constant boolean unpredictable_ress = (dbgtop < 55 && !IsOnes(DBGWVR_EL1[n]<63:dbgtop>) && !IsZero(DBGWVR_EL1[n]<63:dbgtop>) && ConstrainUnpredictableBool(Unpredictable_DBGxVR_RESS)); constant integer cmpmsb = if unpredictable_ress then 63 else dbgtop; constant integer cmplsb = if mask > bottom then mask else bottom; constant integer bottombit = bottom; boolean WVR_match = (vaddress<cmpmsb:cmplsb> == DBGWVR_EL1[n]<cmpmsb:cmplsb>); if mask > bottom then // If masked bits of DBGWVR_EL1[n] are not zero, the behavior is CONSTRAINED UNPREDICTABLE. if WVR_match && !IsZero(DBGWVR_EL1[n]<cmplsb-1:bottombit>) then WVR_match = ConstrainUnpredictableBool(Unpredictable_WPMASKEDBITS); return (WVR_match && byte_select_match);
```

## J1.1.1.130

```
AArch64.WatchpointMatch
```

```
// AArch64.WatchpointMatch() // ========================= // Watchpoint matching in an AArch64 translation regime. WatchpointInfo AArch64.WatchpointMatch(integer n, bits(64) vaddress, integer size, AccessDescriptor accdesc) assert !ELUsingAArch32(S1TranslationRegime()); assert n < NumWatchpointsImplemented(); constant boolean enabled = IsWatchpointEnabled(n); linked = DBGWCR_EL1[n].WT == '1'; isbreakpnt = FALSE; lbnx = if IsFeatureImplemented(FEAT_Debugv8p9) then DBGWCR_EL1[n].LBNX else '00'; linked_n = UInt(lbnx : DBGWCR_EL1[n].LBN); ssce = if IsFeatureImplemented(FEAT_RME) then DBGWCR_EL1[n].SSCE else '0'; mismatch = IsFeatureImplemented(FEAT_BWE2) && DBGWCR_EL1[n].WT2 == '1'; state_match = AArch64.StateMatch(DBGWCR_EL1[n].SSC, ssce, DBGWCR_EL1[n].HMC, DBGWCR_EL1[n].PAC, linked, linked_n, isbreakpnt, PC64, accdesc); WatchpointInfo watchptinfo; boolean ls_match; case DBGWCR_EL1[n].LSC<1:0> of when '00' ls_match = FALSE; when '01' ls_match = accdesc.read;
```

```
when '10' ls_match = accdesc.write || accdesc.acctype == AccessType_DC; when '11' ls_match = TRUE; boolean value_match = FALSE; watchptinfo.vaddress = vaddress; for byte = 0 to size - 1 if (!value_match && !AddressInNaturallyAlignedBlock(watchptinfo.vaddress, vaddress + byte)) then // Watchpoint should report an address which is in // the naturally aligned block of the matched address. watchptinfo.vaddress = vaddress + byte; value_match = value_match || AArch64.WatchpointByteMatch(n, vaddress + byte); watchptinfo.watchpt_num = n; watchptinfo.value_match = value_match; if !(state_match && ls_match && enabled) then watchptinfo.wptype = WatchpointType_Inactive; watchptinfo.value_match = FALSE; elsif mismatch then watchptinfo.wptype = WatchpointType_AddrMismatch; else watchptinfo.wptype = WatchpointType_AddrMatch; return watchptinfo;
```

## J1.1.1.131 IsWatchpointEnabled

```
// IsWatchpointEnabled() // ===================== // Returns TRUE if the effective value of DBGWCR_EL1[n].E is '1', and FALSE boolean IsWatchpointEnabled(integer n) if (n > 15 && ((!HaltOnBreakpointOrWatchpoint() && !SelfHostedExtendedBPWPEnabled()) || (HaltOnBreakpointOrWatchpoint() && EDSCR2.EHBWE == '0'))) then return FALSE; return DBGWCR_EL1[n].E == '1';
```

## J1.1.2 aarch64/exceptions

This section includes the following pseudocode functions:

- AArch64.Abort
- AArch64.AbortSyndrome
- AArch64.CheckPCAlignment
- AArch64.DataAbort
- AArch64.EffectiveTCF
- AArch64.InstructionAbort
- AArch64.PCAlignmentFault
- AArch64.RaiseTagCheckFault
- AArch64.ReportTagCheckFault
- AArch64.RouteToSErrorOffset
- AArch64.SPAlignmentFault
- BranchTargetException
- TCFType
- TakeGPCException
- AArch64.TakeDelegatedSErrorException

```
otherwise.
```

- AArch64.TakePhysicalFIQException
- AArch64.TakePhysicalIRQException
- AArch64.TakePhysicalSErrorException
- AArch64.TakeVirtualFIQException
- AArch64.TakeVirtualIRQException
- AArch64.TakeVirtualSErrorException
- AArch64.BreakpointException
- AArch64.SoftwareBreakpoint
- AArch64.SoftwareStepException
- AArch64.VectorCatchException
- AArch64.WatchpointException
- AArch64.ExceptionClass
- AArch64.ReportException
- AArch64.ResetControlRegisters
- AArch64.TakeReset
- AArch64.FPTrappedException
- AArch64.CallHypervisor
- AArch64.CallSecureMonitor
- AArch64.CallSupervisor
- AArch64.TakeException
- AArch64.AArch32SystemAccessTrap
- AArch64.AArch32SystemAccessTrapSyndrome
- AArch64.AdvSIMDFPAccessTrap
- AArch64.CheckCP15InstrCoarseTraps
- AArch64.CheckFPAdvSIMDEnabled
- AArch64.CheckFPAdvSIMDTrap
- AArch64.CheckFPEnabled
- AArch64.CheckForERetTrap
- AArch64.CheckForSMCUndefOrTrap
- AArch64.CheckForSVCTrap
- AArch64.CheckForWFxTrap
- AArch64.CheckIllegalState
- AArch64.MonitorModeTrap
- AArch64.SystemAccessTrap
- AArch64.SystemAccessTrapSyndrome
- AArch64.Undefined
- AArch64.WFxTrap
- CheckLDST64BEnabled
- CheckST64BV0Enabled
- CheckST64BVEnabled
- LDST64BTrap
- WFETrapDelay
- WaitForEventUntilDelay

## J1.1.2.1 AArch64.Abort

```
// AArch64.Abort() // =============== // Abort and Debug exception handling in an AArch64 translation regime. AArch64.Abort(FaultRecord fault) if IsDebugException(fault) then if fault.accessdesc.acctype == AccessType_IFETCH then if UsingAArch32() && fault.debugmoe == DebugException_VectorCatch AArch64.VectorCatchException(fault); else AArch64.BreakpointException(fault); else AArch64.WatchpointException(fault); elsif fault.gpcf.gpf != GPCF_None && ReportAsGPCException(fault) then TakeGPCException(fault); elsif fault.statuscode == Fault_TagCheck then AArch64.RaiseTagCheckFault(fault); elsif IsExternalAbort(fault) && !IsExternalSyncAbort(fault) then PendSErrorInterrupt(fault); elsif fault.accessdesc.acctype == AccessType_IFETCH then AArch64.InstructionAbort(fault); else AArch64.DataAbort(fault);
```

## J1.1.2.2

```
then AArch64.AbortSyndrome
```

```
// AArch64.AbortSyndrome() // ======================= // Creates an exception syndrome record for Abort and Watchpoint exceptions // from an AArch64 translation regime. ExceptionRecord AArch64.AbortSyndrome(Exception exceptype, FaultRecord fault, bits(2) target_el) except = ExceptionSyndrome(exceptype); except.syndrome = AArch64.FaultSyndrome(exceptype, fault, target_el); if exceptype IN {Exception_NV2Watchpoint, Exception_Watchpoint} then except.vaddress = fault.watchptinfo.vaddress; elsif fault.statuscode == Fault_TagCheck then if IsFeatureImplemented(FEAT_MTE_TAGGED_FAR) then except.vaddress = ZeroExtend(fault.vaddress, 64); else except.vaddress = bits(4) UNKNOWN : fault.vaddress<59:0>; else except.vaddress = ZeroExtend(fault.vaddress, 64); if IPAValid(fault) then except.ipavalid = TRUE; except.NS = if fault.ipaddress.paspace == PAS_NonSecure then '1' else '0'; except.ipaddress = fault.ipaddress.address; else except.ipavalid = FALSE; if except.syndrome.iss<14> == '1' then except.pavalid = TRUE; except.paddress = fault.paddress; else except.pavalid = FALSE; except.paddress = FullAddress UNKNOWN; return except;
```

## J1.1.2.3 AArch64.CheckPCAlignment

```
// AArch64.CheckPCAlignment() // ========================== AArch64.CheckPCAlignment() constant bits(64) pc = ThisInstrAddr(64); if pc<1:0> != '00' then AArch64.PCAlignmentFault();
```

## J1.1.2.4 AArch64.DataAbort

```
// AArch64.DataAbort() // =================== AArch64.DataAbort(FaultRecord fault) bits(2) target_el; if IsExternalAbort(fault) then target_el = SyncExternalAbortTarget(fault); else route_to_el2 = (EL2Enabled() && PSTATE.EL IN {EL0, EL1} && (HCR_EL2.TGE == '1' || (IsFeatureImplemented(FEAT_RME) && fault.gpcf.gpf != GPCF_None && HCR_EL2.GPF == '1') || (IsFeatureImplemented(FEAT_NV2) && fault.accessdesc.acctype == AccessType_NV2) || IsSecondStage(fault))); if PSTATE.EL == EL3 then target_el = EL3; elsif PSTATE.EL == EL2 || route_to_el2 then target_el = EL2; else target_el = EL1; constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant boolean route_to_serr = (IsExternalAbort(fault) && AArch64.RouteToSErrorOffset(target_el)); constant integer vect_offset = if route_to_serr then 0x180 else 0x0; ExceptionRecord except; if IsFeatureImplemented(FEAT_NV2) && fault.accessdesc.acctype == AccessType_NV2 then except = AArch64.AbortSyndrome(Exception_NV2DataAbort, fault, target_el); else except = AArch64.AbortSyndrome(Exception_DataAbort, fault, target_el); AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.2.5 AArch64.EffectiveTCF

```
// AArch64.EffectiveTCF() // ====================== // Indicate if a Tag Check Fault should cause a synchronous exception, // be asynchronously accumulated, or have no effect on the PE. TCFType AArch64.EffectiveTCF(bits(2) el, boolean read) bits(2) tcf; constant Regime regime = TranslationRegime(el); case regime of when Regime_EL3 tcf = SCTLR_EL3.TCF; when Regime_EL2 tcf = SCTLR_EL2.TCF;
```

```
when Regime_EL20 tcf = if el == EL0 then SCTLR_EL2.TCF0 else SCTLR_EL2.TCF; when Regime_EL10 tcf = if el == EL0 then SCTLR_EL1.TCF0 else SCTLR_EL1.TCF; otherwise Unreachable(); if tcf == '11' then // Reserved value if !IsFeatureImplemented(FEAT_MTE_ASYM_FAULT) then (-,tcf) = ConstrainUnpredictableBits(Unpredictable_RESTCF, 2); case tcf of when '00' // Tag Check Faults have no effect on the PE return TCFType_Ignore; when '01' // Tag Check Faults cause a synchronous exception return TCFType_Sync; when '10' if IsFeatureImplemented(FEAT_MTE_ASYNC) then // If asynchronous faults are implemented, // Tag Check Faults are asynchronously accumulated return TCFType_Async; else // Otherwise, Tag Check Faults have no effect on the PE return TCFType_Ignore; when '11' if IsFeatureImplemented(FEAT_MTE_ASYM_FAULT) then // Tag Check Faults cause a synchronous exception on reads or on // a read/write access, and are asynchronously accumulated on writes if read then return TCFType_Sync; else return TCFType_Async; else // Otherwise, Tag Check Faults have no effect on the PE return TCFType_Ignore; otherwise Unreachable();
```

## J1.1.2.6 AArch64.InstructionAbort

```
// AArch64.InstructionAbort() // ========================== AArch64.InstructionAbort(FaultRecord fault) // External aborts on instruction fetch must be taken synchronously if IsFeatureImplemented(FEAT_DoubleFault) then assert fault.statuscode != Fault_AsyncExternal; bits(2) target_el; if IsExternalAbort(fault) then target_el = SyncExternalAbortTarget(fault); else route_to_el2 = (EL2Enabled() && PSTATE.EL IN {EL0, EL1} && (HCR_EL2.TGE == '1' || (IsFeatureImplemented(FEAT_RME) && fault.gpcf.gpf != GPCF_None && HCR_EL2.GPF == '1') || IsSecondStage(fault))); if PSTATE.EL == EL3 then target_el = EL3; elsif PSTATE.EL == EL2 || route_to_el2 then target_el = EL2; else target_el = EL1; constant bits(64) preferred_exception_return = ThisInstrAddr(64); integer vect_offset;
```

```
if IsExternalAbort(fault) && AArch64.RouteToSErrorOffset(target_el) then vect_offset = 0x180; else vect_offset = 0x0; constant ExceptionRecord except = AArch64.AbortSyndrome(Exception_InstructionAbort, fault, target_el); AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.2.7 AArch64.PCAlignmentFault

```
// AArch64.PCAlignmentFault() // ========================== // Called on unaligned program counter in AArch64 state. AArch64.PCAlignmentFault() constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; except = ExceptionSyndrome(Exception_PCAlignment); except.vaddress = ThisInstrAddr(64); bits(2) target_el = EL1; if UInt(PSTATE.EL) > UInt(EL1) then target_el = PSTATE.EL; elsif EL2Enabled() && HCR_EL2.TGE == '1' then target_el = EL2; AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.2.8 AArch64.RaiseTagCheckFault

```
// AArch64.RaiseTagCheckFault() // ============================ // Raise a Tag Check Fault exception. AArch64.RaiseTagCheckFault(FaultRecord fault) constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = 0x0; bits(2) target_el = EL1; if UInt(PSTATE.EL) > UInt(EL1) then target_el = PSTATE.EL; elsif PSTATE.EL == EL0 && EL2Enabled() && HCR_EL2.TGE == '1' then target_el = EL2; except = AArch64.AbortSyndrome(Exception_DataAbort, fault, target_el); AArch64.TakeException(target_el, except, preferred_exception_return,
```

## J1.1.2.9 AArch64.ReportTagCheckFault

```
// AArch64.ReportTagCheckFault() // ============================= // Records a Tag Check Fault exception into the appropriate TFSR_ELx. AArch64.ReportTagCheckFault(bits(2) el, bit ttbr) case el of when EL3 assert ttbr == '0'; TFSR_EL3.TF0 = '1'; when EL2 if ttbr == '0' then TFSR_EL2.TF0 = '1'; else TFSR_EL2.TF1 = '1'; when EL1 if ttbr == '0' then TFSR_EL1.TF0 = '1'; else TFSR_EL1.TF1 = '1'; when EL0 if ttbr == '0' then TFSRE0_EL1.TF0 = '1'; else TFSRE0_EL1.TF1 = '1';
```

```
vect_offset);
```

## J1.1.2.10 AArch64.RouteToSErrorOffset

```
// AArch64.RouteToSErrorOffset() // ============================= // Returns TRUE if synchronous External abort exceptions are taken to the // appropriate SError vector offset, and FALSE otherwise. boolean AArch64.RouteToSErrorOffset(bits(2) target_el) if !IsFeatureImplemented(FEAT_DoubleFault) then return FALSE; bit ease_bit; case target_el of when EL3 ease_bit = SCR_EL3.EASE; when EL2 if IsFeatureImplemented(FEAT_DoubleFault2) && IsSCTLR2EL2Enabled() then ease_bit = SCTLR2_EL2.EASE; else ease_bit = '0'; when EL1 if IsFeatureImplemented(FEAT_DoubleFault2) && IsSCTLR2EL1Enabled() then ease_bit = SCTLR2_EL1.EASE; else ease_bit = '0'; return (ease_bit == '1');
```

## J1.1.2.11 AArch64.SPAlignmentFault

```
// AArch64.SPAlignmentFault() // ========================== // Called on an unaligned stack pointer in AArch64 state. AArch64.SPAlignmentFault() constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; except = ExceptionSyndrome(Exception_SPAlignment); bits(2) target_el = EL1; if UInt(PSTATE.EL) > UInt(EL1) then target_el = PSTATE.EL; elsif EL2Enabled() && HCR_EL2.TGE == '1' then target_el = EL2; AArch64.TakeException(target_el, except, preferred_exception_return,
```

## J1.1.2.12

```
// BranchTargetException() // ======================= // Raise branch target exception. AArch64.BranchTargetException(bits(52) vaddress) constant bits(64) preferred_exception_return = vect_offset = 0x0; except = ExceptionSyndrome(Exception_BranchTarget); except.syndrome.iss<1:0> = PSTATE.BTYPE; except.syndrome.iss<24:2> = Zeros(23); // RES0 bits(2) target_el = EL1; if UInt(PSTATE.EL) > UInt(EL1) then target_el = PSTATE.EL;
```

```
vect_offset); BranchTargetException ThisInstrAddr(64);
```

```
elsif PSTATE.EL == EL0 && EL2Enabled() && HCR_EL2.TGE == '1' then target_el = EL2; AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.2.13 TCFType

```
// TCFType // ======= enumeration TCFType { TCFType_Sync, TCFType_Async, TCFType_Ignore
```

## J1.1.2.14 TakeGPCException

```
// TakeGPCException() // ================== // Report Granule Protection Exception faults TakeGPCException(FaultRecord fault) assert IsFeatureImplemented(FEAT_RME); assert IsFeatureImplemented(FEAT_LSE); assert IsFeatureImplemented(FEAT_HAFDBS); assert IsFeatureImplemented(FEAT_DoubleFault); ExceptionRecord except; except.exceptype = Exception_GPC; except.vaddress = ZeroExtend(fault.vaddress, 64); except.paddress = fault.paddress; except.pavalid = TRUE; if IPAValid(fault) then except.ipavalid = TRUE; except.NS = if fault.ipaddress.paspace == PAS_NonSecure then '1' else '0'; except.ipaddress = fault.ipaddress.address; else except.ipavalid = FALSE; except.syndrome.iss2<11> = if fault.hdbssf then '1' else '0'; // HDBSSF if fault.accessdesc.acctype == AccessType_GCS then except.syndrome.iss2<8> = '1'; //GCS // Populate the fields grouped in ISS except.syndrome.iss<24:22> = Zeros(3); // RES0 except.syndrome.iss<21> = if fault.gpcfs2walk then '1' else '0'; // S2PTW if fault.accessdesc.acctype == AccessType_IFETCH then except.syndrome.iss<20> = '1'; // InD else except.syndrome.iss<20> = '0'; // InD except.syndrome.iss<19:14> = EncodeGPCSC(fault.gpcf); // GPCSC if IsFeatureImplemented(FEAT_NV2) && fault.accessdesc.acctype == AccessType_NV2 then except.syndrome.iss<13> = '1'; // VNCR else except.syndrome.iss<13> = '0'; // VNCR except.syndrome.iss<12:11> = '00'; // RES0 except.syndrome.iss<10:9> = '00'; // RES0 if fault.accessdesc.acctype IN {AccessType_DC, AccessType_IC, AccessType_AT} then except.syndrome.iss<8> = '1'; // CM else except.syndrome.iss<8> = '0'; // CM except.syndrome.iss<7> = if fault.s2fs1walk then '1' else '0'; // S1PTW
```

```
};
```

```
if fault.accessdesc.acctype IN {AccessType_DC, AccessType_IC, AccessType_AT} then except.syndrome.iss<6> = '1'; // WnR elsif fault.statuscode IN {Fault_HWUpdateAccessFlag, Fault_Exclusive} then except.syndrome.iss<6> = bit UNKNOWN; // WnR elsif fault.accessdesc.atomicop && IsExternalAbort(fault) then except.syndrome.iss<6> = bit UNKNOWN; // WnR else except.syndrome.iss<6> = if fault.write then '1' else '0'; // WnR except.syndrome.iss<5:0> = EncodeLDFSC(fault.statuscode, fault.level); // xFSC constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant bits(2) target_el = EL3; integer vect_offset; if IsExternalAbort(fault) && AArch64.RouteToSErrorOffset(target_el) then vect_offset = 0x180; else vect_offset = 0x0; AArch64.TakeException(target_el, except, preferred_exception_return,
```

## vect\_offset); J1.1.2.15 AArch64.TakeDelegatedSErrorException // AArch64.TakeDelegatedSErrorException() // ====================================== AArch64.TakeDelegatedSErrorException() assert IsFeatureImplemented(FEAT\_E3DSE) &amp;&amp; PSTATE.EL != EL3 &amp;&amp; SCR\_EL3.&lt;EnDSE,DSE&gt; == '11'; constant bits(64) preferred\_exception\_return = ThisInstrAddr(64); vect\_offset = 0x180; except = ExceptionSyndrome(Exception\_SError); bits(2) target\_el; boolean dsei\_masked; (dsei\_masked, target\_el) = AArch64.DelegatedSErrorTarget(); assert !dsei\_masked; except.syndrome.iss&lt;24&gt; = VSESR\_EL3.IDS; except.syndrome.iss&lt;23:0&gt; = VSESR\_EL3.ISS; ClearPendingDelegatedSError(); AArch64.TakeException(target\_el, except, preferred\_exception\_return, vect\_offset); J1.1.2.16 AArch64.TakePhysicalFIQException // AArch64.TakePhysicalFIQException() // ================================== AArch64.TakePhysicalFIQException() route\_to\_el3 = HaveEL(EL3) &amp;&amp; SCR\_EL3.FIQ == '1'; route\_to\_el2 = (PSTATE.EL IN {EL0, EL1} &amp;&amp; EL2Enabled() &amp;&amp; (HCR\_EL2.TGE == '1' || HCR\_EL2.FMO == '1')); constant bits(64) preferred\_exception\_return = ThisInstrAddr(64); vect\_offset = 0x100; except = ExceptionSyndrome(Exception\_FIQ); if route\_to\_el3 then AArch64.TakeException(EL3, except, preferred\_exception\_return, vect\_offset); elsif PSTATE.EL == EL2 || route\_to\_el2 then assert PSTATE.EL != EL3; AArch64.TakeException(EL2, except, preferred\_exception\_return, vect\_offset);

```
else assert PSTATE.EL IN {EL0, EL1}; AArch64.TakeException(EL1, except, preferred_exception_return, vect_offset);
```

## J1.1.2.17 AArch64.TakePhysicalIRQException

```
// AArch64.TakePhysicalIRQException() // ================================== // Take an enabled physical IRQ exception. AArch64.TakePhysicalIRQException() route_to_el3 = HaveEL(EL3) && SCR_EL3.IRQ == '1'; route_to_el2 = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && (HCR_EL2.TGE == '1' || HCR_EL2.IMO == '1')); constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x80; except = ExceptionSyndrome(Exception_IRQ); if route_to_el3 then elsif PSTATE.EL == EL2 || route_to_el2 then assert PSTATE.EL != EL3; else assert PSTATE.EL IN {EL0, EL1};
```

```
AArch64.TakeException(EL3, except, preferred_exception_return, vect_offset); AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); AArch64.TakeException(EL1, except, preferred_exception_return, vect_offset);
```

## J1.1.2.18 AArch64.TakePhysicalSErrorException

```
// AArch64.TakePhysicalSErrorException() // ===================================== AArch64.TakePhysicalSErrorException(boolean implicit_esb) boolean masked; bits(2) target_el; (masked, target_el) = PhysicalSErrorTarget(); assert !masked; constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = 0x180; constant FaultRecord fault = GetPendingPhysicalSError(); except = ExceptionSyndrome(Exception_SError); constant boolean is_esb = FALSE; constant bits(25) syndrome = if IsSErrorEdgeTriggered() then ClearPendingPhysicalSError(); if except.syndrome.iss<14> == '1' then except.pavalid = TRUE; except.paddress = fault.paddress; else except.pavalid = FALSE; except.paddress = FullAddress UNKNOWN; except.syndrome.iss = syndrome; AArch64.TakeException(target_el, except, preferred_exception_return,
```

```
AArch64.PhysicalSErrorSyndrome(is_esb, implicit_esb); vect_offset);
```

## J1.1.2.19 AArch64.TakeVirtualFIQException

```
// AArch64.TakeVirtualFIQException() // ================================= AArch64.TakeVirtualFIQException() assert PSTATE.EL IN {EL0, EL1} && EL2Enabled(); assert HCR_EL2.TGE == '0' && HCR_EL2.FMO == '1'; // Virtual IRQ enabled if TGE==0 and FMO==1 constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x100; except = ExceptionSyndrome(Exception_FIQ); AArch64.TakeException(EL1, except, preferred_exception_return, vect_offset);
```

```
// AArch64.TakeVirtualIRQException() // ================================= AArch64.TakeVirtualIRQException() assert PSTATE.EL IN {EL0, EL1} && EL2Enabled(); assert HCR_EL2.TGE == '0' && HCR_EL2.IMO == '1'; // Virtual IRQ enabled if TGE==0 and IMO==1 constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x80; except = ExceptionSyndrome(Exception_IRQ); AArch64.TakeException(EL1, except, preferred_exception_return, vect_offset);
```

## J1.1.2.20 AArch64.TakeVirtualIRQException J1.1.2.21 AArch64.TakeVirtualSErrorException

```
// AArch64.TakeVirtualSErrorException() // ==================================== AArch64.TakeVirtualSErrorException() assert PSTATE.EL IN {EL0, EL1} && EL2Enabled(); // Virtual SError enabled if TGE==0 and AMO==1 or TMEA==1 assert HCR_EL2.TGE == '0' && (HCR_EL2.AMO == '1' || (IsHCRXEL2Enabled() && HCRX_EL2.TMEA == '1')); constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x180; except = ExceptionSyndrome(Exception_SError); if IsFeatureImplemented(FEAT_RAS) then except.syndrome.iss<24> = VSESR_EL2.IDS; except.syndrome.iss<23:0> = VSESR_EL2.ISS; else constant bits(25) syndrome = bits(25) IMPLEMENTATION_DEFINED "Virtual SError syndrome"; impdef_syndrome = syndrome<24> == '1'; if impdef_syndrome then except.syndrome.iss = syndrome; ClearPendingVirtualSError(); AArch64.TakeException(EL1, except, preferred_exception_return, vect_offset);
```

## J1.1.2.22 AArch64.BreakpointException

```
// AArch64.BreakpointException() // ============================= AArch64.BreakpointException(FaultRecord fault) assert PSTATE.EL != EL3; route_to_el2 = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && (HCR_EL2.TGE == '1' || MDCR_EL2.TDE == '1')); constant bits(64) preferred_exception_return = ThisInstrAddr(64); bits(2) target_el; vect_offset = 0x0; target_el = if (PSTATE.EL == EL2 || route_to_el2) then EL2 else EL1; vaddress = bits(64) UNKNOWN; except = AArch64.AbortSyndrome(Exception_Breakpoint, fault, target_el); AArch64.TakeException(target_el, except, preferred_exception_return,
```

## vect\_offset); J1.1.2.23 AArch64.SoftwareBreakpoint // AArch64.SoftwareBreakpoint() // ============================ AArch64.SoftwareBreakpoint(bits(16) immediate) route\_to\_el2 = (PSTATE.EL IN {EL0, EL1} &amp;&amp; EL2Enabled() &amp;&amp; (HCR\_EL2.TGE == '1' || MDCR\_EL2.TDE == '1')); constant bits(64) preferred\_exception\_return = ThisInstrAddr(64); vect\_offset = 0x0; except = ExceptionSyndrome(Exception\_SoftwareBreakpoint); except.syndrome.iss&lt;15:0&gt; = immediate; if UInt(PSTATE.EL) &gt; UInt(EL1) then AArch64.TakeException(PSTATE.EL, except, preferred\_exception\_return, vect\_offset); elsif route\_to\_el2 then AArch64.TakeException(EL2, except, preferred\_exception\_return, vect\_offset); else AArch64.TakeException(EL1, except, preferred\_exception\_return, vect\_offset); J1.1.2.24 AArch64.SoftwareStepException

```
// AArch64.SoftwareStepException() // =============================== AArch64.SoftwareStepException() assert PSTATE.EL != EL3; route_to_el2 = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && (HCR_EL2.TGE == '1' || MDCR_EL2.TDE == '1')); constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; except = ExceptionSyndrome(Exception_SoftwareStep); if SoftwareStep_DidNotStep() then except.syndrome.iss<24> = '0'; else except.syndrome.iss<24> = '1'; except.syndrome.iss<6> = if SoftwareStep_SteppedEX() then '1' else
```

```
'0';
```

```
except.syndrome.iss<5:0> = '100010'; // IFSC = Debug Exception if PSTATE.EL == EL2 || route_to_el2 then AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); else AArch64.TakeException(EL1, except, preferred_exception_return, vect_offset);
```

## J1.1.2.25 AArch64.VectorCatchException

```
// AArch64.VectorCatchException() // ============================== // Vector Catch taken from EL0 or EL1 to EL2. This can only be called when debug exceptions are // being routed to EL2, as Vector Catch is a legacy debug event. AArch64.VectorCatchException(FaultRecord fault) assert PSTATE.EL != EL2; assert EL2Enabled() && (HCR_EL2.TGE == '1' || MDCR_EL2.TDE == '1'); constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; vaddress = bits(64) UNKNOWN; except = AArch64.AbortSyndrome(Exception_VectorCatch, fault, EL2); AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset);
```

## J1.1.2.26 AArch64.WatchpointException

```
// AArch64.WatchpointException() // ============================= AArch64.WatchpointException(FaultRecord fault) assert PSTATE.EL != EL3; route_to_el2 = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && (HCR_EL2.TGE == '1' || MDCR_EL2.TDE == '1')); constant bits(64) preferred_exception_return = ThisInstrAddr(64); bits(2) target_el; vect_offset = 0x0; target_el = if (PSTATE.EL == EL2 || route_to_el2) then EL2 else EL1; ExceptionRecord except; if IsFeatureImplemented(FEAT_NV2) && fault.accessdesc.acctype == AccessType_NV2 except = AArch64.AbortSyndrome(Exception_NV2Watchpoint, fault, target_el); else except = AArch64.AbortSyndrome(Exception_Watchpoint, fault, target_el); AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.2.27 AArch64.ExceptionClass

```
// AArch64.ExceptionClass() // ======================== // Returns the Exception Class and Instruction Length fields to be reported in ESR (integer,bit) AArch64.ExceptionClass(Exception exceptype, bits(2) target_el) il_is_valid = TRUE; from_32 = UsingAArch32(); integer ec; case exceptype of
```

```
then
```

```
when Exception_Uncategorized ec = 0x00; il_is_valid = FALSE; when Exception_WFxTrap ec = 0x01; when Exception_CP15RTTrap ec = 0x03; assert from_32; when Exception_CP15RRTTrap ec = 0x04; assert from_32; when Exception_CP14RTTrap ec = 0x05; assert from_32; when Exception_CP14DTTrap ec = 0x06; assert from_32; when Exception_AdvSIMDFPAccessTrap ec = 0x07; when Exception_FPIDTrap ec = 0x08; when Exception_PACTrap ec = 0x09; when Exception_LDST64BTrap ec = 0x0A; when Exception_GPC ec = 0x1E; when Exception_CP14RRTTrap ec = 0x0C; assert from_32; when Exception_BranchTarget ec = 0x0D; when Exception_IllegalState ec = 0x0E; il_is_valid = FALSE; when Exception_SupervisorCall ec = if from_32 then 0x11 else 0x15; when Exception_HypervisorCall ec = if from_32 then 0x12 else 0x16; when Exception_MonitorCall ec = if from_32 then 0x13 else 0x17; when Exception_SystemRegisterTrap ec = 0x18; assert !from_32; when Exception_SystemRegister128Trap ec = 0x14; assert !from_32; when Exception_SVEAccessTrap ec = 0x19; assert !from_32; when Exception_ERetTrap ec = 0x1A; assert !from_32; when Exception_PACFail ec = 0x1C; assert !from_32; when Exception_SMEAccessTrap ec = 0x1D; assert !from_32; when Exception_InstructionAbort ec = if target_el == PSTATE.EL then 0x21 else 0x20; il_is_valid = FALSE; when Exception_PCAlignment ec = 0x22; il_is_valid = FALSE; when Exception_DataAbort ec = if target_el == PSTATE.EL then 0x25 else 0x24; when Exception_NV2DataAbort ec = 0x25; when Exception_SPAlignment ec = 0x26; il_is_valid = FALSE; assert !from_32; when Exception_MemCpyMemSet ec = 0x27; when Exception_GCSFail ec = 0x2D; assert !from_32; when Exception_FPTrappedException ec = if from_32 then 0x28 else 0x2C; when Exception_SError ec = 0x2F; il_is_valid = FALSE; when Exception_Breakpoint ec = if target_el == PSTATE.EL then 0x31 else 0x30; il_is_valid = FALSE; when Exception_SoftwareStep ec = if target_el == PSTATE.EL then 0x33 else 0x32; il_is_valid = FALSE; when Exception_Watchpoint ec = if target_el == PSTATE.EL then 0x35 else 0x34; il_is_valid = FALSE; when Exception_NV2Watchpoint ec = 0x35; il_is_valid = FALSE; when Exception_SoftwareBreakpoint ec = if from_32 then 0x38 else 0x3C; when Exception_VectorCatch ec = 0x3A; il_is_valid = FALSE; assert from_32; when Exception_Profiling ec = 0x3D; otherwise Unreachable(); bit il; if il_is_valid then il = if ThisInstrLength() == 32 then '1' else '0'; else il = '1'; assert from_32 || il == '1'; // AArch64 instructions always 32-bit return (ec,il);
```

## J1.1.2.28 AArch64.ReportException

```
// AArch64.ReportException() // ========================= // Report syndrome information for exception taken to AArch64 state. AArch64.ReportException(ExceptionRecord except, bits(2) target_el)
```

```
constant Exception exceptype = except.exceptype; (ec,il) = AArch64.ExceptionClass(exceptype, target_el); iss = except.syndrome.iss; iss2 = except.syndrome.iss2; // IL is not valid for Data Abort exceptions without valid instruction syndrome information if ec IN {0x24,0x25} && iss<24> == '0' then il = '1'; ESR_EL[target_el] = (Zeros(8) : // <63:56> iss2 : // <55:32> ec<5:0> : // <31:26> il : // <25> iss); // <24:0> if exceptype IN { Exception_InstructionAbort, Exception_PCAlignment, Exception_DataAbort, Exception_NV2DataAbort, Exception_NV2Watchpoint, Exception_GPC, Exception_Watchpoint } then FAR_EL[target_el] = except.vaddress; else FAR_EL[target_el] = bits(64) UNKNOWN; if except.ipavalid then HPFAR_EL2<47:4> = except.ipaddress<55:12>; if IsSecureEL2Enabled() && CurrentSecurityState() == SS_Secure then HPFAR_EL2.NS = except.NS; else HPFAR_EL2.NS = '0'; elsif target_el == EL2 then HPFAR_EL2<47:4> = bits(44) UNKNOWN; if except.pavalid then bits(64) faultaddr = ZeroExtend(except.paddress.address, 64); if IsFeatureImplemented(FEAT_RME) then case except.paddress.paspace of when PAS_Secure faultaddr<63:62> = '00'; when PAS_NonSecure faultaddr<63:62> = '10'; when PAS_Root faultaddr<63:62> = '01'; when PAS_Realm faultaddr<63:62> = '11'; if exceptype == Exception_GPC then faultaddr<11:0> = Zeros(12); else faultaddr<63> = if except.paddress.paspace == PAS_NonSecure then '1' else '0'; PFAR_EL[target_el] = faultaddr; elsif (IsFeatureImplemented(FEAT_PFAR) || (IsFeatureImplemented(FEAT_RME) && target_el == EL3)) then PFAR_EL[target_el] = bits(64) UNKNOWN; return;
```

## J1.1.2.29 AArch64.ResetControlRegisters

```
// AArch64.ResetControlRegisters() // =============================== // Resets System registers and memory-mapped control registers that have architecturally-defined // reset values to those values. AArch64.ResetControlRegisters(boolean cold_reset);
```

## J1.1.2.30 AArch64.TakeReset

```
// AArch64.TakeReset() // =================== // Reset into AArch64 state AArch64.TakeReset(boolean cold_reset) assert HaveAArch64(); // Enter the highest implemented Exception level in AArch64 state PSTATE.nRW = '0'; if HaveEL(EL3) then PSTATE.EL = EL3; elsif HaveEL(EL2) then PSTATE.EL = EL2; else PSTATE.EL = EL1; // Reset System registers and other system components AArch64.ResetControlRegisters(cold_reset); // Reset all other PSTATE fields PSTATE.SP = '1'; // Select stack pointer PSTATE.<D,A,I,F> = '1111'; // All asynchronous exceptions masked PSTATE.SS = '0'; // Clear software step bit PSTATE.DIT = '0'; // PSTATE.DIT is reset to 0 when resetting into AArch64 if IsFeatureImplemented(FEAT_PAuth_LR) then PSTATE.PACM = '0'; // PAC modifier if IsFeatureImplemented(FEAT_SME) then PSTATE.<SM,ZA> = '00'; // Disable Streaming SVE mode & ZA storage ResetSMEState('0'); if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = bit IMPLEMENTATION_DEFINED "PSTATE.SSBS bit at reset"; if IsFeatureImplemented(FEAT_GCS) then PSTATE.EXLOCK = '0'; // PSTATE.EXLOCK is reset to 0 when resetting into AArch64 if IsFeatureImplemented(FEAT_UINJ) then PSTATE.UINJ = '0'; // PSTATE.UINJ is reset to 0 when resetting into AArch64 PSTATE.IL = '0'; // Clear Illegal Execution state bit // All registers, bits and fields not reset by the above pseudocode or by the BranchTo() call // below are UNKNOWN bitstrings after reset. In particular, the return information registers // ELR_ELx and SPSR_ELx have UNKNOWN values, so that it // is impossible to return from a reset in an architecturally defined way. AArch64.ResetGeneralRegisters(); if IsFeatureImplemented(FEAT_SME) || IsFeatureImplemented(FEAT_SVE) then ResetSVERegisters(); else AArch64.ResetSIMDFPRegisters(); AArch64.ResetSpecialRegisters(); ResetExternalDebugRegisters(cold_reset); bits(64) rv; // IMPLEMENTATION DEFINED reset vector if HaveEL(EL3) then rv = RVBAR_EL3; elsif HaveEL(EL2) then rv = RVBAR_EL2; else rv = RVBAR_EL1; // The reset vector must be correctly aligned constant AddressSize pamax = AArch64.PAMax(); assert IsZero(rv<63:pamax>) && IsZero(rv<1:0>);
```

```
constant boolean branch_conditional = FALSE; EDPRSR.R = '0'; // Leaving Reset State. BranchTo(rv, BranchType_RESET, branch_conditional);
```

## J1.1.2.31 AArch64.FPTrappedException

```
// AArch64.FPTrappedException() // ============================ AArch64.FPTrappedException(boolean is_ase, bits(8) accumulated_exceptions) except = ExceptionSyndrome(Exception_FPTrappedException); if is_ase then if boolean IMPLEMENTATION_DEFINED "vector instructions set TFV to 1" then except.syndrome.iss<23> = '1'; // TFV else except.syndrome.iss<23> = '0'; // TFV else except.syndrome.iss<23> = '1'; // TFV except.syndrome.iss<10:8> = bits(3) UNKNOWN; // VECITR if except.syndrome.iss<23> == '1' then except.syndrome.iss<7,4:0> = accumulated_exceptions<7,4:0>; // IDF,IXF,UFF,OFF,DZF,IOF else except.syndrome.iss<7,4:0> = bits(6) UNKNOWN; route_to_el2 = EL2Enabled() && HCR_EL2.TGE == '1'; constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; if UInt(PSTATE.EL) > UInt(EL1) then AArch64.TakeException(PSTATE.EL, except, preferred_exception_return, vect_offset); elsif route_to_el2 then AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); else AArch64.TakeException(EL1, except, preferred_exception_return, vect_offset);
```

## J1.1.2.32 AArch64.CallHypervisor

```
// AArch64.CallHypervisor() // ======================== // Performs a HVC call AArch64.CallHypervisor(bits(16) immediate) assert HaveEL(EL2); if UsingAArch32() then AArch32.ITAdvance(); SSAdvance(); constant bits(64) preferred_exception_return = NextInstrAddr(64); vect_offset = 0x0; except = ExceptionSyndrome(Exception_HypervisorCall); except.syndrome.iss<15:0> = immediate; if IsFeatureImplemented(FEAT_PAuth_LR) then PSTATE.PACM = '0'; if PSTATE.EL == EL3 then else
```

```
AArch64.TakeException(EL3, except, preferred_exception_return, vect_offset); AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset);
```

## J1.1.2.33 AArch64.CallSecureMonitor

```
// AArch64.CallSecureMonitor() // =========================== AArch64.CallSecureMonitor(bits(16) immediate) assert HaveEL(EL3) && !ELUsingAArch32(EL3); if UsingAArch32() then AArch32.ITAdvance(); HSAdvance(); SSAdvance(); constant bits(64) preferred_exception_return = NextInstrAddr(64); vect_offset = 0x0; except = ExceptionSyndrome(Exception_MonitorCall); except.syndrome.iss<15:0> = immediate; if IsFeatureImplemented(FEAT_PAuth_LR) then PSTATE.PACM = '0'; AArch64.TakeException(EL3, except, preferred_exception_return,
```

```
// AArch64.TakeException() // ======================= // Take an exception to an Exception level using AArch64. AArch64.TakeException(bits(2) target_el, ExceptionRecord exception_in, bits(64) preferred_exception_return, integer vect_offset_in) assert HaveEL(target_el) && !ELUsingAArch32(target_el) && UInt(target_el) >= if Halted() then AArch64.TakeExceptionInDebugState(target_el, exception_in); return; ExceptionRecord except = exception_in; boolean sync_errors; boolean iesb_req; if IsFeatureImplemented(FEAT_IESB) then sync_errors = SCTLR_EL[target_el].IESB == '1'; if IsFeatureImplemented(FEAT_DoubleFault) then sync_errors = sync_errors || (SCR_EL3.<EA,NMEA> == '11' && target_el == EL3); if sync_errors && InsertIESBBeforeException(target_el) then SynchronizeErrors();
```

## vect\_offset); J1.1.2.34 AArch64.CallSupervisor // AArch64.CallSupervisor() // ======================== // Calls the Supervisor AArch64.CallSupervisor(bits(16) immediate) if UsingAArch32() then AArch32.ITAdvance(); SSAdvance(); route\_to\_el2 = PSTATE.EL == EL0 &amp;&amp; EL2Enabled() &amp;&amp; HCR\_EL2.TGE == '1'; constant bits(64) preferred\_exception\_return = NextInstrAddr(64); vect\_offset = 0x0; except = ExceptionSyndrome(Exception\_SupervisorCall); except.syndrome.iss&lt;15:0&gt; = immediate; if IsFeatureImplemented(FEAT\_PAuth\_LR) then PSTATE.PACM = '0'; if UInt(PSTATE.EL) &gt; UInt(EL1) then AArch64.TakeException(PSTATE.EL, except, preferred\_exception\_return, vect\_offset); elsif route\_to\_el2 then AArch64.TakeException(EL2, except, preferred\_exception\_return, vect\_offset); else AArch64.TakeException(EL1, except, preferred\_exception\_return, vect\_offset); J1.1.2.35 AArch64.TakeException UInt(PSTATE.EL);

```
if except.exceptype != Exception_SError then iesb_req = FALSE; sync_errors = FALSE; TakeUnmaskedPhysicalSErrorInterrupts(iesb_req); else sync_errors = FALSE; boolean brbe_source_allowed = FALSE; bits(64) brbe_source_address = Zeros(64); if IsFeatureImplemented(FEAT_BRBE) then brbe_source_allowed = BranchRecordAllowed(PSTATE.EL); brbe_source_address = preferred_exception_return; if !IsFeatureImplemented(FEAT_ExS) || SCTLR_EL[target_el].EIS == '1' then // Synchronize the context, including Instruction Fetch Barrier effect SynchronizeContext(); elsif !(except.exceptype == Exception_SoftwareBreakpoint || (except.exceptype IN {Exception_SupervisorCall, Exception_HypervisorCall, Exception_MonitorCall} && !except.trappedsyscallinst)) then InstructionFetchBarrier(); // If coming from AArch32 state, the top parts of the X[] registers might be set to zero from_32 = UsingAArch32(); if from_32 then AArch64.MaybeZeroRegisterUppers(); if from_32 && IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' then ResetSVEState(); else MaybeZeroSVEUppers(target_el); integer vect_offset = vect_offset_in; if UInt(target_el) > UInt(PSTATE.EL) then boolean lower_32; if target_el == EL3 then if EL2Enabled() then lower_32 = ELUsingAArch32(EL2); else lower_32 = ELUsingAArch32(EL1); elsif IsInHost() && PSTATE.EL == EL0 && target_el == EL2 then lower_32 = ELUsingAArch32(EL0); else lower_32 = ELUsingAArch32(target_el - 1); vect_offset = vect_offset + (if lower_32 then 0x600 else 0x400); elsif PSTATE.SP == '1' then vect_offset = vect_offset + 0x200; bits(64) spsr = GetPSRFromPSTATE(AArch64_NonDebugState, 64); if PSTATE.EL == EL1 && target_el == EL1 && EL2Enabled() then if EffectiveHCR_EL2_NVx() IN {'x01', '111'} then spsr<3:2> = '10'; if IsFeatureImplemented(FEAT_BTI) && !UsingAArch32() then boolean zero_btype; // SPSR_ELx[].BTYPE is only guaranteed valid for these exception types if except.exceptype IN {Exception_SError, Exception_IRQ, Exception_FIQ, Exception_SoftwareStep, Exception_PCAlignment, Exception_InstructionAbort, Exception_Breakpoint, Exception_VectorCatch, Exception_SoftwareBreakpoint, Exception_IllegalState, Exception_BranchTarget} then zero_btype = FALSE; else zero_btype = ConstrainUnpredictableBool(Unpredictable_ZEROBTYPE); if zero_btype then spsr<11:10> = '00';
```

```
if (IsFeatureImplemented(FEAT_NV2) && except.exceptype == Exception_NV2DataAbort && target_el == EL3) then // External aborts are configured to be taken to EL3 except.exceptype = Exception_DataAbort; if ! except.exceptype IN {Exception_IRQ, Exception_FIQ} then AArch64.ReportException(except, target_el); if IsFeatureImplemented(FEAT_BRBE) then constant bits(64) brbe_target_address = VBAR_EL[target_el]<63:11>:vect_offset<10:0>; BRBEException(except, brbe_source_allowed, brbe_source_address, brbe_target_address, target_el, except.trappedsyscallinst); if IsFeatureImplemented(FEAT_GCS) then if PSTATE.EL == target_el then if GetCurrentEXLOCKEN() then PSTATE.EXLOCK = '1'; else PSTATE.EXLOCK = '0'; else PSTATE.EXLOCK = '0'; PSTATE.EL = target_el; PSTATE.nRW = '0'; PSTATE.SP = '1'; SPSR_ELx[] = spsr; ELR_ELx[] = preferred_exception_return; PSTATE.SS = '0'; if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = SCTLR_ELx[].DSSBS; if IsFeatureImplemented(FEAT_EBEP) then PSTATE.PM = '1'; if IsFeatureImplemented(FEAT_SEBEP) then PSTATE.PPEND = '0'; ShouldSetPPEND = FALSE; if IsFeatureImplemented(FEAT_NMI) then PSTATE.ALLINT = NOT SCTLR_ELx[].SPINTMASK; PSTATE.<D,A,I,F> = '1111'; if IsFeatureImplemented(FEAT_MTE) then PSTATE.TCO = '1'; PSTATE.IL = '0'; if IsFeatureImplemented(FEAT_UAO) then PSTATE.UAO = '0'; if IsFeatureImplemented(FEAT_UINJ) then PSTATE.UINJ = '0'; if IsFeatureImplemented(FEAT_PAuth_LR) then PSTATE.PACM = '0'; if (IsFeatureImplemented(FEAT_PAN) && (PSTATE.EL == EL1 || (PSTATE.EL == EL2 && ELIsInHost(EL0))) && SCTLR_ELx[].SPAN == '0') then PSTATE.PAN = '1'; if from_32 then // Coming from AArch32 PSTATE.IT = '00000000'; PSTATE.T = '0'; // PSTATE.J is RES0 if IsFeatureImplemented(FEAT_BTI) then PSTATE.BTYPE = '00'; constant boolean branch_conditional = FALSE; BranchTo(VBAR_ELx[]<63:11>:vect_offset<10:0>, BranchType_EXCEPTION, branch_conditional); CheckExceptionCatch(TRUE); // Check for debug event on exception entry if sync_errors then SynchronizeErrors(); iesb_req = TRUE; TakeUnmaskedPhysicalSErrorInterrupts(iesb_req); EndOfInstruction();
```

## J1.1.2.36 AArch64.AArch32SystemAccessTrap

// AArch64.AArch32SystemAccessTrap()

```
// ================================= // Trapped AArch32 System register access. AArch64.AArch32SystemAccessTrap(bits(2) target_el, integer ec) assert HaveEL(target_el) && target_el != EL0 && UInt(target_el) >= UInt(PSTATE.EL); constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; except = AArch64.AArch32SystemAccessTrapSyndrome(ThisInstr(), ec); AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.2.37 AArch64.AArch32SystemAccessTrapSyndrome

```
// AArch64.AArch32SystemAccessTrapSyndrome() // ========================================= // Returns the syndrome information for traps on AArch32 MCR, MCRR, MRC, MRRC, and VMRS, // VMSR instructions, other than traps that are due to HCPTR or CPACR. ExceptionRecord AArch64.AArch32SystemAccessTrapSyndrome(bits(32) instr, integer ec) ExceptionRecord except; case ec of when 0x0 except = ExceptionSyndrome(Exception_Uncategorized); when 0x3 except = ExceptionSyndrome(Exception_CP15RTTrap); when 0x4 except = ExceptionSyndrome(Exception_CP15RRTTrap); when 0x5 except = ExceptionSyndrome(Exception_CP14RTTrap); when 0x6 except = ExceptionSyndrome(Exception_CP14DTTrap); when 0x7 except = ExceptionSyndrome(Exception_AdvSIMDFPAccessTrap); when 0x8 except = ExceptionSyndrome(Exception_FPIDTrap); when 0xC except = ExceptionSyndrome(Exception_CP14RRTTrap); otherwise Unreachable(); bits(20) iss = Zeros(20); if except.exceptype == Exception_Uncategorized then return except; elsif except.exceptype IN {Exception_FPIDTrap, Exception_CP14RTTrap, Exception_CP15RTTrap} then // Trapped MRC/MCR, VMRS on FPSID if except.exceptype != Exception_FPIDTrap then // When trap is not for VMRS iss<19:17> = instr<7:5>; // opc2 iss<16:14> = instr<23:21>; // opc1 iss<13:10> = instr<19:16>; // CRn iss<4:1> = instr<3:0>; // CRm else iss<19:17> = '000'; iss<16:14> = '111'; iss<13:10> = instr<19:16>; // reg iss<4:1> = '0000'; if instr<20> == '1' && instr<15:12> == '1111' then // MRC, Rt==15 iss<9:5> = '11111'; elsif instr<20> == '0' && instr<15:12> == '1111' then // MCR, Rt==15 iss<9:5> = bits(5) UNKNOWN; else iss<9:5> = LookUpRIndex(UInt(instr<15:12>), PSTATE.M)<4:0>; elsif except.exceptype IN {Exception_CP14RRTTrap, Exception_AdvSIMDFPAccessTrap, Exception_CP15RRTTrap} then // Trapped MRRC/MCRR, VMRS/VMSR iss<19:16> = instr<7:4>; // opc1 if instr<19:16> == '1111' then // Rt2==15 iss<14:10> = bits(5) UNKNOWN; else iss<14:10> = LookUpRIndex(UInt(instr<19:16>), PSTATE.M)<4:0>;
```

```
if instr<15:12> == '1111' then // Rt==15 iss<9:5> = bits(5) UNKNOWN; else iss<9:5> = LookUpRIndex(UInt(instr<15:12>), PSTATE.M)<4:0>; iss<4:1> = instr<3:0>; // CRm elsif except.exceptype == Exception_CP14DTTrap then // Trapped LDC/STC iss<19:12> = instr<7:0>; // imm8 iss<4> = instr<23>; // U iss<2:1> = instr<24,21>; // P,W if instr<19:16> == '1111' then iss<9:5> = bits(5) UNKNOWN; iss<3> = '1'; iss<0> = instr<20>; // Direction except.syndrome.iss<24:20> = ConditionSyndrome(); except.syndrome.iss<19:0> = iss; return except;
```

```
// AArch64.CheckCP15InstrCoarseTraps() // =================================== // Check for coarse-grained AArch32 traps to System registers in the // coproc=0b1111 encoding space by HSTR_EL2, HCR_EL2, and SCTLR_ELx. AArch64.CheckCP15InstrCoarseTraps(integer CRn, integer nreg, integer CRm) trapped_encoding = ((CRn == 9 && CRm IN {0,1,2, 5,6,7,8 }) || (CRn == 10 && CRm IN {0,1, 4, 8 }) || (CRn == 11 && CRm IN {0,1,2,3,4,5,6,7,8,15})); // Check for MRC and MCR disabled by SCTLR_EL1.TIDCP. if (IsFeatureImplemented(FEAT_TIDCP1) && PSTATE.EL == EL0 && !IsInHost() && !ELUsingAArch32(EL1) && SCTLR_EL1.TIDCP == if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x3); else AArch64.AArch32SystemAccessTrap(EL1, 0x3);
```

```
// Rn==15, LDC(Literal addressing)/STC J1.1.2.38 AArch64.AdvSIMDFPAccessTrap // AArch64.AdvSIMDFPAccessTrap() // ============================= // Trapped access to Advanced SIMD or FP registers due to CPACR. AArch64.AdvSIMDFPAccessTrap(bits(2) target_el) constant bits(64) preferred_exception_return = ThisInstrAddr(64); ExceptionRecord except; vect_offset = 0x0; route_to_el2 = (target_el == EL1 && EL2Enabled() && HCR_EL2.TGE == '1'); if route_to_el2 then except = ExceptionSyndrome(Exception_Uncategorized); AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); else except = ExceptionSyndrome(Exception_AdvSIMDFPAccessTrap); except.syndrome.iss<24:20> = ConditionSyndrome(); AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset); return; J1.1.2.39 AArch64.CheckCP15InstrCoarseTraps '1' && trapped_encoding) then
```

```
// Check for coarse-grained Hyp traps if PSTATE.EL IN {EL0, EL1} && EL2Enabled() then // Check for MRC and MCR disabled by SCTLR_EL2.TIDCP. if (IsFeatureImplemented(FEAT_TIDCP1) && PSTATE.EL == EL0 && IsInHost() && SCTLR_EL2.TIDCP == '1' && trapped_encoding) then AArch64.AArch32SystemAccessTrap(EL2, 0x3); major = if nreg == 1 then CRn else CRm; // Check for MCR, MRC, MCRR, and MRRC disabled by HSTR_EL2<CRn/CRm> // and MRC and MCR disabled by HCR_EL2.TIDCP. if ((!IsInHost() && ! major IN {4,14} && HSTR_EL2<major> == '1') || (HCR_EL2.TIDCP == '1' && nreg == 1 && trapped_encoding)) then if (PSTATE.EL == EL0 && boolean IMPLEMENTATION_DEFINED "UNDEF unallocated CP15 access at EL0") then UNDEFINED; AArch64.AArch32SystemAccessTrap(EL2, 0x3);
```

```
// AArch64.CheckFPAdvSIMDEnabled() // =============================== AArch64.CheckFPAdvSIMDEnabled() AArch64.CheckFPEnabled(); // Check for illegal use of Advanced // SIMD in Streaming SVE Mode if IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' && !IsFullA64Enabled() then SMEAccessTrap(SMEExceptionType_Streaming, PSTATE.EL);
```

## J1.1.2.40 AArch64.CheckFPAdvSIMDEnabled J1.1.2.41 AArch64.CheckFPAdvSIMDTrap

```
// AArch64.CheckFPAdvSIMDTrap() // ============================ // Check against CPTR_EL2 and CPTR_EL3. AArch64.CheckFPAdvSIMDTrap() if HaveEL(EL3) && CPTR_EL3.TFP == '1' && EL3SDDUndefPriority() then UNDEFINED; if PSTATE.EL IN {EL0, EL1, EL2} && EL2Enabled() then // Check if access disabled in CPTR_EL2 if ELIsInHost(EL2) then boolean disabled; case CPTR_EL2.FPEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0 && HCR_EL2.TGE == '1'; when '11' disabled = FALSE; if disabled then AArch64.AdvSIMDFPAccessTrap(EL2); else if CPTR_EL2.TFP == '1' then AArch64.AdvSIMDFPAccessTrap(EL2); if HaveEL(EL3) then // Check if access disabled in CPTR_EL3 if CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AdvSIMDFPAccessTrap(EL3);
```

## J1.1.2.42 AArch64.CheckFPEnabled

```
// AArch64.CheckFPEnabled() // ======================== // Check against CPACR AArch64.CheckFPEnabled() if PSTATE.EL IN {EL0, EL1} && !IsInHost() then // Check if access disabled in CPACR_EL1 boolean disabled; case CPACR_EL1.FPEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0; when '11' disabled = FALSE; if disabled then AArch64.AdvSIMDFPAccessTrap(EL1); AArch64.CheckFPAdvSIMDTrap(); // Also check against CPTR_EL2 and CPTR_EL3
```

## J1.1.2.43 AArch64.CheckForERetTrap

```
// AArch64.CheckForERetTrap() // ========================== // Check for trap on ERET, ERETAA, ERETAB instruction AArch64.CheckForERetTrap(boolean eret_with_pac, boolean pac_uses_key_a) if PSTATE.EL == EL1 && EL2Enabled() then boolean route_to_el2 = FALSE; // Check for a fine-grained trap by the hypervisor. if (IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && HFGITR_EL2.ERET == '1') then route_to_el2 = TRUE; // Check for a trap by the Effective value of the HCR_EL2.NV bit elsif EffectiveHCR_EL2_NVx()<0> == '1' then route_to_el2 = TRUE; if route_to_el2 then constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = 0x0; ExceptionRecord except = ExceptionSyndrome(Exception_ERetTrap); if !eret_with_pac then // ERET except.syndrome.iss<1> = '0'; except.syndrome.iss<0> = '0'; // RES0 else except.syndrome.iss<1> = '1'; except.syndrome.iss<0> = if pac_uses_key_a then '0' else '1'; AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); return;
```

## J1.1.2.44 AArch64.CheckForSMCUndefOrTrap

```
// AArch64.CheckForSMCUndefOrTrap() // ================================ // Check for UNDEFINED or trap on SMC instruction AArch64.CheckForSMCUndefOrTrap(bits(16) imm) if PSTATE.EL == EL0 then UNDEFINED; if (!(PSTATE.EL == EL1 && EL2Enabled() && HCR_EL2.TSC == '1') && HaveEL(EL3) && SCR_EL3.SMD == '1') then UNDEFINED;
```

```
route_to_el2 = FALSE; if !HaveEL(EL3) then if (PSTATE.EL == EL1 && EL2Enabled() && HCR_EL2.TSC == '1' && (EffectiveHCR_EL2_NVx() == 'xx1' || (boolean IMPLEMENTATION_DEFINED "Trap SMC execution at EL1 to route_to_el2 = TRUE; else UNDEFINED; else route_to_el2 = PSTATE.EL == EL1 && EL2Enabled() && HCR_EL2.TSC == '1'; if route_to_el2 then constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; except = ExceptionSyndrome(Exception_MonitorCall); except.syndrome.iss<15:0> = imm; except.trappedsyscallinst = TRUE; AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset);
```

## EL2"))) then J1.1.2.45 AArch64.CheckForSVCTrap // AArch64.CheckForSVCTrap() // ========================= // Check for trap on SVC instruction AArch64.CheckForSVCTrap(bits(16) immediate) if IsFeatureImplemented(FEAT\_FGT) then route\_to\_el2 = FALSE; if PSTATE.EL == EL0 then route\_to\_el2 = (!UsingAArch32() &amp;&amp; !ELUsingAArch32(EL1) &amp;&amp; EL2Enabled() &amp;&amp; HFGITR\_EL2.SVC\_EL0 == '1' &amp;&amp; (!IsInHost() &amp;&amp; (!HaveEL(EL3) || SCR\_EL3.FGTEn == '1'))); elsif PSTATE.EL == EL1 then route\_to\_el2 = (EL2Enabled() &amp;&amp; HFGITR\_EL2.SVC\_EL1 == '1' &amp;&amp; (!HaveEL(EL3) || SCR\_EL3.FGTEn == '1')); if route\_to\_el2 then except = ExceptionSyndrome(Exception\_SupervisorCall); except.syndrome.iss&lt;15:0&gt; = immediate; except.trappedsyscallinst = TRUE; constant bits(64) preferred\_exception\_return = ThisInstrAddr(64); vect\_offset = 0x0; AArch64.TakeException(EL2, except, preferred\_exception\_return, vect\_offset); J1.1.2.46 AArch64.CheckForWFxTrap // AArch64.CheckForWFxTrap() // ========================= // Checks for a trap on a WFE, WFET, WFI or WFIT instruction. (boolean, bits(2)) AArch64.CheckForWFxTrap(WFxType wfxtype) constant boolean is\_wfe = wfxtype IN {WFxType\_WFE, WFxType\_WFET}; bits(2) target\_el; boolean trap = FALSE; if HaveEL(EL3) &amp;&amp; EL3SDDUndefPriority() &amp;&amp; PSTATE.EL != EL3 then // Check for traps described by the Secure Monitor. // If the trap is enabled, the instruction will be UNDEFINED because EDSCR.SDD is 1. trap = (if is\_wfe then SCR\_EL3.TWE else SCR\_EL3.TWI) == '1'; target\_el = EL3; if !trap &amp;&amp; PSTATE.EL == EL0 then

## // Check for traps described by the OS which may be EL1 or EL2. trap = (if is\_wfe then SCTLR\_ELx[].nTWE else SCTLR\_ELx[].nTWI) == '0'; target\_el = EL1; if !trap &amp;&amp; PSTATE.EL IN {EL0, EL1} &amp;&amp; EL2Enabled() &amp;&amp; !IsInHost() then // Check for traps described by the Hypervisor. trap = (if is\_wfe then HCR\_EL2.TWE else HCR\_EL2.TWI) == '1'; target\_el = EL2; if !trap &amp;&amp; HaveEL(EL3) &amp;&amp; PSTATE.EL != EL3 then // Check for traps described by the Secure Monitor. trap = (if is\_wfe then SCR\_EL3.TWE else SCR\_EL3.TWI) == '1'; target\_el = EL3; return (trap, target\_el); J1.1.2.47 AArch64.CheckIllegalState // AArch64.CheckIllegalState() // =========================== // Check PSTATE.IL bit and generate Illegal Execution state exception if set. AArch64.CheckIllegalState() if PSTATE.IL == '1' then route\_to\_el2 = PSTATE.EL == EL0 &amp;&amp; EL2Enabled() &amp;&amp; HCR\_EL2.TGE == '1'; constant bits(64) preferred\_exception\_return = ThisInstrAddr(64); vect\_offset = 0x0; except = ExceptionSyndrome(Exception\_IllegalState); if UInt(PSTATE.EL) &gt; UInt(EL1) then AArch64.TakeException(PSTATE.EL, except, preferred\_exception\_return, vect\_offset); elsif route\_to\_el2 then AArch64.TakeException(EL2, except, preferred\_exception\_return, vect\_offset); else AArch64.TakeException(EL1, except, preferred\_exception\_return, vect\_offset); J1.1.2.48 AArch64.MonitorModeTrap // AArch64.MonitorModeTrap() // ========================= // Trapped use of Monitor mode features in a Secure EL1 AArch32 mode AArch64.MonitorModeTrap() constant bits(64) preferred\_exception\_return = ThisInstrAddr(64); vect\_offset = 0x0; except = ExceptionSyndrome(Exception\_Uncategorized); if IsSecureEL2Enabled() then AArch64.TakeException(EL2, except, preferred\_exception\_return, vect\_offset); AArch64.TakeException(EL3, except, preferred\_exception\_return, vect\_offset); J1.1.2.49 AArch64.SystemAccessTrap // AArch64.SystemAccessTrap() // ========================== // Trapped access to AArch64 System register or system instruction. AArch64.SystemAccessTrap(bits(2) target\_el, integer ec) assert HaveEL(target\_el) &amp;&amp; target\_el != EL0 &amp;&amp; UInt(target\_el) &gt;= UInt(PSTATE.EL);

```
constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; except = AArch64.SystemAccessTrapSyndrome(ThisInstr(), ec); AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.2.50 AArch64.SystemAccessTrapSyndrome

```
// AArch64.SystemAccessTrapSyndrome() // ================================== // Returns the syndrome information for traps on AArch64 MSR/MRS instructions. ExceptionRecord AArch64.SystemAccessTrapSyndrome(bits(32) instr_in, integer ec) ExceptionRecord except; bits(32) instr = instr_in; case ec of when 0x0 // Trapped access due to unknown reason. except = ExceptionSyndrome(Exception_Uncategorized); when 0x7 // Trapped access to SVE, Advance SIMD&FP System register. except = ExceptionSyndrome(Exception_AdvSIMDFPAccessTrap); except.syndrome.iss<24:20> = ConditionSyndrome(); when 0x14 // Trapped access to 128-bit System register or // 128-bit System instruction. except = ExceptionSyndrome(Exception_SystemRegister128Trap); instr = ThisInstr(); except.syndrome.iss<21:20> = instr<20:19>; // Op0 except.syndrome.iss<19:17> = instr<7:5>; // Op2 except.syndrome.iss<16:14> = instr<18:16>; // Op1 except.syndrome.iss<13:10> = instr<15:12>; // CRn except.syndrome.iss<9:6> = instr<4:1>; // Rt except.syndrome.iss<4:1> = instr<11:8>; // CRm except.syndrome.iss<0> = instr<21>; // Direction when 0x18 // Trapped access to System register or system instruction. except = ExceptionSyndrome(Exception_SystemRegisterTrap); instr = ThisInstr(); except.syndrome.iss<21:20> = instr<20:19>; // Op0 except.syndrome.iss<19:17> = instr<7:5>; // Op2 except.syndrome.iss<16:14> = instr<18:16>; // Op1 except.syndrome.iss<13:10> = instr<15:12>; // CRn except.syndrome.iss<9:5> = instr<4:0>; // Rt except.syndrome.iss<4:1> = instr<11:8>; // CRm except.syndrome.iss<0> = instr<21>; // Direction when 0x19 // Trapped access to SVE System register except = ExceptionSyndrome(Exception_SVEAccessTrap); when 0x1D // Trapped access to SME System register except = ExceptionSyndrome(Exception_SMEAccessTrap); otherwise Unreachable(); return except;
```

## J1.1.2.51 AArch64.Undefined

```
// AArch64.Undefined() // =================== AArch64.Undefined() route_to_el2 = PSTATE.EL == EL0 && EL2Enabled() && HCR_EL2.TGE == '1'; constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0;
```

```
except = ExceptionSyndrome(Exception_Uncategorized); if UInt(PSTATE.EL) > UInt(EL1) then AArch64.TakeException(PSTATE.EL, except, preferred_exception_return, vect_offset); elsif route_to_el2 then AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); else AArch64.TakeException(EL1, except, preferred_exception_return, vect_offset);
```

## J1.1.2.52 AArch64.WFxTrap

```
// AArch64.WFxTrap() // ================= // Generate an exception for a trapped WFE, WFI, WFET or WFIT instruction. AArch64.WFxTrap(WFxType wfxtype, bits(2) target_el) assert UInt(target_el) > UInt(PSTATE.EL); constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = 0x0; ExceptionRecord except = ExceptionSyndrome(Exception_WFxTrap); except.syndrome.iss<24:20> = ConditionSyndrome(); case wfxtype of when WFxType_WFI except.syndrome.iss<1:0> = '00'; when WFxType_WFE except.syndrome.iss<1:0> = '01'; when WFxType_WFIT except.syndrome.iss<1:0> = '10'; except.syndrome.iss<2> = '1'; // Register field is valid except.syndrome.iss<9:5> = ThisInstr()<4:0>; when WFxType_WFET except.syndrome.iss<1:0> = '11'; except.syndrome.iss<2> = '1'; // Register field is valid except.syndrome.iss<9:5> = ThisInstr()<4:0>; if target_el == EL1 && EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); else AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.2.53 CheckLDST64BEnabled

```
// CheckLDST64BEnabled() // ===================== // Checks for trap on ST64B and LD64B instructions CheckLDST64BEnabled() boolean trap = FALSE; constant bits(25) iss = ZeroExtend('10', 25); // 0x2 bits(2) target_el; if PSTATE.EL == EL0 then if !IsInHost() then trap = SCTLR_EL1.EnALS == '0'; target_el = if EL2Enabled() && HCR_EL2.TGE == '1' then EL2 else EL1; else trap = SCTLR_EL2.EnALS == '0'; target_el = EL2; else target_el = EL1; if (!trap && EL2Enabled() && ((PSTATE.EL == EL0 && !IsInHost()) || PSTATE.EL == EL1)) then
```

```
trap = !IsHCRXEL2Enabled() || HCRX_EL2.EnALS == '0'; target_el = EL2; if trap then LDST64BTrap(target_el, iss);
```

## J1.1.2.54 CheckST64BV0Enabled

```
// CheckST64BV0Enabled() // ===================== // Checks for trap on ST64BV0 instruction CheckST64BV0Enabled() boolean trap = FALSE; constant bits(25) iss = ZeroExtend('1', 25); // 0x1 bits(2) target_el; if (PSTATE.EL != EL3 && HaveEL(EL3) && SCR_EL3.EnAS0 == '0' && EL3SDDUndefPriority()) then UNDEFINED; if PSTATE.EL == EL0 then if !IsInHost() then trap = SCTLR_EL1.EnAS0 == '0'; target_el = if EL2Enabled() && HCR_EL2.TGE == '1' then EL2 else EL1; else trap = SCTLR_EL2.EnAS0 == '0'; target_el = EL2; if (!trap && EL2Enabled() && ((PSTATE.EL == EL0 && !IsInHost()) || PSTATE.EL == EL1)) then trap = !IsHCRXEL2Enabled() || HCRX_EL2.EnAS0 == '0'; target_el = EL2; if !trap && PSTATE.EL != EL3 then trap = HaveEL(EL3) && SCR_EL3.EnAS0 == '0'; target_el = EL3; if trap then if target_el == EL3 && EL3SDDUndef() then UNDEFINED; else LDST64BTrap(target_el, iss);
```

## J1.1.2.55 CheckST64BVEnabled

```
// CheckST64BVEnabled() // ==================== // Checks for trap on ST64BV instruction CheckST64BVEnabled() boolean trap = FALSE; constant bits(25) iss = Zeros(25); bits(2) target_el; if PSTATE.EL == EL0 then if !IsInHost() then trap = SCTLR_EL1.EnASR == '0'; target_el = if EL2Enabled() && HCR_EL2.TGE == '1' then EL2 else EL1; else trap = SCTLR_EL2.EnASR == '0'; target_el = EL2; if (!trap && EL2Enabled() &&
```

```
((PSTATE.EL == EL0 && !IsInHost()) || PSTATE.EL == EL1)) then trap = !IsHCRXEL2Enabled() || HCRX_EL2.EnASR == '0'; target_el = EL2; if trap then LDST64BTrap(target_el, iss);
```

## J1.1.2.56 LDST64BTrap

```
// LDST64BTrap() // ============= // Trapped access to LD64B, ST64B, ST64BV and ST64BV0 instructions LDST64BTrap(bits(2) target_el, bits(25) iss) constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; except = ExceptionSyndrome(Exception_LDST64BTrap); except.syndrome.iss = iss; AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset); return;
```

## J1.1.2.57 WFETrapDelay

```
// WFETrapDelay() // ============== // Returns TRUE when delay in trap to WFE is enabled with value to amount of delay, // FALSE otherwise. (boolean, integer) WFETrapDelay(bits(2) target_el) boolean delay_enabled; integer delay; case target_el of when EL1 if !IsInHost() then delay_enabled = SCTLR_EL1.TWEDEn == '1'; delay = 1 << (UInt(SCTLR_EL1.TWEDEL) + 8); else delay_enabled = SCTLR_EL2.TWEDEn == '1'; delay = 1 << (UInt(SCTLR_EL2.TWEDEL) + 8); when EL2 assert EL2Enabled(); delay_enabled = HCR_EL2.TWEDEn == '1'; delay = 1 << (UInt(HCR_EL2.TWEDEL) + 8); when EL3 delay_enabled = SCR_EL3.TWEDEn == '1'; delay = 1 << (UInt(SCR_EL3.TWEDEL) + 8); return (delay_enabled, delay);
```

## J1.1.2.58 WaitForEventUntilDelay

```
// WaitForEventUntilDelay() // ======================== // Returns TRUE if WaitForEvent() returns before WFE trap delay // FALSE otherwise. boolean WaitForEventUntilDelay(boolean delay_enabled, integer delay);
```

```
expires,
```

## J1.1.3 aarch64/functions

This section includes the following pseudocode functions:

- AArch64.FaultSyndrome
- AArch64.InstructionSyndromeValid
- EncodeGPCSC
- LS64InstructionSyndrome
- WatchpointFARNotPrecise
- AArch64.APAS
- AArch64.LocationSupportsAPAS
- APASRecord
- APAS\_OP
- AArch64.AT
- AArch64.EncodePAR
- AArch64.PARFaultStatus
- AArch64.isPARFormatD128

•

GetPAR\_EL1\_D128

- GetPAR\_EL1\_F
- MemBarrierOp
- BFXPreferred
- AltDecodeBitMasks
- DecodeBitMasks
- AArch64.DataMemZero
- AArch64.WriteTagMem
- CompareOp
- CountOp
- EffectiveCPTA
- EffectiveCPTM
- PointerAddCheck
- PointerAddCheckAtEL
- PointerCheckAtEL
- PointerMultiplyAddCheck
- IsD128Enabled
- AArch64.CanTrapDC
- AArch64.DC
- AArch64.MemZero
- AArch64.TreatDCAsNOP
- MemZero
- AArch64.ExceptionReturn
- AArch64.ExclusiveMonitorsPass
- AArch64.IsExclusiveVA
- AArch64.MarkExclusiveVA
- AArch64.SetExclusiveMonitors
- DecodeRegExtend
- ExtendReg
- ExtendType
- FPConvOp

- FPMaxMinOp
- CheckFPMREnabled
- FPScale
- FPUnaryOp
- FPRSqrtStepFused
- FPRecipStepFused
- AddGCSExRecord
- AddGCSRecord
- CheckGCSExRecord
- CheckGCSSTREnabled
- EXLOCKException
- GCSDataCheckException
- GCSEnabled
- GCSInstruction
- GCSPCREnabled
- GCSPCRSelected
- GCSPOPCX
- GCSPOPM
- GCSPOPX
- GCSPUSHM
- GCSPUSHX
- GCSReturnValueCheckEnabled
- GCSSS1
- GCSSS2
- GCSSTRTrapException
- GCSSynchronizationBarrier
- GetCurrentEXLOCKEN
- GetCurrentGCSPointer
- LoadCheckGCSRecord
- SetCurrentGCSPointer
- HACDBS\_ERR\_REASON\_IPAF
- HACDBS\_ERR\_REASON\_IPHACF
- HACDBS\_ERR\_REASON\_STRUCTF
- IsHACDBSIRQAsserted
- ProcessHACDBSEntry
- AArch64.CanTrapIC
- AArch64.IC
- AArch64.TreatICAsNOP
- ImmediateOp
- LogicalOp
- AArch64.S1AMECFault
- AArch64.S1DisabledOutputMECID
- AArch64.S1OutputMECID
- AArch64.S1TTWalkMECID
- AArch64.S2OutputMECID
- AArch64.S2TTWalkMECID
- DEFAULT\_MECID

- AArch64.AccessIsTagChecked
- AArch64.AddressWithAllocationTag
- AArch64.AllocationTagCheck
- AArch64.AllocationTagFromAddress
- AArch64.CanonicalTagCheck
- AArch64.CheckTag
- AArch64.IsUnprivAccessPriv
- AArch64.LogicalAddressTag
- AArch64.MemSingle
- AArch64.MemSingleRead
- AArch64.MemSingleWrite
- AArch64.MemTag
- AArch64.MemTagRead
- AArch64.MemTagWrite
- AArch64.UnalignedAccessFaults
- AddressSupportsLS64
- AllInAlignedQuantity
- CASCompare
- CheckSPAlignment
- IsConventionalMemory
- Mem
- MemAtomic
- MemAtomicFP
- MemAtomicInt
- MemAtomicRCW
- MemLoad64B
- MemSingleGranule
- MemStore64B
- MemStore64BWithRet
- MemStore64BWithRetStatus
- NVMem
- PhysMemTagRead
- PhysMemTagWrite
- StoreOnlyTagCheckingEnabled
- ArchMaxMOPSBlockSize
- ArchMaxMOPSCPYSize
- ArchMaxMOPSSETGSize
- CPYFOptionA
- CPYOptionA
- CPYParams
- CPYPostSizeChoice
- CPYPreSizeChoice
- CPYSizeChoice
- CheckCPYConstrainedUnpredictable
- CheckMOPSEnabled
- CheckMemCpyParams
- CheckMemSetParams

- CheckSETConstrainedUnpredictable
- IsMemCpyForward
- MOPSBlockSize
- MOPSStage
- MaxBlockSizeCopiedBytes
- MemCpyBytes
- MemCpyParametersIllformedE
- MemCpyParametersIllformedM
- MemCpyStageSize
- MemCpyZeroSizeCheck
- MemSetBytes
- MemSetParametersIllformedE
- MemSetParametersIllformedM
- MemSetStageSize
- MemSetTags
- MemSetZeroSizeCheck
- MemStageCpyZeroSizeCheck
- MemStageSetZeroSizeCheck
- MismatchedCpySetTargetEL
- MismatchedMemCpyException
- MismatchedMemSetException
- SETGOptionA
- SETOptionA

•

SETParams

- SETPostSizeChoice
- SETPreSizeChoice
- SETSizeChoice
- UpdateCpyRegisters
- UpdateSetRegisters
- MoveWideOp
- MoveWidePreferred
- AddPAC
- AddPAC2
- InsertPAC
- AddPACDA
- AddPACDB
- AddPACGA
- AddPACIA
- AddPACIA2
- AddPACIB
- AddPACIB2
- AArch64.PACFailException
- Auth
- Auth2
- Authenticate
- AuthDA
- AuthDB

- AuthIA
- AuthIA2
- AuthIB
- AuthIB2
- AArch64.PACEffectiveTxSZ
- CalculateBottomPACBit
- ComputePAC
- ComputePAC2
- ComputePAC2IMPDEF
- ComputePAC2QARMA
- ComputePACIMPDEF
- ComputePACQARMA
- PACCellInvShuffle
- PACCellShuffle
- PACInvSub
- PACMult
- PACSub
- PacSub1
- RC
- TweakCellInvRot
- TweakCellRot
- TweakInvShuffle
- TweakShuffle
- IsAPDAKeyEnabled
- IsAPDBKeyEnabled
- IsAPIAKeyEnabled
- IsAPIBKeyEnabled

•

IsPACMEnabled

- IsTrivialPACMImplementation
- PtrHasUpperAndLowerAddRanges
- Strip
- TrapPACUse
- AArch64.RestrictPrediction
- Prefetch
- PSTATEField
- AArch64.DelegatedSErrorTarget
- AArch64.ESBOperation
- AArch64.EncodeAsyncErrorSyndrome
- AArch64.EncodeSyncErrorSyndrome
- AArch64.PhysicalSErrorSyndrome
- AArch64.dESBOperation
- AArch64.vESBOperation
- FirstRecordOfNode
- IsCommonFaultInjectionImplemented
- IsCountableErrorsRecorded
- IsErrorAddressIncluded
- IsErrorRecordImplemented

- IsFirstRecordOfNode
- IsPFARValid
- IsSPMUCounterImplemented
- ProtectionEnabled
- RCW128\_PROTECTED\_BIT
- RCW64\_PROTECTED\_BIT
- RCWCheck
- FPReduce
- IntReduce
- ReduceOp
- AArch64.MaybeZeroRegisterUppers
- AArch64.ResetGeneralRegisters
- AArch64.ResetSIMDFPRegisters
- AArch64.ResetSpecialRegisters
- AArch64.ResetSystemRegisters
- PC64
- SP
- SPMCFGR\_EL1
- SPMCGCR\_EL1
- SPMCNTENCLR\_EL0
- SPMCNTENSET\_EL0
- SPMCR\_EL0
- SPMDEVAFF\_EL1
- SPMDEVARCH\_EL1
- SPMEVCNTR\_EL0
- SPMEVFILT2R\_EL0
- SPMEVFILTR\_EL0
- SPMEVTYPER\_EL0
- SPMIIDR\_EL1
- SPMINTENCLR\_EL1
- SPMINTENSET\_EL1
- SPMOVSCLR\_EL0
- SPMOVSSET\_EL0
- SPMROOTCR\_EL3
- SPMSCR\_EL1
- SPMZR\_EL0
- X
- DecodeShift
- ShiftReg
- ShiftType
- CounterToPredicate
- EncodePredCount
- Lookup
- PredCountTest
- System
- ZAhslice
- ZAslice

- ZAtile
- ZAvector
- ZAvslice
- ZT0
- AArch32.IsFPEnabled
- AArch64.IsFPEnabled
- ActivePredicateElement
- AllElementsActive
- AnyActiveElement
- BitDeposit
- BitExtract
- BitGroup
- CheckNonStreamingSVEEnabled
- CheckOriginalSVEEnabled
- CheckSMEAccess
- CheckSMEAndZAEnabled
- CheckSMEEnabled
- CheckSMEZT0Enabled
- CheckSVEEnabled
- CheckStreamingSVEAndZAEnabled
- CheckStreamingSVEEnabled
- CmpOp
- CurrentNSVL
- CurrentSVL
- CurrentVL
- DecodePredCount
- ElemFFR

•

FFR

- FPCompareNE
- FPCompareUN
- FPConvertSVE
- FPExpA
- FPExpCoefficient
- FPLogB

•

FPMinNormal

- FPOne
- FPPointFive
- FPReducePredicated
- FPTrigMAdd
- FPTrigMAddCoefficient
- FPTrigSMul
- FPTrigSSel
- FirstActive
- Getter
- HaveSVE2FP8DOT2
- HaveSVE2FP8DOT4
- HaveSVE2FP8FMA

- ImplementedSMEVectorLength
- ImplementedSVEVectorLength
- InStreamingMode
- IntReducePredicated
- IsFPEnabled
- IsFullA64Enabled
- IsOriginalSVEEnabled
- IsSMEEnabled
- IsSVEEnabled
- LastActive
- LastActiveElement
- MaxImplementedAnyVL
- MaxImplementedSVL
- MaxImplementedVL
- MaybeZeroSVEUppers
- MemNF
- MemSingleNF
- NoneActive
- P
- PredLen
- PredTest
- PredicateElement
- ResetSMEState
- ResetSVERegisters
- ResetSVEState
- SMEAccessTrap
- SMEExceptionType

•

SVEAccessTrap

- SVEMoveMaskPreferred
- SetPSTATE\_SM
- SetPSTATE\_ZA
- Setter
- SupportedPowerTwoSVL
- System
- VecLen
- Z
- SystemHintOp
- SysLOp
- SystemLOp
- SysOp
- SystemOp
- SysOp128
- SystemOp128
- ELR\_EL
- ELR\_ELx
- ESR\_EL
- ESR\_ELx

- FAR\_EL
- FAR\_ELx
- PFAR\_EL
- PFAR\_ELx
- SCTLR\_EL
- SCTLR\_ELx
- VBAR\_EL
- VBAR\_ELx
- AArch64.CheckDAIFAccess
- AArch64.ChooseNonExcludedTag
- AArch64.ChooseNonExludedTagOrZero
- AArch64.ChooseTagOrZero
- AArch64.ExecutingERETInstr
- AArch64.ImpDefSysInstr
- AArch64.ImpDefSysInstr128

•

AArch64.ImpDefSysInstrWithResult

- AArch64.ImpDefSysRegRead
- AArch64.ImpDefSysRegRead128
- AArch64.ImpDefSysRegWrite
- AArch64.ImpDefSysRegWrite128
- AArch64.InterruptPending
- AArch64.NextRandomTagBit
- AArch64.RandomTag
- AArch64.SysInstr
- AArch64.SysInstrWithResult
- AArch64.SysRegRead
- AArch64.SysRegWrite
- BTypeCompatible
- BTypeCompatible\_BTI
- BTypeCompatible\_PAC
- BTypeCompatible\_PACIXSP
- BTypeNext
- ChooseRandomNonExcludedTag
- EffectiveBADDR
- EffectiveICC\_SRE\_EL3\_Enable
- InGuardedPage

•

IsHCRXEL2Enabled

- IsMTEEnabled
- IsPMTESelected
- IsSCTLR2EL1Enabled
- IsSCTLR2EL2Enabled
- IsTCR2EL1Enabled
- IsTCR2EL2Enabled
- PACInstType
- SetBTypeCompatible
- SetBTypeNext
- SetInGuardedPage

- AArch64.SysInstr128
- AArch64.SysRegRead128
- AArch64.SysRegWrite128
- AArch64.TLBIP\_IPAS2
- AArch64.TLBIP\_RIPAS2
- AArch64.TLBIP\_RVA
- AArch64.TLBIP\_RVAA
- AArch64.TLBIP\_VA
- AArch64.TLBIP\_VAA
- AArch64.TLBI\_ALL
- AArch64.TLBI\_ASID
- AArch64.TLBI\_IPAS2
- AArch64.TLBI\_PAALL
- AArch64.TLBI\_RIPAS2
- AArch64.TLBI\_RPA
- AArch64.TLBI\_RVA
- AArch64.TLBI\_RVAA
- AArch64.TLBI\_VA
- AArch64.TLBI\_VAA
- AArch64.TLBI\_VMALL
- AArch64.TLBI\_VMALLS12
- AArch64.TLBI\_VMALLWS2
- DecodeTLBITG
- GPTTLBIMatch
- HasLargeAddress
- ResTLBIRTTL
- ResTLBITTL
- TGBits
- TLBIMatch
- TLBIPRange
- TLBIRange
- VBitOp

## J1.1.3.1 AArch64.FaultSyndrome

```
// AArch64.FaultSyndrome() // ======================= // Creates an exception syndrome value and updates the virtual address for Abort and Watchpoint // exceptions taken to an Exception level using AArch64. IssType AArch64.FaultSyndrome(Exception exceptype, FaultRecord fault, bits(2) target_el) assert fault.statuscode != Fault_None; IssType isstype; isstype.iss = Zeros(25); isstype.iss2 = Zeros(24); constant boolean d_side = exceptype IN {Exception_DataAbort, Exception_NV2DataAbort, Exception_Watchpoint, Exception_NV2Watchpoint}; if IsFeatureImplemented(FEAT_RAS) && fault.statuscode == Fault_SyncExternal then constant ErrorState errstate = PEErrorState(fault); isstype.iss<12:11> = AArch64.EncodeSyncErrorSyndrome(errstate); // SET
```

```
if d_side then if fault.accessdesc.acctype == AccessType_GCS then isstype.iss2<8> = '1'; if exceptype IN {Exception_Watchpoint, Exception_NV2Watchpoint} then isstype.iss<23:0> = WatchpointRelatedSyndrome(fault); if AArch64.InstructionSyndromeValid(fault) then if fault.accessdesc.ls64 then (isstype.iss2, isstype.iss<24:14>) = LS64InstructionSyndrome(); else isstype.iss<24:14> = LSInstructionSyndrome(); if IsFeatureImplemented(FEAT_NV2) && fault.accessdesc.acctype == AccessType_NV2 then isstype.iss<13> = '1'; // Fault is generated by use of VNCR_EL2 if (IsFeatureImplemented(FEAT_LS64) && fault.statuscode IN {Fault_AccessFlag, Fault_Translation, Fault_Permission}) then isstype.iss<12:11> = GetLoadStoreType(); if fault.accessdesc.acctype IN {AccessType_DC, AccessType_IC, AccessType_AT} then isstype.iss<8> = '1'; if fault.accessdesc.acctype IN {AccessType_DC, AccessType_IC, AccessType_AT} then isstype.iss<6> = '1'; elsif fault.statuscode IN {Fault_HWUpdateAccessFlag, Fault_Exclusive} then isstype.iss<6> = bit UNKNOWN; elsif fault.accessdesc.atomicop && IsExternalAbort(fault) then isstype.iss<6> = bit UNKNOWN; else isstype.iss<6> = if fault.write then '1' else '0'; isstype.iss2<9> = if fault.tagaccess then '1' else '0'; if fault.statuscode == Fault_Permission then isstype.iss2<5> = if fault.dirtybit then '1' else '0'; isstype.iss2<6> = if fault.overlay then '1' else '0'; if isstype.iss<24> == '0' then isstype.iss<21> = if fault.toplevel then '1' else '0'; isstype.iss2<7> = if fault.assuredonly then '1' else '0'; isstype.iss2<10> = if fault.s1tagnotdata then '1' else '0'; else if (fault.accessdesc.acctype == AccessType_IFETCH && fault.statuscode == Fault_Permission) then isstype.iss2<5> = if fault.dirtybit then '1' else '0'; isstype.iss<21> = if fault.toplevel then '1' else '0'; isstype.iss2<7> = if fault.assuredonly then '1' else '0'; isstype.iss2<6> = if fault.overlay then '1' else '0'; if fault.hdbssf then isstype.iss2<11> = '1'; if (IsFeatureImplemented(FEAT_PFAR) && IsExternalSyncAbort(fault) && !(EL2Enabled() && (HCR_EL2.VM == '1' || HCR_EL2.DC == '1') && target_el == EL1)) then isstype.iss<14> = if IsPFARValid(fault) then '1' else '0'; if IsExternalAbort(fault) then isstype.iss<9> = fault.extflag; isstype.iss<7> = if fault.s2fs1walk then '1' else '0'; isstype.iss<5:0> = EncodeLDFSC(fault.statuscode, fault.level); return isstype;
```

## J1.1.3.2 AArch64.InstructionSyndromeValid

```
// AArch64.InstructionSyndromeValid() // ================================== // Returns TRUE if ESR_ELx.ISV is '1' for the given Fault.
```

```
boolean AArch64.InstructionSyndromeValid(FaultRecord fault) if !fault.accessdesc.lowestaddress then return FALSE; if fault.accessdesc.ls64 then return fault.statuscode IN {Fault_AccessFlag, Fault_Translation, Fault_Permission}; if fault.accessdesc.acctype == AccessType_GCS then return FALSE; if IsSecondStage(fault) && !fault.s2fs1walk then return (!IsExternalSyncAbort(fault) || (!IsFeatureImplemented(FEAT_RAS) && IsExternalAbortOnWalk(fault) && boolean IMPLEMENTATION_DEFINED "ISV on second stage translation table walk")); return FALSE;
```

```
J1.1.3.3 EncodeGPCSC // EncodeGPCSC() // ============= // Function that gives the GPCSC code for types of GPT Fault bits(6) EncodeGPCSC(GPCFRecord gpcf) assert gpcf.level IN {0,1}; case gpcf.gpf of when GPCF_AddressSize return '00000':gpcf.level<0>; when GPCF_Walk return '00010':gpcf.level<0>; when GPCF_Fail return '00110':gpcf.level<0>; when GPCF_EABT return '01010':gpcf.level<0>; J1.1.3.4 LS64InstructionSyndrome // LS64InstructionSyndrome() // ========================= // Returns the syndrome information and LST for a Data Abort by a // ST64B, ST64BV, ST64BV0, or LD64B instruction. The syndrome information // includes the ISS2, extended syndrome field. (bits(24), bits(11)) LS64InstructionSyndrome(); J1.1.3.5 WatchpointFARNotPrecise
```

```
// WatchpointFARNotPrecise() // ========================= // Returns TRUE If the lowest watchpointed address that is higher than or equal to the address // recorded in EDWAR might not have been accessed by the instruction, other than the CONSTRAINED // UNPREDICTABLE condition of watchpoint matching a range of addresses with lowest address 16 bytes // rounded down and upper address rounded up to nearest 16 byte multiple, // FALSE otherwise. boolean WatchpointFARNotPrecise(FaultRecord fault);
```

## J1.1.3.6 AArch64.APAS

## // AArch64.APAS() // ============== // Decode Xt and perform an APAS operation for the decoded record. AArch64.APAS(bits(64) Xt) APASRecord apas; constant bit nse2 = '0'; apas.paspace = DecodePASpace(nse2, Xt&lt;62&gt;, Xt&lt;63&gt;); apas.pa = Xt&lt;55:6&gt; : '000000'; apas.target\_attributes = Xt&lt;2:0&gt;; if AArch64.LocationSupportsAPAS(apas) then APAS\_OP(apas); J1.1.3.7 AArch64.LocationSupportsAPAS // AArch64.LocationSupportsAPAS() // ============================== // Returns TRUE if the given memory location supports the APAS instruction. boolean AArch64.LocationSupportsAPAS(APASRecord apas); J1.1.3.8 APASRecord // APASRecord // ========== // Details related to an APAS operation. type APASRecord is ( bits(56) pa, PASpace paspace, bits(3) target\_attributes ) J1.1.3.9 APAS\_OP // APAS\_OP() // ========= // Sets the PA Space of the address in the APASRecord to the target PA space. If the location // does not support the APAS instruction or cannot be associated with the indicated PASpace, // then the instruction has no effect on the location and does not generate an External abort. APAS\_OP(APASRecord apas) IMPLEMENTATION\_DEFINED; J1.1.3.10 AArch64.AT EffectiveSCR\_EL3\_NS();

```
// AArch64.AT() // ============ // Perform address translation as per AT instructions. AArch64.AT(bits(64) address, TranslationStage stage, bits(2) el_in, ATAccess ataccess) bits(2) el = el_in; constant bits(2) effective_nse_ns = EffectiveSCR_EL3_NSE() : if (IsFeatureImplemented(FEAT_RME) && PSTATE.EL == EL3 && effective_nse_ns == '10' && el != EL3) then
```

```
UNDEFINED; // For stage 1 translation, when HCR_EL2.{E2H, TGE} is {1,1} and requested EL is EL1, // the EL2&0 translation regime is used. if ELIsInHost(EL0) && el == EL1 && stage == TranslationStage_1 then el = EL2; constant SecurityState ss = SecurityStateAtEL(el); accdesc = CreateAccDescAT(ss, el, ataccess); aligned = TRUE; FaultRecord fault = NoFault(accdesc, address); Regime regime; if stage == TranslationStage_12 then regime = Regime_EL10; else regime = TranslationRegime(el); AddressDescriptor addrdesc; if (el == EL0 && ELUsingAArch32(EL1)) || (el != EL0 && ELUsingAArch32(el)) then if regime == Regime_EL2 || TTBCR.EAE == '1' then (fault, addrdesc) = AArch32.S1TranslateLD(fault, regime, address<31:0>, aligned, accdesc); else (fault, addrdesc, -) = AArch32.S1TranslateSD(fault, regime, address<31:0>, aligned, accdesc); else constant integer size = 1; (fault, addrdesc) = AArch64.S1Translate(fault, regime, address, size, aligned, accdesc); if stage == TranslationStage_12 && fault.statuscode == Fault_None then constant boolean s1aarch64 = TRUE; if ELUsingAArch32(EL1) && regime == Regime_EL10 && EL2Enabled() then addrdesc.vaddress = ZeroExtend(address, 64); (fault, addrdesc) = AArch32.S2Translate(fault, addrdesc, aligned, accdesc); elsif regime == Regime_EL10 && EL2Enabled() then (fault, addrdesc) = AArch64.S2Translate(fault, addrdesc, s1aarch64, aligned, accdesc); is_ATS1Ex = stage != TranslationStage_12; if fault.statuscode != Fault_None then addrdesc = CreateFaultyAddressDescriptor(fault); // Take an exception on: // * A Synchronous External abort occurs on translation table walk // * A stage 2 fault occurs on a stage 1 walk // * A GPC Exception (FEAT_RME) // * A GPF from ATS1E{1,0}* when executed from EL1 and HCR_EL2.GPF == '1' (FEAT_RME) if (IsExternalAbort(fault) || (PSTATE.EL == EL1 && fault.s2fs1walk) || (IsFeatureImplemented(FEAT_RME) && fault.gpcf.gpf != GPCF_None && ( ReportAsGPCException(fault) || (EL2Enabled() && HCR_EL2.GPF == '1' && PSTATE.EL == EL1 && el IN {EL1, EL0} && is_ATS1Ex) ))) then if IsFeatureImplemented(FEAT_D128) then PAR_EL1 = bits(128) UNKNOWN; else PAR_EL1<63:0> = bits(64) UNKNOWN; AArch64.Abort(addrdesc.fault); AArch64.EncodePAR(regime, el, is_ATS1Ex, addrdesc); return;
```

## J1.1.3.11 AArch64.EncodePAR

// AArch64.EncodePAR()

```
// =================== // Encode PAR register with result of translation. AArch64.EncodePAR(Regime regime, bits(2) el, boolean is_ATS1Ex, AddressDescriptor addrdesc) paspace = addrdesc.paddress.paspace; if IsFeatureImplemented(FEAT_D128) then PAR_EL1 = Zeros(128); if AArch64.isPARFormatD128(regime, is_ATS1Ex) then PAR_EL1.D128 = '1'; else PAR_EL1.D128 = '0'; else PAR_EL1<63:0> = Zeros(64); if !IsFault(addrdesc) then PAR_EL1.F = '0'; if IsFeatureImplemented(FEAT_RME) then if regime == Regime_EL3 then case paspace of when PAS_Secure PAR_EL1.<NSE,NS> = '00'; when PAS_NonSecure PAR_EL1.<NSE,NS> = '01'; when PAS_Root PAR_EL1.<NSE,NS> = '10'; when PAS_Realm PAR_EL1.<NSE,NS> = '11'; elsif SecurityStateForRegime(regime) == SS_Secure then PAR_EL1.NSE = bit UNKNOWN; PAR_EL1.NS = if paspace == PAS_Secure then '0' else '1'; elsif SecurityStateForRegime(regime) == SS_Realm then if regime == Regime_EL10 && is_ATS1Ex then PAR_EL1.NSE = bit UNKNOWN; PAR_EL1.NS = bit UNKNOWN; else PAR_EL1.NSE = bit UNKNOWN; PAR_EL1.NS = if paspace == PAS_Realm then '0' else '1'; else PAR_EL1.NSE = bit UNKNOWN; PAR_EL1.NS = bit UNKNOWN; else PAR_EL1<11> = '1'; // RES1 if SecurityStateForRegime(regime) == SS_Secure then PAR_EL1.NS = if paspace == PAS_Secure then '0' else '1'; else PAR_EL1.NS = bit UNKNOWN; PAR_EL1.SH = ReportedPARShareability(PAREncodeShareability(addrdesc.memattrs)); if IsFeatureImplemented(FEAT_D128) && PAR_EL1.D128 == '1' then PAR_EL1<119:76> = addrdesc.paddress.address<55:12>; else PAR_EL1<55:12> = addrdesc.paddress.address<55:12>; PAR_EL1.ATTR = ReportedPARAttrs(EncodePARAttrs(addrdesc.memattrs)); PAR_EL1<10> = bit IMPLEMENTATION_DEFINED "Non-Faulting PAR"; else PAR_EL1.F = '1'; PAR_EL1.DirtyBit = if addrdesc.fault.dirtybit then '1' else '0'; PAR_EL1.Overlay = if addrdesc.fault.overlay then '1' else '0'; PAR_EL1.TopLevel = if addrdesc.fault.toplevel then '1' else '0'; PAR_EL1.AssuredOnly = if addrdesc.fault.assuredonly then '1' else '0'; PAR_EL1.FST = AArch64.PARFaultStatus(addrdesc.fault); PAR_EL1.PTW = if addrdesc.fault.s2fs1walk then '1' else '0'; PAR_EL1.S = if addrdesc.fault.secondstage then '1' else '0'; PAR_EL1<11> = '1'; // RES1 PAR_EL1<63:48> = bits(16) IMPLEMENTATION_DEFINED "Faulting PAR"; return;
```

## J1.1.3.12 AArch64.PARFaultStatus

```
// AArch64.PARFaultStatus() // ======================== // Fault status field decoding of 64-bit PAR. bits(6) AArch64.PARFaultStatus(FaultRecord fault) bits(6) fst; if fault.statuscode == Fault_Domain then // Report Domain fault assert fault.level IN {1,2}; fst<1:0> = if fault.level == 1 then '01' else fst<5:2> = '1111'; else fst = EncodeLDFSC(fault.statuscode, fault.level); return fst;
```

```
// GetPAR_EL1_F() // ============== // Query the PAR_EL1.F bit GetPAR_EL1_F()
```

```
'10'; J1.1.3.13 AArch64.isPARFormatD128 // AArch64.isPARFormatD128() // ========================= // Check if last stage of translation uses VMSAv9-128. // Last stage of translation is stage 2 if enabled, else it is stage 1. boolean AArch64.isPARFormatD128(Regime regime, boolean is_ATS1Ex) boolean isPARFormatD128; // Regime_EL2 does not support VMSAv9-128 if regime == Regime_EL2 || !IsFeatureImplemented(FEAT_D128) then isPARFormatD128 = FALSE; else isPARFormatD128 = FALSE; case regime of when Regime_EL3 isPARFormatD128 = TCR_EL3.D128 == '1'; when Regime_EL20 isPARFormatD128 = IsTCR2EL2Enabled() && TCR2_EL2.D128 == '1'; when Regime_EL10 if is_ATS1Ex || !EL2Enabled() || HCR_EL2.<VM,DC> == '00' then isPARFormatD128 = IsTCR2EL1Enabled() && TCR2_EL1.D128 == '1'; else isPARFormatD128 = VTCR_EL2.D128 == '1'; return isPARFormatD128; J1.1.3.14 GetPAR_EL1_D128 // GetPAR_EL1_D128() // ================= // Query the PAR_EL1.D128 field bit GetPAR_EL1_D128() return if IsFeatureImplemented(FEAT_D128) then PAR_EL1.D128 else '0'; J1.1.3.15 GetPAR_EL1_F field.
```

```
bit F; F = PAR_EL1.F; return F;
```

## J1.1.3.16 MemBarrierOp

// MemBarrierOp

// ============

// Memory barrier

instruction types.

enumeration

MemBarrierOp

## J1.1.3.17 BFXPreferred

```
// BFXPreferred() // ============== // // Return TRUE if UBFX or SBFX is the preferred disassembly of a // UBFM or SBFM bitfield instruction. Must exclude more specific // aliases UBFIZ, SBFIZ, UXT[BH], SXT[BHW], LSL, LSR and ASR. boolean BFXPreferred(bit sf, bit uns, bits(6) imms, bits(6) immr) // must not match UBFIZ/SBFIX alias if UInt(imms) < UInt(immr) then return FALSE; // must not match LSR/ASR/LSL alias (imms == 31 or 63) if imms == sf:'11111' then return FALSE; // must not match UXTx/SXTx alias if immr == '000000' then // must not match 32-bit UXT[BH] or SXT[BH] if sf == '0' && imms IN {'000111', '001111'} then return FALSE; // must not match 64-bit SXT[BHW] if sf:uns == '10' && imms IN {'000111', '001111', '011111'} then return FALSE; // must be UBFX/SBFX alias return TRUE;
```

## J1.1.3.18 AltDecodeBitMasks

```
// AltDecodeBitMasks() // =================== // Alternative but logically equivalent implementation of DecodeBitMasks() that // uses simpler primitives to compute tmask and wmask. (bits(M), bits(M)) AltDecodeBitMasks(bit immN, bits(6) imms, bits(6) immr, boolean immediate, integer M) bits(64) tmask, wmask; bits(6) tmask_and, wmask_and;
```

{MemBarrierOp\_DSB,

MemBarrierOp\_DMB,

MemBarrierOp\_ISB,

MemBarrierOp\_SSBB,

MemBarrierOp\_PSSBB,

MemBarrierOp\_SB

};

//

Data

Synchronization

//

Data

Memory Barrier

// Instruction

Synchronization

// Speculative

// Speculative

// Speculation

Synchronization

Synchronization

Barrier

Barrier

Barrier

Barrier

Barrier to

to

VA

PA

```
bits(6) tmask_or, wmask_or; bits(6) levels; // Compute log2 of element size // 2^len must be in range [2, M] if immN:NOT(imms) == '000000x' then UNDEFINED; constant integer len = HighestSetBitNZ(immN:NOT(imms)); assert 2 <= (2^len) && (2^len) <= M; // Determine s, r and s -r parameters levels = ZeroExtend(Ones(len), 6); // For logical immediates an all-ones value of s is reserved // since it would generate a useless all-ones result (many times) if immediate && (imms AND levels) == levels then UNDEFINED; s = UInt(imms AND levels); r = UInt(immr AND levels); diff = s - r; // 6-bit subtract with borrow // Compute "top mask" tmask_and = diff<5:0> OR NOT(levels); tmask_or = diff<5:0> AND levels; tmask = Ones(64); tmask = ((tmask AND Replicate(Replicate(tmask_and<0>, 1) : Ones(1), 32)) OR Replicate(Zeros(1) : Replicate(tmask_or<0>, 1), 32)); // tmask = Replicate(tmask_and<0> : '1', 32); tmask = ((tmask AND Replicate(Replicate(tmask_and<1>, 2) : Ones(2), 16)) OR Replicate(Zeros(2) : Replicate(tmask_or<1>, 2), 16)); tmask = ((tmask AND Replicate(Replicate(tmask_and<2>, 4) : Ones(4), 8)) OR Replicate(Zeros(4) : Replicate(tmask_or<2>, 4), 8)); tmask = ((tmask AND Replicate(Replicate(tmask_and<3>, 8) : Ones(8), 4)) OR Replicate(Zeros(8) : Replicate(tmask_or<3>, 8), 4)); tmask = ((tmask AND Replicate(Replicate(tmask_and<4>, 16) : Ones(16), 2)) OR Replicate(Zeros(16) : Replicate(tmask_or<4>, 16), 2)); tmask = ((tmask AND Replicate(Replicate(tmask_and<5>, 32) : Ones(32), 1)) OR Replicate(Zeros(32) : Replicate(tmask_or<5>, 32), 1)); // Compute "wraparound mask" wmask_and = immr OR NOT(levels); wmask_or = immr AND levels; wmask = Zeros(64); wmask = ((wmask AND Replicate(Ones(1) : Replicate(wmask_and<0>, 1), 32)) OR Replicate(Replicate(wmask_or<0>, 1) : Zeros(1), 32)); // wmask = Replicate(wmask_or<0> : '0', 32); wmask = ((wmask AND Replicate(Ones(2) : Replicate(wmask_and<1>, 2), 16)) OR Replicate(Replicate(wmask_or<1>, 2) : Zeros(2), 16)); wmask = ((wmask AND Replicate(Ones(4) : Replicate(wmask_and<2>, 4), 8)) OR Replicate(Replicate(wmask_or<2>, 4) : Zeros(4), 8)); wmask = ((wmask AND Replicate(Ones(8) : Replicate(wmask_and<3>, 8), 4)) OR Replicate(Replicate(wmask_or<3>, 8) : Zeros(8), 4)); wmask = ((wmask AND Replicate(Ones(16) : Replicate(wmask_and<4>, 16), 2)) OR Replicate(Replicate(wmask_or<4>, 16) : Zeros(16), 2));
```

```
wmask = ((wmask AND Replicate(Ones(32) : Replicate(wmask_and<5>, 32), 1)) OR Replicate(Replicate(wmask_or<5>, 32) : if diff<6> != '0' then // borrow from s -r wmask = wmask AND tmask; else wmask = wmask OR tmask; return (wmask<M-1:0>, tmask<M-1:0>);
```

```
Zeros(32), 1)); J1.1.3.19 DecodeBitMasks // DecodeBitMasks() // ================ // Decode AArch64 bitfield and logical immediate masks which use a similar encoding structure (bits(M), bits(M)) DecodeBitMasks(bit immN, bits(6) imms, bits(6) immr, boolean immediate, integer M) bits(M) tmask, wmask; bits(6) levels; // Compute log2 of element size // 2^len must be in range [2, M] if immN:NOT(imms) == '000000x' then UNDEFINED; constant integer len = HighestSetBitNZ(immN:NOT(imms)); assert 2 <= (2^len) && (2^len) <= M; // Determine s, r and s -r parameters levels = ZeroExtend(Ones(len), 6); // For logical immediates an all-ones value of s is reserved // since it would generate a useless all-ones result (many times) if immediate && (imms AND levels) == levels then UNDEFINED; constant integer s = UInt(imms AND levels); constant integer r = UInt(immr AND levels); constant integer diff = s - r; // 6-bit subtract with borrow constant integer esize = 1 << len; constant integer d = UInt(diff<len-1:0>); welem = ZeroExtend(Ones(s + 1), esize); telem = ZeroExtend(Ones(d + 1), esize); wmask = Replicate(ROR(welem, r), M DIV esize); tmask = Replicate(telem, M DIV esize); return (wmask, tmask); J1.1.3.20 AArch64.DataMemZero // AArch64.DataMemZero() // ===================== // Write Zero to data memory. AArch64.DataMemZero(bits(64) regval, bits(64) vaddress, AccessDescriptor accdesc_in, integer size) AccessDescriptor accdesc = accdesc_in; // If the instruction targets tags as a payload, confer with system register configuration // which may override this. if accdesc.tagaccess then accdesc.tagaccess = IsMTEEnabled(accdesc.el); // If the instruction encoding permits tag checking, confer with system register configuration // which may override this.
```

```
if accdesc.tagchecked then accdesc.tagchecked = AArch64.AccessIsTagChecked(vaddress, accdesc); constant boolean aligned = TRUE; AddressDescriptor memaddrdesc = AArch64.TranslateAddress(vaddress, accdesc, aligned, size); if IsFault(memaddrdesc) then if !IsDebugException(memaddrdesc.fault) then memaddrdesc.fault.vaddress = regval; AArch64.Abort(memaddrdesc.fault); for i = 0 to size-1 if accdesc.tagchecked then constant bits(4) ltag = AArch64.LogicalAddressTag(vaddress); FaultRecord fault = AArch64.CheckTag(memaddrdesc, accdesc, 1, ltag); if fault.statuscode != Fault_None then if (boolean IMPLEMENTATION_DEFINED "DC_ZVA tag fault reported with lowest faulting address") then AArch64.Abort(fault); else fault.vaddress = regval; AArch64.Abort(fault); memstatus = PhysMemWrite(memaddrdesc, 1, accdesc, Zeros(8)); if IsFault(memstatus) then HandleExternalWriteAbort(memstatus, memaddrdesc, 1, accdesc); memaddrdesc.paddress.address = memaddrdesc.paddress.address + 1; return;
```

## J1.1.3.21 AArch64.WriteTagMem

```
// AArch64.WriteTagMem() // ===================== // Write to tag memory. AArch64.WriteTagMem(bits(64) regval, bits(64) vaddress, AccessDescriptor accdesc_in, integer size) assert accdesc_in.tagaccess && !accdesc_in.tagchecked; AccessDescriptor accdesc = accdesc_in; constant integer count = size >> LOG2_TAG_GRANULE; constant bits(4) tag = AArch64.AllocationTagFromAddress(vaddress); constant boolean aligned = IsAligned(vaddress, TAG_GRANULE); assert aligned; accdesc.tagaccess = IsMTEEnabled(accdesc.el); (memtagtype, memaddrdesc) = AArch64.TranslateTagAddress(vaddress, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then if IsDebugException(memaddrdesc.fault) then AArch64.Abort(memaddrdesc.fault); else memaddrdesc.fault.vaddress = regval; AArch64.Abort(memaddrdesc.fault); if !accdesc.tagaccess || memtagtype != MemTag_AllocationTagged then return; PhysMemRetStatus memstatus; for i = 0 to count-1 memstatus = PhysMemTagWrite(memaddrdesc, accdesc, tag); if IsFault(memstatus) then
```

```
HandleExternalWriteAbort(memstatus, memaddrdesc, 1, accdesc); memaddrdesc.paddress.address = memaddrdesc.paddress.address + TAG_GRANULE; memaddrdesc.vaddress = memaddrdesc.vaddress + TAG_GRANULE;
```

return;

## J1.1.3.22 CompareOp

```
// CompareOp // ========= // Vector compare instruction types. enumeration CompareOp {CompareOp_GT, CompareOp_GE, CompareOp_EQ, CompareOp_LE, CompareOp_LT};
```

## J1.1.3.23 CountOp

```
// CountOp // ======= // Bit counting instruction types. enumeration CountOp {CountOp_CLZ, CountOp_CLS, CountOp_CNT};
```

## J1.1.3.24 EffectiveCPTA

```
// EffectiveCPTA() // =============== // Returns the CPTA bit applied to Checked Pointer Arithmetic for Addition in the given EL. bit EffectiveCPTA(bits(2) el) if !IsFeatureImplemented(FEAT_CPA2) then return '0'; if Halted() then return '0'; bits(1) cpta; constant Regime regime = TranslationRegime(el); case regime of when Regime_EL3 cpta = SCTLR2_EL3.CPTA; when Regime_EL2 if IsSCTLR2EL2Enabled() then cpta = SCTLR2_EL2.CPTA; else cpta = '0'; when Regime_EL20 if IsSCTLR2EL2Enabled() then cpta = if el == EL0 then SCTLR2_EL2.CPTA0 else SCTLR2_EL2.CPTA; else cpta = '0'; when Regime_EL10 if IsSCTLR2EL1Enabled() then cpta = if el == EL0 then SCTLR2_EL1.CPTA0 else SCTLR2_EL1.CPTA; else cpta = '0'; otherwise Unreachable(); return cpta;
```

## J1.1.3.25 EffectiveCPTM

```
// EffectiveCPTM() // =============== // Returns the CPTM bit applied to Checked Pointer Arithmetic for Multiplication in the given EL. bit EffectiveCPTM(bits(2) el) if !IsFeatureImplemented(FEAT_CPA2) then return '0'; if EffectiveCPTA(el) == '0' then return '0'; if Halted() then return '0'; bits(1) cptm; constant Regime regime = TranslationRegime(el); case regime of when Regime_EL3 cptm = SCTLR2_EL3.CPTM; when Regime_EL2 if IsSCTLR2EL2Enabled() then cptm = SCTLR2_EL2.CPTM; else cptm = '0'; when Regime_EL20 if IsSCTLR2EL2Enabled() then cptm = if el == EL0 then SCTLR2_EL2.CPTM0 else SCTLR2_EL2.CPTM; else cptm = '0'; when Regime_EL10 if IsSCTLR2EL1Enabled() then cptm = if el == EL0 then SCTLR2_EL1.CPTM0 else SCTLR2_EL1.CPTM; else cptm = '0'; otherwise Unreachable(); return cptm;
```

## J1.1.3.26 PointerAddCheck

```
// PointerAddCheck() // ================= // Apply Checked Pointer Arithmetic for addition. bits(64) PointerAddCheck(bits(64) result, bits(64) base) return PointerCheckAtEL(PSTATE.EL, result, base, FALSE);
```

## J1.1.3.27 PointerAddCheckAtEL

```
// PointerAddCheckAtEL() // ===================== // Apply Checked Pointer Arithmetic for addition at the specified EL. bits(64) PointerAddCheckAtEL(bits(2) el, bits(64) result, bits(64) base) return PointerCheckAtEL(el, result, base, FALSE);
```

## J1.1.3.28 PointerCheckAtEL

```
// PointerCheckAtEL() // ================== // Apply Checked Pointer Arithmetic at the specified EL. bits(64) PointerCheckAtEL(bits(2) el, bits(64) result, bits(64) base, boolean cptm_detected) bits(64) rv = result; constant boolean previous_detection = (base<55> != base<54>); constant boolean cpta_detected = (result<63:56> != base<63:56> || previous_detection); if((cpta_detected && EffectiveCPTA(el) == '1') || (cptm_detected && EffectiveCPTM(el) == '1')) then rv<63:55> = base<63:55>; rv<54> = NOT(rv<55>); return rv;
```

## J1.1.3.29 PointerMultiplyAddCheck // PointerMultiplyAddCheck() // ========================= // Apply Checked Pointer Arithmetic for multiplication. bits(64) PointerMultiplyAddCheck(bits(64) result, bits(64) base, boolean cptm\_detected) return PointerCheckAtEL(PSTATE.EL, result, base, cptm\_detected); J1.1.3.30 IsD128Enabled // IsD128Enabled() // =============== // Returns true if 128-bit page descriptor is enabled boolean IsD128Enabled(bits(2) el) boolean d128enabled; if IsFeatureImplemented(FEAT\_D128) then case el of when EL0 if !ELIsInHost(EL0) then d128enabled = IsTCR2EL1Enabled() &amp;&amp; TCR2\_EL1.D128 == '1'; else d128enabled = IsTCR2EL2Enabled() &amp;&amp; TCR2\_EL2.D128 == '1'; when EL1 d128enabled = IsTCR2EL1Enabled() &amp;&amp; TCR2\_EL1.D128 == '1'; when EL2 d128enabled = IsTCR2EL2Enabled() &amp;&amp; IsInHost() &amp;&amp; TCR2\_EL2.D128 == '1'; when EL3 d128enabled = TCR\_EL3.D128 == '1'; else d128enabled = FALSE; return d128enabled; J1.1.3.31 AArch64.CanTrapDC // AArch64.CanTrapDC() // =================== // Determines whether the execution of the DC instruction can be trapped. boolean AArch64.CanTrapDC(CacheType cachetype, CacheOp cacheop, CacheOpScope opscope)

return (!AArch64.TreatDCAsNOP(cachetype, cacheop, opscope) || boolean IMPLEMENTATION\_DEFINED "When DC is treated as NOP, data cache maintenance operations are trapped");

## J1.1.3.32 AArch64.DC

```
// AArch64.DC() // ============ // Perform Data Cache Operation. AArch64.DC(bits(64) regval, CacheType cachetype, CacheOp cacheop, CacheOpScope opscope_in) CacheOpScope opscope = opscope_in; CacheRecord cache; cache.acctype = AccessType_DC; cache.cachetype = cachetype; cache.cacheop = cacheop; cache.opscope = opscope; if opscope == CacheOpScope_SetWay then ss = SecurityStateAtEL(PSTATE.EL); cache.cpas = CPASAtSecurityState(ss); cache.shareability = Shareability_NSH; (cache.setnum, cache.waynum, cache.level) = DecodeSW(regval, cachetype); if (cacheop == CacheOp_Invalidate && PSTATE.EL == EL1 && EL2Enabled() && (HCR_EL2.SWIO == '1' || HCR_EL2.<DC,VM> != '00')) then cache.cacheop = CacheOp_CleanInvalidate; CACHE_OP(cache); return; if EL2Enabled() && !IsInHost() then if PSTATE.EL IN {EL0, EL1} then cache.is_vmid_valid = TRUE; cache.vmid = VMID[]; else cache.is_vmid_valid = FALSE; else cache.is_vmid_valid = FALSE; if PSTATE.EL == EL0 then cache.is_asid_valid = TRUE; cache.asid = ASID[]; else cache.is_asid_valid = FALSE; if (opscope == CacheOpScope_PoPS && boolean IMPLEMENTATION_DEFINED "Memory system does not support PoPS") then opscope = CacheOpScope_PoC; if (opscope == CacheOpScope_PoDP && boolean IMPLEMENTATION_DEFINED "Memory system does not support PoDP") then opscope = CacheOpScope_PoP; if (opscope == CacheOpScope_PoP && boolean IMPLEMENTATION_DEFINED "Memory system does not support PoP") then opscope = CacheOpScope_PoC; vaddress = regval; integer size = 0; // by default no watchpoint address if cacheop == CacheOp_Invalidate then size = DataCacheWatchpointSize(); vaddress = Align(regval, size); if opscope == CacheOpScope_PoE then cache.shareability = Shareability_OSH; cache.paddress.address = regval<55:0>; constant bit nse2 = if IsFeatureImplemented(FEAT_RME_GDI) then regval<61> else '0';
```

```
cache.paddress.paspace = DecodePASpace(nse2, regval<62>, regval<63>); cache.cpas = CPASAtPAS(cache.paddress.paspace); // If a Reserved encoding is selected, the instruction is permitted to be treated as a NOP. if cache.paddress.paspace != PAS_Realm then ExecuteAsNOP(); if boolean IMPLEMENTATION_DEFINED "Apply granule protection check on DC to PoE" then AddressDescriptor memaddrdesc; constant AccessDescriptor accdesc = CreateAccDescDC(cache); memaddrdesc.paddress = cache.paddress; memaddrdesc.fault.gpcf = GranuleProtectionCheck(memaddrdesc, accdesc); if memaddrdesc.fault.gpcf.gpf != GPCF_None then memaddrdesc.fault.statuscode = Fault_GPCFOnOutput; memaddrdesc.fault.paddress = memaddrdesc.paddress; memaddrdesc.fault.vaddress = bits(64) UNKNOWN; AArch64.Abort(memaddrdesc.fault); elsif opscope == CacheOpScope_PoPA then cache.shareability = Shareability_OSH; cache.paddress.address = regval<55:0>; constant bit nse2 = if IsFeatureImplemented(FEAT_RME_GDI) then regval<61> else '0'; cache.paddress.paspace = DecodePASpace(nse2, regval<62>, regval<63>); // If {NSE2, NSE, NS} is reserved, then no cache entries are required // to be cleaned or invalidated. if cache.paddress.paspace IN {PAS_NA6, PAS_NA7} then ExecuteAsNOP(); cache.cpas = CPASAtPAS(cache.paddress.paspace); else cache.vaddress = vaddress; constant boolean aligned = TRUE; constant AccessDescriptor accdesc = CreateAccDescDC(cache); AddressDescriptor memaddrdesc = AArch64.TranslateAddress(vaddress, accdesc, aligned, size); if IsFault(memaddrdesc) then memaddrdesc.fault.vaddress = regval; AArch64.Abort(memaddrdesc.fault); cache.paddress = memaddrdesc.paddress; cache.cpas = CPASAtPAS(memaddrdesc.paddress.paspace); if (opscope IN { CacheOpScope_PoDP, CacheOpScope_PoP, CacheOpScope_PoC, CacheOpScope_PoU }) then cache.shareability = memaddrdesc.memattrs.shareability; else cache.shareability = Shareability_NSH; if (cacheop == CacheOp_Invalidate && PSTATE.EL == EL1 && EL2Enabled() && HCR_EL2.<DC,VM> != '00') then cache.cacheop = CacheOp_CleanInvalidate; // If Secure state is not implemented, but RME is, the instruction acts as a NOP if cache.cpas == CPAS_Secure && !HaveSecureState() then return; CACHE_OP(cache); return;
```

## J1.1.3.33 AArch64.MemZero

```
// AArch64.MemZero() // ================= AArch64.MemZero(bits(64) regval, CacheType cachetype) constant integer size = 4*(2^(UInt(DCZID_EL0.BS))); assert size <= MAX_ZERO_BLOCK_SIZE; if IsFeatureImplemented(FEAT_MTE2) then assert size >= TAG_GRANULE; constant bits(64) vaddress = Align(regval, size); constant AccessDescriptor accdesc = if cachetype IN {CacheType_Tag, CacheType_Data_Tag} then AArch64.WriteTagMem(regval, vaddress, accdesc, size); if cachetype IN {CacheType_Data, CacheType_Data_Tag} then AArch64.DataMemZero(regval, vaddress, accdesc, size); return;
```

```
// AArch64.TreatDCAsNOP() // ====================== // Determines whether the execution of the DC instruction is treated as a NOP. boolean AArch64.TreatDCAsNOP(CacheType cachetype, CacheOp cacheop, CacheOpScope opscope) // DC to PoU: IMPLEMENTATION DEFINED - treated as NOP if LoUU and LoUIS are 0 if opscope == CacheOpScope_PoU && CLIDR_EL1.LoUU == '000' && CLIDR_EL1.LoUIS == '000' then return boolean IMPLEMENTATION_DEFINED "DC to PoU is treated as a NOP"; // DC to PoC: IMPLEMENTATION DEFINED - treated as NOP if LoC is 0 if opscope == CacheOpScope_PoC && CLIDR_EL1.LoC == '000' then return boolean IMPLEMENTATION_DEFINED "DC to PoC is treated as a NOP"; // DC to PoP: IMPLEMENTATION DEFINED - treated as NOP if LoC is 0 and PoP unsupported if (opscope == CacheOpScope_PoP && CLIDR_EL1.LoC == '000' && !(boolean IMPLEMENTATION_DEFINED "Memory system supports PoP")) then return boolean IMPLEMENTATION_DEFINED "DC to PoP is treated as a NOP"; // DC to PoDP: IMPLEMENTATION DEFINED treated as NOP if LoC is 0 and PoP/PoDP unsupported if (opscope == CacheOpScope_PoDP && CLIDR_EL1.LoC == '000' && !(boolean IMPLEMENTATION_DEFINED "Memory system supports PoP") && !(boolean IMPLEMENTATION_DEFINED "Memory system supports PoDP")) then return boolean IMPLEMENTATION_DEFINED "DC to PoDP is treated as a NOP"; return FALSE;
```

## CreateAccDescDCZero(cachetype); J1.1.3.34 AArch64.TreatDCAsNOP J1.1.3.35 MemZero // MemZero block size // ================== constant integer MAX\_ZERO\_BLOCK\_SIZE = 2048; J1.1.3.36 AArch64.ExceptionReturn

```
// AArch64.ExceptionReturn() // ========================= AArch64.ExceptionReturn(bits(64) new_pc_in, bits(64) spsr)
```

```
bits(64) new_pc = new_pc_in; if IsFeatureImplemented(FEAT_IESB) then sync_errors = SCTLR_ELx[].IESB == '1'; if IsFeatureImplemented(FEAT_DoubleFault) then sync_errors = sync_errors || (SCR_EL3.<EA,NMEA> == '11' && PSTATE.EL == EL3); if sync_errors then SynchronizeErrors(); iesb_req = TRUE; TakeUnmaskedPhysicalSErrorInterrupts(iesb_req); boolean brbe_source_allowed = FALSE; bits(64) brbe_source_address = Zeros(64); if IsFeatureImplemented(FEAT_BRBE) then brbe_source_allowed = BranchRecordAllowed(PSTATE.EL); brbe_source_address = PC64; if !IsFeatureImplemented(FEAT_ExS) || SCTLR_ELx[].EOS == '1' then SynchronizeContext(); // Attempts to change to an illegal state will invoke the Illegal Execution state mechanism constant bits(2) source_el = PSTATE.EL; constant boolean illegal_psr_state = IllegalExceptionReturn(spsr); SetPSTATEFromPSR(spsr, illegal_psr_state); ClearExclusiveLocal(ProcessorID()); SendEventLocal(); if illegal_psr_state && spsr<4> == '1' then // If the exception return is illegal, PC[63:32,1:0] are UNKNOWN new_pc<63:32> = bits(32) UNKNOWN; new_pc<1:0> = bits(2) UNKNOWN; elsif UsingAArch32() then // Return to AArch32 // ELR_ELx[1:0] or ELR_ELx[0] are treated as being 0, depending on the // target instruction set state if PSTATE.T == '1' then new_pc<0> = '0'; // T32 else new_pc<1:0> = '00'; // A32 else // Return to AArch64 // ELR_ELx[63:56] might include a tag new_pc = AArch64.BranchAddr(new_pc, PSTATE.EL); if IsFeatureImplemented(FEAT_BRBE) then BRBEExceptionReturn(new_pc, source_el, brbe_source_allowed, brbe_source_address); if UsingAArch32() then if IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' then ResetSVEState(); // 32 most significant bits are ignored. constant boolean branch_conditional = FALSE; BranchTo(new_pc<31:0>, BranchType_ERET, branch_conditional); else BranchToAddr(new_pc, BranchType_ERET); CheckExceptionCatch(FALSE); // Check for debug event on exception return
```

## J1.1.3.37 AArch64.ExclusiveMonitorsPass

```
// AArch64.ExclusiveMonitorsPass() // =============================== // Return TRUE if the Exclusives monitors for the current PE include all of the addresses // associated with the virtual address region of size bytes starting at address. // The immediately following memory write must be to the same addresses.
```

```
// It is IMPLEMENTATION DEFINED whether the detection of memory aborts happens // before or after the check on the local Exclusives monitor. As a result a failure // of the local monitor can occur on some implementations even if the memory // access would give an memory abort. boolean AArch64.ExclusiveMonitorsPass(bits(64) address, integer size, AccessDescriptor accdesc) constant boolean aligned = IsAligned(address, size); if !aligned && AArch64.UnalignedAccessFaults(accdesc, address, size) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault); if !AArch64.IsExclusiveVA(address, ProcessorID(), size) then return FALSE; memaddrdesc = AArch64.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); passed = IsExclusiveLocal(memaddrdesc.paddress, ProcessorID(), size); ClearExclusiveLocal(ProcessorID()); if passed && memaddrdesc.memattrs.shareability != Shareability_NSH then passed = IsExclusiveGlobal(memaddrdesc.paddress, ProcessorID(), size); return passed; J1.1.3.38 AArch64.IsExclusiveVA // AArch64.IsExclusiveVA() // ======================= // An optional IMPLEMENTATION DEFINED test for an exclusive access to a virtual // address region of size bytes starting at address. // // It is permitted (but not required) for this function to return FALSE and // cause a store exclusive to fail if the virtual address region is not // totally included within the region recorded by MarkExclusiveVA(). // // It is always safe to return TRUE which will check the physical address only. boolean AArch64.IsExclusiveVA(bits(64) address, integer processorid, integer size); J1.1.3.39 AArch64.MarkExclusiveVA // AArch64.MarkExclusiveVA() // ========================= // Optionally record an exclusive access to the virtual address region of size bytes // starting at address for processorid. AArch64.MarkExclusiveVA(bits(64) address, integer processorid, integer size); J1.1.3.40 AArch64.SetExclusiveMonitors // AArch64.SetExclusiveMonitors() // ============================== // Sets the Exclusives monitors for the current PE to record the addresses associated // with the virtual address region of size bytes starting at address.
```

```
AArch64.SetExclusiveMonitors(bits(64) address, integer size, AccessDescriptor accdesc) constant boolean aligned = IsAligned(address, size); if !aligned && AArch64.UnalignedAccessFaults(accdesc, address, size) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault); memaddrdesc = AArch64.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then return; if memaddrdesc.memattrs.shareability != Shareability_NSH then MarkExclusiveGlobal(memaddrdesc.paddress, ProcessorID(), size); MarkExclusiveLocal(memaddrdesc.paddress, ProcessorID(), size); AArch64.MarkExclusiveVA(address, ProcessorID(), size);
```

## J1.1.3.41 DecodeRegExtend

```
// DecodeRegExtend() // ================= // Decode a register extension option ExtendType DecodeRegExtend(bits(3) op) case op of when '000' return ExtendType_UXTB; when '001' return ExtendType_UXTH; when '010' return ExtendType_UXTW; when '011' return ExtendType_UXTX; when '100' return ExtendType_SXTB; when '101' return ExtendType_SXTH; when '110' return ExtendType_SXTW; when '111' return ExtendType_SXTX;
```

## J1.1.3.42 ExtendReg

```
// ExtendReg() // =========== // Perform a register extension and shift bits(N) ExtendReg(integer reg, ExtendType exttype, integer shift, integer N) assert shift >= 0 && shift <= 4; constant bits(N) val = X[reg, N]; boolean unsigned; ESize len; case exttype of when ExtendType_SXTB unsigned = FALSE; len = 8; when ExtendType_SXTH unsigned = FALSE; len = 16; when ExtendType_SXTW unsigned = FALSE; len = 32; when ExtendType_SXTX unsigned = FALSE; len = 64; when ExtendType_UXTB unsigned = TRUE; len = 8; when ExtendType_UXTH unsigned = TRUE; len = 16; when ExtendType_UXTW unsigned = TRUE; len = 32; when ExtendType_UXTX unsigned = TRUE; len = 64; // Sign or zero extend bottom LEN bits of register and shift left by SHIFT constant nbits = Min(len, N); constant bits(N) extval = Extend(val<nbits-1:0>, N, unsigned);
```

```
return LSL(extval, shift);
```

## J1.1.3.43 ExtendType

```
// ExtendType // ========== // AArch64 register extend and shift. enumeration ExtendType {ExtendType_SXTB, ExtendType_SXTH, ExtendType_SXTW, ExtendType_SXTX,
```

```
ExtendType_UXTB, ExtendType_UXTH, ExtendType_UXTW, ExtendType_UXTX};
```

```
FPConvOp_CVT_ItoF, FPConvOp_MOV_ItoF,
```

## J1.1.3.44 FPConvOp

```
// FPConvOp // ======== // Floating-point convert/move instruction types. enumeration FPConvOp {FPConvOp_CVT_FtoI, FPConvOp_MOV_FtoI, FPConvOp_CVT_FtoI_JS };
```

## J1.1.3.45 FPMaxMinOp

```
// FPMaxMinOp // ========== // Floating-point min/max instruction types. enumeration FPMaxMinOp {FPMaxMinOp_MAX, FPMaxMinOp_MIN, FPMaxMinOp_MAXNUM, FPMaxMinOp_MINNUM};
```

## J1.1.3.46 CheckFPMREnabled

```
// CheckFPMREnabled() // ================== // Check for Undefined instruction exception on indirect FPMR accesses. CheckFPMREnabled() assert IsFeatureImplemented(FEAT_FPMR); if PSTATE.EL == EL0 then if !IsInHost() then if SCTLR_EL1.EnFPM == '0' then UNDEFINED; else if SCTLR_EL2.EnFPM == '0' then UNDEFINED; if PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !IsInHost() then if !IsHCRXEL2Enabled() || HCRX_EL2.EnFPM == '0' then UNDEFINED; if PSTATE.EL != EL3 && HaveEL(EL3) then if SCR_EL3.EnFPM == '0' then UNDEFINED;
```

## J1.1.3.47 FPScale

```
// FPScale() // ========= bits(N) FPScale(bits(N) op, integer scale, FPCR_Type fpcr) assert N IN {16,32,64}; bits(N) result; (fptype,sign,value) = FPUnpack(op, fpcr); if fptype == FPType_SNaN || fptype == FPType_QNaN then result = FPProcessNaN(fptype, op, fpcr); elsif fptype == FPType_Zero then result = FPZero(sign, N); elsif fptype == FPType_Infinity then result = FPInfinity(sign, N); else result = FPRound(value * (2.0^scale), fpcr, N); FPProcessDenorm(fptype, N, fpcr); return result;
```

## J1.1.3.48 FPUnaryOp

```
// FPUnaryOp // ========= // Floating-point unary instruction types. enumeration FPUnaryOp {FPUnaryOp_ABS, FPUnaryOp_MOV, FPUnaryOp_NEG, FPUnaryOp_SQRT};
```

## J1.1.3.49 FPRSqrtStepFused

```
// FPRSqrtStepFused() // ================== bits(N) FPRSqrtStepFused(bits(N) op1_in, bits(N) op2, FPCR_Type fpcr_in) assert N IN {16, 32, 64}; FPCR_Type fpcr = fpcr_in; bits(N) result; bits(N) op1 = op1_in; boolean done; op1 = FPNeg(op1, fpcr); constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && fpcr.AH == '1'; constant boolean fpexc = !altfp; // Generate no floating-point exceptions if altfp then fpcr.<FIZ,FZ> = '11'; // Flush denormal input and output to zero if altfp then fpcr.RMode = '00'; // Use RNE rounding mode (type1,sign1,value1) = FPUnpack(op1, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2, fpcr, fpexc); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr, fpexc); constant FPRounding rounding = FPRoundingMode(fpcr); if !done then inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if (inf1 && zero2) || (zero1 && inf2) then result = FPOnePointFive('0', N); elsif inf1 || inf2 then result = FPInfinity(sign1 EOR sign2, N); else
```

```
'0';
```

```
// Fully fused multiply-add and halve result_value = (3.0 + (value1 * value2)) / 2.0; if result_value == 0.0 then // Sign of exact zero result depends on rounding mode sign = if rounding == FPRounding_NEGINF then '1' else result = FPZero(sign, N); else result = FPRound(result_value, fpcr, rounding, fpexc, N); return result;
```

## J1.1.3.50 FPRecipStepFused

```
// FPRecipStepFused() // ================== bits(N) FPRecipStepFused(bits(N) op1_in, bits(N) op2, FPCR_Type fpcr_in) assert N IN {16, 32, 64}; FPCR_Type fpcr = fpcr_in; bits(N) op1 = op1_in; bits(N) result; boolean done; op1 = FPNeg(op1, fpcr); constant boolean altfp = IsFeatureImplemented(FEAT_AFP) && fpcr.AH == '1'; constant boolean fpexc = !altfp; // Generate no floating-point exceptions if altfp then fpcr.<FIZ,FZ> = '11'; // Flush denormal input and output to zero if altfp then fpcr.RMode = '00'; // Use RNE rounding mode (type1,sign1,value1) = FPUnpack(op1, fpcr, fpexc); (type2,sign2,value2) = FPUnpack(op2, fpcr, fpexc); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr, fpexc); constant FPRounding rounding = FPRoundingMode(fpcr); if !done then inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); if (inf1 && zero2) || (zero1 && inf2) then result = FPTwo('0', N); elsif inf1 || inf2 then result = FPInfinity(sign1 EOR sign2, N); else // Fully fused multiply-add result_value = 2.0 + (value1 * value2); if result_value == 0.0 then // Sign of exact zero result depends on rounding mode sign = if rounding == FPRounding_NEGINF then '1' else '0'; result = FPZero(sign, N); else result = FPRound(result_value, fpcr, rounding, fpexc, N); return result;
```

## J1.1.3.51 AddGCSExRecord

```
// AddGCSExRecord() // ================ // Generates and then writes an exception record to the // current Guarded control stack.
```

```
AddGCSExRecord(bits(64) elr, bits(64) spsr, bits(64) lr) bits(64) ptr; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGCS(MemOp_STORE, privileged); ptr = GetCurrentGCSPointer(); // Store the record Mem[ptr-8, 8, accdesc] = lr; Mem[ptr-16, 8, accdesc] = spsr; Mem[ptr-24, 8, accdesc] = elr; Mem[ptr-32, 8, accdesc] = Zeros(60):'1001'; // Decrement the pointer value ptr = ptr - 32; SetCurrentGCSPointer(ptr); return;
```

```
J1.1.3.52 AddGCSRecord // AddGCSRecord() // ============== // Generates and then writes a record to the current Guarded // control stack. AddGCSRecord(bits(64) vaddress) bits(64) ptr; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGCS(MemOp_STORE, privileged); ptr = GetCurrentGCSPointer(); // Store the record Mem[ptr-8, 8, accdesc] = vaddress; // Decrement the pointer value ptr = ptr - 8; SetCurrentGCSPointer(ptr); return; J1.1.3.53 CheckGCSExRecord gcsinst_type)
```

```
// CheckGCSExRecord() // ================== // Validates the provided values against the top entry of the // current Guarded control stack. CheckGCSExRecord(bits(64) elr, bits(64) spsr, bits(64) lr, GCSInstruction bits(64) ptr; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGCS(MemOp_LOAD, privileged); ptr = GetCurrentGCSPointer(); // Check the lowest doubleword is correctly formatted constant bits(64) recorded_first_dword = Mem[ptr, 8, accdesc]; if recorded_first_dword != Zeros(60):'1001' then GCSDataCheckException(gcsinst_type); // Check the ELR matches the recorded value constant bits(64) recorded_elr = Mem[ptr+8, 8, accdesc]; if recorded_elr != elr then
```

```
GCSDataCheckException(gcsinst_type); // Check the SPSR matches the recorded value constant bits(64) recorded_spsr = Mem[ptr+16, 8, accdesc]; if recorded_spsr != spsr then GCSDataCheckException(gcsinst_type); // Check the LR matches the recorded value constant bits(64) recorded_lr = Mem[ptr+24, 8, accdesc]; if recorded_lr != lr then GCSDataCheckException(gcsinst_type); // Increment the pointer value ptr = ptr + 32; SetCurrentGCSPointer(ptr); return;
```

## J1.1.3.54 CheckGCSSTREnabled

```
// CheckGCSSTREnabled() // ==================== // Trap GCSSTR or GCSSTTR instruction if trapping is enabled. CheckGCSSTREnabled() case PSTATE.EL of when EL0 if GCSCRE0_EL1.STREn == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then GCSSTRTrapException(EL2); else GCSSTRTrapException(EL1); when EL1 if GCSCR_EL1.STREn == '0' then GCSSTRTrapException(EL1); elsif (EL2Enabled() && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && HFGITR_EL2.nGCSSTR_EL1 == '0') then GCSSTRTrapException(EL2); when EL2 if GCSCR_EL2.STREn == '0' then GCSSTRTrapException(EL2); when EL3 if GCSCR_EL3.STREn == '0' then GCSSTRTrapException(EL3); return;
```

## J1.1.3.55 EXLOCKException

```
// EXLOCKException() // ================= // Handle an EXLOCK exception condition. EXLOCKException() constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = 0x0; except = ExceptionSyndrome(Exception_GCSFail); except.syndrome.iss<24> = '0'; except.syndrome.iss<23:20> = '0001'; except.syndrome.iss<19:0> = Zeros(20); AArch64.TakeException(PSTATE.EL, except, preferred_exception_return, vect_offset);
```

## J1.1.3.56 GCSDataCheckException

```
// GCSDataCheckException() // ======================= // Handle a Guarded Control Stack data check fault condition. GCSDataCheckException(GCSInstruction gcsinst_type) bits(2) target_el; constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = 0x0; boolean rn_unknown = FALSE; boolean is_ret = FALSE; boolean is_reta = FALSE; if PSTATE.EL == EL0 then target_el = if (EL2Enabled() && HCR_EL2.TGE == '1') then EL2 else EL1; else target_el = PSTATE.EL; except = ExceptionSyndrome(Exception_GCSFail); case gcsinst_type of when GCSInstType_PRET except.syndrome.iss<4:0> = '00000'; is_ret = TRUE; when GCSInstType_POPM except.syndrome.iss<4:0> = '00001'; when GCSInstType_PRETAA except.syndrome.iss<4:0> = '00010'; is_reta = TRUE; when GCSInstType_PRETAB except.syndrome.iss<4:0> = '00011'; is_reta = TRUE; when GCSInstType_SS1 except.syndrome.iss<4:0> = '00100'; when GCSInstType_SS2 except.syndrome.iss<4:0> = '00101'; rn_unknown = TRUE; when GCSInstType_POPCX rn_unknown = TRUE; except.syndrome.iss<4:0> = '01000'; when GCSInstType_POPX except.syndrome.iss<4:0> = '01001'; if rn_unknown == TRUE then except.syndrome.iss<9:5> = bits(5) UNKNOWN; elsif is_ret == TRUE then except.syndrome.iss<9:5> = ThisInstr()<9:5>; elsif is_reta == TRUE then except.syndrome.iss<9:5> = '11110'; else except.syndrome.iss<9:5> = ThisInstr()<4:0>; except.syndrome.iss<24:10> = Zeros(15); except.vaddress = bits(64) UNKNOWN; AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.3.57 GCSEnabled

```
// GCSEnabled() // ============ // Returns TRUE if the Guarded control stack is enabled at // the provided Exception level. boolean GCSEnabled(bits(2) el) if UsingAArch32() then return FALSE;
```

```
if HaveEL(EL3) && el != EL3 && SCR_EL3.GCSEn == '0' then return FALSE; if (el IN {EL0, EL1} && (!IsHCRXEL2Enabled() || HCRX_EL2.GCSEn == '0')) then return FALSE; return GCSPCRSelected(el);
```

```
// GCSPOPCX() // ========== // Called to pop and compare a Guarded control stack exception return GCSPOPCX() constant bits(64) spsr = SPSR_ELx[]; CheckGCSExRecord(ELR_ELx[], spsr, X[30,64], GCSInstType_POPCX);
```

```
EL2Enabled() && !ELIsInHost(EL0) && J1.1.3.58 GCSInstruction // GCSInstruction // ============== enumeration GCSInstruction { GCSInstType_PRET, // Procedure return without Pointer authentication GCSInstType_POPM, // GCSPOPM instruction GCSInstType_PRETAA, // Procedure return with Pointer authentication that used key A GCSInstType_PRETAB, // Procedure return with Pointer authentication that used key B GCSInstType_SS1, // GCSSS1 instruction GCSInstType_SS2, // GCSSS2 instruction GCSInstType_POPCX, // GCSPOPCX instruction GCSInstType_POPX // GCSPOPX instruction }; J1.1.3.59 GCSPCREnabled // GCSPCREnabled() // =============== // Returns TRUE if the Guarded control stack is PCR enabled // at the provided Exception level. boolean GCSPCREnabled(bits(2) el) return GCSPCRSelected(el) && GCSEnabled(el); J1.1.3.60 GCSPCRSelected // GCSPCRSelected() // ================ // Returns TRUE if the Guarded control stack is PCR selected // at the provided Exception level. boolean GCSPCRSelected(bits(2) el) case el of when EL0 return GCSCRE0_EL1.PCRSEL == '1'; when EL1 return GCSCR_EL1.PCRSEL == '1'; when EL2 return GCSCR_EL2.PCRSEL == '1'; when EL3 return GCSCR_EL3.PCRSEL == '1'; Unreachable(); return TRUE; J1.1.3.61 GCSPOPCX record.
```

```
PSTATE.EXLOCK = if GetCurrentEXLOCKEN() then '1' else '0'; return;
```

## J1.1.3.62 GCSPOPM

```
// GCSPOPM() // ========= // Called to pop a Guarded control stack procedure return record. bits(64) GCSPOPM() bits(64) ptr; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGCS(MemOp_LOAD, privileged); ptr = GetCurrentGCSPointer(); constant bits(64) gcs_entry = Mem[ptr, 8, accdesc]; if gcs_entry<1:0> != '00' then GCSDataCheckException(GCSInstType_POPM); ptr = ptr + 8; SetCurrentGCSPointer(ptr); return gcs_entry;
```

## J1.1.3.63 GCSPOPX

```
// GCSPOPX() // ========= // Called to pop a Guarded control stack exception return record. GCSPOPX() bits(64) ptr; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGCS(MemOp_LOAD, privileged); ptr = GetCurrentGCSPointer(); // Check the lowest doubleword is correctly formatted constant bits(64) recorded_first_dword = Mem[ptr, 8, accdesc]; if recorded_first_dword != Zeros(60):'1001' then GCSDataCheckException(GCSInstType_POPX); // Ignore these loaded values, however they might have // faulted which is why we load them anyway constant bits(64) recorded_elr = Mem[ptr+8, 8, accdesc]; constant bits(64) recorded_spsr = Mem[ptr+16, 8, accdesc]; constant bits(64) recorded_lr = Mem[ptr+24, 8, accdesc]; // Increment the pointer value ptr = ptr + 32; SetCurrentGCSPointer(ptr); return;
```

## J1.1.3.64 GCSPUSHM

```
// GCSPUSHM() // ========== // Called to push a Guarded control stack procedure return record. GCSPUSHM(bits(64) value) AddGCSRecord(value); return;
```

## J1.1.3.65 GCSPUSHX

```
// GCSPUSHX() // ========== // Called to push a Guarded control stack exception return GCSPUSHX() constant bits(64) spsr = SPSR_ELx[]; AddGCSExRecord(ELR_ELx[], spsr, X[30,64]); PSTATE.EXLOCK = '0'; return;
```

```
record. J1.1.3.66 GCSReturnValueCheckEnabled // GCSReturnValueCheckEnabled() // ============================ // Returns TRUE if the Guarded control stack has return value // checking enabled at the current Exception level. boolean GCSReturnValueCheckEnabled(bits(2) el) if UsingAArch32() then return FALSE; case el of when EL0 return GCSCRE0_EL1.RVCHKEN == '1'; when EL1 return GCSCR_EL1.RVCHKEN == '1'; when EL2 return GCSCR_EL2.RVCHKEN == '1'; when EL3 return GCSCR_EL3.RVCHKEN == '1'; J1.1.3.67 GCSSS1 // GCSSS1() // ======== // Operational pseudocode for GCSSS1 instruction. GCSSS1(bits(64) incoming_pointer) bits(64) outgoing_pointer, cmpoperand, operand, data; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGCSSS1(privileged); outgoing_pointer = GetCurrentGCSPointer(); // Valid cap entry is expected cmpoperand = incoming_pointer<63:12>:'000000000001'; // In-progress cap entry should be stored if the comparison is successful operand = outgoing_pointer<63:3>:'101'; data = MemAtomic(incoming_pointer, cmpoperand, operand, accdesc); if data == cmpoperand then SetCurrentGCSPointer(incoming_pointer<63:3>:'000'); else GCSDataCheckException(GCSInstType_SS1); return; J1.1.3.68 GCSSS2
```

```
// GCSSS2() // ======== // Operational pseudocode for GCSSS2 instruction. bits(64) GCSSS2() bits(64) outgoing_pointer, incoming_pointer, outgoing_value; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc_ld = CreateAccDescGCS(MemOp_LOAD, privileged);
```

```
constant AccessDescriptor accdesc_st = CreateAccDescGCS(MemOp_STORE, privileged); incoming_pointer = GetCurrentGCSPointer(); outgoing_value = Mem[incoming_pointer, 8, accdesc_ld]; if outgoing_value<2:0> == '101' then //in_progress token outgoing_pointer<63:3> = (outgoing_value<63:3>) - 1; outgoing_pointer<2:0> = '000'; outgoing_value = outgoing_pointer<63:12>: '000000000001'; Mem[outgoing_pointer, 8, accdesc_st] = outgoing_value; SetCurrentGCSPointer(incoming_pointer + 8); GCSSynchronizationBarrier(); else GCSDataCheckException(GCSInstType_SS2); return outgoing_pointer;
```

## J1.1.3.69 GCSSTRTrapException

```
// GCSSTRTrapException() // ===================== // Handle a trap on GCSSTR instruction condition. GCSSTRTrapException(bits(2) target_el) constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = 0x0; except = ExceptionSyndrome(Exception_GCSFail); except.syndrome.iss<24> = '0'; except.syndrome.iss<23:20> = '0010'; except.syndrome.iss<19:15> = '00000'; except.syndrome.iss<14:10> = ThisInstr()<9:5>; except.syndrome.iss<9:5> = ThisInstr()<4:0>; except.syndrome.iss<4:0> = '00000'; AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.3.70 GCSSynchronizationBarrier

```
// GCSSynchronizationBarrier() // =========================== // Barrier instruction that synchronizes Guarded Control Stack // accesses in relation to other load and store accesses GCSSynchronizationBarrier();
```

## J1.1.3.71 GetCurrentEXLOCKEN

```
// GetCurrentEXLOCKEN() // ==================== boolean GetCurrentEXLOCKEN() if Halted() || Restarting() then return FALSE; case PSTATE.EL of when EL0 Unreachable(); when EL1 return GCSCR_EL1.EXLOCKEN == '1'; when EL2 return GCSCR_EL2.EXLOCKEN == '1'; when EL3 return GCSCR_EL3.EXLOCKEN == '1';
```

## J1.1.3.72 GetCurrentGCSPointer

```
// GetCurrentGCSPointer() // ====================== // Returns the value of the current Guarded control stack // pointer register. bits(64) GetCurrentGCSPointer() bits(64) ptr; case PSTATE.EL of when EL0 ptr = GCSPR_EL0.PTR:'000'; when EL1 ptr = GCSPR_EL1.PTR:'000'; when EL2 ptr = GCSPR_EL2.PTR:'000'; when EL3 ptr = GCSPR_EL3.PTR:'000'; return ptr;
```

## J1.1.3.73 LoadCheckGCSRecord

```
// LoadCheckGCSRecord() // ==================== // Validates the provided address against the top entry of the // current Guarded control stack. bits(64) LoadCheckGCSRecord(bits(64) vaddress, GCSInstruction gcsinst_type) bits(64) ptr; bits(64) recorded_va; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescGCS(MemOp_LOAD, privileged); ptr = GetCurrentGCSPointer(); recorded_va = Mem[ptr, 8, accdesc]; if GCSReturnValueCheckEnabled(PSTATE.EL) && (recorded_va != vaddress) then GCSDataCheckException(gcsinst_type); return recorded_va;
```

## J1.1.3.74 SetCurrentGCSPointer

```
// SetCurrentGCSPointer() // ====================== // Writes a value to the current Guarded control stack pointer register. SetCurrentGCSPointer(bits(64) ptr) case PSTATE.EL of when EL0 GCSPR_EL0.PTR = ptr<63:3>; when EL1 GCSPR_EL1.PTR = ptr<63:3>; when EL2 GCSPR_EL2.PTR = ptr<63:3>; when EL3 GCSPR_EL3.PTR = ptr<63:3>; return;
```

## J1.1.3.75 HACDBS\_ERR\_REASON\_IPAF

constant bits(2) HACDBS\_ERR\_REASON\_IPAF = '10';

## J1.1.3.76 HACDBS\_ERR\_REASON\_IPHACF

constant bits(2) HACDBS\_ERR\_REASON\_IPHACF = '11';

## J1.1.3.77 HACDBS\_ERR\_REASON\_STRUCTF

constant bits(2) HACDBS\_ERR\_REASON\_STRUCTF = '01';

## J1.1.3.78 IsHACDBSIRQAsserted

```
// IsHACDBSIRQAsserted() // ===================== // Returns TRUE if HACDBSIRQ is asserted, and FALSE otherwise. boolean IsHACDBSIRQAsserted();
```

## J1.1.3.79 ProcessHACDBSEntry

```
// ProcessHACDBSEntry() // ==================== // Process a single entry entry from the HACDBS. ProcessHACDBSEntry() if !IsFeatureImplemented(FEAT_HACDBS) then return; if (HaveEL(EL3) && SCR_EL3.HACDBSEn == '0') || HACDBSBR_EL2.EN == '0' then SetInterruptRequestLevel(InterruptID_HACDBSIRQ, LOW); return; if HCR_EL2.VM == '0' then return; if (UInt(HACDBSCONS_EL2.INDEX) >= (2 ^ (UInt(HACDBSBR_EL2.SZ) + 12)) DIV 8 || HACDBSCONS_EL2.ERR_REASON != '00') then SetInterruptRequestLevel(InterruptID_HACDBSIRQ, HIGH); return; elsif IsHACDBSIRQAsserted() then SetInterruptRequestLevel(InterruptID_HACDBSIRQ, LOW); constant integer hacdbs_size = UInt(HACDBSBR_EL2.SZ); bits(56) baddr = HACDBSBR_EL2.BADDR<43 : 0> : Zeros(12); baddr<11 + hacdbs_size : 12> = Zeros(hacdbs_size); AccessDescriptor accdesc = CreateAccDescHACDBS(); AddressDescriptor addrdesc; addrdesc.paddress.address = baddr + (8 * UInt(HACDBSCONS_EL2.INDEX)); constant bit nse2 = '0'; // NSE2 has the Effective value of 0 within a PE. addrdesc.paddress.paspace = DecodePASpace(nse2, EffectiveSCR_EL3_NSE(), EffectiveSCR_EL3_NS()); // Accesses to the HACDBS use the same memory attributes as used for stage 2 translation walks. addrdesc.memattrs = WalkMemAttrs(VTCR_EL2.SH0, VTCR_EL2.IRGN0, VTCR_EL2.ORGN0); constant bit emec = (if IsFeatureImplemented(FEAT_MEC) && IsSCTLR2EL2Enabled() then SCTLR2_EL2.EMEC else '0'); addrdesc.mecid = AArch64.S2TTWalkMECID(emec, accdesc.ss);
```

```
FaultRecord fault = NoFault(accdesc); if IsFeatureImplemented(FEAT_RME) then fault.gpcf = GranuleProtectionCheck(addrdesc, accdesc); if fault.gpcf.gpf != GPCF_None then HACDBSCONS_EL2.ERR_REASON = HACDBS_ERR_REASON_STRUCTF; return; PhysMemRetStatus memstatus; bits(64) hacdbs_entry; (memstatus, hacdbs_entry) = PhysMemRead(addrdesc, 8, accdesc); if IsFault(memstatus) then HACDBSCONS_EL2.ERR_REASON = HACDBS_ERR_REASON_STRUCTF; return; if BigEndian(accdesc.acctype) then hacdbs_entry = BigEndianReverse(hacdbs_entry); // If the Valid field is clear, do not perform any cleaning operation // and increment HACDBSCONS_EL2.INDEX. if hacdbs_entry<0> == '0' then HACDBSCONS_EL2.INDEX = HACDBSCONS_EL2.INDEX + 1; return; accdesc = CreateAccDescTTEUpdate(accdesc); AddressDescriptor ipa; ipa.paddress.address = hacdbs_entry<55:12> : Zeros(12); constant bit nsipa = hacdbs_entry<11>; constant PASpace paspace = DecodePASpace(nse2, EffectiveSCR_EL3_NSE(), EffectiveSCR_EL3_NS()); ipa.paddress.paspace = (if accdesc.ss == SS_Secure && nsipa == '1' then PAS_NonSecure else paspace); constant boolean s1aarch64 = TRUE; constant S2TTWParams walkparams = AArch64.GetS2TTWParams(accdesc.ss, ipa.paddress.paspace, s1aarch64); AddressDescriptor descpaddr; TTWState walkstate; bits(128) descriptor; if walkparams.d128 == '1' then (fault, descpaddr, walkstate, descriptor) = AArch64.S2Walk(fault, ipa, walkparams, accdesc, 128); else (fault, descpaddr, walkstate, descriptor<63:0>) = AArch64.S2Walk(fault, ipa, walkparams, accdesc, 64); // If the Access flag on the Block or Page descriptor is set to 0, this does not generate // an Access flag fault and the PE can still perform the cleaning operation on that descriptor. if fault.statuscode == Fault_AccessFlag then fault.statuscode = Fault_None; elsif fault.statuscode != Fault_None then HACDBSCONS_EL2.ERR_REASON = HACDBS_ERR_REASON_IPAF; return; constant integer hacdbs_level = SInt(hacdbs_entry<3:1>); if walkstate.level != hacdbs_level || walkstate.contiguous == '1' then HACDBSCONS_EL2.ERR_REASON = HACDBS_ERR_REASON_IPHACF; return; // For the purpose of cleaning HACDBS entries, it is not required that HW update of dirty bit // is enabled for a descriptor to be qualified as writeable-clean or writeable-dirty. // Check if the descriptor is neither writeable-clean nor writeable-dirty.
```

```
if walkparams.s2pie == '1' then constant S2AccessControls perms = AArch64.S2ComputePermissions(walkstate.permissions, walkparams, accdesc); if perms.w == '0' && perms.w_mmu == '0' then HACDBSCONS_EL2.ERR_REASON = HACDBS_ERR_REASON_IPHACF; return; // If DBM is 0, the descriptor is not writeable-clean or writeable-dirty. elsif descriptor<51> == '0' then HACDBSCONS_EL2.ERR_REASON = HACDBS_ERR_REASON_IPHACF; return; // If the descriptor is writeable-clean, do not perform any cleaning // operation and increment HACDBSCONS_EL2.INDEX. if descriptor<7> == '0' then HACDBSCONS_EL2.INDEX = HACDBSCONS_EL2.INDEX + 1; return; bits(128) new_descriptor = descriptor; new_descriptor<7> = '0'; constant AccessDescriptor descaccess = CreateAccDescTTEUpdate(accdesc); if walkparams.d128 == '1' then (fault, -) = descaccess, descpaddr, 128); else (fault, -) = AArch64.MemSwapTableDesc(fault, descriptor<63:0>, new_descriptor<63:0>, walkparams.ee, descaccess, descpaddr, 64); if fault.statuscode != Fault_None then HACDBSCONS_EL2.ERR_REASON = HACDBS_ERR_REASON_IPAF; else HACDBSCONS_EL2.INDEX = HACDBSCONS_EL2.INDEX + 1; return;
```

```
AArch64.MemSwapTableDesc(fault, descriptor, new_descriptor, walkparams.ee, J1.1.3.80 AArch64.CanTrapIC // AArch64.CanTrapIC() // =================== // Determines whether the execution of the IC instruction can be trapped. boolean AArch64.CanTrapIC(CacheType cachetype, CacheOp cacheop, CacheOpScope opscope) return (!AArch64.TreatICAsNOP(cachetype, cacheop, opscope) ||boolean IMPLEMENTATION_DEFINED "When IC is treated as NOP, data cache maintenance operations are trapped"); J1.1.3.81 AArch64.IC // AArch64.IC() // ============ // Perform Instruction Cache Operation. AArch64.IC(CacheOpScope opscope) regval = bits(64) UNKNOWN; AArch64.IC(regval, opscope); // AArch64.IC() // ============ // Perform Instruction Cache Operation. AArch64.IC(bits(64) regval, CacheOpScope opscope) CacheRecord cache;
```

```
cache.acctype = AccessType_IC; cache.cachetype = CacheType_Instruction; cache.cacheop = CacheOp_Invalidate; cache.opscope = opscope; if opscope IN {CacheOpScope_ALLU, CacheOpScope_ALLUIS} then ss = SecurityStateAtEL(PSTATE.EL); cache.cpas = CPASAtSecurityState(ss); case opscope of when CacheOpScope_ALLU cache.shareability = Shareability_NSH; when CacheOpScope_ALLUIS cache.shareability = Shareability_ISH; otherwise Unreachable(); cache.regval = regval; CACHE_OP(cache); else assert opscope == CacheOpScope_PoU; if EL2Enabled() && !IsInHost() then if PSTATE.EL IN {EL0, EL1} then cache.is_vmid_valid = TRUE; cache.vmid = VMID[]; else cache.is_vmid_valid = FALSE; else cache.is_vmid_valid = FALSE; if PSTATE.EL == EL0 then cache.is_asid_valid = TRUE; cache.asid = ASID[]; else cache.is_asid_valid = FALSE; constant bits(64) vaddress = regval; cache.vaddress = regval; constant AccessDescriptor accdesc = CreateAccDescIC(cache); constant boolean aligned = TRUE; constant integer size = 0; AddressDescriptor memaddrdesc = AArch64.TranslateAddress(vaddress, accdesc, aligned, size); if IsFault(memaddrdesc) then memaddrdesc.fault.vaddress = regval; AArch64.Abort(memaddrdesc.fault); cache.cpas = CPASAtPAS(memaddrdesc.paddress.paspace); cache.paddress = memaddrdesc.paddress; cache.shareability = memaddrdesc.memattrs.shareability; if memaddrdesc.memattrs.shareability == Shareability_OSH then cache.shareability = Shareability_ISH; CACHE_OP(cache); return;
```

## J1.1.3.82 AArch64.TreatICAsNOP

```
// AArch64.TreatICAsNOP() // ====================== // Determines whether the execution of the IC instruction is treated as a NOP. boolean AArch64.TreatICAsNOP(CacheType cachetype, CacheOp cacheop, CacheOpScope opscope)
```

```
if CTR_EL0.DIC == '1' then return boolean IMPLEMENTATION_DEFINED "IC is treated as NOP"; return FALSE;
```

## J1.1.3.83 ImmediateOp

```
// ImmediateOp // =========== // Vector logical immediate instruction types. enumeration ImmediateOp {ImmediateOp_MOVI, ImmediateOp_MVNI, ImmediateOp_ORR, ImmediateOp_BIC};
```

## J1.1.3.84 LogicalOp

```
// LogicalOp // ========= // Logical instruction types. enumeration LogicalOp {LogicalOp_AND, LogicalOp_EOR,
```

## J1.1.3.85 AArch64.S1AMECFault

```
// AArch64.S1AMECFault() // ===================== // Returns TRUE if a Translation fault should occur for Realm EL2 and Realm EL2&0 // stage 1 translated addresses to Realm PA space. boolean AArch64.S1AMECFault(S1TTWParams walkparams, PASpace paspace, Regime regime, bits(N) descriptor) assert N IN {64,128}; constant bit descriptor_amec = (if walkparams.d128 == '1' then descriptor<108> else descriptor<63>); return (walkparams.<emec,amec> == '10' && regime IN {Regime_EL2, Regime_EL20} && paspace == PAS_Realm && descriptor_amec == '1');
```

## J1.1.3.86 AArch64.S1DisabledOutputMECID

```
// AArch64.S1DisabledOutputMECID() // =============================== // Returns the output MECID when stage 1 address translation is disabled. bits(16) AArch64.S1DisabledOutputMECID(S1TTWParams walkparams, Regime regime, PASpace paspace) if walkparams.emec == '0' then return DEFAULT_MECID; if ! regime IN {Regime_EL2, Regime_EL20, Regime_EL10} then return DEFAULT_MECID; if paspace != PAS_Realm then return DEFAULT_MECID; if regime == Regime_EL10 then return VMECID_P_EL2.MECID; else return MECID_P0_EL2.MECID;
```

```
LogicalOp_ORR};
```

## J1.1.3.87 AArch64.S1OutputMECID

```
// AArch64.S1OutputMECID() // ======================= // Returns the output MECID when stage 1 address translation is enabled. bits(16) AArch64.S1OutputMECID(S1TTWParams walkparams, Regime regime, VARange varange, PASpace paspace, bits(N) descriptor) assert N IN {64,128}; if walkparams.emec == '0' then return DEFAULT_MECID; if paspace != PAS_Realm then return DEFAULT_MECID; constant bit descriptor_amec = (if walkparams.d128 == '1' then descriptor<108> else descriptor<63>); case regime of when Regime_EL3 return MECID_RL_A_EL3.MECID; when Regime_EL2 if descriptor_amec == '0' then return MECID_P0_EL2.MECID; else return MECID_A0_EL2.MECID; when Regime_EL20 if varange == VARange_LOWER then if descriptor_amec == '0' then return MECID_P0_EL2.MECID; else return MECID_A0_EL2.MECID; else if descriptor_amec == '0' then return MECID_P1_EL2.MECID; else return MECID_A1_EL2.MECID; // Stage 2 translation might later override the MECID according to AMEC configuration. when Regime_EL10 return VMECID_P_EL2.MECID;
```

```
J1.1.3.88 AArch64.S1TTWalkMECID
```

```
// AArch64.S1TTWalkMECID() // ======================= // Returns the associated MECID for the stage 1 translation table walk of the given // translation regime and Security state. bits(16) AArch64.S1TTWalkMECID(bit emec, Regime regime, SecurityState ss) if emec == '0' then return DEFAULT_MECID; if ss != SS_Realm then return DEFAULT_MECID; case regime of when Regime_EL2 return MECID_P0_EL2.MECID; when Regime_EL20 if TCR_EL2.A1 == '0' then return MECID_P1_EL2.MECID; else return MECID_P0_EL2.MECID; // Stage 2 translation for a stage 1 walk might later override the
```

```
// MECID according to AMEC configuration. when Regime_EL10 return VMECID_P_EL2.MECID; otherwise Unreachable();
```

## J1.1.3.89 AArch64.S2OutputMECID

```
// AArch64.S2OutputMECID() // ======================= // Returns the output MECID for stage 2 address translation. bits(16) AArch64.S2OutputMECID(S2TTWParams walkparams, PASpace paspace, bits(N) descriptor) assert N IN {64,128}; if walkparams.emec == '0' then return DEFAULT_MECID; if paspace != PAS_Realm then return DEFAULT_MECID; constant bit descriptor_amec = (if walkparams.d128 == '1' then descriptor<108> else descriptor<63>); if descriptor_amec == '0' then return VMECID_P_EL2.MECID; else return VMECID_A_EL2.MECID;
```

## J1.1.3.90 AArch64.S2TTWalkMECID

```
// AArch64.S2TTWalkMECID() // ======================= // Returns the associated MECID for the stage 2 translation table walk of the // given Security state. bits(16) AArch64.S2TTWalkMECID(bit emec, SecurityState ss) if emec == '0' then return DEFAULT_MECID; if ss != SS_Realm then return DEFAULT_MECID; //Stage 2 translation might later override the MECID according to AMEC configuration return VMECID_P_EL2.MECID;
```

## J1.1.3.91 DEFAULT\_MECID

```
constant bits(16) DEFAULT_MECID = Zeros(16);
```

## J1.1.3.92 AArch64.AccessIsTagChecked

```
// AArch64.AccessIsTagChecked() // ============================ // TRUE if a given access is tag-checked, FALSE otherwise. boolean AArch64.AccessIsTagChecked(bits(64) vaddr, AccessDescriptor accdesc) assert accdesc.tagchecked; if UsingAArch32() then return FALSE;
```

```
if !IsMTEEnabled(accdesc.el) then return FALSE; if PSTATE.TCO == '1' then return FALSE; if (Halted() && EDSCR.MA == '1' && ConstrainUnpredictableBool(Unpredictable_NODTRTAGCHK)) then return FALSE; if StoreOnlyTagCheckingEnabled(accdesc.el)) then return FALSE; constant boolean is_instr = FALSE; if (EffectiveMTX(vaddr, is_instr, PSTATE.EL) == '0' && EffectiveTBI(vaddr, is_instr, PSTATE.EL) == '0') then return FALSE; if (EffectiveTCMA(vaddr, PSTATE.EL) == '1' && (vaddr<59:55> == '00000' || vaddr<59:55> == '11111')) then return FALSE; return TRUE;
```

## (IsFeatureImplemented(FEAT\_MTE\_STORE\_ONLY) &amp;&amp; !accdesc.write &amp;&amp; J1.1.3.93 AArch64.AddressWithAllocationTag // AArch64.AddressWithAllocationTag() // ================================== // Generate a 64-bit value containing a Logical Address Tag from a 64-bit // virtual address and an Allocation Tag. bits(64) AArch64.AddressWithAllocationTag(bits(64) address, bits(4) allocation\_tag) return address&lt;63:60&gt;:allocation\_tag:address&lt;55:0&gt;; J1.1.3.94 AArch64.AllocationTagCheck

```
// AArch64.AllocationTagCheck() // ============================ // Performs an Allocation Tag Check operation for a memory access and // returns whether the check passed. FaultRecord AArch64.AllocationTagCheck(AddressDescriptor memaddrdesc, AccessDescriptor accdesc, bits(4) ltag) FaultRecord fault = NoFault(accdesc, memaddrdesc.vaddress); if memaddrdesc.memattrs.tags == MemTag_AllocationTagged then PhysMemRetStatus memstatus; bits(4) readtag; // Physical tagging needs no further translation, use the data PA to read the tag (memstatus, readtag) = PhysMemTagRead(memaddrdesc, accdesc); if IsFault(memstatus) then constant boolean iswrite = FALSE; return ExternalFault(memstatus, iswrite, memaddrdesc, 1, accdesc); if ltag != readtag then fault.statuscode = Fault_TagCheck; return fault;
```

## J1.1.3.95 AArch64.AllocationTagFromAddress

```
// AArch64.AllocationTagFromAddress() // ================================== // Generate an Allocation Tag from a 64-bit value containing a Logical Address Tag. bits(4) AArch64.AllocationTagFromAddress(bits(64) tagged_address) return tagged_address<59:56>;
```

## J1.1.3.96 AArch64.CanonicalTagCheck

```
// AArch64.CanonicalTagCheck() // =========================== // Performs a Canonical Tag Check operation for a memory access and // returns whether the check passed. boolean AArch64.CanonicalTagCheck(AddressDescriptor memaddrdesc, bits(4) ltag) expected_tag = if memaddrdesc.vaddress<55> == '0' then '0000' else '1111'; return ltag == expected_tag;
```

## J1.1.3.97 AArch64.CheckTag

```
// AArch64.CheckTag() // ================== // Performs a Tag Check operation for a memory access and returns a FaultRecord indicating if // the check passed. If Tag Check Faults are asynchronously accumulated, a Tag Check Fault // exception is recorded in TFSR_ELx. FaultRecord AArch64.CheckTag(AddressDescriptor memaddrdesc_in, AccessDescriptor accdesc, integer size, bits(4) ltag) AddressDescriptor memaddrdesc = memaddrdesc_in; // NoFault() will set fault.write to FALSE to accesses that perform both a read and a write. FaultRecord fault = NoFault(accdesc, memaddrdesc.vaddress); constant integer granules = Max(size DIV TAG_GRANULE, 1); constant boolean forcesync = accdesc.nonfault || (accdesc.firstfault && !accdesc.first); constant TCFType tcf = AArch64.EffectiveTCF(accdesc.el, accdesc.read); for i = 0 to granules - 1 case memaddrdesc.memattrs.tags of when MemTag_AllocationTagged fault = AArch64.AllocationTagCheck(memaddrdesc, accdesc, ltag); if fault.statuscode == Fault_TagCheck then if tcf == TCFType_Sync || forcesync then fault.statuscode = Fault_TagCheck; return fault; elsif tcf == TCFType_Async then AArch64.ReportTagCheckFault(accdesc.el, memaddrdesc.vaddress<55>); fault.statuscode = Fault_None; return fault; else // Tag Check Faults have no effect on the PE. fault.statuscode = Fault_None; elsif fault.statuscode != Fault_None then return fault; when MemTag_CanonicallyTagged if !AArch64.CanonicalTagCheck(memaddrdesc, ltag) then if tcf == TCFType_Sync || forcesync then fault.statuscode = Fault_TagCheck; return fault; elsif tcf == TCFType_Async then AArch64.ReportTagCheckFault(accdesc.el, memaddrdesc.vaddress<55>); return fault; else
```

```
// Tag Check Faults have no effect on the PE. when MemTag_Untagged otherwise Unreachable(); memaddrdesc.paddress.address = memaddrdesc.paddress.address + TAG_GRANULE; memaddrdesc.vaddress = memaddrdesc.vaddress + TAG_GRANULE; return fault;
```

## J1.1.3.98 AArch64.IsUnprivAccessPriv

```
// AArch64.IsUnprivAccessPriv() // ============================ // Returns TRUE if an unprivileged access is privileged, and FALSE otherwise. boolean AArch64.IsUnprivAccessPriv() boolean privileged; case PSTATE.EL of when EL0 privileged = FALSE; when EL1 privileged = EffectiveHCR_EL2_NVx()<1:0> == '11'; when EL2 privileged = !ELIsInHost(EL0); when EL3 privileged = TRUE; if IsFeatureImplemented(FEAT_UAO) && PSTATE.UAO == '1' then privileged = PSTATE.EL != EL0; return privileged;
```

## J1.1.3.99 AArch64.LogicalAddressTag

```
// AArch64.LogicalAddressTag() // =========================== // Extract the Logical Address Tag from an address bits(4) AArch64.LogicalAddressTag(bits(64) vaddr) return vaddr<59:56>;
```

## J1.1.3.100 AArch64.MemSingle

```
// AArch64.MemSingle -non-assignment (read) form // ============================================== // Perform an atomic, little-endian read of 'size' bytes. bits(size*8) AArch64.MemSingle[bits(64) address, integer size, AccessDescriptor accdesc, boolean aligned] bits(size*8) value; AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; (value, memaddrdesc, memstatus) = AArch64.MemSingleRead(address, size, accdesc, aligned); // Check for a fault from translation or the output of translation. if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); // Check for external aborts. if IsFault(memstatus) then
```

```
HandleExternalAbort(memstatus, accdesc.write, memaddrdesc, size, accdesc); return value; // AArch64.MemSingle -assignment (write) form // =========================================== // Perform an atomic, little-endian write of 'size' bytes. AArch64.MemSingle[bits(64) address, integer size, AccessDescriptor accdesc, boolean aligned] = bits(size*8) value AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; (memaddrdesc, memstatus) = AArch64.MemSingleWrite(address, size, accdesc, aligned, value); // Check for a fault from translation or the output of translation. if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); // Check for external aborts. if IsFault(memstatus) then HandleExternalWriteAbort(memstatus, memaddrdesc, size, accdesc); return;
```

## J1.1.3.101 AArch64.MemSingleRead

```
// AArch64.MemSingleRead() // ======================= // Perform an atomic, little-endian read of 'size' bytes. (bits(size*8), AddressDescriptor, PhysMemRetStatus) AArch64.MemSingleRead(bits(64) address, integer size, AccessDescriptor accdesc_in, boolean aligned) assert size IN {1, 2, 4, 8, 16, 32}; bits(size*8) value = bits(size*8) UNKNOWN; PhysMemRetStatus memstatus = PhysMemRetStatus UNKNOWN; memstatus.statuscode = Fault_None; AccessDescriptor accdesc = accdesc_in; if IsFeatureImplemented(FEAT_LSE2) then constant integer quantity = MemSingleGranule(); assert ((IsFeatureImplemented(FEAT_LS64WB) && size == 32 && accdesc.acctype == AccessType_ASIMD) || AllInAlignedQuantity(address, size, quantity)); else assert IsAligned(address, size); // If the instruction encoding permits tag checking, confer with system register configuration // which may override this. if accdesc.tagchecked then accdesc.tagchecked = AArch64.AccessIsTagChecked(address, accdesc); AddressDescriptor memaddrdesc; memaddrdesc = AArch64.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then return (value, memaddrdesc, memstatus); // Memory array access if accdesc.tagchecked then constant bits(4) ltag = AArch64.LogicalAddressTag(address); constant FaultRecord fault = AArch64.CheckTag(memaddrdesc, accdesc, size, ltag); if fault.statuscode != Fault_None then
```

```
memaddrdesc.fault = fault; return (value, memaddrdesc, memstatus); if accdesc.acctype != AccessType_IFETCH && SPESampleInFlight then constant boolean is_load = TRUE; SPESampleLoadStore(is_load, accdesc, memaddrdesc); boolean atomic; if IsWBShareable(memaddrdesc.memattrs) then atomic = TRUE; elsif accdesc.exclusive then atomic = TRUE; elsif (accdesc.acctype == AccessType_SVE && accdesc.predicated && size == 8 && IsAligned(address, 8)) then // An SVE predicated load of a 128-bit element that is 64-bit aligned // is treated as a pair of 64-bit single-copy atomic accesses. // This is one of the 64-bit single-copy atomic access. atomic = TRUE; elsif aligned then atomic = !accdesc.ispair; else // Misaligned accesses within MemSingleGranule() byte aligned memory but // not Normal Cacheable Writeback are Atomic atomic = boolean IMPLEMENTATION_DEFINED "FEAT_LSE2: access is atomic"; if atomic then (memstatus, value) = PhysMemRead(memaddrdesc, size, accdesc); elsif accdesc.acctype == AccessType_ASIMD && size == 32 && accdesc.ispair then // A 32 byte LDP (SIMD&FP) that does not target Normal Inner Write-Back, Outer // Write-Back cacheable, Shareable memory is treated as four 8 byte atomic accesses. // As this access was not split in Mem[], it must be aligned to 32 bytes. assert IsAligned(address, 32); accdesc.ispair = FALSE; for i = 0 to 3 if !IsFault(memstatus) then // Do not continue past a fault (memstatus, value<i*64+:64>) = PhysMemRead(memaddrdesc, 8, accdesc); if !IsFault(memstatus) then memaddrdesc.paddress.address = memaddrdesc.paddress.address + 8; memaddrdesc.vaddress = memaddrdesc.vaddress + 8; elsif aligned && accdesc.ispair then assert size IN {4, 8, 16}; constant integer halfsize = size DIV 2; bits(halfsize * 8) lowhalf, highhalf; (memstatus, lowhalf) = PhysMemRead(memaddrdesc, halfsize, accdesc); if !IsFault(memstatus) then memaddrdesc.paddress.address = memaddrdesc.paddress.address + halfsize; memaddrdesc.vaddress = memaddrdesc.vaddress + halfsize; (memstatus, highhalf) = PhysMemRead(memaddrdesc, halfsize, accdesc); if !IsFault(memstatus) then value = highhalf:lowhalf; else for i = 0 to size-1 if !IsFault(memstatus) then // Do not continue past a fault (memstatus, Elem[value, i, 8]) = PhysMemRead(memaddrdesc, 1, accdesc); if !IsFault(memstatus) then memaddrdesc.paddress.address = memaddrdesc.paddress.address + 1; memaddrdesc.vaddress = memaddrdesc.vaddress + 1; if IsFault(memstatus) then return (value, memaddrdesc, memstatus);
```

```
if accdesc.acctype == AccessType_IFETCH then memaddrdesc.fault = AArch64.CheckDebug(address, accdesc, size); return (value, memaddrdesc, memstatus);
```

## J1.1.3.102 AArch64.MemSingleWrite

```
// AArch64.MemSingleWrite() // ======================== // Perform an atomic, little-endian write of 'size' bytes. (AddressDescriptor, PhysMemRetStatus) AArch64.MemSingleWrite(bits(64) address, integer size, AccessDescriptor accdesc_in, boolean aligned, bits(size*8) value) assert size IN {1, 2, 4, 8, 16, 32}; AccessDescriptor accdesc = accdesc_in; if IsFeatureImplemented(FEAT_LSE2) then constant integer quantity = MemSingleGranule(); assert ((IsFeatureImplemented(FEAT_LS64WB) && size == 32 && accdesc.acctype == AccessType_ASIMD) || AllInAlignedQuantity(address, size, quantity)); else assert IsAligned(address, size); // If the instruction encoding permits tag checking, confer with system register configuration // which may override this. if accdesc.tagchecked then accdesc.tagchecked = AArch64.AccessIsTagChecked(address, accdesc); AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus = PhysMemRetStatus UNKNOWN; memaddrdesc = AArch64.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then return (memaddrdesc, memstatus); // Effect on exclusives if memaddrdesc.memattrs.shareability != Shareability_NSH then ClearExclusiveByAddress(memaddrdesc.paddress, ProcessorID(), size); if accdesc.tagchecked then constant bits(4) ltag = AArch64.LogicalAddressTag(address); constant FaultRecord fault = AArch64.CheckTag(memaddrdesc, accdesc, size, ltag); if fault.statuscode != Fault_None then memaddrdesc.fault = fault; return (memaddrdesc, memstatus); if SPESampleInFlight then constant boolean is_load = FALSE; SPESampleLoadStore(is_load, accdesc, memaddrdesc); boolean atomic; if IsWBShareable(memaddrdesc.memattrs) then atomic = TRUE; elsif accdesc.exclusive then atomic = TRUE; elsif (accdesc.acctype == AccessType_SVE && accdesc.predicated && size == 8 && IsAligned(address, 8)) then // An SVE predicated load of a 128-bit element that is 64-bit aligned // is treated as a pair of 64-bit single-copy atomic accesses. // This is one of the 64-bit single-copy atomic access. atomic = TRUE; elsif aligned then
```

```
atomic = !accdesc.ispair; else // Misaligned accesses within MemSingleGranule() byte aligned memory but // not Normal Cacheable Writeback are Atomic atomic = boolean IMPLEMENTATION_DEFINED "FEAT_LSE2: access is atomic"; if atomic then memstatus = PhysMemWrite(memaddrdesc, size, accdesc, value); if IsFault(memstatus) then return (memaddrdesc, memstatus); elsif accdesc.acctype == AccessType_ASIMD && size == 32 && accdesc.ispair then // A 32 byte STP (SIMD&FP) that does not target Normal Inner Write-Back, Outer // Write-Back cacheable, Shareable memory is treated as four 8 byte atomic accesses. // As this access was not split in Mem[], it must be aligned to 32 bytes. assert IsAligned(address, 32); accdesc.ispair = FALSE; for i = 0 to 3 memstatus = PhysMemWrite(memaddrdesc, 8, accdesc, value<64*i+:64>); if IsFault(memstatus) then return (memaddrdesc, memstatus); memaddrdesc.paddress.address = memaddrdesc.paddress.address + 8; memaddrdesc.vaddress = memaddrdesc.vaddress + 8; elsif aligned && accdesc.ispair then assert size IN {8, 16}; constant integer halfsize = size DIV 2; bits(halfsize*8) lowhalf, highhalf; (highhalf, lowhalf) = (value<halfsize*8+:halfsize*8>, value<0+:halfsize*8>); memstatus = PhysMemWrite(memaddrdesc, halfsize, accdesc, lowhalf); if IsFault(memstatus) then return (memaddrdesc, memstatus); memaddrdesc.paddress.address = memaddrdesc.paddress.address + halfsize; memaddrdesc.vaddress = memaddrdesc.vaddress + halfsize; memstatus = PhysMemWrite(memaddrdesc, halfsize, accdesc, highhalf); if IsFault(memstatus) then return (memaddrdesc, memstatus); else for i = 0 to size-1 memstatus = PhysMemWrite(memaddrdesc, 1, accdesc, Elem[value, i, 8]); if IsFault(memstatus) then return (memaddrdesc, memstatus); memaddrdesc.paddress.address = memaddrdesc.paddress.address + 1; memaddrdesc.vaddress = memaddrdesc.vaddress + 1; return (memaddrdesc, memstatus);
```

## J1.1.3.103 AArch64.MemTag

```
// AArch64.MemTag - non-assignment (read) form // =========================================== // Load an Allocation Tag from memory. bits(4) AArch64.MemTag[bits(64) address, AccessDescriptor accdesc] bits(4) value; AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; (value, memaddrdesc, memstatus) = AArch64.MemTagRead(address, accdesc); if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); if IsFault(memstatus) then
```

```
HandleExternalReadAbort(memstatus, memaddrdesc, 1, accdesc); return value; // AArch64.MemTag - assignment (write) form // ======================================== // Store an Allocation Tag to memory. AArch64.MemTag[bits(64) address, AccessDescriptor accdesc] = bits(4) value AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; (memaddrdesc, memstatus) = if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); if IsFault(memstatus) then HandleExternalWriteAbort(memstatus, memaddrdesc, 1, accdesc); return;
```

## J1.1.3.104 AArch64.MemTagRead

```
// AArch64.MemTagRead() // ==================== // Load an Allocation Tag from memory. (bits(4), AddressDescriptor, PhysMemRetStatus) AArch64.MemTagRead(bits(64) address, AccessDescriptor accdesc_in) assert accdesc_in.tagaccess && !accdesc_in.tagchecked; AccessDescriptor accdesc = accdesc_in; bits(4) tag = bits(4) UNKNOWN; AddressDescriptor memaddrdesc = AddressDescriptor UNKNOWN; MemTagType memtagtype = MemTagType UNKNOWN; PhysMemRetStatus memstatus = PhysMemRetStatus UNKNOWN; constant boolean aligned = TRUE; accdesc.tagaccess = IsMTEEnabled(accdesc.el); (memtagtype, memaddrdesc) = AArch64.TranslateTagAddress(address, accdesc, aligned, TAG_GRANULE); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then return (tag, memaddrdesc, memstatus); if accdesc.tagaccess && memtagtype == MemTag_AllocationTagged then (memstatus, tag) = PhysMemTagRead(memaddrdesc, accdesc); return (tag, memaddrdesc, memstatus); elsif (IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS) && accdesc.tagaccess && memtagtype == MemTag_CanonicallyTagged) then tag = if address<55> == '0' then '0000' else '1111'; return (tag, memaddrdesc, memstatus); else // Otherwise read the tag as zero tag = '0000'; return (tag, memaddrdesc, memstatus);
```

## J1.1.3.105

```
AArch64.MemTagWrite(address, accdesc, value); AArch64.MemTagWrite
```

```
// AArch64.MemTagWrite() // =====================
```

```
// Store an Allocation Tag to memory. (AddressDescriptor, PhysMemRetStatus) AArch64.MemTagWrite(bits(64) address, AccessDescriptor accdesc_in, bits(4) value) assert accdesc_in.tagaccess && !accdesc_in.tagchecked; AccessDescriptor accdesc = accdesc_in; AddressDescriptor memaddrdesc = AddressDescriptor UNKNOWN; MemTagType memtagtype = MemTagType UNKNOWN; PhysMemRetStatus memstatus = PhysMemRetStatus UNKNOWN; constant boolean aligned = IsAligned(address, TAG_GRANULE); // Stores of allocation tags must be aligned if !aligned then memaddrdesc.fault = AlignmentFault(accdesc, address); return (memaddrdesc, memstatus); accdesc.tagaccess = IsMTEEnabled(accdesc.el); (memtagtype, memaddrdesc) = AArch64.TranslateTagAddress(address, accdesc, aligned, TAG_GRANULE); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then memaddrdesc.fault.vaddress = memaddrdesc.vaddress; return (memaddrdesc, memstatus); if accdesc.tagaccess && memtagtype == MemTag_AllocationTagged then memstatus = PhysMemTagWrite(memaddrdesc, accdesc, value); return (memaddrdesc, memstatus);
```

## J1.1.3.106

```
// AArch64.UnalignedAccessFaults() // =============================== // Determine whether the unaligned access generates an Alignment fault boolean AArch64.UnalignedAccessFaults(AccessDescriptor accdesc, bits(64) address, integer if AlignmentEnforced() then return TRUE; elsif accdesc.acctype == AccessType_GCS then return TRUE; elsif accdesc.rcw then return TRUE; elsif accdesc.ls64 then return TRUE; elsif (accdesc.exclusive || accdesc.atomicop) then constant integer quantity = MemSingleGranule(); return (!IsFeatureImplemented(FEAT_LSE2) || !AllInAlignedQuantity(address, size, quantity)); elsif (accdesc.acqsc || accdesc.acqpc || accdesc.relsc) then // If nAA is 0, the address accessed by each register in the pair // must lie within a single 16-byte aligned block if accdesc.ispair then return (SCTLR_ELx[].nAA == '0' && (!AllInAlignedQuantity(address, size DIV 2, 16) || !AllInAlignedQuantity(address + size DIV 2, size DIV 2, 16))); else return (SCTLR_ELx[].nAA == '0' && !AllInAlignedQuantity(address, size, 16)); else return FALSE;
```

```
AArch64.UnalignedAccessFaults size)
```

## J1.1.3.107 AddressSupportsLS64

```
// AddressSupportsLS64() // ===================== // Returns TRUE if the 64-byte block following the given address supports // LD64B and ST64B instructions, and FALSE otherwise. boolean AddressSupportsLS64(bits(56) paddress);
```

```
// CheckSPAlignment() // ================== // Check correct stack pointer alignment for CheckSPAlignment() constant bits(64) sp = SP[64]; boolean stack_align_check; if PSTATE.EL == EL0 then stack_align_check = (SCTLR_ELx[].SA0 != '0'); else stack_align_check = (SCTLR_ELx[].SA != '0'); if stack_align_check && sp != Align(sp, 16) then AArch64.SPAlignmentFault(); return;
```

## the J1.1.3.108 AllInAlignedQuantity // AllInAlignedQuantity() // ====================== // Returns TRUE if all accessed bytes are within one aligned quantity, FALSE otherwise. boolean AllInAlignedQuantity(bits(64) address, integer size, integer alignment) return (Align(address+(size-1), alignment) == Align(address, alignment)); J1.1.3.109 CASCompare // CASCompare() // ============ // Performs a comparison for CAS (bits(N), boolean, bits(N)) CASCompare(bits(N) oldvalue, bits(N) comparevalue, bits(N) newvalue) bits(N) memresult; boolean cmpfail; bits(N) regresult = oldvalue; if oldvalue == comparevalue then cmpfail = FALSE; memresult = newvalue; if !ConstrainUnpredictableBool(Unpredictable\_CASRETURNOLDVALUE) then regresult = comparevalue; else cmpfail = TRUE; memresult = oldvalue; return (memresult, cmpfail, regresult); J1.1.3.110 CheckSPAlignment AArch64 state.

## J1.1.3.111 IsConventionalMemory

```
// IsConventionalMemory() // ====================== // Returns TRUE if the memory location is in Conventional memory, and FALSE otherwise. boolean IsConventionalMemory(AddressDescriptor addrdesc);
```

## J1.1.3.112 Mem

```
// Mem - non-assignment (read) form // ================================ // Perform a read of 'size' bytes. The access byte order is reversed for a big-endian access. // Instruction fetches would call AArch64.MemSingle directly. bits(size*8) Mem[bits(64) address, integer size, AccessDescriptor accdesc_in] assert size IN {1, 2, 4, 8, 16, 32}; AccessDescriptor accdesc = accdesc_in; bits(size * 8) value; // Check alignment on size of element accessed, not overall access size constant integer alignment = (if accdesc.ispair && !accdesc.exclusive then size DIV 2 else size); boolean aligned = IsAligned(address, alignment); constant integer quantity = MemSingleGranule(); if !aligned && AArch64.UnalignedAccessFaults(accdesc, address, size) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault); if accdesc.acctype == AccessType_ASIMD && size == 16 && IsAligned(address, 8) then // If 128-bit SIMD&FP ordered access are treated as a pair of // 64-bit single-copy atomic accesses, then these single copy atomic // access can be observed in any order. constant integer halfsize = size DIV 2; constant bits(64) highaddress = AddressIncrement(address, halfsize, accdesc); bits(halfsize * 8) lowhalf, highhalf; lowhalf = AArch64.MemSingle[address, halfsize, accdesc, aligned]; highhalf = AArch64.MemSingle[highaddress, halfsize, accdesc, aligned]; value = highhalf:lowhalf; elsif (accdesc.acctype == AccessType_ASIMD && size == 32 && accdesc.ispair && IsAligned(address, 32)) then value = AArch64.MemSingle[address, size, accdesc, aligned]; elsif accdesc.acctype == AccessType_ASIMD && size == 32 && IsAligned(address, 8) then // If a 32 byte LDP (SIMD&FP) access is not aligned to 32 bytes but aligned to // 8 bytes, it is treated as four 8 byte single-copy atomic accesses. accdesc.ispair = FALSE; aligned = TRUE; for i = 0 to 3 constant bits(64) blockaddress = AddressIncrement(address, i*8, accdesc); value<64*i+:64> = AArch64.MemSingle[blockaddress, 8, accdesc, aligned]; elsif (IsFeatureImplemented(FEAT_LSE2) && AllInAlignedQuantity(address, size, quantity)) then value = AArch64.MemSingle[address, size, accdesc, aligned]; elsif ((aligned && accdesc.ispair) || (accdesc.acctype == AccessType_SVE && accdesc.predicated && size == 16 && IsAligned(address, 8))) then // Either: an aligned pair access, OR // an SVE predicated load of a 128-bit element that is 64-bit aligned, // which is treated as two 64-bit single-copy atomic accesses. assert size > 1; accdesc.ispair = FALSE; constant integer halfsize = size DIV 2; constant bits(64) highaddress = AddressIncrement(address, halfsize, accdesc); bits(halfsize * 8) lowhalf, highhalf;
```

```
if IsFeatureImplemented(FEAT_LRCPC3) && accdesc.highestaddressfirst then highhalf = AArch64.MemSingle[highaddress, halfsize, accdesc, aligned]; lowhalf = AArch64.MemSingle[address, halfsize, accdesc, aligned]; else lowhalf = AArch64.MemSingle[address, halfsize, accdesc, aligned]; highhalf = AArch64.MemSingle[highaddress, halfsize, accdesc, aligned]; value = highhalf:lowhalf; elsif aligned then value = AArch64.MemSingle[address, size, accdesc, aligned]; else assert size > 1; if IsFeatureImplemented(FEAT_LRCPC3) && accdesc.ispair && accdesc.highestaddressfirst then constant integer halfsize = size DIV 2; bits(halfsize * 8) lowhalf, highhalf; for i = 0 to halfsize-1 constant bits(64) byteaddress = AddressIncrement(address, halfsize + i, accdesc); // Individual byte access can be observed in any order Elem[highhalf, i, 8] = AArch64.MemSingle[byteaddress, 1, accdesc, aligned]; for i = 0 to halfsize-1 constant bits(64) byteaddress = AddressIncrement(address, i, accdesc); // Individual byte access can be observed in any order Elem[lowhalf, i, 8] = AArch64.MemSingle[byteaddress, 1, accdesc, aligned]; value = highhalf:lowhalf; else value<7:0> = AArch64.MemSingle[address, 1, accdesc, aligned]; accdesc.lowestaddress = FALSE; // For subsequent bytes, if they cross to a new translation page which assigns // Device memory type, it is CONSTRAINED UNPREDICTABLE whether an unaligned access // will generate an Alignment Fault. c = ConstrainUnpredictable(Unpredictable_DEVPAGE2); assert c IN {Constraint_FAULT, Constraint_NONE}; if c == Constraint_NONE then aligned = TRUE; for i = 1 to size-1 constant bits(64) byteaddress = AddressIncrement(address, i, accdesc); Elem[value, i, 8] = AArch64.MemSingle[byteaddress, 1, accdesc, aligned]; if BigEndian(accdesc.acctype) then value = BigEndianReverse(value); return value; // Mem - assignment (write) form // ============================= // Perform a write of 'size' bytes. The byte order is reversed for a big-endian access. Mem[bits(64) address, integer size, AccessDescriptor accdesc_in] = bits(size*8) value_in bits(size*8) value = value_in; AccessDescriptor accdesc = accdesc_in; // Check alignment on size of element accessed, not overall access size constant integer alignment = (if accdesc.ispair && !accdesc.exclusive then size DIV 2 else size); boolean aligned = IsAligned(address, alignment); constant integer quantity = MemSingleGranule(); if !aligned && AArch64.UnalignedAccessFaults(accdesc, address, size) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault); if BigEndian(accdesc.acctype) then value = BigEndianReverse(value);
```

```
if accdesc.acctype == AccessType_ASIMD && size == 16 && IsAligned(address, 8) then constant integer halfsize = size DIV 2; bits(halfsize*8) lowhalf, highhalf; // 128-bit SIMD&FP stores are treated as a pair of 64-bit single-copy atomic accesses // 64-bit aligned. (highhalf, lowhalf) = (value<halfsize*8+:halfsize*8>, value<0+:halfsize*8>); constant bits(64) highaddress = AddressIncrement(address, halfsize, accdesc); AArch64.MemSingle[address, halfsize, accdesc, aligned] = lowhalf; AArch64.MemSingle[highaddress, halfsize, accdesc, aligned] = highhalf; elsif (accdesc.acctype == AccessType_ASIMD && size == 32 && accdesc.ispair && IsAligned(address, 32)) then AArch64.MemSingle[address, size, accdesc, aligned] = value; elsif accdesc.acctype == AccessType_ASIMD && size == 32 && IsAligned(address, 8) then // If a 32 byte STP (SIMD&FP) access is not aligned to 32 bytes but aligned to // 8 bytes, it is treated as four 8 byte single-copy atomic accesses. accdesc.ispair = FALSE; aligned = TRUE; for i = 0 to 3 constant bits(64) blockaddress = AddressIncrement(address, i*8, accdesc); AArch64.MemSingle[blockaddress, 8, accdesc, aligned] = value<64*i+:64>; elsif (IsFeatureImplemented(FEAT_LSE2) && AllInAlignedQuantity(address, size, quantity)) then AArch64.MemSingle[address, size, accdesc, aligned] = value; elsif ((aligned && accdesc.ispair) || (accdesc.acctype == AccessType_SVE && accdesc.predicated && size == 16 && IsAligned(address, 8))) then // Either: an aligned pair access, OR // an SVE predicated load of a 128-bit element that is 64-bit aligned, // which is treated as two 64-bit single-copy atomic accesses. assert size > 1; constant integer halfsize = size DIV 2; bits(halfsize*8) lowhalf, highhalf; (highhalf, lowhalf) = (value<halfsize*8+:halfsize*8>, value<0+:halfsize*8>); accdesc.ispair = FALSE; constant bits(64) highaddress = AddressIncrement(address, halfsize, accdesc); if IsFeatureImplemented(FEAT_LRCPC3) && accdesc.highestaddressfirst then AArch64.MemSingle[highaddress, halfsize, accdesc, aligned] = highhalf; AArch64.MemSingle[address, halfsize, accdesc, aligned] = lowhalf; else AArch64.MemSingle[address, halfsize, accdesc, aligned] = lowhalf; AArch64.MemSingle[highaddress, halfsize, accdesc, aligned] = highhalf; elsif aligned then AArch64.MemSingle[address, size, accdesc, aligned] = value; else assert size > 1; if IsFeatureImplemented(FEAT_LRCPC3) && accdesc.ispair && accdesc.highestaddressfirst then constant integer halfsize = size DIV 2; bits(halfsize*8) lowhalf, highhalf; (highhalf, lowhalf) = (value<halfsize*8+:halfsize*8>, value<0+:halfsize*8>); for i = 0 to halfsize-1 constant bits(64) byteaddress = AddressIncrement(address, halfsize + i, accdesc); // Individual byte access can be observed in any order AArch64.MemSingle[byteaddress, 1, accdesc, aligned] = Elem[highhalf, i, 8]; for i = 0 to halfsize-1 constant bits(64) byteaddress = AddressIncrement(address, halfsize + i, accdesc); // Individual byte access can be observed in any order, but implies observability // of highhalf AArch64.MemSingle[byteaddress, 1, accdesc, aligned] = Elem[lowhalf, i, 8]; else AArch64.MemSingle[address, 1, accdesc, aligned] = value<7:0>; accdesc.lowestaddress = FALSE; // For subsequent bytes, if they cross to a new translation page which assigns // Device memory type, it is CONSTRAINED UNPREDICTABLE whether an unaligned access // will generate an Alignment Fault.
```

```
c = ConstrainUnpredictable(Unpredictable_DEVPAGE2); assert c IN {Constraint_FAULT, Constraint_NONE}; if c == Constraint_NONE then aligned = TRUE; for i = 1 to size-1 constant bits(64) byteaddress = AddressIncrement(address, i, accdesc); AArch64.MemSingle[byteaddress, 1, accdesc, aligned] = Elem[value, i, 8]; return;
```

## J1.1.3.113 MemAtomic

```
// MemAtomic() // =========== // Performs load and store memory operations for a given virtual address. bits(size) MemAtomic(bits(64) address, bits(size) cmpoperand, bits(size) operand, AccessDescriptor accdesc_in) assert accdesc_in.atomicop; constant integer bytes = size DIV 8; assert bytes IN {1, 2, 4, 8, 16}; bits(size) newvalue; bits(size) oldvalue; AccessDescriptor accdesc = accdesc_in; constant boolean aligned = IsAligned(address, bytes); // If the instruction encoding permits tag checking, confer with system register configuration // which may override this. if accdesc.tagchecked then accdesc.tagchecked = AArch64.AccessIsTagChecked(address, accdesc); if !aligned && AArch64.UnalignedAccessFaults(accdesc, address, bytes) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault); // MMU or MPU lookup constant AddressDescriptor memaddrdesc = AArch64.TranslateAddress(address, accdesc, aligned, bytes); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); if (!IsWBShareable(memaddrdesc.memattrs) && ConstrainUnpredictableBool(Unpredictable_Atomic_NOP)) then return bits(size) UNKNOWN; // Effect on exclusives if memaddrdesc.memattrs.shareability != Shareability_NSH then ClearExclusiveByAddress(memaddrdesc.paddress, ProcessorID(), bytes); // For Store-only Tag checking, the tag check is performed on the store. if (accdesc.tagchecked && (!IsFeatureImplemented(FEAT_MTE_STORE_ONLY) || !StoreOnlyTagCheckingEnabled(accdesc.el))) then constant bits(4) ltag = AArch64.LogicalAddressTag(address); constant FaultRecord fault = AArch64.CheckTag(memaddrdesc, accdesc, bytes, ltag); if fault.statuscode != Fault_None then AArch64.Abort(fault); // All observers in the shareability domain observe the following load and store atomically. PhysMemRetStatus memstatus; (memstatus, oldvalue) = PhysMemRead(memaddrdesc, bytes, accdesc); // Depending on the memory type of the physical address, the access might generate
```

```
// either a synchronous External abort or an SError exception // among other CONSTRAINED UNPREDICTABLE choices. if IsFault(memstatus) then HandleExternalReadAbort(memstatus, memaddrdesc, bytes, accdesc); if BigEndian(accdesc.acctype) then oldvalue = BigEndianReverse(oldvalue); boolean cmpfail = FALSE; bits(size) retvalue = oldvalue; if accdesc.acctype == AccessType_FP then newvalue = MemAtomicFP(accdesc.modop, oldvalue, operand); else (newvalue, cmpfail, retvalue) = MemAtomicInt(accdesc.modop, oldvalue, operand, cmpoperand); constant boolean requirewrite = (!cmpfail || ConstrainUnpredictableBool(Unpredictable_WRITEFAILEDCAS)); if IsFeatureImplemented(FEAT_MTE_STORE_ONLY) && StoreOnlyTagCheckingEnabled(accdesc.el) then // If the compare on a CAS fails, then it is CONSTRAINED UNPREDICTABLE whether the // Tag check is performed. if accdesc.tagchecked && !requirewrite then accdesc.tagchecked = ConstrainUnpredictableBool(Unpredictable_STRONLYTAGCHECKEDCAS); if accdesc.tagchecked then constant bits(4) ltag = AArch64.LogicalAddressTag(address); FaultRecord fault = AArch64.CheckTag(memaddrdesc, accdesc, bytes, ltag); if fault.statuscode != Fault_None then // For a synchronous Tag Check Fault due to FEAT_MTE_STORE_ONLY, set WnR. fault.write = TRUE; AArch64.Abort(fault); if requirewrite then if BigEndian(accdesc.acctype) then newvalue = BigEndianReverse(newvalue); memstatus = PhysMemWrite(memaddrdesc, bytes, accdesc, newvalue); if IsFault(memstatus) then HandleExternalWriteAbort(memstatus, memaddrdesc, bytes, accdesc); if SPESampleInFlight then constant boolean is_load = FALSE; SPESampleLoadStore(is_load, accdesc, memaddrdesc); // Load operations return the old (pre-operation) value. // Compare and Swap operations return the old (pre-operation) value. For a successful CAS, // this might be the value from the compare operand or from memory. return retvalue;
```

```
J1.1.3.114 MemAtomicFP
```

```
// MemAtomicFP() // ============= // Performs FP Atomic operation bits(N) MemAtomicFP(MemAtomicOp modop, bits(N) op1, bits(N) op2) FPCR_Type fpcr = FPCR; constant boolean altfp = FALSE; constant boolean fpexc = FALSE; fpcr.<AH,DN> = '01'; fpcr.FZ = fpcr.FZ OR fpcr.FIZ; // Treat FPCR.FIZ as equivalent to FPCR.FZ bits(N) result; case modop of when MemAtomicOp_FPADD result = FPAdd(op1, op2, fpcr, fpexc); when MemAtomicOp_FPMAX result = FPMax(op1, op2, fpcr, altfp, fpexc);
```

```
when MemAtomicOp_FPMIN result = FPMin(op1, op2, fpcr, altfp, fpexc); when MemAtomicOp_FPMAXNM result = FPMaxNum(op1, op2, fpcr, fpexc); when MemAtomicOp_FPMINNM result = FPMinNum(op1, op2, fpcr, fpexc); when MemAtomicOp_BFADD result = BFAdd(op1, op2, fpcr, fpexc); when MemAtomicOp_BFMAX result = BFMax(op1, op2, fpcr, altfp, fpexc); when MemAtomicOp_BFMIN result = BFMin(op1, op2, fpcr, altfp, fpexc); when MemAtomicOp_BFMAXNM result = BFMaxNum(op1, op2, fpcr, fpexc); when MemAtomicOp_BFMINNM result = BFMinNum(op1, op2, fpcr, fpexc); return result; J1.1.3.115 MemAtomicInt // MemAtomicInt() // ============== // Performs Integer Atomic operation (bits(N), boolean, bits(N)) MemAtomicInt(MemAtomicOp modop, bits(N) op1, bits(N) op2, bits(N) cmpop) bits(N) result; boolean cmpfail = FALSE; bits(N) retvalue = op1; case modop of when MemAtomicOp_ADD result = op1 + op2; when MemAtomicOp_BIC result = op1 AND NOT(op2); when MemAtomicOp_EOR result = op1 EOR op2; when MemAtomicOp_ORR result = op1 OR op2; when MemAtomicOp_SMAX result = Max(SInt(op1), SInt(op2))<N-1:0>; when MemAtomicOp_SMIN result = Min(SInt(op1), SInt(op2))<N-1:0>; when MemAtomicOp_UMAX result = Max(UInt(op1), UInt(op2))<N-1:0>; when MemAtomicOp_UMIN result = Min(UInt(op1), UInt(op2))<N-1:0>; when MemAtomicOp_SWP result = op2; when MemAtomicOp_CAS (result, cmpfail, retvalue) = CASCompare(op1, cmpop, op2); when MemAtomicOp_GCSSS1 (result, cmpfail, retvalue) = CASCompare(op1, cmpop, op2); return (result, cmpfail, retvalue); J1.1.3.116 MemAtomicRCW // MemAtomicRCW() // ============== // Perform a single-copy-atomic access with Read-Check-Write operation (bits(4), bits(size)) MemAtomicRCW(bits(64) address, bits(size) cmpoperand, bits(size) operand, AccessDescriptor accdesc_in) assert accdesc_in.atomicop; assert accdesc_in.rcw; constant integer bytes = size DIV 8; assert bytes IN {8, 16}; bits(4) nzcv; bits(size) oldvalue; bits(size) newvalue; AccessDescriptor accdesc = accdesc_in; constant boolean aligned = IsAligned(address, bytes); // If the instruction encoding permits tag checking, confer with system register configuration // which may override this. if accdesc.tagchecked then accdesc.tagchecked = AArch64.AccessIsTagChecked(address, accdesc); if !aligned && AArch64.UnalignedAccessFaults(accdesc, address, bytes) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault);
```

```
// MMU or MPU lookup constant AddressDescriptor memaddrdesc = AArch64.TranslateAddress(address, accdesc, aligned, bytes); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); if (!IsWBShareable(memaddrdesc.memattrs) && ConstrainUnpredictableBool(Unpredictable_Atomic_NOP)) then return (bits(4) UNKNOWN, bits(size) UNKNOWN); // Effect on exclusives if memaddrdesc.memattrs.shareability != Shareability_NSH then ClearExclusiveByAddress(memaddrdesc.paddress, ProcessorID(), bytes); // For Store-only Tag checking, the tag check is performed on the store. if (accdesc.tagchecked && (!IsFeatureImplemented(FEAT_MTE_STORE_ONLY) || !StoreOnlyTagCheckingEnabled(accdesc.el))) then constant bits(4) ltag = AArch64.LogicalAddressTag(address); constant FaultRecord fault = AArch64.CheckTag(memaddrdesc, accdesc, bytes, ltag); if fault.statuscode != Fault_None then AArch64.Abort(fault); // All observers in the shareability domain observe the following load and store atomically. PhysMemRetStatus memstatus; (memstatus, oldvalue) = PhysMemRead(memaddrdesc, bytes, accdesc); // Depending on the memory type of the physical address, the access might generate // either a synchronous External abort or an SError exception // among other CONSTRAINED UNPREDICTABLE choices. if IsFault(memstatus) then HandleExternalReadAbort(memstatus, memaddrdesc, bytes, accdesc); if BigEndian(accdesc.acctype) then oldvalue = BigEndianReverse(oldvalue); boolean cmpfail = FALSE; bits(size) retvalue = oldvalue; case accdesc.modop of when MemAtomicOp_BIC newvalue = oldvalue AND NOT(operand); when MemAtomicOp_ORR newvalue = oldvalue OR operand; when MemAtomicOp_SWP newvalue = operand; when MemAtomicOp_CAS (newvalue, cmpfail, retvalue) = CASCompare(oldvalue, cmpoperand, operand); if cmpfail then nzcv = '1010'; // N = 1 indicates compare failure else nzcv = RCWCheck(retvalue, newvalue, accdesc.rcws); // If RCWCheck() passes, it returns nzcv == '0010' constant boolean requirewrite = ((nzcv == '0010') || (accdesc.modop == MemAtomicOp_CAS && ConstrainUnpredictableBool(Unpredictable_WRITEFAILEDCAS))); if IsFeatureImplemented(FEAT_MTE_STORE_ONLY) && StoreOnlyTagCheckingEnabled(accdesc.el) then // If the RCW(S) check fails, or if the compare on a RCW(S)CAS fails, // then it is CONSTRAINED UNPREDICTABLE whether the Tag check is performed. if accdesc.tagchecked && !requirewrite then accdesc.tagchecked = ConstrainUnpredictableBool(Unpredictable_STRONLYTAGCHECKEDRCWSCAS); if accdesc.tagchecked then constant bits(4) ltag = AArch64.LogicalAddressTag(address); FaultRecord fault = AArch64.CheckTag(memaddrdesc, accdesc, bytes, ltag);
```

```
if fault.statuscode != Fault_None then // For a synchronous Tag Check Fault due to FEAT_MTE_STORE_ONLY, set WnR. fault.write = TRUE; AArch64.Abort(fault); if requirewrite then if BigEndian(accdesc.acctype) then newvalue = BigEndianReverse(newvalue); memstatus = PhysMemWrite(memaddrdesc, bytes, accdesc, newvalue); if IsFault(memstatus) then HandleExternalWriteAbort(memstatus, memaddrdesc, bytes, accdesc); if SPESampleInFlight then constant boolean is_load = TRUE; SPESampleLoadStore(is_load, accdesc, memaddrdesc); // Load operations return the old (pre-operation) value. // Compare and Swap operations return the old (pre-operation) value. For a successful CAS, // this might be the value from the compare operand or from memory. return (nzcv, retvalue);
```

```
J1.1.3.117 MemLoad64B // MemLoad64B() // ============ // Performs an atomic 64-byte read from a given virtual address. bits(512) MemLoad64B(bits(64) address, AccessDescriptor accdesc_in) bits(512) data; constant integer size = 64; AccessDescriptor accdesc = accdesc_in; constant boolean aligned = IsAligned(address, size); if !aligned && AArch64.UnalignedAccessFaults(accdesc, address, size) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault); // If the instruction encoding permits tag checking, confer with system register configuration // which may override this. if accdesc.tagchecked then accdesc.tagchecked = AArch64.AccessIsTagChecked(address, accdesc); AddressDescriptor memaddrdesc = AArch64.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); // Effect on exclusives if memaddrdesc.memattrs.shareability != Shareability_NSH then ClearExclusiveByAddress(memaddrdesc.paddress, ProcessorID(), size); if accdesc.tagchecked then constant bits(4) ltag = AArch64.LogicalAddressTag(address); constant FaultRecord fault = AArch64.CheckTag(memaddrdesc, accdesc, size, ltag); if fault.statuscode != Fault_None then AArch64.Abort(fault); boolean byte_atomic = FALSE; if ((memaddrdesc.memattrs.memtype == MemType_Device || (memaddrdesc.memattrs.inner.attrs == MemAttr_NC && memaddrdesc.memattrs.outer.attrs == MemAttr_NC)) && !AddressSupportsLS64(memaddrdesc.paddress.address)) then
```

```
c = ConstrainUnpredictable(Unpredictable_LS64UNSUPPORTED); assert c IN {Constraint_LIMITED_ATOMICITY, Constraint_FAULT}; if c == Constraint_FAULT then // Generate a stage 1 Data Abort reported using the DFSC code of 110101. constant FaultRecord fault = ExclusiveFault(accdesc, address); AArch64.Abort(fault); else byte_atomic = TRUE; elsif IsWBShareable(memaddrdesc.memattrs) && !IsConventionalMemory(memaddrdesc) then if boolean IMPLEMENTATION_DEFINED "LD64B faults to iWBoWB non-Conventional // Generate a Data Abort reported using the DFSC code of 110101. constant FaultRecord fault = ExclusiveFault(accdesc, address); AArch64.Abort(fault); else byte_atomic = TRUE; if SPESampleInFlight then constant boolean is_load = TRUE; SPESampleLoadStore(is_load, accdesc, memaddrdesc); PhysMemRetStatus memstatus; if byte_atomic then // Accesses are not single-copy atomic above the byte level. for i = 0 to size-1 (memstatus, Elem[data, i, 8]) = PhysMemRead(memaddrdesc, 1, accdesc); if IsFault(memstatus) then HandleExternalReadAbort(memstatus, memaddrdesc, 1, accdesc); memaddrdesc.paddress.address = memaddrdesc.paddress.address + 1; memaddrdesc.vaddress = memaddrdesc.vaddress + 1; else (memstatus, data) = PhysMemRead(memaddrdesc, size, accdesc); if IsFault(memstatus) then HandleExternalReadAbort(memstatus, memaddrdesc, size, accdesc); return data;
```

```
memory" then J1.1.3.118 MemSingleGranule // MemSingleGranule() // ================== // When FEAT_LSE2 is implemented, for some memory accesses if all bytes // of the accesses are within 16-byte quantity aligned to 16-bytes and // satisfy additional requirements - then the access is guaranteed to // be single copy atomic. // However, when the accesses do not all lie within such a boundary, it // is CONSTRAINED UNPREDICTABLE if the access is single copy atomic. // In the pseudocode, this CONSTRAINED UNPREDICTABLE aspect is modeled via // MemSingleGranule() which is IMPLEMENTATION DEFINED and, is at least 16 bytes // and at most 4096 bytes. // This is a limitation of the pseudocode. integer MemSingleGranule() size = integer IMPLEMENTATION_DEFINED "Aligned quantity for atomic access"; // access is assumed to be within 4096 byte aligned quantity to // avoid multiple translations for a single copy atomic access. assert (size >= 16) && (size <= 4096); return size; J1.1.3.119 MemStore64B // MemStore64B() // ============= // Performs an atomic 64-byte store to a given virtual address. Function does
```

```
// not return the status of the store. MemStore64B(bits(64) address, bits(512) value, AccessDescriptor accdesc_in) constant integer size = 64; AccessDescriptor accdesc = accdesc_in; constant boolean aligned = IsAligned(address, size); if !aligned && AArch64.UnalignedAccessFaults(accdesc, address, size) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault); // If the instruction encoding permits tag checking, confer with system register configuration // which may override this. if accdesc.tagchecked then accdesc.tagchecked = AArch64.AccessIsTagChecked(address, accdesc); AddressDescriptor memaddrdesc = AArch64.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); // Effect on exclusives if memaddrdesc.memattrs.shareability != Shareability_NSH then ClearExclusiveByAddress(memaddrdesc.paddress, ProcessorID(), 64); if accdesc.tagchecked then constant bits(4) ltag = AArch64.LogicalAddressTag(address); constant FaultRecord fault = AArch64.CheckTag(memaddrdesc, accdesc, size, ltag); if fault.statuscode != Fault_None then AArch64.Abort(fault); boolean byte_atomic = FALSE; if ((memaddrdesc.memattrs.memtype == MemType_Device || (memaddrdesc.memattrs.inner.attrs == MemAttr_NC && memaddrdesc.memattrs.outer.attrs == MemAttr_NC)) && !AddressSupportsLS64(memaddrdesc.paddress.address)) then c = ConstrainUnpredictable(Unpredictable_LS64UNSUPPORTED); assert c IN {Constraint_LIMITED_ATOMICITY, Constraint_FAULT}; if c == Constraint_FAULT then // Generate a Data Abort reported using the DFSC code of 110101. constant FaultRecord fault = ExclusiveFault(accdesc, address); AArch64.Abort(fault); else byte_atomic = TRUE; elsif IsWBShareable(memaddrdesc.memattrs) && !IsConventionalMemory(memaddrdesc) then if boolean IMPLEMENTATION_DEFINED "ST64B faults to iWBoWB non-Conventional memory" then // Generate a Data Abort reported using the DFSC code of 110101. constant FaultRecord fault = ExclusiveFault(accdesc, address); AArch64.Abort(fault); else byte_atomic = TRUE; if SPESampleInFlight then constant boolean is_load = FALSE; SPESampleLoadStore(is_load, accdesc, memaddrdesc); PhysMemRetStatus memstatus; if byte_atomic then // Accesses are not single-copy atomic above the byte level. for i = 0 to size-1 memstatus = PhysMemWrite(memaddrdesc, 1, accdesc, Elem[value, i, 8]); if IsFault(memstatus) then HandleExternalWriteAbort(memstatus, memaddrdesc, 1, accdesc); memaddrdesc.paddress.address = memaddrdesc.paddress.address + 1; memaddrdesc.vaddress = memaddrdesc.vaddress + 1;
```

```
else memstatus = PhysMemWrite(memaddrdesc, size, accdesc, value); if IsFault(memstatus) then HandleExternalWriteAbort(memstatus, memaddrdesc, size, accdesc); return;
```

## J1.1.3.120 MemStore64BWithRet

```
// MemStore64BWithRet() // ==================== // Performs an atomic 64-byte store to a given virtual address returning // the status value of the operation. bits(64) MemStore64BWithRet(bits(64) address, bits(512) value, AccessDescriptor accdesc_in) constant integer size = 64; AccessDescriptor accdesc = accdesc_in; constant boolean aligned = IsAligned(address, size); if !aligned && AArch64.UnalignedAccessFaults(accdesc, address, size) then constant FaultRecord fault = AlignmentFault(accdesc, address); AArch64.Abort(fault); // If the instruction encoding permits tag checking, confer with system register configuration // which may override this. if accdesc.tagchecked then accdesc.tagchecked = AArch64.AccessIsTagChecked(address, accdesc); constant AddressDescriptor memaddrdesc = AArch64.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then AArch64.Abort(memaddrdesc.fault); // Effect on exclusives if memaddrdesc.memattrs.shareability != Shareability_NSH then ClearExclusiveByAddress(memaddrdesc.paddress, ProcessorID(), 64); if accdesc.tagchecked then constant bits(4) ltag = AArch64.LogicalAddressTag(address); constant FaultRecord fault = AArch64.CheckTag(memaddrdesc, accdesc, size, ltag); if fault.statuscode != Fault_None then AArch64.Abort(fault); PhysMemRetStatus memstatus; memstatus = PhysMemWrite(memaddrdesc, size, accdesc, value); // If an access generated by ST64BV or ST64BV0 fails solely because the memory location // does not support 64-byte access, then memstatus does not indicate a fault, if IsFault(memstatus) then HandleExternalWriteAbort(memstatus, memaddrdesc, size, accdesc); if SPESampleInFlight then constant boolean is_load = FALSE; SPESampleLoadStore(is_load, accdesc, memaddrdesc); return memstatus.store64bstatus;
```

## J1.1.3.121 MemStore64BWithRetStatus

```
// MemStore64BWithRetStatus() // ==========================
```

```
// Generates the return status of memory write with ST64BV or ST64BV0 // instructions. The status indicates if the operation succeeded, // or was not supported at this memory location. bits(64) MemStore64BWithRetStatus();
```

```
failed, J1.1.3.122 NVMem
```

```
// NVMem -getter // ============== // This function is the load memory access for the transformed System register read access // when Enhanced Nested Virtualization is enabled with HCR_EL2.NV2 = 1. // The address for the load memory access is calculated using // the formula SignExtend(VNCR_EL2.BADDR : Offset<11:0>, 64) where, // * VNCR_EL2.BADDR holds the base address of the memory location, and // * Offset is the unique offset value defined architecturally for each System register that // supports transformation of register access to memory access. bits(64) NVMem[integer offset] assert offset > 0 && offset MOD 8 == 0; constant boolean directread = FALSE; constant bits(64) baddr = EffectiveBADDR(VNCR_EL2.BADDR : Zeros(12), directread); constant bits(64) address = baddr + offset; constant AccessDescriptor accdesc = CreateAccDescNV2(MemOp_LOAD); return Mem[address, 8, accdesc]; bits(128) NVMem128[integer offset] assert offset > 0 && offset MOD 16 == 0; constant boolean directread = FALSE; constant bits(64) baddr = EffectiveBADDR(VNCR_EL2.BADDR : Zeros(12), directread); constant bits(64) address = baddr + offset; constant AccessDescriptor accdesc = CreateAccDescNV2(MemOp_LOAD); return Mem[address, 16, accdesc]; // NVMem -setter // ============== // This function is the store memory access for the transformed System register write access // when Enhanced Nested Virtualization is enabled with HCR_EL2.NV2 = 1. // The address for the store memory access is calculated using // the formula SignExtend(VNCR_EL2.BADDR : Offset<11:0>, 64) where, // * VNCR_EL2.BADDR holds the base address of the memory location, and // * Offset is the unique offset value defined architecturally for each System register that // supports transformation of register access to memory access. NVMem[integer offset] = bits(64) value assert offset > 0 && offset MOD 8 == 0; constant boolean directread = FALSE; constant bits(64) baddr = EffectiveBADDR(VNCR_EL2.BADDR : Zeros(12), directread); constant bits(64) address = baddr + offset; constant AccessDescriptor accdesc = CreateAccDescNV2(MemOp_STORE); Mem[address, 8, accdesc] = value; return; NVMem128[integer offset] = bits(128) value assert offset > 0 && offset MOD 16 == 0; constant boolean directread = FALSE; constant bits(64) baddr = EffectiveBADDR(VNCR_EL2.BADDR : Zeros(12), directread); constant bits(64) address = baddr + offset; constant AccessDescriptor accdesc = CreateAccDescNV2(MemOp_STORE); Mem[address, 16, accdesc] = value; return;
```

## J1.1.3.123 PhysMemTagRead

```
// PhysMemTagRead() // ================ // This is the hardware operation which perform a single-copy atomic, // Allocation Tag granule aligned, memory access from the tag in PA space. // // The function address the array using desc.paddress which supplies: // * A 52-bit physical address // * A single NS bit to select between Secure and Non-secure parts of the array. // // The accdesc descriptor describes the access type: normal, exclusive, ordered, streaming, // etc and other parameters required to access the physical memory or for setting syndrome // register in the event of an External abort. (PhysMemRetStatus, bits(4)) PhysMemTagRead(AddressDescriptor desc, AccessDescriptor accdesc);
```

## J1.1.3.124 PhysMemTagWrite

```
// PhysMemTagWrite() // ================= // This is the hardware operation which perform a single-copy atomic, // Allocation Tag granule aligned, memory access to the tag in PA space. // // The function address the array using desc.paddress which supplies: // * A 52-bit physical address // * A single NS bit to select between Secure and Non-secure parts of the array. // // The accdesc descriptor describes the access type: normal, exclusive, ordered, streaming, // etc and other parameters required to access the physical memory or for setting syndrome // register in the event of an External abort. PhysMemRetStatus PhysMemTagWrite(AddressDescriptor desc, AccessDescriptor accdesc, bits (4) value);
```

## J1.1.3.125 StoreOnlyTagCheckingEnabled

```
// StoreOnlyTagCheckingEnabled() // ============================= // Returns TRUE if loads executed at the given Exception level are Tag unchecked. boolean StoreOnlyTagCheckingEnabled(bits(2) el) assert IsFeatureImplemented(FEAT_MTE_STORE_ONLY); bit tcso; case el of when EL0 if !ELIsInHost(el) then tcso = SCTLR_EL1.TCSO0; else tcso = SCTLR_EL2.TCSO0; when EL1 tcso = SCTLR_EL1.TCSO; when EL2 tcso = SCTLR_EL2.TCSO; otherwise tcso = SCTLR_EL3.TCSO; return tcso == '1';
```

## J1.1.3.126 ArchMaxMOPSBlockSize

```
// ArchMaxMOPSBlockSize // ==================== // Maximum number of bytes CPY/SET instructions can use constant integer ArchMaxMOPSBlockSize = 0x7FFF_FFFF_FFFF_FFFF;
```

## J1.1.3.127 ArchMaxMOPSCPYSize

```
// ArchMaxMOPSCPYSize // ================== // Maximum number of bytes CPY instructions can use constant integer ArchMaxMOPSCPYSize = 0x007F_FFFF_FFFF_FFFF;
```

## J1.1.3.128 ArchMaxMOPSSETGSize

```
// ArchMaxMOPSSETGSize // =================== // Maximum number of bytes SETG instructions can use constant integer ArchMaxMOPSSETGSize = 0x7FFF_FFFF_FFFF_FFF0;
```

## J1.1.3.129 CPYFOptionA

```
// CPYFOptionA() // ============= // Returns TRUE if the implementation uses Option A for the // CPYF* instructions, and FALSE otherwise. boolean CPYFOptionA() return boolean IMPLEMENTATION_DEFINED "CPYF* instructions use Option A";
```

## J1.1.3.130 CPYOptionA

```
// CPYOptionA() // ============ // Returns TRUE if the implementation uses Option A for the // CPY* instructions, and FALSE otherwise. boolean CPYOptionA() return boolean IMPLEMENTATION_DEFINED "CPY* instructions use Option A";
```

## J1.1.3.131 CPYParams

```
// CPYParams // ========= type CPYParams is ( MOPSStage stage, boolean implements_option_a, boolean forward, integer cpysize, integer stagecpysize, bits(64) toaddress, bits(64) fromaddress, bits(4) nzcv,
```

## integer n, integer d, integer s ) J1.1.3.132 CPYPostSizeChoice // CPYPostSizeChoice() // =================== // Returns the size of the copy that is performed by the CPYE* instructions for this // implementation given the parameters of the destination, source and size of the copy. integer CPYPostSizeChoice(CPYParams memcpy); J1.1.3.133 CPYPreSizeChoice // CPYPreSizeChoice() // ================== // Returns the size of the copy that is performed by the CPYP* instructions for this // implementation given the parameters of the destination, source and size of the copy. integer CPYPreSizeChoice(CPYParams memcpy); J1.1.3.134 CPYSizeChoice // CPYSizeChoice() // =============== // Returns the size of the block this performed for an iteration of the copy given the // parameters of the destination, source and size of the copy. MOPSBlockSize CPYSizeChoice(CPYParams memcpy); J1.1.3.135 CheckCPYConstrainedUnpredictable

```
// CheckCPYConstrainedUnpredictable() // ================================== // Check for CONSTRAINED UNPREDICTABLE behaviour in the CPY* and CPYF* instructions. CheckCPYConstrainedUnpredictable(integer n, integer d, integer s) if (s == n || s == d || n == d) then constant Constraint c = ConstrainUnpredictable(Unpredictable_MOPSOVERLAP); assert c IN {Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNDEF UNDEFINED; when Constraint_NOP ExecuteAsNOP(); if (d == 31 || s == 31 || n == 31) then constant Constraint c = ConstrainUnpredictable(Unpredictable_MOPS_R31); assert c IN {Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNDEF UNDEFINED; when Constraint_NOP ExecuteAsNOP();
```

## J1.1.3.136 CheckMOPSEnabled

```
// CheckMOPSEnabled() // ================== // Check for EL0 and EL1 access to the CPY* and SET* instructions. CheckMOPSEnabled() if (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !ELIsInHost(EL0) && (!IsHCRXEL2Enabled() || HCRX_EL2.MSCEn == '0')) then UNDEFINED; if PSTATE.EL == EL0 && !IsInHost() && SCTLR_EL1.MSCEn == '0' then UNDEFINED; if PSTATE.EL == EL0 && IsInHost() && SCTLR_EL2.MSCEn == '0' then UNDEFINED;
```

## J1.1.3.137 CheckMemCpyParams

```
// CheckMemCpyParams() // =================== // Check if the parameters to a CPY* or CPYF* instruction are consistent with the // PE state and well-formed. CheckMemCpyParams(CPYParams memcpy, bits(4) options) constant boolean from_epilogue = memcpy.stage == MOPSStage_Epilogue; // Check if this version is consistent with the state of the call. if ((memcpy.stagecpysize != 0 || MemStageCpyZeroSizeCheck()) && (memcpy.cpysize != 0 || MemCpyZeroSizeCheck())) then constant boolean using_option_a = memcpy.nzcv<1> == '0'; if memcpy.implements_option_a != using_option_a then constant bits(2) formatoption = '1': (if memcpy.implements_option_a then '1' else '0'); MismatchedMemCpyException(memcpy, options, formatoption); // Check if the parameters to this instruction are valid. if memcpy.stage == MOPSStage_Main then if MemCpyParametersIllformedM(memcpy) then constant bits(2) formatoption = '0': (if memcpy.implements_option_a then '1' else '0'); MismatchedMemCpyException(memcpy, options, formatoption); else constant integer postsize = CPYPostSizeChoice(memcpy); if memcpy.cpysize != postsize || MemCpyParametersIllformedE(memcpy) then constant bits(2) formatoption = '0': (if memcpy.implements_option_a then '1' else '0'); MismatchedMemCpyException(memcpy, options, formatoption); return;
```

## J1.1.3.138 CheckMemSetParams

```
// CheckMemSetParams() // =================== // Check if the parameters to a SET* or SETG* instruction are consistent with the // PE state and well-formed. CheckMemSetParams(SETParams memset, bits(2) options) constant boolean from_epilogue = memset.stage == MOPSStage_Epilogue; // Check if this version is consistent with the state of the call. if ((memset.stagesetsize != 0 || MemStageSetZeroSizeCheck()) && (memset.setsize != 0 || MemSetZeroSizeCheck())) then constant boolean using_option_a = memset.nzcv<1> == '0'; if memset.implements_option_a != using_option_a then
```

```
constant bits(2) formatoption = '1': (if memset.implements_option_a then '1' else '0'); MismatchedMemSetException(memset, options, formatoption); // Check if the parameters to this instruction are valid. if memset.stage == MOPSStage_Main then if MemSetParametersIllformedM(memset) then constant bits(2) formatoption = '0': (if memset.implements_option_a then '1' else '0'); MismatchedMemSetException(memset, options, formatoption); else constant integer postsize = SETPostSizeChoice(memset); if memset.setsize != postsize || MemSetParametersIllformedE(memset) then constant bits(2) formatoption = '0': (if memset.implements_option_a then '1' else '0'); MismatchedMemSetException(memset, options, formatoption); return;
```

## J1.1.3.139 CheckSETConstrainedUnpredictable

```
// CheckSETConstrainedUnpredictable() // ================================== // Check for CONSTRAINED UNPREDICTABLE behaviour in the SET* and SETG* instructions. CheckSETConstrainedUnpredictable(integer n, integer d, integer s) if (s == n || s == d || n == d) then constant Constraint c = ConstrainUnpredictable(Unpredictable_MOPSOVERLAP); assert c IN {Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNDEF UNDEFINED; when Constraint_NOP ExecuteAsNOP(); if (d == 31 || n == 31) then constant Constraint c = ConstrainUnpredictable(Unpredictable_MOPS_R31); assert c IN {Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNDEF UNDEFINED; when Constraint_NOP ExecuteAsNOP();
```

## J1.1.3.140 IsMemCpyForward

```
// IsMemCpyForward() // ================= // Returns TRUE if in a memcpy of size cpysize bytes from the source address fromaddress // to destination address toaddress is done in the forward direction on this implementation. boolean IsMemCpyForward(CPYParams memcpy) boolean forward; // Check for overlapping cases if ((UInt(memcpy.fromaddress<55:0>) > UInt(memcpy.toaddress<55:0>)) && (UInt(memcpy.fromaddress<55:0>) < UInt(ZeroExtend(memcpy.toaddress<55:0>, 64) + memcpy.cpysize))) then forward = TRUE; elsif ((UInt(memcpy.fromaddress<55:0>) < UInt(memcpy.toaddress<55:0>)) && (UInt(ZeroExtend(memcpy.fromaddress<55:0>, 64) + memcpy.cpysize) > UInt(memcpy.toaddress<55:0>))) then forward = FALSE; // Non-overlapping case else forward = boolean IMPLEMENTATION_DEFINED "CPY in the forward direction"; return forward;
```

## J1.1.3.141 MOPSBlockSize

```
// MOPSBlockSize // ================ type MOPSBlockSize = integer;
```

## J1.1.3.142 MOPSStage

```
// MOPSStage // ========= enumeration MOPSStage { MOPSStage_Prologue, MOPSStage_Main, MOPSStage_Epilogue };
```

## J1.1.3.143 MaxBlockSizeCopiedBytes

```
// MaxBlockSizeCopiedBytes() // ========================= // Returns the maximum number of bytes that can used in a single block of the copy. integer MaxBlockSizeCopiedBytes() return integer IMPLEMENTATION_DEFINED "Maximum bytes used in a single block of a copy";
```

## J1.1.3.144 MemCpyBytes

```
// MemCpyBytes() // ============= // Copies 'bytes' bytes of memory from fromaddress to toaddress. // The integer return parameter indicates the number of bytes copied. The boolean return parameter // indicates if a Fault or Abort occurred on the write. The AddressDescriptor and PhysMemRetStatus // parameters contain Fault or Abort information for the caller to handle. (integer, boolean, AddressDescriptor, PhysMemRetStatus) MemCpyBytes(bits(64) toaddress, bits(64) fromaddress, boolean forward, MOPSBlockSize bytes, AccessDescriptor raccdesc, AccessDescriptor waccdesc) AddressDescriptor rmemaddrdesc; // AddressDescriptor for reads PhysMemRetStatus rmemstatus; // PhysMemRetStatus for writes rmemaddrdesc.fault = NoFault(); rmemstatus.statuscode = Fault_None; AddressDescriptor wmemaddrdesc; // AddressDescriptor for writes PhysMemRetStatus wmemstatus; // PhysMemRetStatus for writes wmemaddrdesc.fault = NoFault(); wmemstatus.statuscode = Fault_None; bits(8*bytes) value; constant boolean aligned = TRUE; if forward then integer read = 0; // Bytes read integer write = 0; // Bytes written // Read until all bytes are read or until a fault is encountered. while read < bytes && !IsFault(rmemaddrdesc) && !IsFault(rmemstatus) do (value<8 * read +:8>, rmemaddrdesc, rmemstatus) = AArch64.MemSingleRead( fromaddress + read, 1, raccdesc, aligned); read = read + 1;
```

```
// Ensure no UNKNOWN data is written. if IsFault(rmemaddrdesc) || IsFault(rmemstatus) then read = read - 1; // Write all bytes that were read or until a fault is encountered. while write < read && !IsFault(wmemaddrdesc) && !IsFault(wmemstatus) do (wmemaddrdesc, wmemstatus) = AArch64.MemSingleWrite(toaddress + write, 1, waccdesc, aligned, value<8 * write +:8>); write = write + 1; // Check all bytes were written. if IsFault(wmemaddrdesc) || IsFault(wmemstatus) then constant boolean fault_on_write = TRUE; return (write - 1, fault_on_write, wmemaddrdesc, wmemstatus); // Check all bytes were read. if IsFault(rmemaddrdesc) || IsFault(rmemstatus) then constant boolean fault_on_write = FALSE; return (read, fault_on_write, rmemaddrdesc, rmemstatus); else integer read = bytes; // Bytes to read integer write = bytes; // Bytes to write // Read until all bytes are read or until a fault is encountered. while read > 0 && !IsFault(rmemaddrdesc) && !IsFault(rmemstatus) do read = read - 1; (value<8 * read +:8>, rmemaddrdesc, rmemstatus) = AArch64.MemSingleRead( fromaddress + read, 1, raccdesc, aligned); // Ensure no UNKNOWN data is written. if IsFault(rmemaddrdesc) || IsFault(rmemstatus) then read = read + 1; // Write all bytes that were read or until a fault is encountered. while write > read && !IsFault(wmemaddrdesc) && !IsFault(wmemstatus) do write = write - 1; (wmemaddrdesc, wmemstatus) = AArch64.MemSingleWrite(toaddress + write, 1, waccdesc, aligned, value<8 * write +:8>); // Check all bytes were written. if IsFault(wmemaddrdesc) || IsFault(wmemstatus) then constant boolean fault_on_write = TRUE; return (bytes - (write + 1), fault_on_write, wmemaddrdesc, wmemstatus); // Check all bytes were read. if IsFault(rmemaddrdesc) || IsFault(rmemstatus) then constant boolean fault_on_write = FALSE; return (bytes -read, fault_on_write, rmemaddrdesc, rmemstatus); // Return any AddressDescriptor and PhysMemRetStatus. return (bytes, FALSE, wmemaddrdesc, wmemstatus);
```

## J1.1.3.145 MemCpyParametersIllformedE

```
// MemCpyParametersIllformedE() // ============================ // Returns TRUE if the inputs are not well formed (in terms of their size and/or alignment) // for a CPYE* instruction for this implementation given the parameters of the destination, // source and size of the copy.
```

boolean MemCpyParametersIllformedE(CPYParams memcpy);

## J1.1.3.146 MemCpyParametersIllformedM

```
// MemCpyParametersIllformedM() // ============================ // Returns TRUE if the inputs are not well formed (in terms of their size and/or alignment) // for a CPYM* instruction for this implementation given the parameters of the destination, // source and size of the copy. boolean MemCpyParametersIllformedM(CPYParams memcpy);
```

## J1.1.3.147 MemCpyStageSize

```
// MemCpyStageSize() // ================= // Returns the number of bytes copied by the given stage of a CPY* or CPYF* instruction. integer MemCpyStageSize(CPYParams memcpy) integer stagecpysize; if memcpy.stage == MOPSStage_Prologue then // IMP DEF selection of the amount covered by pre-processing. stagecpysize = CPYPreSizeChoice(memcpy); assert stagecpysize == 0 || (stagecpysize < 0) == (memcpy.cpysize < 0); if memcpy.cpysize > 0 then assert stagecpysize <= memcpy.cpysize; else assert stagecpysize >= memcpy.cpysize; else constant integer postsize = CPYPostSizeChoice(memcpy); assert postsize == 0 || (postsize < 0) == (memcpy.cpysize < 0); if memcpy.stage == MOPSStage_Main then stagecpysize = memcpy.cpysize postsize; else stagecpysize = postsize; return stagecpysize;
```

## J1.1.3.148 MemCpyZeroSizeCheck

```
// MemCpyZeroSizeCheck() // ===================== // Returns TRUE if the implementation option is checked on a copy of size zero remaining. boolean MemCpyZeroSizeCheck() return boolean IMPLEMENTATION_DEFINED "Implementation option is checked with a cpysize of 0";
```

## J1.1.3.149 MemSetBytes

```
// MemSetBytes() // ============= // Writes a byte of data to the given address 'bytes' times. // The integer return parameter indicates the number of bytes set. The AddressDescriptor and // PhysMemRetStatus parameters contain Fault or Abort information for the caller to handle. (integer, AddressDescriptor, PhysMemRetStatus) MemSetBytes(bits(64) toaddress, bits(8) data,
```

## MOPSBlockSize bytes, AccessDescriptor accdesc) AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; memaddrdesc.fault = NoFault(); memstatus.statuscode = Fault\_None; constant boolean aligned = TRUE; integer write = 0; // Bytes written // Write until all bytes are written or a fault is encountered. while write &lt; bytes &amp;&amp; !IsFault(memaddrdesc) &amp;&amp; !IsFault(memstatus) do (memaddrdesc, memstatus) = AArch64.MemSingleWrite(toaddress + write, 1, accdesc, aligned, data); write = write + 1; // Check all bytes were written. if IsFault(memaddrdesc) || IsFault(memstatus) then return (write - 1, memaddrdesc, memstatus); return (bytes, memaddrdesc, memstatus); J1.1.3.150 MemSetParametersIllformedE // MemSetParametersIllformedE() // ============================ // Returns TRUE if the inputs are not well formed (in terms of their size and/or // alignment) for a SETE* or SETGE* instruction for this implementation given the // parameters of the destination and size of the set. boolean MemSetParametersIllformedE(SETParams memset); J1.1.3.151 MemSetParametersIllformedM // MemSetParametersIllformedM() // ============================ // Returns TRUE if the inputs are not well formed (in terms of their size and/or // alignment) for a SETM* or SETGM* instruction for this implementation given the // parameters of the destination and size of the copy. boolean MemSetParametersIllformedM(SETParams memset); J1.1.3.152 MemSetStageSize // MemSetStageSize() // ================= // Returns the number of bytes set by the given stage of a SET* or SETG* instruction. integer MemSetStageSize(SETParams memset) integer stagesetsize; if memset.stage == MOPSStage\_Prologue then // IMP DEF selection of the amount covered by pre-processing. stagesetsize = SETPreSizeChoice(memset); assert stagesetsize == 0 || (stagesetsize &lt; 0) == (memset.setsize &lt; 0); if memset.is\_setg then assert stagesetsize&lt;3:0&gt; == '0000'; if memset.setsize &gt; 0 then assert stagesetsize &lt;= memset.setsize; else

```
assert stagesetsize >= memset.setsize; else constant integer postsize = SETPostSizeChoice(memset); assert postsize == 0 || (postsize < 0) == (memset.setsize if memset.is_setg then assert postsize<3:0> == '0000'; if memset.stage == MOPSStage_Main then stagesetsize = memset.setsize postsize; else stagesetsize = postsize; return stagesetsize;
```

```
// MemStageCpyZeroSizeCheck() // ========================== // Returns TRUE if the implementation option is checked on a stage copy of size zero boolean MemStageCpyZeroSizeCheck()
```

## &lt; 0); J1.1.3.153 MemSetTags // MemSetTags() // ============ // Write Allocation Tags for each Tag Granule in 'size'. // The integer return parameter indicates the number of Tag Granules written. The // AddressDescriptor and PhysMemRetStatus parameters contain Fault or Abort information for // the caller to handle. (integer, AddressDescriptor, PhysMemRetStatus) MemSetTags(bits(64) toaddress, bits(4) tag, integer size, AccessDescriptor accdesc) assert IsAligned(toaddress, TAG\_GRANULE) &amp;&amp; size MOD TAG\_GRANULE == 0; AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; memaddrdesc.fault = NoFault(); memstatus.statuscode = Fault\_None; integer tagstep = size DIV TAG\_GRANULE; // Write until all tags are written or a fault is encountered. while tagstep &gt; 0 &amp;&amp; !IsFault(memaddrdesc) &amp;&amp; !IsFault(memstatus) do constant bits(64) tagaddr = toaddress + (tagstep - 1) * TAG\_GRANULE; (memaddrdesc, memstatus) = AArch64.MemTagWrite(tagaddr, accdesc, tag); tagstep = tagstep - 1; if IsFault(memaddrdesc) || IsFault(memstatus) then tagstep = tagstep + 1; constant integer tags\_written = (size DIV TAG\_GRANULE) -tagstep; return (tags\_written, memaddrdesc, memstatus); J1.1.3.154 MemSetZeroSizeCheck // MemSetZeroSizeCheck() // ===================== // Returns TRUE if the implementation option is checked on a set of size zero remaining. boolean MemSetZeroSizeCheck() return boolean IMPLEMENTATION\_DEFINED "Implementation option is checked with a setsize of 0"; J1.1.3.155 MemStageCpyZeroSizeCheck remaining.

```
return (boolean IMPLEMENTATION_DEFINED "Implementation option is checked with a stage cpysize of 0");
```

## J1.1.3.156 MemStageSetZeroSizeCheck

```
// MemStageSetZeroSizeCheck() // ========================== // Returns TRUE if the implementation option is checked on a stage set of size zero remaining. boolean MemStageSetZeroSizeCheck() return (boolean IMPLEMENTATION_DEFINED "Implementation option is checked with a stage setsize of 0");
```

## J1.1.3.157 MismatchedCpySetTargetEL

```
// MismatchedCpySetTargetEL() // ========================== // Return the target exception level for an Exception_MemCpyMemSet. bits(2) MismatchedCpySetTargetEL() bits(2) target_el; if UInt(PSTATE.EL) > UInt(EL1) then target_el = PSTATE.EL; elsif PSTATE.EL == EL0 && EL2Enabled() && HCR_EL2.TGE == '1' then target_el = EL2; elsif (PSTATE.EL == EL1 && EL2Enabled() && IsHCRXEL2Enabled() && HCRX_EL2.MCE2 == '1') then target_el = EL2; else target_el = EL1; return target_el;
```

## J1.1.3.158 MismatchedMemCpyException

```
// MismatchedMemCpyException() // =========================== // Generates an exception for a CPY* instruction if the version // is inconsistent with the state of the call. MismatchedMemCpyException(CPYParams memcpy, bits(4) options, bits(2) formatoption) constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = 0x0; constant bits(2) target_el = MismatchedCpySetTargetEL(); ExceptionRecord except = ExceptionSyndrome(Exception_MemCpyMemSet); except.syndrome.iss<24> = '0'; except.syndrome.iss<23> = '0'; except.syndrome.iss<22:19> = options; except.syndrome.iss<18> = if memcpy.stage == MOPSStage_Epilogue then '1' else '0'; except.syndrome.iss<17:16> = formatoption; // exception.syndrome<15> is RES0. except.syndrome.iss<14:10> = memcpy.d<4:0>; except.syndrome.iss<9:5> = memcpy.s<4:0>; except.syndrome.iss<4:0> = memcpy.n<4:0>; AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.3.159 MismatchedMemSetException

```
// MismatchedMemSetException() // =========================== // Generates an exception for a SET* instruction if the version // is inconsistent with the state of the call. MismatchedMemSetException(SETParams memset, bits(2) options, bits(2) formatoption) constant bits(64) preferred_exception_return = ThisInstrAddr(64); constant integer vect_offset = 0x0; constant bits(2) target_el = MismatchedCpySetTargetEL(); ExceptionRecord except = ExceptionSyndrome(Exception_MemCpyMemSet); except.syndrome.iss<24> = '1'; except.syndrome.iss<23> = if memset.is_setg then '1' else '0'; // exception.syndrome<22:21> is RES0. except.syndrome.iss<20:19> = options; except.syndrome.iss<18> = if memset.stage == MOPSStage_Epilogue then '1' else except.syndrome.iss<17:16> = formatoption; // exception.syndrome<15> is RES0. except.syndrome.iss<14:10> = memset.d<4:0>; except.syndrome.iss<9:5> = memset.s<4:0>; except.syndrome.iss<4:0> = memset.n<4:0>; AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

```
// SETParams // ========= type SETParams is ( MOPSStage stage, boolean boolean is_setg, integer setsize, integer stagesetsize, bits(64) toaddress, bits(4) nzcv, integer n, integer d,
```

## '0'; J1.1.3.160 SETGOptionA // SETGOptionA() // ============= // Returns TRUE if the implementation uses Option A for the // SETG* instructions, and FALSE otherwise. boolean SETGOptionA() return boolean IMPLEMENTATION\_DEFINED "SETG* instructions use Option A"; J1.1.3.161 SETOptionA // SETOptionA() // ============ // Returns TRUE if the implementation uses Option A for the // SET* instructions, and FALSE otherwise. boolean SETOptionA() return boolean IMPLEMENTATION\_DEFINED "SET* instructions use Option A"; J1.1.3.162 SETParams implements\_option\_a,

```
integer s )
```

## J1.1.3.163 SETPostSizeChoice // SETPostSizeChoice() // =================== // Returns the size of the set that is performed by the SETE* or SETGE* instructions // for this implementation, given the parameters of the destination and size of the set. integer SETPostSizeChoice(SETParams memset); J1.1.3.164 SETPreSizeChoice // SETPreSizeChoice() // ================== // Returns the size of the set that is performed by the SETP* or SETGP* instructions // for this implementation, given the parameters of the destination and size of the set. integer SETPreSizeChoice(SETParams memset); J1.1.3.165 SETSizeChoice // SETSizeChoice() // =============== // Returns the size of the block this performed for an iteration of the set given // the parameters of the destination and size of the set. The size of the block // is an integer multiple of alignsize. MOPSBlockSize SETSizeChoice(SETParams memset, integer alignsize); J1.1.3.166 UpdateCpyRegisters the CPY* and CPYF*

```
// UpdateCpyRegisters() // ==================== // Performs updates to the X[n], X[d], and X[s] registers, as appropriate, for // instructions. When fault is TRUE, the values correspond to the first element not copied, // such that a return to the instruction will enable a resumption of the copy. UpdateCpyRegisters(CPYParams memcpy, boolean fault, integer copied) if fault then if memcpy.stage == MOPSStage_Prologue then // Undo any formatting of the input parameters performed in the prologue. if memcpy.implements_option_a then if memcpy.forward then // cpysize is negative. constant integer cpysize = memcpy.cpysize + copied; X[memcpy.n, 64] = (0 -cpysize)<63:0>; X[memcpy.d, 64] = memcpy.toaddress + cpysize; X[memcpy.s, 64] = memcpy.fromaddress + cpysize; else X[memcpy.n, 64] = (memcpy.cpysize - copied)<63:0>; else if memcpy.forward then X[memcpy.n, 64] = (memcpy.cpysize - copied)<63:0>; X[memcpy.d, 64] = memcpy.toaddress + copied; X[memcpy.s, 64] = memcpy.fromaddress + copied;
```

```
else X[memcpy.n, 64] = (memcpy.cpysize - copied)<63:0>; else if memcpy.implements_option_a then if memcpy.forward then X[memcpy.n, 64] = (memcpy.cpysize + copied)<63:0>; else X[memcpy.n, 64] = (memcpy.cpysize - copied)<63:0>; else X[memcpy.n, 64] = (memcpy.cpysize - copied)<63:0>; if memcpy.forward then X[memcpy.d, 64] = memcpy.toaddress + copied; X[memcpy.s, 64] = memcpy.fromaddress + copied; else X[memcpy.d, 64] = memcpy.toaddress -copied; X[memcpy.s, 64] = memcpy.fromaddress -copied; else X[memcpy.n, 64] = memcpy.cpysize<63:0>; if memcpy.stage == MOPSStage_Prologue || !memcpy.implements_option_a then X[memcpy.d, 64] = memcpy.toaddress; X[memcpy.s, 64] = memcpy.fromaddress; return; UpdateSetRegisters
```

## J1.1.3.167

```
// UpdateSetRegisters() // ==================== // Performs updates to the X[n] and X[d] registers, as appropriate, for the SET* and SETG* // instructions. When fault is TRUE, the values correspond to the first element not set, such // that a return to the instruction will enable a resumption of the memory set. UpdateSetRegisters(SETParams memset, boolean fault, integer memory_set) if fault then // Undo any formatting of the input parameters performed in the prologue. if memset.stage == MOPSStage_Prologue then if memset.implements_option_a then // setsize is negative. constant integer setsize = memset.setsize + memory_set; X[memset.n, 64] = (0 -setsize)<63:0>; X[memset.d, 64] = memset.toaddress + setsize; else X[memset.n, 64] = (memset.setsize - memory_set)<63:0>; X[memset.d, 64] = memset.toaddress + memory_set; else if memset.implements_option_a then X[memset.n, 64] = (memset.setsize + memory_set)<63:0>; else X[memset.n, 64] = (memset.setsize - memory_set)<63:0>; X[memset.d, 64] = memset.toaddress + memory_set; else X[memset.n, 64] = memset.setsize<63:0>; if memset.stage == MOPSStage_Prologue || !memset.implements_option_a then X[memset.d, 64] = memset.toaddress; return;
```

## J1.1.3.168

MoveWideOp

```
// MoveWideOp // ========== // Move wide 16-bit immediate instruction types. enumeration MoveWideOp {MoveWideOp_N,
```

```
// AddPAC2() // ========= // Calculates the pointer authentication code for a 64-bit quantity and then // inserts that into pointer authentication code field of that 64-bit quantity. bits(64) AddPAC2(bits(64) ptr, bits(64) modifier1, bits(64) modifier2, bits(128) K, constant boolean use_modifier2 = TRUE; return InsertPAC(ptr, modifier1, modifier2, use_modifier2, K, data);
```

```
MoveWideOp_Z, MoveWideOp_K}; J1.1.3.169 MoveWidePreferred // MoveWidePreferred() // =================== // // Return TRUE if a bitmask immediate encoding would generate an immediate // value that could also be represented by a single MOVZ or MOVN instruction. // Used as a condition for the preferred MOV<-ORR alias. boolean MoveWidePreferred(bit sf, bit immN, bits(6) imms, bits(6) immr) constant integer s = UInt(imms); constant integer r = UInt(immr); constant integer width = if sf == '1' then 64 else 32; // element size must equal total immediate size if sf == '1' && (immN:imms) != '1xxxxxx' then return FALSE; if sf == '0' && (immN:imms) != '00xxxxx' then return FALSE; // for MOVZ must contain no more than 16 ones if s < 16 then // ones must not span halfword boundary when rotated return (-r MOD 16) <= (15 s); // for MOVN must contain no more than 16 zeros if s >= width - 15 then // zeros must not span halfword boundary when rotated return (r MOD 16) <= (s - (width - 15)); return FALSE; J1.1.3.170 AddPAC // AddPAC() // ======== // Calculates the pointer authentication code for a 64-bit quantity and then // inserts that into pointer authentication code field of that 64-bit quantity. bits(64) AddPAC(bits(64) ptr, bits(64) modifier, bits(128) K, boolean data) constant boolean use_modifier2 = FALSE; return InsertPAC(ptr, modifier, Zeros(64), use_modifier2, K, data); J1.1.3.171 AddPAC2 boolean data)
```

## J1.1.3.172 InsertPAC

```
// InsertPAC() // =========== // Calculates the pointer authentication code for a 64-bit quantity and then // inserts that into pointer authentication code field of that 64-bit quantity. bits(64) InsertPAC(bits(64) ptr, bits(64) modifier, bits(64) modifier2, boolean use_modifier2, bits(128) K, boolean data) bits(64) PAC; bits(64) result; bits(64) ext_ptr; bits(64) extfield; bit selbit; bit bit55; constant boolean tbi = EffectiveTBI(ptr, !data, PSTATE.EL) == '1'; constant boolean mtx = (IsFeatureImplemented(FEAT_MTE_NO_ADDRESS_TAGS) && EffectiveMTX(ptr, !data, PSTATE.EL) == '1'); constant integer top_bit = if tbi then 55 else 63; constant boolean EL3_using_lva3 = (IsFeatureImplemented(FEAT_LVA3) && TranslationRegime(PSTATE.EL) == Regime_EL3 && AArch64.IASize(TCR_EL3.T0SZ) > 52); constant boolean is_VA_56bit = (TranslationRegime(PSTATE.EL) == Regime_EL3 && AArch64.IASize(TCR_EL3.T0SZ) == 56); // If tagged pointers are in use for a regime with two TTBRs, use bit<55> of // the pointer to select between upper and lower ranges, and preserve this. // This handles the awkward case where there is apparently no correct choice between // the upper and lower address range - ie an addr of 1xxxxxxx0... with TBI0=0 and TBI1=1 // and 0xxxxxxx1 with TBI1=0 and TBI0=1: if PtrHasUpperAndLowerAddRanges() then assert S1TranslationRegime() IN {EL1, EL2}; if S1TranslationRegime() == EL1 then // EL1 translation regime registers if data then if TCR_EL1.TBI1 == '1' || TCR_EL1.TBI0 == '1' then selbit = ptr<55>; else selbit = ptr<63>; else if ((TCR_EL1.TBI1 == '1' && TCR_EL1.TBID1 == '0') || (TCR_EL1.TBI0 == '1' && TCR_EL1.TBID0 == '0')) then selbit = ptr<55>; else selbit = ptr<63>; else // EL2 translation regime registers if data then if TCR_EL2.TBI1 == '1' || TCR_EL2.TBI0 == '1' then selbit = ptr<55>; else selbit = ptr<63>; else if ((TCR_EL2.TBI1 == '1' && TCR_EL2.TBID1 == '0') || (TCR_EL2.TBI0 == '1' && TCR_EL2.TBID0 == '0')) then selbit = ptr<55>; else selbit = ptr<63>; else selbit = if tbi then ptr<55> else ptr<63>; if IsFeatureImplemented(FEAT_PAuth2) && IsFeatureImplemented(FEAT_CONSTPACFIELD) then selbit = ptr<55>; constant AddressSize bottom_PAC_bit = CalculateBottomPACBit(selbit); if EL3_using_lva3 then extfield = Replicate('0', 64);
```

```
else extfield = Replicate(selbit, 64); // Compute the pointer authentication code for a ptr with good extension bits if tbi then if bottom_PAC_bit <= 55 then ext_ptr = (ptr<63:56> : extfield<55:bottom_PAC_bit> : ptr<bottom_PAC_bit-1:0>); else ext_ptr = ptr<63:56> : ptr<55:0>; elsif mtx then if bottom_PAC_bit <= 55 then ext_ptr = (extfield<63:60> : ptr<59:56> : extfield<55:bottom_PAC_bit> : ptr<bottom_PAC_bit-1:0>); else ext_ptr = extfield<63:60> : ptr<59:56> : ptr<55:0>; else ext_ptr = extfield<63:bottom_PAC_bit> : ptr<bottom_PAC_bit-1:0>; if use_modifier2 then assert IsFeatureImplemented(FEAT_PAuth_LR); PAC = ComputePAC2(ext_ptr, modifier, modifier2, K<127:64>, K<63:0>); else PAC = ComputePAC(ext_ptr, modifier, K<127:64>, K<63:0>); if !IsFeatureImplemented(FEAT_PAuth2) then // If FEAT_PAuth2 is not implemented, the PAC is corrupted if the pointer does not have // a canonical VA. assert bottom_PAC_bit <= 52; if !IsZero(ptr<top_bit:bottom_PAC_bit>) && !IsOnes(ptr<top_bit:bottom_PAC_bit>) then if IsFeatureImplemented(FEAT_EPAC) then PAC = 0x0000000000000000<63:0>; else PAC<top_bit-1> = NOT(PAC<top_bit-1>); // Preserve the determination between upper and lower address at bit<55> and insert PAC into // bits that are not used for the address or the tag(s). if !IsFeatureImplemented(FEAT_PAuth2) then assert (bottom_PAC_bit <= 52); if tbi then result = ptr<63:56>:selbit:PAC<54:bottom_PAC_bit>:ptr<bottom_PAC_bit-1:0>; else result = PAC<63:56>:selbit:PAC<54:bottom_PAC_bit>:ptr<bottom_PAC_bit-1:0>; else if EL3_using_lva3 then // Bit 55 is an address bit (when VA size is 56-bits) or // used to store PAC (when VA size is less than 56-bits) if is_VA_56bit then bit55 = ptr<55>; else bit55 = ptr<55> EOR PAC<55>; else bit55 = selbit; if tbi then if bottom_PAC_bit < 55 then result = (ptr<63:56> : bit55 : (ptr<54:bottom_PAC_bit> EOR PAC<54:bottom_PAC_bit>) : ptr<bottom_PAC_bit-1:0>); else result = (ptr<63:56> : bit55 : ptr<54:0>); elsif mtx then if bottom_PAC_bit < 55 then result = ((ptr<63:60> EOR PAC<63:60>) : ptr<59:56> : bit55 : (ptr<54:bottom_PAC_bit> EOR PAC<54:bottom_PAC_bit>) : ptr<bottom_PAC_bit-1:0>); else
```

```
result = ((ptr<63:60> EOR PAC<63:60>) : ptr<59:56> : bit55 : ptr<54:0>); else if bottom_PAC_bit < 55 then result = ((ptr<63:56> EOR PAC<63:56>) : bit55 : (ptr<54:bottom_PAC_bit> ptr<bottom_PAC_bit-1:0>); else result = ((ptr<63:56> EOR PAC<63:56>) : bit55 : ptr<54:0>); return result;
```

```
// AddPACGA() // ========== // Returns a 64-bit value where the lower 32 bits are 0, and the upper 32 bits // a 32-bit pointer authentication code which is derived using a cryptographic // algorithm as a combination of x, y and the APGAKey_EL1. bits(64) AddPACGA(bits(64) x, bits(64) y) boolean TrapEL2; constant bits(128) APGAKey_EL1 = APGAKeyHi_EL1<63:0> : APGAKeyLo_EL1<63:0>; boolean TrapEL3; case PSTATE.EL of when EL0 TrapEL2 = EL2Enabled() && HCR_EL2.API == '0' && !IsInHost(); TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0';
```

```
EOR PAC<54:bottom_PAC_bit>) : J1.1.3.173 AddPACDA // AddPACDA() // ========== // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with a pointer authentication code, where the pointer authentication // code is derived using a cryptographic algorithm as a combination of x, y and the // APDAKey_EL1. bits(64) AddPACDA(bits(64) x, bits(64) y) constant bits(128) APDAKey_EL1 = APDAKeyHi_EL1<63:0> : APDAKeyLo_EL1<63:0>; if !IsAPDAKeyEnabled() then return x; else return AddPAC(x, y, APDAKey_EL1, TRUE); J1.1.3.174 AddPACDB // AddPACDB() // ========== // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with a pointer authentication code, where the pointer authentication // code is derived using a cryptographic algorithm as a combination of x, y and the // APDBKey_EL1. bits(64) AddPACDB(bits(64) x, bits(64) y) constant bits(128) APDBKey_EL1 = APDBKeyHi_EL1<63:0> : APDBKeyLo_EL1<63:0>; if !IsAPDBKeyEnabled() then return x; else return AddPAC(x, y, APDBKey_EL1, TRUE); J1.1.3.175 AddPACGA contain
```

```
when EL1
```

```
TrapEL2 = EL2Enabled() && HCR_EL2.API == '0'; TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL2 TrapEL2 = FALSE; TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL3 TrapEL2 = FALSE; TrapEL3 = FALSE; if TrapEL3 && EL3SDDUndefPriority() then UNDEFINED; elsif TrapEL2 then TrapPACUse(EL2); elsif TrapEL3 then if EL3SDDUndef() then UNDEFINED; else TrapPACUse(EL3); else return ComputePAC(x, y, APGAKey_EL1<127:64>,
```

```
// AddPACIB() // ========== // Returns a 64-bit value containing x, but replacing the pointer authentication // field bits with a pointer authentication code, where the pointer authentication // code is derived using a cryptographic algorithm as a combination of x, y and the
```

```
APGAKey_EL1<63:0>)<63:32>:Zeros(32); J1.1.3.176 AddPACIA // AddPACIA() // ========== // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with a pointer authentication code, where the pointer authentication // code is derived using a cryptographic algorithm as a combination of x, y, and the // APIAKey_EL1. bits(64) AddPACIA(bits(64) x, bits(64) y) constant bits(128) APIAKey_EL1 = APIAKeyHi_EL1<63:0>:APIAKeyLo_EL1<63:0>; if !IsAPIAKeyEnabled() then return x; else return AddPAC(x, y, APIAKey_EL1, FALSE); J1.1.3.177 AddPACIA2 // AddPACIA2() // =========== // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with a pointer authentication code, where the pointer authentication // code is derived using a cryptographic algorithm as a combination of x, y, z, and // the APIAKey_EL1. bits(64) AddPACIA2(bits(64) x, bits(64) y, bits(64) z) constant bits(128) APIAKey_EL1 = APIAKeyHi_EL1<63:0>:APIAKeyLo_EL1<63:0>; if !IsAPIAKeyEnabled() then return x; else return AddPAC2(x, y, z, APIAKey_EL1, FALSE); J1.1.3.178 AddPACIB code
```

```
// APIBKey_EL1. bits(64) AddPACIB(bits(64) x, bits(64) y) constant bits(128) APIBKey_EL1 = APIBKeyHi_EL1<63:0> : if !IsAPIBKeyEnabled() then return x; else return AddPAC(x, y, APIBKey_EL1, FALSE);
```

```
APIBKeyLo_EL1<63:0>; J1.1.3.179 AddPACIB2 // AddPACIB2() // =========== // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with a pointer authentication code, where the pointer authentication // code is derived using a cryptographic algorithm as a combination of x, y, z, and // the APIBKey_EL1. bits(64) AddPACIB2(bits(64) x, bits(64) y, bits(64) z) constant bits(128) APIBKey_EL1 = APIBKeyHi_EL1<63:0> : APIBKeyLo_EL1<63:0>; if !IsAPIBKeyEnabled() then return x; else return AddPAC2(x, y, z, APIBKey_EL1, FALSE); J1.1.3.180 AArch64.PACFailException // AArch64.PACFailException() // ========================== // Generates a PAC Fail Exception AArch64.PACFailException(bits(2) syndrome) route_to_el2 = PSTATE.EL == EL0 && EL2Enabled() && HCR_EL2.TGE == '1'; constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; except = ExceptionSyndrome(Exception_PACFail); except.syndrome.iss<1:0> = syndrome; except.syndrome.iss<24:2> = Zeros(23); // RES0 if UInt(PSTATE.EL) > UInt(EL0) then AArch64.TakeException(PSTATE.EL, except, preferred_exception_return, vect_offset); elsif route_to_el2 then AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); else AArch64.TakeException(EL1, except, preferred_exception_return, vect_offset); J1.1.3.181 Auth // Auth() // ====== // Restores the upper bits of the address to be all zeros or all ones (based on the // value of bit[55]) and computes and checks the pointer authentication code. If the // check passes, then the restored address is returned. If the check fails, the // second-top and third-top bits of the extension bits in the pointer authentication code // field are corrupted to ensure that accessing the address will give a translation fault. bits(64) Auth(bits(64) ptr, bits(64) modifier, bits(128) K, boolean data, bit key_number, boolean is_combined) constant boolean use_modifier2 = FALSE; return Authenticate(ptr, modifier, Zeros(64), use_modifier2, K, data, key_number, is_combined);
```

## J1.1.3.182 Auth2

```
// Auth2() // ======= // Restores the upper bits of the address to be all zeros or all ones (based on the // value of bit[55]) and computes and checks the pointer authentication code. If the // check passes, then the restored address is returned. If the check fails, the // second-top and third-top bits of the extension bits in the pointer authentication code // field are corrupted to ensure that accessing the address will give a translation fault. bits(64) Auth2(bits(64) ptr, bits(64) modifier1, bits(64) modifier2, bits(128) K, boolean data, bit key_number, boolean is_combined) constant boolean use_modifier2 = TRUE; return Authenticate(ptr, modifier1, modifier2, use_modifier2, K, data, key_number, is_combined);
```

## J1.1.3.183 Authenticate

```
// Authenticate() // ============== // Restores the upper bits of the address to be all zeros or all ones (based on the // value of bit[55]) and computes and checks the pointer authentication code. If the // check passes, then the restored address is returned. If the check fails, the // second-top and third-top bits of the extension bits in the pointer authentication code // field are corrupted to ensure that accessing the address will give a translation fault. bits(64) Authenticate(bits(64) ptr, bits(64) modifier, bits(64) modifier2, boolean use_modifier2, bits(128) K, boolean data, bit key_number, boolean is_combined) bits(64) PAC; bits(64) result; bits(64) original_ptr; bits(2) error_code; bits(64) extfield; // Reconstruct the extension field used of adding the PAC to the pointer constant boolean tbi = EffectiveTBI(ptr, !data, PSTATE.EL) == '1'; constant boolean mtx = (IsFeatureImplemented(FEAT_MTE_NO_ADDRESS_TAGS) && EffectiveMTX(ptr, !data, PSTATE.EL) == '1'); constant AddressSize bottom_PAC_bit = CalculateBottomPACBit(ptr<55>); constant boolean EL3_using_lva3 = (IsFeatureImplemented(FEAT_LVA3) && TranslationRegime(PSTATE.EL) == Regime_EL3 && AArch64.IASize(TCR_EL3.T0SZ) > 52); constant boolean is_VA_56bit = (TranslationRegime(PSTATE.EL) == Regime_EL3 && AArch64.IASize(TCR_EL3.T0SZ) == 56); if EL3_using_lva3 then extfield = Replicate('0', 64); else extfield = Replicate(ptr<55>, 64); if tbi then if bottom_PAC_bit <= 55 then original_ptr = (ptr<63:56> : extfield<55:bottom_PAC_bit> : ptr<bottom_PAC_bit-1:0>); else original_ptr = ptr<63:56> : ptr<55:0>; elsif mtx then if bottom_PAC_bit <= 55 then original_ptr = (extfield<63:60> : ptr<59:56> : extfield<55:bottom_PAC_bit> : ptr<bottom_PAC_bit-1:0>); else original_ptr = extfield<63:60> : ptr<59:56> : ptr<55:0>; else original_ptr = extfield<63:bottom_PAC_bit> : ptr<bottom_PAC_bit-1:0>; if use_modifier2 then
```

```
assert IsFeatureImplemented(FEAT_PAuth_LR); PAC = ComputePAC2(original_ptr, modifier, modifier2, K<127:64>, K<63:0>); else PAC = ComputePAC(original_ptr, modifier, K<127:64>, K<63:0>); // Check pointer authentication code if tbi then if !IsFeatureImplemented(FEAT_PAuth2) then assert (bottom_PAC_bit <= 52); if PAC<54:bottom_PAC_bit> == ptr<54:bottom_PAC_bit> then result = original_ptr; else error_code = key_number:NOT(key_number); result = original_ptr<63:55>:error_code:original_ptr<52:0>; else result = ptr; if EL3_using_lva3 && !is_VA_56bit then result<55> = result<55> EOR PAC<55>; if (bottom_PAC_bit < 55) then result<54:bottom_PAC_bit> = result<54:bottom_PAC_bit> EOR PAC<54:bottom_PAC_bit>; if (IsFeatureImplemented(FEAT_FPACCOMBINE) || (IsFeatureImplemented(FEAT_FPAC) && !is_combined)) then if (EL3_using_lva3 && !is_VA_56bit && !IsZero(result<55:bottom_PAC_bit>)) then error_code = (if data then '1' else '0'):key_number; AArch64.PACFailException(error_code); elsif (!EL3_using_lva3 && (bottom_PAC_bit < 55) && result<54:bottom_PAC_bit> != Replicate(result<55>, (55-bottom_PAC_bit))) then error_code = (if data then '1' else '0'):key_number; AArch64.PACFailException(error_code); elsif mtx then assert IsFeatureImplemented(FEAT_PAuth2); result = ptr; if EL3_using_lva3 && !is_VA_56bit then result<55> = result<55> EOR PAC<55>; if (bottom_PAC_bit < 55) then result<54:bottom_PAC_bit> = result<54:bottom_PAC_bit> EOR PAC<54:bottom_PAC_bit>; result<63:60> = result<63:60> EOR PAC<63:60>; if (IsFeatureImplemented(FEAT_FPACCOMBINE) || (IsFeatureImplemented(FEAT_FPAC) && !is_combined)) then if (EL3_using_lva3 && !is_VA_56bit && (!IsZero(result<55:bottom_PAC_bit>) || !IsZero(result<63:60>))) then error_code = (if data then '1' else '0'):key_number; AArch64.PACFailException(error_code); elsif (!EL3_using_lva3 && (bottom_PAC_bit < 55) && (((result<54:bottom_PAC_bit> != Replicate(result<55>, (55-bottom_PAC_bit)))) || (result<63:60> != Replicate(result<55>, 4)))) then error_code = (if data then '1' else '0'):key_number; AArch64.PACFailException(error_code); else if !IsFeatureImplemented(FEAT_PAuth2) then assert (bottom_PAC_bit <= 52); if PAC<54:bottom_PAC_bit> == ptr<54:bottom_PAC_bit> && PAC<63:56> == ptr<63:56> then result = original_ptr; else error_code = key_number:NOT(key_number); result = original_ptr<63>:error_code:original_ptr<60:0>; else result = ptr; if EL3_using_lva3 && !is_VA_56bit then result<55> = result<55> EOR PAC<55>; if bottom_PAC_bit < 55 then result<54:bottom_PAC_bit> = result<54:bottom_PAC_bit> EOR PAC<54:bottom_PAC_bit>; result<63:56> = result<63:56> EOR PAC<63:56>; if (IsFeatureImplemented(FEAT_FPACCOMBINE) || (IsFeatureImplemented(FEAT_FPAC) && !is_combined)) then
```

```
if (EL3_using_lva3 && !IsZero(result<63:bottom_PAC_bit>)) then error_code = (if data then '1' else '0'):key_number; AArch64.PACFailException(error_code); elsif (!EL3_using_lva3 && result<63:bottom_PAC_bit> != Replicate(result<55>, (64-bottom_PAC_bit))) then error_code = (if data then '1' else '0'):key_number; AArch64.PACFailException(error_code); return result;
```

```
// AuthDA() // ======== // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with the extension of the address bits. The instruction checks a pointer // authentication code in the pointer authentication code field bits of x, using the same // algorithm and key as AddPACDA(). bits(64) AuthDA(bits(64) x, bits(64) y, boolean is_combined) constant bits(128) APDAKey_EL1 = APDAKeyHi_EL1<63:0> : APDAKeyLo_EL1<63:0>; if !IsAPDAKeyEnabled() then return x; else return Auth(x, y, APDAKey_EL1, TRUE, '0', is_combined);
```

```
// AuthDB() // ======== // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with the extension of the address bits. The instruction checks a // pointer authentication code in the pointer authentication code field bits of x, using // the same algorithm and key as AddPACDB(). bits(64) AuthDB(bits(64) x, bits(64) y, boolean is_combined) constant bits(128) APDBKey_EL1 = APDBKeyHi_EL1<63:0> : APDBKeyLo_EL1<63:0>; if !IsAPDBKeyEnabled() then return x; else return Auth(x, y, APDBKey_EL1, TRUE, '1', is_combined);
```

```
J1.1.3.184 AuthDA J1.1.3.185 AuthDB J1.1.3.186 AuthIA
```

```
// AuthIA() // ======== // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with the extension of the address bits. The instruction checks a pointer // authentication code in the pointer authentication code field bits of x, using the same // algorithm and key as AddPACIA(). bits(64) AuthIA(bits(64) x, bits(64) y, boolean is_combined) constant bits(128) APIAKey_EL1 = APIAKeyHi_EL1<63:0> : APIAKeyLo_EL1<63:0>; if !IsAPIAKeyEnabled() then return x; else return Auth(x, y, APIAKey_EL1, FALSE, '0', is_combined);
```

## J1.1.3.187 AuthIA2

```
// AuthIA2() // ========= // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with the extension of the address bits. The instruction checks a pointer // authentication code in the pointer authentication code field bits of x, using the same // algorithm and key as AddPACIA2(). bits(64) AuthIA2(bits(64) x, bits(64) y, bits(64) z, boolean is_combined) constant bits(128) APIAKey_EL1 = APIAKeyHi_EL1<63:0> : APIAKeyLo_EL1<63:0>; if !IsAPIAKeyEnabled() then return x; else return Auth2(x, y, z, APIAKey_EL1, FALSE, '0', is_combined);
```

```
// AuthIB() // ======== // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with the extension of the address bits. The instruction checks a pointer // authentication code in the pointer authentication code field bits of x, using the same // algorithm and key as AddPACIB(). bits(64) AuthIB(bits(64) x, bits(64) y, boolean is_combined) constant bits(128) APIBKey_EL1 = APIBKeyHi_EL1<63:0> : APIBKeyLo_EL1<63:0>; if !IsAPIBKeyEnabled() then return x; else return Auth(x, y, APIBKey_EL1, FALSE, '1', is_combined);
```

```
// AuthIB2() // ========= // Returns a 64-bit value containing x, but replacing the pointer authentication code // field bits with the extension of the address bits. The instruction checks a pointer // authentication code in the pointer authentication code field bits of x, using the same // algorithm and key as AddPACIB2(). bits(64) AuthIB2(bits(64) x, bits(64) y, bits(64) z, boolean is_combined) constant bits(128) APIBKey_EL1 = APIBKeyHi_EL1<63:0> : APIBKeyLo_EL1<63:0>; if !IsAPIBKeyEnabled() then return x; else return Auth2(x, y, z, APIBKey_EL1, FALSE, '1', is_combined);
```

```
// AArch64.PACEffectiveTxSZ() // ========================== // Compute the effective value for TxSZ used to determine the placement of the PAC field bits(6) AArch64.PACEffectiveTxSZ(Regime regime, S1TTWParams walkparams) constant integer s1maxtxsz = AArch64.MaxTxSZ(walkparams.tgx); constant integer s1mintxsz = AArch64.S1MinTxSZ(regime, walkparams); if AArch64.S1TxSZFaults(regime, walkparams) then if ConstrainUnpredictable(Unpredictable_RESTnSZ) == Constraint_FORCE then
```

```
J1.1.3.188 AuthIB J1.1.3.189 AuthIB2 J1.1.3.190 AArch64.PACEffectiveTxSZ if UInt(walkparams.txsz) < s1mintxsz then
```

```
return s1mintxsz<5:0>; if UInt(walkparams.txsz) > s1maxtxsz then return s1maxtxsz<5:0>; elsif UInt(walkparams.txsz) < s1mintxsz then return s1mintxsz<5:0>; elsif UInt(walkparams.txsz) > s1maxtxsz then return s1maxtxsz<5:0>; return walkparams.txsz;
```

## J1.1.3.191 CalculateBottomPACBit

```
// CalculateBottomPACBit() // ======================= AddressSize CalculateBottomPACBit(bit top_bit) Regime regime; S1TTWParams walkparams; AddressSize bottom_PAC_bit; regime = TranslationRegime(PSTATE.EL); ss = CurrentSecurityState(); walkparams = AArch64.GetS1TTWParams(regime, PSTATE.EL, ss, Replicate(top_bit, 64)); bottom_PAC_bit = 64 -UInt(AArch64.PACEffectiveTxSZ(regime, walkparams)); return bottom_PAC_bit;
```

## J1.1.3.192 ComputePAC

```
// ComputePAC() // ============ bits(64) ComputePAC(bits(64) data, bits(64) modifier, bits(64) key0, bits(64) key1) if IsFeatureImplemented(FEAT_PACIMP) then return ComputePACIMPDEF(data, modifier, key0, key1); if IsFeatureImplemented(FEAT_PACQARMA3) then constant boolean isqarma3 = TRUE; return ComputePACQARMA(data, modifier, key0, key1, isqarma3); if IsFeatureImplemented(FEAT_PACQARMA5) then constant boolean isqarma3 = FALSE; return ComputePACQARMA(data, modifier, key0, key1, isqarma3); Unreachable();
```

## J1.1.3.193 ComputePAC2

```
// ComputePAC2() // ============= bits(64) ComputePAC2(bits(64) data, bits(64) modifier1, bits(64) modifier2, bits(64) key0, bits(64) key1) if IsFeatureImplemented(FEAT_PACIMP) then return ComputePAC2IMPDEF(data, modifier1, modifier2, key0, key1); if IsFeatureImplemented(FEAT_PACQARMA3) then constant boolean isqarma3 = TRUE; return ComputePAC2QARMA(data, modifier1, modifier2, key0, key1, isqarma3); if IsFeatureImplemented(FEAT_PACQARMA5) then constant boolean isqarma3 = FALSE; return ComputePAC2QARMA(data, modifier1, modifier2, key0, key1, isqarma3); Unreachable();
```

## J1.1.3.194 ComputePAC2IMPDEF

```
// ComputePAC2IMPDEF() // ================== // Compute IMPLEMENTATION DEFINED cryptographic algorithm to be used for PAC calculation. bits(64) ComputePAC2IMPDEF(bits(64) data, bits(64) modifier1, bits(64) modifier2, bits(64) key0, bits(64) key1);
```

## J1.1.3.195 ComputePAC2QARMA

```
// ComputePAC2QARMA() // ================== bits(64) ComputePAC2QARMA(bits(64) data, bits(64) modifier1, bits(64) modifier2, bits(64) key0, bits(64) key1, boolean isqarma3) constant bits(64) concat_modifiers = modifier2<36:5>:modifier1<35:4>; return ComputePACQARMA(data, concat_modifiers, key0, key1, isqarma3);
```

## J1.1.3.196 ComputePACIMPDEF

```
// ComputePACIMPDEF() // ================== // Compute IMPLEMENTATION DEFINED cryptographic algorithm to be used for PAC calculation. bits(64) ComputePACIMPDEF(bits(64) data, bits(64) modifier, bits(64) key0, bits(64) key1);
```

## J1.1.3.197 ComputePACQARMA

```
// ComputePACQARMA() // ================= // Compute QARMA3 or QARMA5 cryptographic algorithm for PAC calculation bits(64) ComputePACQARMA(bits(64) data, bits(64) modifier, bits(64) key0, bits(64) key1, boolean isqarma3) bits(64) workingval; bits(64) runningmod; bits(64) roundkey; bits(64) modk0; constant bits(64) Alpha = 0xC0AC29B7C97C50DD<63:0>; integer iterations; RC[0] = 0x0000000000000000<63:0>; RC[1] = 0x13198A2E03707344<63:0>; RC[2] = 0xA4093822299F31D0<63:0>; if isqarma3 then iterations = 2; else // QARMA5 iterations = 4; RC[3] = 0x082EFA98EC4E6C89<63:0>; RC[4] = 0x452821E638D01377<63:0>; modk0 = key0<0>:key0<63:2>:(key0<63> EOR key0<1>); runningmod = modifier; workingval = data EOR key0; for i = 0 to iterations roundkey = key1 EOR runningmod; workingval = workingval EOR roundkey; workingval = workingval EOR RC[i];
```

```
if i > 0 then workingval = PACCellShuffle(workingval); workingval = PACMult(workingval); if isqarma3 then workingval = PACSub1(workingval); else workingval = PACSub(workingval); runningmod = TweakShuffle(runningmod<63:0>); roundkey = modk0 EOR runningmod; workingval = workingval EOR roundkey; workingval = PACCellShuffle(workingval); workingval = PACMult(workingval); if isqarma3 then workingval = PACSub1(workingval); else workingval = PACSub(workingval); workingval = PACCellShuffle(workingval); workingval = PACMult(workingval); workingval = key1 EOR workingval; workingval = PACCellInvShuffle(workingval); if isqarma3 then workingval = PACSub1(workingval); else workingval = PACInvSub(workingval); workingval = PACMult(workingval); workingval = PACCellInvShuffle(workingval); workingval = workingval EOR key0; workingval = workingval EOR runningmod; for i = 0 to iterations if isqarma3 then workingval = PACSub1(workingval); else workingval = PACInvSub(workingval); if i < iterations then workingval = PACMult(workingval); workingval = PACCellInvShuffle(workingval); runningmod = TweakInvShuffle(runningmod<63:0>); roundkey = key1 EOR runningmod; workingval = workingval EOR RC[iterations-i]; workingval = workingval EOR roundkey; workingval = workingval EOR Alpha; workingval = workingval EOR modk0; return workingval;
```

## J1.1.3.198 PACCellInvShuffle

```
// PACCellInvShuffle() // =================== bits(64) PACCellInvShuffle(bits(64) indata) bits(64) outdata; outdata<3:0> = indata<15:12>; outdata<7:4> = indata<27:24>; outdata<11:8> = indata<51:48>; outdata<15:12> = indata<39:36>; outdata<19:16> = indata<59:56>; outdata<23:20> = indata<47:44>; outdata<27:24> = indata<7:4>; outdata<31:28> = indata<19:16>; outdata<35:32> = indata<35:32>; outdata<39:36> = indata<55:52>; outdata<43:40> = indata<31:28>; outdata<47:44> = indata<11:8>; outdata<51:48> = indata<23:20>;
```

```
outdata<55:52> = indata<3:0>; outdata<59:56> = indata<43:40>; outdata<63:60> = indata<63:60>; return outdata;
```

## J1.1.3.199 PACCellShuffle

```
// PACCellShuffle() // ================ bits(64) PACCellShuffle(bits(64) indata) bits(64) outdata; outdata<3:0> = indata<55:52>; outdata<7:4> = indata<27:24>; outdata<11:8> = indata<47:44>; outdata<15:12> = indata<3:0>; outdata<19:16> = indata<31:28>; outdata<23:20> = indata<51:48>; outdata<27:24> = indata<7:4>; outdata<31:28> = indata<43:40>; outdata<35:32> = indata<35:32>; outdata<39:36> = indata<15:12>; outdata<43:40> = indata<59:56>; outdata<47:44> = indata<23:20>; outdata<51:48> = indata<11:8>; outdata<55:52> = indata<39:36>; outdata<59:56> = indata<19:16>; outdata<63:60> = indata<63:60>; return outdata;
```

## J1.1.3.200 PACInvSub

```
// PACInvSub() // =========== bits(64) PACInvSub(bits(64) Tinput) // This is a 4-bit substitution from the PRINCE-family bits(64) Toutput; for i = 0 to 15 case Elem[Tinput, i, 4] of when '0000' Elem[Toutput, i, 4] = '0101'; when '0001' Elem[Toutput, i, 4] = '1110'; when '0010' Elem[Toutput, i, 4] = '1101'; when '0011' Elem[Toutput, i, 4] = '1000'; when '0100' Elem[Toutput, i, 4] = '1010'; when '0101' Elem[Toutput, i, 4] = '1011'; when '0110' Elem[Toutput, i, 4] = '0001'; when '0111' Elem[Toutput, i, 4] = '1001'; when '1000' Elem[Toutput, i, 4] = '0010'; when '1001' Elem[Toutput, i, 4] = '0110'; when '1010' Elem[Toutput, i, 4] = '1111'; when '1011' Elem[Toutput, i, 4] = '0000'; when '1100' Elem[Toutput, i, 4] = '0100'; when '1101' Elem[Toutput, i, 4] = '1100'; when '1110' Elem[Toutput, i, 4] = '0111'; when '1111' Elem[Toutput, i, 4] = '0011'; return Toutput;
```

```
cipher
```

## J1.1.3.201 PACMult

```
// PACMult() // ========= bits(64) PACMult(bits(64) Sinput) bits(4) t0; bits(4) t1; bits(4) t2; bits(4) t3; bits(64) Soutput; for i = 0 to 3 t0<3:0> = ROL(Elem[Sinput, (i+8), 4], 1) EOR ROL(Elem[Sinput, (i+4), 4], 2); t0<3:0> = t0<3:0> EOR ROL(Elem[Sinput, i, 4], 1); t1<3:0> = ROL(Elem[Sinput, (i+12), 4], 1) EOR ROL(Elem[Sinput, (i+4), 4], 1); t1<3:0> = t1<3:0> EOR ROL(Elem[Sinput, i, 4], 2); t2<3:0> = ROL(Elem[Sinput, (i+12), 4], 2) EOR ROL(Elem[Sinput, (i+8), 4], 1); t2<3:0> = t2<3:0> EOR ROL(Elem[Sinput, i, 4], 1); t3<3:0> = ROL(Elem[Sinput, (i+12), 4], 1) EOR ROL(Elem[Sinput, (i+8), 4], 2); t3<3:0> = t3<3:0> EOR ROL(Elem[Sinput, (i+4), 4], 1); Elem[Soutput, i, 4] = t3<3:0>; Elem[Soutput, (i+4), 4] = t2<3:0>; Elem[Soutput, (i+8), 4] = t1<3:0>; Elem[Soutput, (i+12), 4] = t0<3:0>; return Soutput;
```

```
J1.1.3.202 PACSub // PACSub() // ======== bits(64) PACSub(bits(64) Tinput) // This is a 4-bit substitution from the PRINCE-family cipher bits(64) Toutput; for i = 0 to 15 case Elem[Tinput, i, 4] of when '0000' Elem[Toutput, i, 4] = '1011'; when '0001' Elem[Toutput, i, 4] = '0110'; when '0010' Elem[Toutput, i, 4] = '1000'; when '0011' Elem[Toutput, i, 4] = '1111'; when '0100' Elem[Toutput, i, 4] = '1100'; when '0101' Elem[Toutput, i, 4] = '0000'; when '0110' Elem[Toutput, i, 4] = '1001'; when '0111' Elem[Toutput, i, 4] = '1110'; when '1000' Elem[Toutput, i, 4] = '0011'; when '1001' Elem[Toutput, i, 4] = '0111'; when '1010' Elem[Toutput, i, 4] = '0100'; when '1011' Elem[Toutput, i, 4] = '0101'; when '1100' Elem[Toutput, i, 4] = '1101'; when '1101' Elem[Toutput, i, 4] = '0010'; when '1110' Elem[Toutput, i, 4] = '0001'; when '1111' Elem[Toutput, i, 4] = '1010'; return Toutput; J1.1.3.203 PacSub1 // PacSub1() // ========= bits(64) PACSub1(bits(64) Tinput) // This is a 4-bit substitution from Qarma sigma1 bits(64) Toutput;
```

```
for i = 0 to 15 case Elem[Tinput, i, 4] of when '0000' Elem[Toutput, i, 4] = '1010'; when '0001' Elem[Toutput, i, 4] = '1101'; when '0010' Elem[Toutput, i, 4] = '1110'; when '0011' Elem[Toutput, i, 4] = '0110'; when '0100' Elem[Toutput, i, 4] = '1111'; when '0101' Elem[Toutput, i, 4] = '0111'; when '0110' Elem[Toutput, i, 4] = '0011'; when '0111' Elem[Toutput, i, 4] = '0101'; when '1000' Elem[Toutput, i, 4] = '1001'; when '1001' Elem[Toutput, i, 4] = '1000'; when '1010' Elem[Toutput, i, 4] = '0000'; when '1011' Elem[Toutput, i, 4] = '1100'; when '1100' Elem[Toutput, i, 4] = '1011'; when '1101' Elem[Toutput, i, 4] = '0001'; when '1110' Elem[Toutput, i, 4] = '0010'; when '1111' Elem[Toutput, i, 4] = '0100'; return Toutput; J1.1.3.204 RC // RC[] // ==== array bits(64) RC[0..4]; J1.1.3.205 TweakCellInvRot // TweakCellInvRot() // ================= bits(4) TweakCellInvRot(bits(4) incell) bits(4) outcell; outcell<3> = incell<2>; outcell<2> = incell<1>; outcell<1> = incell<0>; outcell<0> = incell<0> EOR incell<3>; return outcell; J1.1.3.206 TweakCellRot // TweakCellRot() // ============== bits(4) TweakCellRot(bits(4) incell) bits(4) outcell; outcell<3> = incell<0> EOR incell<1>; outcell<2> = incell<3>; outcell<1> = incell<2>; outcell<0> = incell<1>; return outcell; J1.1.3.207 TweakInvShuffle indata)
```

```
// TweakInvShuffle() // ================= bits(64) TweakInvShuffle(bits(64) bits(64) outdata;
```

```
outdata<3:0> = TweakCellInvRot(indata<51:48>); outdata<7:4> = indata<55:52>; outdata<11:8> = indata<23:20>; outdata<15:12> = indata<27:24>; outdata<19:16> = indata<3:0>; outdata<23:20> = indata<7:4>; outdata<27:24> = TweakCellInvRot(indata<11:8>); outdata<31:28> = indata<15:12>; outdata<35:32> = outdata<39:36> = outdata<43:40> = outdata<47:44> = outdata<51:48> = indata<35:32>; outdata<55:52> = indata<39:36>; outdata<59:56> = indata<43:40>; outdata<63:60> = return outdata;
```

```
// IsAPDAKeyEnabled() // ================== // Returns TRUE if authentication using the APDAKey_EL1 key is enabled. // Otherwise, depending on the state of the PE, generate a trap, or boolean IsAPDAKeyEnabled() boolean TrapEL2; boolean TrapEL3; bits(1) Enable; case PSTATE.EL of when EL0 constant boolean IsEL1Regime = S1TranslationRegime() == EL1; Enable = if IsEL1Regime then SCTLR_EL1.EnDA else SCTLR_EL2.EnDA; TrapEL2 = EL2Enabled() && HCR_EL2.API == '0' && !IsInHost(); TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL1 Enable = SCTLR_EL1.EnDA;
```

## TweakCellInvRot(indata&lt;31:28&gt;); TweakCellInvRot(indata&lt;63:60&gt;); TweakCellInvRot(indata&lt;59:56&gt;); TweakCellInvRot(indata&lt;19:16&gt;); TweakCellInvRot(indata&lt;47:44&gt;); J1.1.3.208 TweakShuffle // TweakShuffle() // ============== bits(64) TweakShuffle(bits(64) indata) bits(64) outdata; outdata&lt;3:0&gt; = indata&lt;19:16&gt;; outdata&lt;7:4&gt; = indata&lt;23:20&gt;; outdata&lt;11:8&gt; = TweakCellRot(indata&lt;27:24&gt;); outdata&lt;15:12&gt; = indata&lt;31:28&gt;; outdata&lt;19:16&gt; = TweakCellRot(indata&lt;47:44&gt;); outdata&lt;23:20&gt; = indata&lt;11:8&gt;; outdata&lt;27:24&gt; = indata&lt;15:12&gt;; outdata&lt;31:28&gt; = TweakCellRot(indata&lt;35:32&gt;); outdata&lt;35:32&gt; = indata&lt;51:48&gt;; outdata&lt;39:36&gt; = indata&lt;55:52&gt;; outdata&lt;43:40&gt; = indata&lt;59:56&gt;; outdata&lt;47:44&gt; = TweakCellRot(indata&lt;63:60&gt;); outdata&lt;51:48&gt; = TweakCellRot(indata&lt;3:0&gt;); outdata&lt;55:52&gt; = indata&lt;7:4&gt;; outdata&lt;59:56&gt; = TweakCellRot(indata&lt;43:40&gt;); outdata&lt;63:60&gt; = TweakCellRot(indata&lt;39:36&gt;); return outdata; J1.1.3.209 IsAPDAKeyEnabled return FALSE.

```
TrapEL2 = EL2Enabled() && HCR_EL2.API == '0'; TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL2 Enable = SCTLR_EL2.EnDA; TrapEL2 = FALSE; TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL3 Enable = SCTLR_EL3.EnDA; TrapEL2 = FALSE; TrapEL3 = FALSE; if Enable == '0' then return FALSE; elsif TrapEL3 && EL3SDDUndefPriority() then UNDEFINED; elsif TrapEL2 then TrapPACUse(EL2); elsif TrapEL3 then if EL3SDDUndef() then UNDEFINED; else TrapPACUse(EL3); else return TRUE;
```

## J1.1.3.210 IsAPDBKeyEnabled

```
// IsAPDBKeyEnabled() // ================== // Returns TRUE if authentication using the APDBKey_EL1 key is enabled. // Otherwise, depending on the state of the PE, generate a trap, or return FALSE. boolean IsAPDBKeyEnabled() boolean TrapEL2; boolean TrapEL3; bits(1) Enable; case PSTATE.EL of when EL0 constant boolean IsEL1Regime = S1TranslationRegime() == EL1; Enable = if IsEL1Regime then SCTLR_EL1.EnDB else SCTLR_EL2.EnDB; TrapEL2 = EL2Enabled() && HCR_EL2.API == '0' && !IsInHost(); TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL1 Enable = SCTLR_EL1.EnDB; TrapEL2 = EL2Enabled() && HCR_EL2.API == '0'; TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL2 Enable = SCTLR_EL2.EnDB; TrapEL2 = FALSE; TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL3 Enable = SCTLR_EL3.EnDB; TrapEL2 = FALSE; TrapEL3 = FALSE; if Enable == '0' then return FALSE; elsif TrapEL3 && EL3SDDUndefPriority() then UNDEFINED; elsif TrapEL2 then TrapPACUse(EL2); elsif TrapEL3 then if EL3SDDUndef() then UNDEFINED;
```

```
else TrapPACUse(EL3); else return TRUE;
```

## J1.1.3.211 IsAPIAKeyEnabled

```
// IsAPIAKeyEnabled() // ================== // Returns TRUE if authentication using the APIAKey_EL1 key is enabled. // Otherwise, depending on the state of the PE, generate a trap, or return FALSE. boolean IsAPIAKeyEnabled() boolean TrapEL2; boolean TrapEL3; bits(1) Enable; case PSTATE.EL of when EL0 constant boolean IsEL1Regime = S1TranslationRegime() == EL1; Enable = if IsEL1Regime then SCTLR_EL1.EnIA else SCTLR_EL2.EnIA; TrapEL2 = EL2Enabled() && HCR_EL2.API == '0' && !IsInHost(); TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL1 Enable = SCTLR_EL1.EnIA; TrapEL2 = EL2Enabled() && HCR_EL2.API == '0'; TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL2 Enable = SCTLR_EL2.EnIA; TrapEL2 = FALSE; TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL3 Enable = SCTLR_EL3.EnIA; TrapEL2 = FALSE; TrapEL3 = FALSE; if Enable == '0' then return FALSE; elsif TrapEL3 && EL3SDDUndefPriority() then UNDEFINED; elsif TrapEL2 then TrapPACUse(EL2); elsif TrapEL3 then if EL3SDDUndef() then UNDEFINED; else TrapPACUse(EL3); else return TRUE;
```

## J1.1.3.212 IsAPIBKeyEnabled

```
// IsAPIBKeyEnabled() // ================== // Returns TRUE if authentication using the APIBKey_EL1 key is enabled. // Otherwise, depending on the state of the PE, generate a trap, or return FALSE. boolean IsAPIBKeyEnabled() boolean TrapEL2; boolean TrapEL3; bits(1) Enable; case PSTATE.EL of
```

```
when EL0 constant boolean IsEL1Regime = S1TranslationRegime() == EL1; Enable = if IsEL1Regime then SCTLR_EL1.EnIB else SCTLR_EL2.EnIB; TrapEL2 = EL2Enabled() && HCR_EL2.API == '0' && !IsInHost(); TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL1 Enable = SCTLR_EL1.EnIB; TrapEL2 = EL2Enabled() && HCR_EL2.API == '0'; TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL2 Enable = SCTLR_EL2.EnIB; TrapEL2 = FALSE; TrapEL3 = HaveEL(EL3) && SCR_EL3.API == '0'; when EL3 Enable = SCTLR_EL3.EnIB; TrapEL2 = FALSE; TrapEL3 = FALSE; if Enable == '0' then return FALSE; elsif TrapEL3 && EL3SDDUndefPriority() then UNDEFINED; elsif TrapEL2 then TrapPACUse(EL2); elsif TrapEL3 then if EL3SDDUndef() then UNDEFINED; else TrapPACUse(EL3); else return TRUE;
```

## J1.1.3.213 IsPACMEnabled

```
// IsPACMEnabled() // =============== // Returns TRUE if the effects of the PACM instruction are enabled, otherwise FALSE. boolean IsPACMEnabled() assert IsFeatureImplemented(FEAT_PAuth) && IsFeatureImplemented(FEAT_PAuth_LR); if IsTrivialPACMImplementation() then return FALSE; boolean enabled; // EL2 could force the behavior at EL1 and EL0 to NOP. if PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !IsInHost() then enabled = IsHCRXEL2Enabled() && HCRX_EL2.PACMEn == '1'; else enabled = TRUE; // Otherwise, the SCTLR2_ELx bit determines the behavior. if enabled then bit enpacm_bit; case PSTATE.EL of when EL3 enpacm_bit = SCTLR2_EL3.EnPACM; when EL2 enpacm_bit = if IsSCTLR2EL2Enabled() then SCTLR2_EL2.EnPACM else '0'; when EL1 enpacm_bit = if IsSCTLR2EL1Enabled() then SCTLR2_EL1.EnPACM else '0'; when EL0 if IsInHost() then enpacm_bit = if IsSCTLR2EL2Enabled() then SCTLR2_EL2.EnPACM0 else '0';
```

## else enpacm\_bit = if IsSCTLR2EL1Enabled() then SCTLR2\_EL1.EnPACM0 else '0'; enabled = enpacm\_bit == '1'; return enabled; J1.1.3.214 IsTrivialPACMImplementation // IsTrivialPACMImplementation() // ============================= // Returns TRUE if the PE has a trivial implementation of PACM. boolean IsTrivialPACMImplementation() return (IsFeatureImplemented(FEAT\_PACIMP) &amp;&amp; boolean IMPLEMENTATION\_DEFINED "Trivial PSTATE.PACM implementation"); J1.1.3.215 PtrHasUpperAndLowerAddRanges // PtrHasUpperAndLowerAddRanges() // ============================== // Returns TRUE if the pointer has upper and lower address ranges, FALSE otherwise. boolean PtrHasUpperAndLowerAddRanges() regime = TranslationRegime(PSTATE.EL); return HasUnprivileged(regime); J1.1.3.216 Strip the pointer authentication

```
// Strip() // ======= // Strip() returns a 64-bit value containing A, but replacing // code field bits with the extension of the address bits. This can apply to either // instructions or data, where, as the use of tagged pointers is distinct, it might be // handled differently. bits(64) Strip(bits(64) A, boolean data) bits(64) original_ptr; bits(64) extfield; constant boolean tbi = EffectiveTBI(A, !data, PSTATE.EL) == '1'; constant boolean mtx = (IsFeatureImplemented(FEAT_MTE_NO_ADDRESS_TAGS) && EffectiveMTX(A, !data, PSTATE.EL) == '1'); constant AddressSize bottom_PAC_bit = CalculateBottomPACBit(A<55>); constant boolean EL3_using_lva3 = (IsFeatureImplemented(FEAT_LVA3) && TranslationRegime(PSTATE.EL) == Regime_EL3 && AArch64.IASize(TCR_EL3.T0SZ) > 52); if EL3_using_lva3 then extfield = Replicate('0', 64); else extfield = Replicate(A<55>, 64); if tbi then if (bottom_PAC_bit <= 55) then original_ptr = (A<63:56> : extfield<55:bottom_PAC_bit> : A<bottom_PAC_bit-1:0>); else original_ptr = A<63:56> : A<55:0>; elsif mtx then if (bottom_PAC_bit <= 55) then original_ptr = (extfield<63:60> : A<59:56> : extfield<55:bottom_PAC_bit> : A<bottom_PAC_bit-1:0>);
```

```
else original_ptr = extfield<63:60> : A<59:56> : A<55:0>; else original_ptr = extfield<63:bottom_PAC_bit> : A<bottom_PAC_bit-1:0>; return original_ptr;
```

## J1.1.3.217 TrapPACUse

```
// TrapPACUse() // ============ // Used for the trapping of the pointer authentication functions by higher exception // levels. TrapPACUse(bits(2) target_el) assert HaveEL(target_el) && target_el != EL0 && UInt(target_el) >= UInt(PSTATE.EL); constant bits(64) preferred_exception_return = ThisInstrAddr(64); ExceptionRecord except; vect_offset = 0; except = ExceptionSyndrome(Exception_PACTrap); AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

## J1.1.3.218 AArch64.RestrictPrediction

```
// AArch64.RestrictPrediction() // ============================ // Clear all predictions in the context. AArch64.RestrictPrediction(bits(64) val, RestrictType restriction) ExecutionCntxt c; target_el = val<25:24>; // If the target EL is not implemented or the instruction is executed at an // EL lower than the specified level, the instruction is treated as a NOP. if !HaveEL(target_el) || UInt(target_el) > UInt(PSTATE.EL) then ExecuteAsNOP(); constant bit ns = val<26>; constant bit nse = val<27>; ss = TargetSecurityState(ns, nse); // If the combination of Security state and Exception level is not implemented, // the instruction is treated as a NOP. if ss == SS_Root && target_el != EL3 then ExecuteAsNOP(); if !IsFeatureImplemented(FEAT_RME) && target_el == EL3 && ss != SS_Secure then ExecuteAsNOP(); c.security = ss; c.target_el = target_el; if EL2Enabled() then if (PSTATE.EL == EL0 && !IsInHost()) || PSTATE.EL == EL1 then c.is_vmid_valid = TRUE; c.all_vmid = FALSE; c.vmid = VMID[]; elsif (target_el == EL0 && !ELIsInHost(target_el)) || target_el == EL1 then c.is_vmid_valid = TRUE; c.all_vmid = val<48> == '1'; c.vmid = val<47:32>; // Only valid if val<48> == '0'; else
```

```
c.is_vmid_valid = FALSE; else c.is_vmid_valid = FALSE; if PSTATE.EL == EL0 then c.is_asid_valid = TRUE; c.all_asid = FALSE; c.asid = ASID[]; elsif target_el == EL0 then c.is_asid_valid = TRUE; c.all_asid = val<16> == '1'; c.asid = val<15:0>; // Only valid if val<16> == '0'; else c.is_asid_valid = FALSE; c.restriction = restriction; RESTRICT_PREDICTIONS(c);
```

```
J1.1.3.219 Prefetch // Prefetch() // ========== // Decode and execute the prefetch hint on ADDRESS specified by PRFOP Prefetch(bits(64) address, bits(5) prfop) PrefetchHint hint; integer target; boolean stream; case prfop<4:3> of when '00' hint = Prefetch_READ; // PLD: prefetch for load when '01' hint = Prefetch_EXEC; // PLI: preload instructions when '10' hint = Prefetch_WRITE; // PST: prepare for store when '11' return; // unallocated hint target = UInt(prfop<2:1>); // target cache level stream = (prfop<0> != '0'); // streaming (non-temporal) Hint_Prefetch(address, hint, target, stream); return; J1.1.3.220 PSTATEField {PSTATEField_DAIFSet, PSTATEField_DAIFClr,
```

```
// PSTATEField // =========== // MSR (immediate) instruction destinations. enumeration PSTATEField PSTATEField_PAN, // Armv8.1 PSTATEField_UAO, // Armv8.2 PSTATEField_DIT, // Armv8.4 PSTATEField_SSBS, PSTATEField_TCO, // Armv8.5 PSTATEField_SVCRSM, PSTATEField_SVCRZA, PSTATEField_SVCRSMZA, PSTATEField_ALLINT, PSTATEField_PM, PSTATEField_SP };
```

## J1.1.3.221 AArch64.DelegatedSErrorTarget

```
// AArch64.DelegatedSErrorTarget() // =============================== // Returns whether a delegated SError exception pended by SCR_EL3.VSE is masked, // and the target Exception level of the delegated SError exception. (boolean, bits(2)) AArch64.DelegatedSErrorTarget() assert IsFeatureImplemented(FEAT_E3DSE); if Halted() || PSTATE.EL == EL3 then return (TRUE, bits(2) UNKNOWN); constant bit effective_amo = EffectiveHCR_AMO(); constant bit effective_tge = EffectiveTGE(); // The exception is masked by software. boolean masked; case PSTATE.EL of when EL2 masked = ((effective_tge == '0' && effective_amo == '0') || PSTATE.A == '1'); when EL1, EL0 masked = (effective_amo == '0' && PSTATE.A == '1'); otherwise Unreachable(); // The exception might be disabled debug in the Security state indicated by // SCR_EL3.{NS, NSE} by external debug. constant boolean intdis = ExternalDebugInterruptsDisabled(EL1); bits(2) target_el = bits(2) UNKNOWN; if EL2Enabled() && effective_amo == '1' && !intdis && PSTATE.EL IN {EL0, EL1} then target_el = EL2; masked = FALSE; elsif (EffectiveHCRX_EL2_TMEA() == '1' && !intdis && ((PSTATE.EL == EL1 && PSTATE.A == '1') || (PSTATE.EL == EL0 && masked && !IsInHost()))) then target_el = EL2; masked = FALSE; elsif PSTATE.EL == EL2 || IsInHost() then if !masked then target_el = EL2; else assert (PSTATE.EL == EL1 || (PSTATE.EL == EL0 && !IsInHost())); if !masked then target_el = EL1; // External debug might disable the delegated exception for the target Exception level. if ExternalDebugInterruptsDisabled(target_el) then masked = TRUE; target_el = bits(2) UNKNOWN; return (masked, target_el); J1.1.3.222 AArch64.ESBOperation or for
```

```
// AArch64.ESBOperation() // ====================== // Perform the AArch64 ESB operation, either for ESB executed in AArch64 state, // ESB in AArch32 state when SError interrupts are routed to an Exception level using // AArch64 AArch64.ESBOperation() bits(2) target_el;
```

```
boolean masked; (masked, target_el) = PhysicalSErrorTarget(); // Check for a masked Physical SError pending that can be synchronized // by an Error synchronization event. if masked && IsSynchronizablePhysicalSErrorPending() then // This function might be called for an interprocessing case, and INTdis is // the SError interrupt. if ELUsingAArch32(S1TranslationRegime()) then bits(32) syndrome = Zeros(32); syndrome<31> = '1'; // A syndrome<15:0> = AArch32.PhysicalSErrorSyndrome(); DISR = syndrome; else constant boolean implicit_esb = FALSE; constant boolean is_esb = TRUE; bits(64) syndrome = Zeros(64); syndrome<31> = '1'; // A syndrome<24:0> = AArch64.PhysicalSErrorSyndrome(is_esb, implicit_esb); DISR_EL1 = syndrome; ClearPendingPhysicalSError(); // Set ISR_EL1.A to 0 return;
```

```
// AArch64.EncodeSyncErrorSyndrome() // ================================= // Return the encoding for specified ErrorState for a synchronous // exception taken to AArch64 state. bits(2) AArch64.EncodeSyncErrorSyndrome(ErrorState errorstate) case errorstate of when ErrorState_UC return '10'; when ErrorState_UEU return '10'; // UEU is reported as UC when ErrorState_UEO return '11'; when ErrorState_UER return '00'; otherwise Unreachable();
```

## masking J1.1.3.223 AArch64.EncodeAsyncErrorSyndrome // AArch64.EncodeAsyncErrorSyndrome() // ================================== // Return the encoding for specified ErrorState for an SError exception taken // to AArch64 state. bits(3) AArch64.EncodeAsyncErrorSyndrome(ErrorState errorstate) case errorstate of when ErrorState\_UC return '000'; when ErrorState\_UEU return '001'; when ErrorState\_UEO return '010'; when ErrorState\_UER return '011'; when ErrorState\_CE return '110'; otherwise Unreachable(); J1.1.3.224 AArch64.EncodeSyncErrorSyndrome Abort

## J1.1.3.225 AArch64.PhysicalSErrorSyndrome

```
// AArch64.PhysicalSErrorSyndrome() // ================================ // Generate SError syndrome. bits(25) AArch64.PhysicalSErrorSyndrome(boolean is_esb, boolean implicit_esb) bits(25) syndrome = Zeros(25); bits(2) target_el; (-, target_el) = PhysicalSErrorTarget(); if ReportErrorAsUncategorized() then syndrome = Zeros(25); elsif ReportErrorAsIMPDEF() then syndrome<24> = '1'; // IDS syndrome<23:0> = bits(24) IMPLEMENTATION_DEFINED "IMPDEF ErrorState"; else constant FaultRecord fault = GetPendingPhysicalSError(); constant ErrorState errorstate = PEErrorState(fault); syndrome<24> = '0'; // IDS if (!is_esb && IsFeatureImplemented(FEAT_PFAR) && !(EL2Enabled() && (HCR_EL2.VM == '1' || HCR_EL2.DC == '1') && target_el == EL1)) then syndrome<14> = if IsPFARValid(fault) then '1' else '0'; syndrome<13> = if implicit_esb then '1' else '0'; // IESB syndrome<12:10> = AArch64.EncodeAsyncErrorSyndrome(errorstate); // AET syndrome<9> = fault.extflag; // EA syndrome<5:0> = '010001'; // DFSC return syndrome;
```

```
J1.1.3.226 AArch64.dESBOperation // AArch64.dESBOperation() // ======================= // Perform the AArch64 ESB operation for a pending delegated SError exception. AArch64.dESBOperation() assert (IsFeatureImplemented(FEAT_E3DSE) && !ELUsingAArch32(EL3) && PSTATE.EL != EL3); // When FEAT_E3DSE is implemented, SCR_EL3.DSE might inject a delegated SError exception. boolean dsei_pending, dsei_masked; dsei_pending = SCR_EL3.<EnDSE,DSE> == '11'; (dsei_masked, -) = AArch64.DelegatedSErrorTarget(); if dsei_pending && dsei_masked then bits(64) target = Zeros(64); target<31> = '1'; // A target<24:0> = VSESR_EL3<24:0>; VDISR_EL3 = target; ClearPendingDelegatedSError(); return; J1.1.3.227 AArch64.vESBOperation // AArch64.vESBOperation() // ======================= // Perform the AArch64 ESB operation for an unmasked pending virtual SError exception. // If FEAT_E3DSE is implemented and there is no unmasked virtual SError exception // pending, then AArch64.dESBOperation() is called to perform the AArch64 ESB operation // for a pending delegated SError exception. AArch64.vESBOperation() assert PSTATE.EL IN {EL0, EL1} && EL2Enabled() && !ELUsingAArch32(EL2); // If physical SError exceptions are routed to EL2, and TGE is not set, then a virtual
```

```
// SError exception might be pending. vsei_pending = (IsVirtualSErrorPending() && EffectiveTGE() == '0' && (EffectiveHCR_AMO() == '1' || EffectiveHCRX_EL2_TMEA() == '1')); vsei_masked = PSTATE.A == '1' || Halted() || ExternalDebugInterruptsDisabled(EL1); // Check for a masked virtual SError pending if vsei_pending && vsei_masked then // This function might be called for the interprocessing case, and INTdis is masking // the virtual SError exception. if ELUsingAArch32(EL1) then bits(32) target = Zeros(32); target<31> = '1'; // A target<15:14> = VDFSR<15:14>; // AET target<12> = VDFSR<12>; // ExT target<9> = TTBCR.EAE; // LPAE if TTBCR.EAE == '1' then // Long-descriptor format target<5:0> = '010001'; // STATUS else // Short-descriptor format target<10,3:0> = '10110'; // FS VDISR = target; else bits(64) target = Zeros(64); target<31> = '1'; // A target<24:0> = VSESR_EL2<24:0>; VDISR_EL2 = target; ClearPendingVirtualSError(); elsif IsFeatureImplemented(FEAT_E3DSE) then AArch64.dESBOperation(); return;
```

```
// IsCommonFaultInjectionImplemented() // =================================== // Check if the Common Fault Injection Model Extension is implemented by the node that owns this // error record. boolean IsCommonFaultInjectionImplemented(integer n);
```

```
// IsCountableErrorsRecorded() // =========================== // Check whether Error record n records countable boolean IsCountableErrorsRecorded(integer n);
```

## J1.1.3.228 FirstRecordOfNode // FirstRecordOfNode() // =================== // Return the first record in the node that contains the record n. integer FirstRecordOfNode(integer n) for q = n downto 0 if IsFirstRecordOfNode(q) then return q; Unreachable(); J1.1.3.229 IsCommonFaultInjectionImplemented J1.1.3.230 IsCountableErrorsRecorded errors.

## J1.1.3.231 IsErrorAddressIncluded

```
// IsErrorAddressIncluded() // ======================== // Check whether Error record n includes an address associated with an error. boolean IsErrorAddressIncluded(integer n);
```

## J1.1.3.232 IsErrorRecordImplemented

```
// IsErrorRecordImplemented() // ========================== // Is the error record n implemented boolean IsErrorRecordImplemented(integer n);
```

## J1.1.3.233 IsFirstRecordOfNode

```
// IsFirstRecordOfNode() // ===================== // Check if the record q is the first error record in its node. boolean IsFirstRecordOfNode(integer q);
```

## J1.1.3.234 IsPFARValid

```
// IsPFARValid() // ============= // Determine if faulting PA can be reported. boolean IsPFARValid(FaultRecord fault);
```

## J1.1.3.235 IsSPMUCounterImplemented

```
// IsSPMUCounterImplemented() // ========================== // Does the System PMU s implement the counter n. boolean IsSPMUCounterImplemented(integer s, integer n);
```

## J1.1.3.236 ProtectionEnabled

```
// ProtectionEnabled() // =================== // Returns TRUE if the ProtectedBit is // enabled in the current Exception level. boolean ProtectionEnabled(bits(2) el) assert HaveEL(el); regime = S1TranslationRegime(el); assert(!ELUsingAArch32(regime)); if (!IsD128Enabled(el)) then case regime of when EL1 return IsTCR2EL1Enabled() && TCR2_EL1.PnCH == '1'; when EL2 return IsTCR2EL2Enabled() && TCR2_EL2.PnCH == '1'; when EL3
```

```
return TCR_EL3.PnCH == '1'; else return TRUE; return FALSE;
```

## J1.1.3.237 RCW128\_PROTECTED\_BIT

```
constant integer RCW128_PROTECTED_BIT = 114;
```

## J1.1.3.238 RCW64\_PROTECTED\_BIT

```
constant integer RCW64_PROTECTED_BIT = 52;
```

## J1.1.3.239 RCWCheck

```
// RCWCheck() // ========== // Returns nzcv based on : if the new value for RCW/RCWS instructions satisfy RCW and/or RCWS checks // Z is set to 1 if RCW checks fail // C is set to 0 if RCWS checks fail bits(4) RCWCheck(bits(N) old, bits(N) new, boolean soft) assert N IN {64,128}; constant integer protectedbit = if N == 128 then RCW128_PROTECTED_BIT else RCW64_PROTECTED_BIT; boolean rcw_fail = FALSE; boolean rcws_fail = FALSE; boolean rcw_state_fail = FALSE; boolean rcws_state_fail = FALSE; boolean rcw_mask_fail = FALSE; boolean rcws_mask_fail = FALSE; //Effective RCWMask calculation bits(N) rcwmask = RCWMASK_EL1<N-1:0>; if N == 64 then rcwmask<49:18> = Replicate(rcwmask<17>, 32); rcwmask<0> = '0'; else rcwmask<55:17> = Replicate(rcwmask<16>, 39); rcwmask<126:125,120:119,107:101,90:56,1:0> = Zeros(48); //Effective RCWSMask calculation bits(N) rcwsoftmask = RCWSMASK_EL1<N-1:0>; if N == 64 then rcwsoftmask<49:18> = Replicate(rcwsoftmask<17>, 32); rcwsoftmask<0> = '0'; if(ProtectionEnabled(PSTATE.EL)) then rcwsoftmask<52> = '0'; else rcwsoftmask<55:17> = Replicate(rcwsoftmask<16>, 39); rcwsoftmask<126:125,120:119,107:101,90:56,1:0> = Zeros(48); rcwsoftmask<114> = '0'; //RCW Checks //State Check if (ProtectionEnabled(PSTATE.EL)) then if old<protectedbit> == '1' then rcw_state_fail = new<protectedbit,0> != old<protectedbit,0>; elsif old<protectedbit> == '0' then rcw_state_fail = new<protectedbit> != old<protectedbit>; //Mask Check
```

```
if (ProtectionEnabled(PSTATE.EL)) then if old<protectedbit,0> == '11' then rcw_mask_fail = !IsZero((new EOR old) AND NOT(rcwmask)); //RCWS Checks if soft then //State Check if old<0> == '1' then rcws_state_fail = new<0> != old<0>; elsif (!ProtectionEnabled(PSTATE.EL) || (ProtectionEnabled(PSTATE.EL) && old<protectedbit> == rcws_state_fail = new<0> != old<0> ; //Mask Check if old<0> == '1' then rcws_mask_fail = !IsZero((new EOR old) AND NOT(rcwsoftmask)); rcw_fail = rcw_state_fail || rcw_mask_fail ; rcws_fail = rcws_state_fail || rcws_mask_fail; constant bit n = '0'; constant bit z = if rcw_fail then '1' else '0'; constant bit c = if rcws_fail then '0' else '1'; constant bit v = '0'; return n:z:c:v;
```

```
// IntReduce() // =========== // Perform the integer operation 'op' on pairs of elements from the input // reducing the vector to a scalar result.
```

```
'0')) then J1.1.3.240 FPReduce // FPReduce() // ========== // Perform the floating-point operation 'op' on pairs of elements from the input vector, // reducing the vector to a scalar result. bits(esize) FPReduce(ReduceOp op, bits(N) input, integer esize, FPCR_Type fpcr) bits(esize) hi; bits(esize) lo; bits(esize) result; constant integer half = N DIV 2; if N == esize then return input<esize-1:0>; hi = FPReduce(op, input<N-1:half>, esize, fpcr); lo = FPReduce(op, input<half-1:0>, esize, fpcr); case op of when ReduceOp_FMINNUM result = FPMinNum(lo, hi, fpcr); when ReduceOp_FMAXNUM result = FPMaxNum(lo, hi, fpcr); when ReduceOp_FMIN result = FPMin(lo, hi, fpcr); when ReduceOp_FMAX result = FPMax(lo, hi, fpcr); when ReduceOp_FADD result = FPAdd(lo, hi, fpcr); return result; J1.1.3.241 IntReduce vector,
```

## bits(esize) IntReduce(ReduceOp op, bits(N) input, integer esize) bits(esize) hi; bits(esize) lo; bits(esize) result; constant integer half = N DIV 2; if N == esize then return input&lt;esize-1:0&gt;; hi = IntReduce(op, input&lt;N-1:half&gt;, esize); lo = IntReduce(op, input&lt;half-1:0&gt;, esize); case op of when ReduceOp\_ADD result = lo + hi; return result; J1.1.3.242 ReduceOp // ReduceOp // ======== // Vector reduce instruction types. enumeration ReduceOp {ReduceOp\_FMINNUM, ReduceOp\_FMAXNUM, ReduceOp\_FMIN, ReduceOp\_FMAX, ReduceOp\_FADD, ReduceOp\_ADD}; J1.1.3.243 AArch64.MaybeZeroRegisterUppers // AArch64.MaybeZeroRegisterUppers() // ================================= // On taking an exception to AArch64 from AArch32, it is CONSTRAINED UNPREDICTABLE whether the top // 32 bits of registers visible at any lower Exception level using AArch32 are set to zero. AArch64.MaybeZeroRegisterUppers() assert UsingAArch32(); // Always called from AArch32 state before entering AArch64 state integer first; integer last; boolean include\_R15; if PSTATE.EL == EL0 &amp;&amp; !ELUsingAArch32(EL1) then first = 0; last = 14; include\_R15 = FALSE; elsif PSTATE.EL IN {EL0, EL1} &amp;&amp; EL2Enabled() &amp;&amp; !ELUsingAArch32(EL2) then first = 0; last = 30; include\_R15 = FALSE; else first = 0; last = 30; include\_R15 = TRUE; for n = first to last if (n != 15 || include\_R15) &amp;&amp; ConstrainUnpredictableBool(Unpredictable\_ZEROUPPER) then \_R[n]&lt;63:32&gt; = Zeros(32); return; J1.1.3.244 AArch64.ResetGeneralRegisters // AArch64.ResetGeneralRegisters() // ===============================

```
AArch64.ResetGeneralRegisters() for i = 0 to 30
```

```
X[i, 64] = bits(64) UNKNOWN; return;
```

## J1.1.3.245 AArch64.ResetSIMDFPRegisters

```
// AArch64.ResetSIMDFPRegisters() // ============================== AArch64.ResetSIMDFPRegisters() for i = 0 to 31 V[i, 128] = bits(128) UNKNOWN; return;
```

## J1.1.3.246 AArch64.ResetSpecialRegisters

```
// AArch64.ResetSpecialRegisters() // =============================== AArch64.ResetSpecialRegisters() // AArch64 special registers SP_EL0 = bits(64) UNKNOWN; SP_EL1 = bits(64) UNKNOWN; SPSR_EL1 = bits(64) UNKNOWN; ELR_EL1 = bits(64) UNKNOWN; if HaveEL(EL2) then SP_EL2 = bits(64) UNKNOWN; SPSR_EL2 = bits(64) UNKNOWN; ELR_EL2 = bits(64) UNKNOWN; // AArch32 special registers that are not architecturally mapped to AArch64 registers if HaveAArch32EL(EL1) then SPSR_fiq<31:0> = bits(32) UNKNOWN; SPSR_irq<31:0> = bits(32) UNKNOWN; SPSR_abt<31:0> = bits(32) UNKNOWN; SPSR_und<31:0> = bits(32) UNKNOWN; // External debug special registers DLR_EL0 = bits(64) UNKNOWN; DSPSR_EL0 = bits(64) UNKNOWN; return;
```

## J1.1.3.247 AArch64.ResetSystemRegisters

```
// AArch64.ResetSystemRegisters() // ============================== AArch64.ResetSystemRegisters(boolean cold_reset);
```

## J1.1.3.248 PC64

```
// Program counter // +++++++++++++++ // PC64 -getter // ============= // Read 64-bit program bits(64) PC64 return _PC;
```

```
// SPMCGCR_EL1 -getter // ==================== // Read counter group 'n' configuration for System bits(64) SPMCGCR_EL1[integer s, integer n];
```

## counter. J1.1.3.249 SP // SP - setter // =========== // Write a 32-bit or 64-bit value to the current stack pointer. SP[integer width] = bits(width) value assert width IN {64, 32}; if PSTATE.SP == '0' then SP\_EL0 = ZeroExtend(value, 64); else case PSTATE.EL of when EL0 SP\_EL0 = ZeroExtend(value, 64); when EL1 SP\_EL1 = ZeroExtend(value, 64); when EL2 SP\_EL2 = ZeroExtend(value, 64); when EL3 SP\_EL3 = ZeroExtend(value, 64); return; // SP - getter // =========== // Read the least-significant 32 or 64 bits from the current stack pointer. bits(width) SP[integer width] assert width IN {64, 32}; if PSTATE.SP == '0' then return SP\_EL0&lt;width-1:0&gt;; else case PSTATE.EL of when EL0 return SP\_EL0&lt;width-1:0&gt;; when EL1 return SP\_EL1&lt;width-1:0&gt;; when EL2 return SP\_EL2&lt;width-1:0&gt;; when EL3 return SP\_EL3&lt;width-1:0&gt;; J1.1.3.250 SPMCFGR\_EL1 // SPMCFGR\_EL1 -getter // ==================== // Read the current configuration of System Performance monitor for // System PMU 's'. bits(64) SPMCFGR\_EL1[integer s]; J1.1.3.251 SPMCGCR\_EL1 PMU 's'.

## J1.1.3.252 SPMCNTENCLR\_EL0

## // SPMCNTENCLR\_EL0 - getter // ======================== // Read the current mapping of disabled event counters for an 's'. bits(64) SPMCNTENCLR\_EL0[integer s]; // SPMCNTENCLR\_EL0 - setter // ======================== // Disable event counters for System PMU 's'. SPMCNTENCLR\_EL0[integer s] = bits(64) value; J1.1.3.253 SPMCNTENSET\_EL0 // SPMCNTENSET\_EL0 - getter // ======================== // Read the current mapping for enabled event counters of System PMU 's'. bits(64) SPMCNTENSET\_EL0[integer s]; // SPMCNTENSET\_EL0 - setter // ======================== // Enable event counters of System PMU 's'. SPMCNTENSET\_EL0[integer s] = bits(64) value; J1.1.3.254 SPMCR\_EL0 // SPMCR\_EL0 - getter // ================== // Read the control register for System PMU 's'. bits(64) SPMCR\_EL0[integer s]; // SPMCR\_EL0 - setter // ================== // Write to the control register for System PMU 's'. SPMCR\_EL0[integer s] = bits(64) value; J1.1.3.255 SPMDEVAFF\_EL1 // SPMDEVAFF\_EL1 - getter // ====================== // Read the discovery information for System PMU 's'. bits(64) SPMDEVAFF\_EL1[integer s]; J1.1.3.256 SPMDEVARCH\_EL1 PMU 's'.

```
// SPMDEVARCH_EL1 - getter // ======================= // Read the discovery information for System bits(64) SPMDEVARCH_EL1[integer s];
```

## J1.1.3.257 SPMEVCNTR\_EL0

```
// SPMEVCNTR_EL0 - getter // ====================== // Read a System PMU Event Counter register for counter 'n' of a given // System PMU 's'. bits(64) SPMEVCNTR_EL0[integer s, integer n]; // SPMEVCNTR_EL0 - setter // ====================== // Write to a System PMU Event Counter register for counter 'n' of a given // System PMU 's'. SPMEVCNTR_EL0[integer s, integer n] = bits(64) value;
```

```
J1.1.3.258 SPMEVFILT2R_EL0 // SPMEVFILT2R_EL0 - getter // ======================== // Read the additional event selection controls for // counter 'n' of a given System PMU 's'. bits(64) SPMEVFILT2R_EL0[integer s, integer n]; // SPMEVFILT2R_EL0 - setter // ======================== // Configure the additional event selection controls for // counter 'n' of a given System PMU 's'. SPMEVFILT2R_EL0[integer s, integer n] = bits(64) value; J1.1.3.259 SPMEVFILTR_EL0 // SPMEVFILTR_EL0 - getter // ======================= // Read the additional event selection controls for // counter 'n' of a given System PMU 's'. bits(64) SPMEVFILTR_EL0[integer s, integer n]; // SPMEVFILTR_EL0 - setter // ======================= // Configure the additional event selection controls for // counter 'n' of a given System PMU 's'. SPMEVFILTR_EL0[integer s, integer n] = bits(64) value; J1.1.3.260 SPMEVTYPER_EL0
```

```
// SPMEVTYPER_EL0 - getter // ======================= // Read the current mapping of event with event counter SPMEVCNTR_EL0 // for counter 'n' of a given System PMU 's'. bits(64) SPMEVTYPER_EL0[integer s, integer n]; // SPMEVTYPER_EL0 - setter // ======================= // Configure which event increments the event counter SPMEVCNTR_EL0, for // counter 'n' of a given System PMU 's'.
```

```
SPMEVTYPER_EL0[integer s, integer n] = bits(64) value;
```

## J1.1.3.261 SPMIIDR\_EL1

```
// SPMIIDR_EL1 -getter // ==================== // Read the discovery information for System PMU 's'. bits(64) SPMIIDR_EL1[integer s];
```

## J1.1.3.262 SPMINTENCLR\_EL1

```
// SPMINTENCLR_EL1 - getter // ======================== // Read the masking information for interrupt requests on overflows of // implemented counters of System PMU 's'. bits(64) SPMINTENCLR_EL1[integer s]; // SPMINTENCLR_EL1 - setter // ======================== // Disable the generation of interrupt requests on overflows of // implemented counters of System PMU 's'. SPMINTENCLR_EL1[integer s] = bits(64) value;
```

## J1.1.3.263 SPMINTENSET\_EL1

```
// SPMINTENSET_EL1 - getter // ======================== // Read the masking information for interrupt requests on overflows of // implemented counters of System PMU 's'. bits(64) SPMINTENSET_EL1[integer s]; // SPMINTENSET_EL1 - setter // ======================== // Disable the generation of interrupt requests on overflows of // implemented counters for System PMU 's'. SPMINTENSET_EL1[integer s] = bits(64) value;
```

## J1.1.3.264 SPMOVSCLR\_EL0

```
// SPMOVSCLR_EL0 - getter // ====================== // Read the overflow bit clear status of implemented counters for System PMU 's'. bits(64) SPMOVSCLR_EL0[integer s]; // SPMOVSCLR_EL0 - setter // ====================== // Clear the overflow bit clear status of implemented counters for // System PMU 's'. SPMOVSCLR_EL0[integer s] = bits(64) value;
```

## J1.1.3.265 SPMOVSSET\_EL0

```
// SPMOVSSET_EL0 - getter // ====================== // Read state of the overflow bit for the implemented event counters // of System PMU 's'. bits(64) SPMOVSSET_EL0[integer s]; // SPMOVSSET_EL0 - setter // ====================== // Sets the state of the overflow bit for the implemented event counters // of System PMU 's'. SPMOVSSET_EL0[integer s] = bits(64) value;
```

## J1.1.3.266 SPMROOTCR\_EL3 // SPMROOTCR\_EL3 - getter // ====================== // Read the observability of Root and Realm events by System Performance // Monitor for System PMU 's'. bits(64) SPMROOTCR\_EL3[integer s]; // SPMROOTCR\_EL3 - setter // ====================== // Configure the observability of Root and Realm events by System // Performance Monitor for System PMU 's'. SPMROOTCR\_EL3[integer s] = bits(64) value; J1.1.3.267 SPMSCR\_EL1 // SPMSCR\_EL1 -getter // =================== // Read the observability of Secure events by System Performance Monitor // for System PMU 's'. bits(64) SPMSCR\_EL1[integer s]; // SPMSCR\_EL1 -setter // =================== // Configure the observability of secure events by System Performance // Monitor for System PMU 's'. SPMSCR\_EL1[integer s] = bits(64) value; J1.1.3.268 SPMZR\_EL0 // SPMZR\_EL0 - getter // ================== // Read SPMZR\_EL0. bits(64) SPMZR\_EL0[integer s]; // SPMZR\_EL0 - setter // ================== // Set event counters for System PMU 's' to zero. SPMZR\_EL0[integer s] = bits(64) value;

## J1.1.3.269 X

```
// X -setter // ========== // Write a 32-bit or 64-bit value to a general-purpose register. X[integer n, integer width] = bits(width) value assert n >= 0 && n <= 31; assert width IN {32,64}; if n != 31 then _R[n] = ZeroExtend(value, 64); return; // X -getter // ========== // Read the least-significant 8, 16, 32, or 64 bits from a general-purpose register. bits(width) X[integer n, integer width] assert n >= 0 && n <= 31; assert width IN {8, 16, 32, 64}; constant rw = width; if n != 31 then return _R[n]<rw-1:0>; else return Zeros(rw); // X -setter // ========== // Write a 128-bit value to two general-purpose registers. X[integer lr, integer hr, integer width] = bits(width) value assert width == 128; constant integer half = width DIV 2; X[lr, half] = value<0+:half>; X[hr, half] = value<half+:half>; return; // X -getter // ========== // Read 128 bits from two separate general-purpose registers. bits(width) X[integer lr, integer hr, integer width] assert width == 128; constant integer half = width DIV 2; return X[hr, half] : X[lr, half];
```

```
J1.1.3.270 DecodeShift
```

```
// DecodeShift() // ============= // Decode shift encodings ShiftType DecodeShift(bits(2) op) case op of when '00' return when '01' return when '10' return when '11' return
```

## J1.1.3.271

```
ShiftType_LSL; ShiftType_LSR; ShiftType_ASR; ShiftType_ROR;
```

ShiftReg

```
// ShiftReg() // ========== // Perform shift of a register operand bits(N) ShiftReg(integer reg, ShiftType shiftype, integer amount, bits(N) result = X[reg, N]; case shiftype of when ShiftType_LSL result = LSL(result, amount); when ShiftType_LSR result = LSR(result, amount); when ShiftType_ASR result = ASR(result, amount); when ShiftType_ROR result = ROR(result, amount); return result;
```

```
integer N)
```

## J1.1.3.272 ShiftType // ShiftType // ========= // AArch64 register shifts. enumeration ShiftType {ShiftType\_LSL, ShiftType\_LSR, ShiftType\_ASR, ShiftType\_ROR}; J1.1.3.273 CounterToPredicate == PL*4;

```
// CounterToPredicate() // ==================== bits(width) CounterToPredicate(bits(16) pred, integer width) integer count; ESize esize; integer elements; constant VecLen VL = CurrentVL; constant PredLen PL = VL DIV 8; constant integer maxbit = Log2(PL * 4); assert maxbit <= 14; bits(PL*4) result; constant boolean invert = pred<15> == '1'; assert width == PL || width == PL*2 || width == PL*3 || width case pred<3:0> of when '0000' return Zeros(width); when 'xxx1' count = UInt(pred<maxbit:1>); esize = 8; when 'xx10' count = UInt(pred<maxbit:2>); esize = 16; when 'x100' count = UInt(pred<maxbit:3>); esize = 32; when '1000' count = UInt(pred<maxbit:4>); esize = 64; elements = (VL * 4) DIV esize; result = Zeros(PL*4); constant integer psize = esize DIV 8; for e = 0 to elements-1 bit pbit = if e < count then '1' else '0'; if invert then
```

```
pbit = NOT(pbit); Elem[result, e, psize] = ZeroExtend(pbit, psize); return result<width-1:0>;
```

## J1.1.3.274 EncodePredCount

```
// EncodePredCount() // ================= bits(width) EncodePredCount(ESize esize, integer elements, integer count_in, boolean invert_in, integer width) integer count = count_in; boolean invert = invert_in; constant PredLen PL = CurrentVL DIV 8; assert width == PL; assert esize IN {8, 16, 32, 64}; assert count >=0 && count <= elements; bits(16) pred; if count == 0 then return Zeros(width); if invert then count = elements -count; elsif count == elements then count = 0; invert = TRUE; constant bit inv = (if invert then '1' else '0'); case esize of when 8 pred = inv : count<13:0> : '1'; when 16 pred = inv : count<12:0> : '10'; when 32 pred = inv : count<11:0> : '100'; when 64 pred = inv : count<10:0> : '1000'; return ZeroExtend(pred, width);
```

## J1.1.3.275 Lookup

```
// Lookup Table // ============ bits(ZT0_LEN) _ZT0;
```

## J1.1.3.276 PredCountTest

```
// PredCountTest() // =============== bits(4) PredCountTest(integer elements, integer count, boolean invert) bit n, z, c, v; z = (if count == 0 then '1' else '0'); // none active if !invert then n = (if count != 0 then '1' else '0'); // first active c = (if count == elements then '0' else '1'); // NOT last active else n = (if count == elements then '1' else '0'); // first active c = (if count != 0 then '0' else '1'); // NOT last active v = '0'; return n:z:c:v;
```

## J1.1.3.277 System

```
// System Registers // ================ array
```

```
bits(MAX_VL) _ZA[0..255]; J1.1.3.278 ZAhslice // ZAhslice - getter // ================= bits(width) ZAhslice[integer tile, ESize esize, integer slice, integer width] assert esize IN {8, 16, 32, 64, 128}; constant integer tiles = esize DIV 8; assert tile >= 0 && tile < tiles; constant integer slices = CurrentSVL DIV esize; assert slice >= 0 && slice < slices; return ZAvector[tile + slice * tiles, width]; // ZAhslice - setter // ================= ZAhslice[integer tile, ESize esize, integer slice, integer width] = bits(width) value assert esize IN {8, 16, 32, 64, 128}; constant integer tiles = esize DIV 8; assert tile >= 0 && tile < tiles; constant integer slices = CurrentSVL DIV esize; assert slice >= 0 && slice < slices; ZAvector[tile + slice * tiles, width] = value; J1.1.3.279 ZAslice
```

```
// ZAslice - getter // ================ bits(width) ZAslice[integer tile, ESize esize, boolean vertical, integer slice, integer width] bits(width) result; if vertical then result = ZAvslice[tile, esize, slice, width]; else result = ZAhslice[tile, esize, slice, width]; return result; // ZAslice - setter // ================ ZAslice[integer tile, ESize esize, boolean vertical, integer slice, integer width] = bits(width) value if vertical then ZAvslice[tile, esize, slice, width] = value; else ZAhslice[tile, esize, slice, width] = value;
```

## J1.1.3.280 ZAtile

```
// ZAtile -getter // =============== bits(width) ZAtile[integer tile, ESize esize, integer width] constant VecLen SVL = CurrentSVL; constant integer slices = SVL DIV esize; assert width == SVL * slices; bits(width) result; for slice = 0 to slices-1 Elem[result, slice, SVL] = ZAhslice[tile, esize, slice, SVL]; return result; // ZAtile -setter // =============== ZAtile[integer tile, ESize esize, integer width] = bits(width) value constant VecLen SVL = CurrentSVL; constant integer slices = SVL DIV esize; assert width == SVL * slices; for slice = 0 to slices-1 ZAhslice[tile, esize, slice, SVL] = Elem[value, slice, SVL];
```

## J1.1.3.281 ZAvector

```
// ZAvector - getter // ================= bits(width) ZAvector[integer index, integer width] assert width == CurrentSVL; assert index >= 0 && index < (width DIV 8); return _ZA[index]<width-1:0>; // ZAvector - setter // ================= ZAvector[integer index, integer width] = bits(width) value assert width == CurrentSVL; assert index >= 0 && index < (width DIV 8); if ConstrainUnpredictableBool(Unpredictable_SMEZEROUPPER) then _ZA[index] = ZeroExtend(value, MAX_VL); else _ZA[index]<width-1:0> = value;
```

## J1.1.3.282 ZAvslice

```
// ZAvslice - getter // ================= bits(width) ZAvslice[integer tile, ESize esize, integer slice, integer width] constant integer slices = CurrentSVL DIV esize; bits(width) result; for s = 0 to slices-1 constant bits(width) hslice = ZAhslice[tile, esize, s, width]; Elem[result, s, esize] = Elem[hslice, slice, esize];
```

```
return result; // ZAvslice - setter // ================= ZAvslice[integer tile, ESize esize, integer slice, integer width] = bits(width) constant integer slices = CurrentSVL DIV esize; for s = 0 to slices-1 bits(width) hslice = ZAhslice[tile, esize, s, width]; Elem[hslice, slice, esize] = Elem[value, s, esize]; ZAhslice[tile, esize, s, width] = hslice;
```

```
value J1.1.3.283 ZT0 // ZT0 - getter // ============ bits(width) ZT0[integer width] assert width == ZT0_LEN; return _ZT0<width-1:0>; // ZT0 - setter // ============ ZT0[integer width] = bits(width) value assert width == ZT0_LEN; _ZT0<width-1:0> = value; J1.1.3.284 AArch32.IsFPEnabled
```

```
// AArch32.IsFPEnabled() // ===================== // Returns TRUE if access to the SIMD&FP instructions or System registers are // enabled at the target exception level in AArch32 state and FALSE otherwise. boolean AArch32.IsFPEnabled(bits(2) el) if el == EL0 && !ELUsingAArch32(EL1) then return AArch64.IsFPEnabled(el); if HaveEL(EL3) && ELUsingAArch32(EL3) && CurrentSecurityState() == SS_NonSecure then // Check if access disabled in NSACR if NSACR.cp10 == '0' then return FALSE; if el IN {EL0, EL1} then // Check if access disabled in CPACR boolean disabled; case CPACR.cp10 of when '00' disabled = TRUE; when '01' disabled = el == EL0; when '10' disabled = ConstrainUnpredictableBool(Unpredictable_RESCPACR); when '11' disabled = FALSE; if disabled then return FALSE; if el IN {EL0, EL1, EL2} && EL2Enabled() then if !ELUsingAArch32(EL2) then return AArch64.IsFPEnabled(EL2); if HCPTR.TCP10 == '1' then return FALSE; if HaveEL(EL3) && !ELUsingAArch32(EL3) then // Check if access disabled in CPTR_EL3 if CPTR_EL3.TFP == '1' then return FALSE;
```

return TRUE;

## J1.1.3.285 AArch64.IsFPEnabled

```
// AArch64.IsFPEnabled() // ===================== // Returns TRUE if access to the SIMD&FP instructions or System registers are // enabled at the target exception level in AArch64 state and FALSE otherwise. boolean AArch64.IsFPEnabled(bits(2) el) // Check if access disabled in CPACR_EL1 if el IN {EL0, EL1} && !IsInHost() then // Check SIMD&FP at EL0/EL1 boolean disabled; case CPACR_EL1.FPEN of when 'x0' disabled = TRUE; when '01' disabled = el == EL0; when '11' disabled = FALSE; if disabled then return FALSE; // Check if access disabled in CPTR_EL2 if el IN {EL0, EL1, EL2} && EL2Enabled() then if ELIsInHost(EL2) then boolean disabled; case CPTR_EL2.FPEN of when 'x0' disabled = TRUE; when '01' disabled = el == EL0 && HCR_EL2.TGE == '1'; when '11' disabled = FALSE; if disabled then return FALSE; else if CPTR_EL2.TFP == '1' then return FALSE; // Check if access disabled in CPTR_EL3 if HaveEL(EL3) then if CPTR_EL3.TFP == '1' then return FALSE; return TRUE;
```

## J1.1.3.286 ActivePredicateElement

```
// ActivePredicateElement() // ======================== // Returns TRUE if the predicate bit is 1 and FALSE otherwise boolean ActivePredicateElement(bits(N) pred, integer e, integer esize) assert esize IN {8, 16, 32, 64, 128}; constant integer n = e * (esize DIV 8); assert n >= 0 && n < N; return pred<n> == '1';
```

## J1.1.3.287 AllElementsActive

```
// AllElementsActive() // =================== // Return TRUE if all the elements are active in the mask. Otherwise, // return FALSE. boolean AllElementsActive(bits(N) mask, integer esize) constant integer elements = N DIV (esize DIV 8); integer active = 0; for e = 0 to elements-1
```

```
if ActivePredicateElement(mask, e, esize) then active = active + 1; return active == elements;
```

## J1.1.3.288 AnyActiveElement

```
// AnyActiveElement() // ================== // Return TRUE if there is at least one active element // return FALSE. boolean AnyActiveElement(bits(N) mask, integer esize) return LastActiveElement(mask, esize) >= 0;
```

## J1.1.3.289 BitDeposit

```
// BitDeposit() // ============ // Deposit the least significant bits from DATA into result positions // selected by nonzero bits in MASK, setting other result bits to zero. bits(N) BitDeposit (bits(N) data, bits(N) mask) bits(N) res = Zeros(N); integer db = 0; for rb = 0 to N-1 if mask<rb> == '1' then res<rb> = data<db>; db = db + 1; return res;
```

## J1.1.3.290 BitExtract

```
// BitExtract() // ============ // Extract and pack DATA bits selected by the nonzero bits in MASK into // the least significant result bits, setting other result bits to zero. bits(N) BitExtract (bits(N) data, bits(N) mask) bits(N) res = Zeros(N); integer rb = 0; for db = 0 to N-1 if mask<db> == '1' then res<rb> = data<db>; rb = rb + 1; return res;
```

## J1.1.3.291 BitGroup

```
// BitGroup() // ========== // Extract and pack DATA bits selected by the nonzero bits in MASK into // the least significant result bits, and pack unselected bits into the // most significant result bits. bits(N) BitGroup (bits(N) data, bits(N) mask) bits(N) res; integer rb = 0; // compress masked bits to right for db = 0 to N-1 if mask<db> == '1' then
```

```
in mask. Otherwise,
```

```
res<rb> = data<db>; rb = rb + 1; // compress unmasked bits to left for db = 0 to N-1 if mask<db> == '0' then res<rb> = data<db>; rb = rb + 1; return res;
```

## J1.1.3.292 CheckNonStreamingSVEEnabled

```
// CheckNonStreamingSVEEnabled() // ============================= // Checks for traps on SVE instructions that are not legal when executed in Streaming mode. CheckNonStreamingSVEEnabled() CheckSVEEnabled(); if IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' && !IsFullA64Enabled() then SMEAccessTrap(SMEExceptionType_Streaming, PSTATE.EL);
```

## J1.1.3.293 CheckOriginalSVEEnabled

```
// CheckOriginalSVEEnabled() // ========================= // Checks for traps on SVE instructions and instructions that access SVE System // registers. CheckOriginalSVEEnabled() assert IsFeatureImplemented(FEAT_SVE); boolean disabled; if (HaveEL(EL3) && (CPTR_EL3.EZ == '0' || CPTR_EL3.TFP == '1') && EL3SDDUndefPriority()) then UNDEFINED; // Check if access disabled in CPACR_EL1 if PSTATE.EL IN {EL0, EL1} && !IsInHost() then // Check SVE at EL0/EL1 case CPACR_EL1.ZEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0; when '11' disabled = FALSE; if disabled then SVEAccessTrap(EL1); // Check SIMD&FP at EL0/EL1 case CPACR_EL1.FPEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0; when '11' disabled = FALSE; if disabled then AArch64.AdvSIMDFPAccessTrap(EL1); // Check if access disabled in CPTR_EL2 if PSTATE.EL IN {EL0, EL1, EL2} && EL2Enabled() then if ELIsInHost(EL2) then // Check SVE at EL2 case CPTR_EL2.ZEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0 && HCR_EL2.TGE == '1'; when '11' disabled = FALSE; if disabled then SVEAccessTrap(EL2); // Check SIMD&FP at EL2 case CPTR_EL2.FPEN of
```

```
when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0 && HCR_EL2.TGE == '1'; when '11' disabled = FALSE; if disabled then AArch64.AdvSIMDFPAccessTrap(EL2); else if CPTR_EL2.TZ == '1' then SVEAccessTrap(EL2); if CPTR_EL2.TFP == '1' then AArch64.AdvSIMDFPAccessTrap(EL2); // Check if access disabled in CPTR_EL3 if HaveEL(EL3) then if CPTR_EL3.EZ == '0' then if EL3SDDUndef() then UNDEFINED; SVEAccessTrap(EL3); if CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; AArch64.AdvSIMDFPAccessTrap(EL3);
```

## J1.1.3.294 CheckSMEAccess

```
// CheckSMEAccess() // ================ // Check that access to SME System registers is enabled. CheckSMEAccess() boolean disabled; if HaveEL(EL3) && CPTR_EL3.ESM == '0' && EL3SDDUndefPriority() then UNDEFINED; // Check if access disabled in CPACR_EL1 if PSTATE.EL IN {EL0, EL1} && !IsInHost() then // Check SME at EL0/EL1 case CPACR_EL1.SMEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0; when '11' disabled = FALSE; if disabled then SMEAccessTrap(SMEExceptionType_AccessTrap, EL1); if PSTATE.EL IN {EL0, EL1, EL2} && EL2Enabled() then if ELIsInHost(EL2) then // Check SME at EL2 case CPTR_EL2.SMEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0 && HCR_EL2.TGE == '1'; when '11' disabled = FALSE; if disabled then SMEAccessTrap(SMEExceptionType_AccessTrap, EL2); else if CPTR_EL2.TSM == '1' then SMEAccessTrap(SMEExceptionType_AccessTrap, EL2); // Check if access disabled in CPTR_EL3 if HaveEL(EL3) then if CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; SMEAccessTrap(SMEExceptionType_AccessTrap, EL3);
```

## J1.1.3.295 CheckSMEAndZAEnabled

```
// CheckSMEAndZAEnabled() // ====================== CheckSMEAndZAEnabled() CheckSMEEnabled();
```

```
if PSTATE.ZA == '0' then SMEAccessTrap(SMEExceptionType_InactiveZA, PSTATE.EL);
```

## J1.1.3.296 CheckSMEEnabled

```
// CheckSMEEnabled() // ================= CheckSMEEnabled() boolean disabled; if HaveEL(EL3) && CPTR_EL3.<ESM,TFP> != '10' && EL3SDDUndefPriority() then UNDEFINED; // Check if access disabled in CPACR_EL1 if PSTATE.EL IN {EL0, EL1} && !IsInHost() then // Check SME at EL0/EL1 case CPACR_EL1.SMEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0; when '11' disabled = FALSE; if disabled then SMEAccessTrap(SMEExceptionType_AccessTrap, EL1); // Check SIMD&FP at EL0/EL1 case CPACR_EL1.FPEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0; when '11' disabled = FALSE; if disabled then AArch64.AdvSIMDFPAccessTrap(EL1); if PSTATE.EL IN {EL0, EL1, EL2} && EL2Enabled() then if ELIsInHost(EL2) then // Check SME at EL2 case CPTR_EL2.SMEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0 && HCR_EL2.TGE == '1'; when '11' disabled = FALSE; if disabled then SMEAccessTrap(SMEExceptionType_AccessTrap, EL2); // Check SIMD&FP at EL2 case CPTR_EL2.FPEN of when 'x0' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0 && HCR_EL2.TGE == '1'; when '11' disabled = FALSE; if disabled then AArch64.AdvSIMDFPAccessTrap(EL2); else if CPTR_EL2.TSM == '1' then SMEAccessTrap(SMEExceptionType_AccessTrap, EL2); if CPTR_EL2.TFP == '1' then AArch64.AdvSIMDFPAccessTrap(EL2); // Check if access disabled in CPTR_EL3 if HaveEL(EL3) then if CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; SMEAccessTrap(SMEExceptionType_AccessTrap, EL3); if CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; AArch64.AdvSIMDFPAccessTrap(EL3);
```

## J1.1.3.297 CheckSMEZT0Enabled

```
// CheckSMEZT0Enabled() // ==================== // Checks for ZT0 enabled. CheckSMEZT0Enabled() if HaveEL(EL3) && SMCR_EL3.EZT0 == '0' && EL3SDDUndefPriority() then UNDEFINED; // Check if ZA and ZT0 are inactive in PSTATE if PSTATE.ZA == '0' then SMEAccessTrap(SMEExceptionType_InactiveZA, PSTATE.EL); // Check if EL0/EL1 accesses to ZT0 are disabled in SMCR_EL1 if PSTATE.EL IN {EL0, EL1} && !IsInHost() then if SMCR_EL1.EZT0 == '0' then SMEAccessTrap(SMEExceptionType_InaccessibleZT0, EL1); // Check if EL0/EL1/EL2 accesses to ZT0 are disabled in SMCR_EL2 if PSTATE.EL IN {EL0, EL1, EL2} && EL2Enabled() then if SMCR_EL2.EZT0 == '0' then SMEAccessTrap(SMEExceptionType_InaccessibleZT0, EL2); // Check if all accesses to ZT0 are disabled in SMCR_EL3 if HaveEL(EL3) then if SMCR_EL3.EZT0 == '0' then if EL3SDDUndef() then UNDEFINED; SMEAccessTrap(SMEExceptionType_InaccessibleZT0, EL3);
```

```
// CheckSVEEnabled() // ================= // Checks for traps on SVE instructions and instructions that // access SVE System registers. CheckSVEEnabled() if IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' then CheckSMEEnabled(); elsif IsFeatureImplemented(FEAT_SME) && !IsFeatureImplemented(FEAT_SVE) then CheckStreamingSVEEnabled(); else CheckOriginalSVEEnabled();
```

## J1.1.3.298 CheckSVEEnabled J1.1.3.299 CheckStreamingSVEAndZAEnabled // CheckStreamingSVEAndZAEnabled() // =============================== CheckStreamingSVEAndZAEnabled() CheckStreamingSVEEnabled(); if PSTATE.ZA == '0' then SMEAccessTrap(SMEExceptionType\_InactiveZA, PSTATE.EL); J1.1.3.300 CheckStreamingSVEEnabled // CheckStreamingSVEEnabled() // ==========================

```
CheckStreamingSVEEnabled()
```

```
CheckSMEEnabled(); if PSTATE.SM == '0' then SMEAccessTrap(SMEExceptionType_NotStreaming, PSTATE.EL);
```

## J1.1.3.301 CmpOp

```
// CmpOp // ===== enumeration CmpOp { Cmp_EQ, Cmp_NE, Cmp_GE, Cmp_GT, Cmp_LT, Cmp_LE,
```

## J1.1.3.302 CurrentNSVL

```
// CurrentNSVL -getter // ==================== // Non-Streaming VL VecLen CurrentNSVL integer vl; if PSTATE.EL == EL1 || (PSTATE.EL == EL0 && !IsInHost()) then vl = UInt(ZCR_EL1.LEN); if PSTATE.EL == EL2 || (PSTATE.EL == EL0 && IsInHost()) then vl = UInt(ZCR_EL2.LEN); elsif PSTATE.EL IN {EL0, EL1} && EL2Enabled() then vl = Min(vl, UInt(ZCR_EL2.LEN)); if PSTATE.EL == EL3 then vl = UInt(ZCR_EL3.LEN); elsif HaveEL(EL3) then vl = Min(vl, UInt(ZCR_EL3.LEN)); return ImplementedSVEVectorLength((vl + 1) * 128);
```

## J1.1.3.303 CurrentSVL

```
// CurrentSVL -getter // =================== // Streaming SVL VecLen CurrentSVL integer vl; if PSTATE.EL == EL1 || (PSTATE.EL == EL0 && !IsInHost()) then vl = UInt(SMCR_EL1.LEN); if PSTATE.EL == EL2 || (PSTATE.EL == EL0 && IsInHost()) then vl = UInt(SMCR_EL2.LEN); elsif PSTATE.EL IN {EL0, EL1} && EL2Enabled() then vl = Min(vl, UInt(SMCR_EL2.LEN)); if PSTATE.EL == EL3 then vl = UInt(SMCR_EL3.LEN); elsif HaveEL(EL3) then vl = Min(vl, UInt(SMCR_EL3.LEN)); return ImplementedSMEVectorLength((vl + 1) * 128);
```

```
Cmp_UN };
```

## J1.1.3.304 CurrentVL

```
// CurrentVL - getter // ================== VecLen CurrentVL return if IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' then CurrentSVL else CurrentNSVL;
```

## J1.1.3.305 DecodePredCount

```
// DecodePredCount() // ================= integer DecodePredCount(bits(5) bitpattern, integer esize) constant integer elements = CurrentVL DIV esize; integer numElem; case bitpattern of when '00000' numElem = FloorPow2(elements); when '00001' numElem = if elements >= 1 then 1 else 0; when '00010' numElem = if elements >= 2 then 2 else 0; when '00011' numElem = if elements >= 3 then 3 else 0; when '00100' numElem = if elements >= 4 then 4 else 0; when '00101' numElem = if elements >= 5 then 5 else 0; when '00110' numElem = if elements >= 6 then 6 else 0; when '00111' numElem = if elements >= 7 then 7 else 0; when '01000' numElem = if elements >= 8 then 8 else 0; when '01001' numElem = if elements >= 16 then 16 else 0; when '01010' numElem = if elements >= 32 then 32 else 0; when '01011' numElem = if elements >= 64 then 64 else 0; when '01100' numElem = if elements >= 128 then 128 else 0; when '01101' numElem = if elements >= 256 then 256 else 0; when '11101' numElem = elements - (elements MOD 4); when '11110' numElem = elements - (elements MOD 3); when '11111' numElem = elements; otherwise numElem = 0; return numElem;
```

## J1.1.3.306 ElemFFR

```
// ElemFFR - getter // ================ bit ElemFFR[integer e, ESize esize] return PredicateElement(_FFR, e, esize); // ElemFFR - setter // ================ ElemFFR[integer e, ESize esize] = bit value constant integer psize = esize DIV 8; Elem[_FFR, e, psize] = return;
```

## J1.1.3.307 FFR

```
// FFR - getter // ============ bits(width) FFR[integer width] assert width == CurrentVL DIV 8; return _FFR<width-1:0>;
```

```
ZeroExtend(value, psize);
```

```
// FFR - setter // ============ FFR[integer width] = bits(width) value assert width == CurrentVL DIV 8; if ConstrainUnpredictableBool(Unpredictable_SVEZEROUPPER) then _FFR = ZeroExtend(value, MAX_PL); else _FFR<width-1:0> = value;
```

## J1.1.3.308 FPCompareNE

```
// FPCompareNE() // ============= boolean FPCompareNE(bits(N) op1, bits(N) op2, FPCR_Type fpcr) assert N IN {16,32,64}; boolean result; (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); op1_nan = type1 IN {FPType_SNaN, FPType_QNaN}; op2_nan = type2 IN {FPType_SNaN, FPType_QNaN}; if op1_nan || op2_nan then result = TRUE; if type1 == FPType_SNaN || type2 == FPType_SNaN then FPProcessException(FPExc_InvalidOp, fpcr); else // All non-NaN cases can be evaluated on the values produced by FPUnpack() result = (value1 != value2); FPProcessDenorms(type1, type2, N, fpcr); return result;
```

## J1.1.3.309 FPCompareUN

```
// FPCompareUN() // ============= boolean FPCompareUN(bits(N) op1, bits(N) op2, FPCR_Type fpcr) assert N IN {16,32,64}; (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); if type1 == FPType_SNaN || type2 == FPType_SNaN then FPProcessException(FPExc_InvalidOp, fpcr); result = type1 IN {FPType_SNaN, FPType_QNaN} || type2 IN {FPType_SNaN, FPType_QNaN}; if !result then FPProcessDenorms(type1, type2, N, fpcr); return result;
```

## J1.1.3.310 FPConvertSVE

```
// FPConvertSVE() // ============== bits(M) FPConvertSVE(bits(N) op, FPCR_Type fpcr_in, FPRounding rounding, integer M) FPCR_Type fpcr = fpcr_in; fpcr.AHP = '0'; return FPConvert(op, fpcr, rounding, M);
```

```
// FPConvertSVE() // ============== bits(M) FPConvertSVE(bits(N) op, FPCR_Type fpcr_in, integer M) FPCR_Type fpcr = fpcr_in; fpcr.AHP = '0'; return FPConvert(op, fpcr, FPRoundingMode(fpcr), M);
```

## J1.1.3.311 FPExpA

```
// FPExpA() // ======== bits(N) FPExpA(bits(N) op) assert N IN {16,32,64}; bits(N) result; bits(N) coeff; constant integer idx = if N == 16 then UInt(op<4:0>) else coeff = FPExpCoefficient[idx, N]; if N == 16 then result<15:0> = '0':op<9:5>:coeff<9:0>; elsif N == 32 then result<31:0> = '0':op<13:6>:coeff<22:0>; else // N == 64 result<63:0> = '0':op<16:6>:coeff<51:0>; return result;
```

## J1.1.3.312 FPExpCoefficient

```
// FPExpCoefficient() // ================== bits(N) FPExpCoefficient[integer index, integer N] assert N IN {16,32,64}; integer result; if N == 16 then case index of when 0 result = 0x000; when 1 result = 0x016; when 2 result = 0x02d; when 3 result = 0x045; when 4 result = 0x05d; when 5 result = 0x075; when 6 result = 0x08e; when 7 result = 0x0a8; when 8 result = 0x0c2; when 9 result = 0x0dc; when 10 result = 0x0f8; when 11 result = 0x114; when 12 result = 0x130; when 13 result = 0x14d; when 14 result = 0x16b; when 15 result = 0x189; when 16 result = 0x1a8; when 17 result = 0x1c8; when 18 result = 0x1e8; when 19 result = 0x209; when 20 result = 0x22b; when 21 result = 0x24e; when 22 result = 0x271;
```

```
UInt(op<5:0>);
```

```
when 23 result = 0x295; when 24 result = 0x2ba; when 25 result = 0x2e0; when 26 result = 0x306; when 27 result = 0x32e; when 28 result = 0x356; when 29 result = 0x37f; when 30 result = 0x3a9; when 31 result = 0x3d4; elsif N == 32 then case index of when 0 result = 0x000000; when 1 result = 0x0164d2; when 2 result = 0x02cd87; when 3 result = 0x043a29; when 4 result = 0x05aac3; when 5 result = 0x071f62; when 6 result = 0x08980f; when 7 result = 0x0a14d5; when 8 result = 0x0b95c2; when 9 result = 0x0d1adf; when 10 result = 0x0ea43a; when 11 result = 0x1031dc; when 12 result = 0x11c3d3; when 13 result = 0x135a2b; when 14 result = 0x14f4f0; when 15 result = 0x16942d; when 16 result = 0x1837f0; when 17 result = 0x19e046; when 18 result = 0x1b8d3a; when 19 result = 0x1d3eda; when 20 result = 0x1ef532; when 21 result = 0x20b051; when 22 result = 0x227043; when 23 result = 0x243516; when 24 result = 0x25fed7; when 25 result = 0x27cd94; when 26 result = 0x29a15b; when 27 result = 0x2b7a3a; when 28 result = 0x2d583f; when 29 result = 0x2f3b79; when 30 result = 0x3123f6; when 31 result = 0x3311c4; when 32 result = 0x3504f3; when 33 result = 0x36fd92; when 34 result = 0x38fbaf; when 35 result = 0x3aff5b; when 36 result = 0x3d08a4; when 37 result = 0x3f179a; when 38 result = 0x412c4d; when 39 result = 0x4346cd; when 40 result = 0x45672a; when 41 result = 0x478d75; when 42 result = 0x49b9be; when 43 result = 0x4bec15; when 44 result = 0x4e248c; when 45 result = 0x506334; when 46 result = 0x52a81e; when 47 result = 0x54f35b; when 48 result = 0x5744fd; when 49 result = 0x599d16; when 50 result = 0x5bfbb8; when 51 result = 0x5e60f5; when 52 result = 0x60ccdf; when 53 result = 0x633f89;
```

```
when 54 result = 0x65b907; when 55 result = 0x68396a; when 56 result = 0x6ac0c7; when 57 result = 0x6d4f30; when 58 result = 0x6fe4ba; when 59 result = 0x728177; when 60 result = 0x75257d; when 61 result = 0x77d0df; when 62 result = 0x7a83b3; when 63 result = 0x7d3e0c; else // N == 64 case index of when 0 result = 0x0000000000000; when 1 result = 0x02C9A3E778061; when 2 result = 0x059B0D3158574; when 3 result = 0x0874518759BC8; when 4 result = 0x0B5586CF9890F; when 5 result = 0x0E3EC32D3D1A2; when 6 result = 0x11301D0125B51; when 7 result = 0x1429AAEA92DE0; when 8 result = 0x172B83C7D517B; when 9 result = 0x1A35BEB6FCB75; when 10 result = 0x1D4873168B9AA; when 11 result = 0x2063B88628CD6; when 12 result = 0x2387A6E756238; when 13 result = 0x26B4565E27CDD; when 14 result = 0x29E9DF51FDEE1; when 15 result = 0x2D285A6E4030B; when 16 result = 0x306FE0A31B715; when 17 result = 0x33C08B26416FF; when 18 result = 0x371A7373AA9CB; when 19 result = 0x3A7DB34E59FF7; when 20 result = 0x3DEA64C123422; when 21 result = 0x4160A21F72E2A; when 22 result = 0x44E086061892D; when 23 result = 0x486A2B5C13CD0; when 24 result = 0x4BFDAD5362A27; when 25 result = 0x4F9B2769D2CA7; when 26 result = 0x5342B569D4F82; when 27 result = 0x56F4736B527DA; when 28 result = 0x5AB07DD485429; when 29 result = 0x5E76F15AD2148; when 30 result = 0x6247EB03A5585; when 31 result = 0x6623882552225; when 32 result = 0x6A09E667F3BCD; when 33 result = 0x6DFB23C651A2F; when 34 result = 0x71F75E8EC5F74; when 35 result = 0x75FEB564267C9; when 36 result = 0x7A11473EB0187; when 37 result = 0x7E2F336CF4E62; when 38 result = 0x82589994CCE13; when 39 result = 0x868D99B4492ED; when 40 result = 0x8ACE5422AA0DB; when 41 result = 0x8F1AE99157736; when 42 result = 0x93737B0CDC5E5; when 43 result = 0x97D829FDE4E50; when 44 result = 0x9C49182A3F090; when 45 result = 0xA0C667B5DE565; when 46 result = 0xA5503B23E255D; when 47 result = 0xA9E6B5579FDBF; when 48 result = 0xAE89F995AD3AD; when 49 result = 0xB33A2B84F15FB; when 50 result = 0xB7F76F2FB5E47; when 51 result = 0xBCC1E904BC1D2; when 52 result = 0xC199BDD85529C;
```

```
when 53 result when 54 result when 55 result when 56 result when 57 result when 58 result when 59 result when 60 result when 61 result when 62 result when 63 result return result<N-1:0>;
```

## J1.1.3.313 FPLogB

```
// FPLogB() // ======== bits(N) FPLogB(bits(N) op, FPCR_Type fpcr) assert N IN {16,32,64}; integer result; (fptype,sign,value) = FPUnpack(op, fpcr); if fptype == FPType_SNaN || fptype == FPType_QNaN || fptype == FPType_Zero then FPProcessException(FPExc_InvalidOp, fpcr); result = -(2^(N-1)); // MinInt, 100..00 elsif fptype == FPType_Infinity then result = 2^(N-1) 1; // MaxInt, 011..11 else // FPUnpack has already scaled a subnormal input value = Abs(value); (value, result) = NormalizeReal(value); FPProcessDenorm(fptype, N, fpcr); return result<N-1:0>;
```

## J1.1.3.314 FPMinNormal

```
// FPMinNormal() // ============= bits(N) FPMinNormal(bit sign, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else 11)); constant integer F = N - (E + 1); exp = Zeros(E-1):'1'; frac = Zeros(F); return sign : exp : frac;
```

## J1.1.3.315 FPOne

```
// FPOne() // ======= bits(N) FPOne(bit sign, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else 11)); constant integer F = N - (E + 1); exp = '0':Ones(E-1); frac = Zeros(F); return sign : exp : frac;
```

```
= 0xC67F12E57D14B; = 0xCB720DCEF9069; = 0xD072D4A07897C; = 0xD5818DCFBA487; = 0xDA9E603DB3285; = 0xDFC97337B9B5F; = 0xE502EE78B3FF6; = 0xEA4AFA2A490DA; = 0xEFA1BEE615A27; = 0xF50765B6E4540; = 0xFA7C1819E90D8;
```

## J1.1.3.316 FPPointFive

```
// FPPointFive() // ============= bits(N) FPPointFive(bit sign, integer N) assert N IN {16,32,64}; constant integer E = (if N == 16 then 5 else (if N == 32 then 8 else constant integer F = N - (E + 1); exp = '0':Ones(E-2):'0'; frac = Zeros(F); return sign : exp : frac;
```

```
// FPTrigMAdd() // ============ bits(N) FPTrigMAdd(integer x_in, bits(N) op1, bits(N) op2_in, FPCR_Type assert N IN {16,32,64}; bits(N) coeff; bits(N) op2 = op2_in; integer x = x_in; assert x >= 0; assert x < 8; if op2<N-1> == '1' then x = x + 8; coeff = FPTrigMAddCoefficient[x, N]; // Safer to use EffectiveFPCR() in case the input fpcr argument // is modified as opposed to actual value of FPCR op2 = FPAbs(op2, EffectiveFPCR()); result = FPMulAdd(coeff, op1, op2, fpcr); return result;
```

```
11)); J1.1.3.317 FPReducePredicated // FPReducePredicated() // ==================== bits(esize) FPReducePredicated(ReduceOp op, bits(N) input, bits(M) mask, bits(esize) identity, FPCR_Type fpcr) assert(N == M * 8); assert IsPow2(N); bits(N) operand; constant integer elements = N DIV esize; for e = 0 to elements-1 if e * esize < N && ActivePredicateElement(mask, e, esize) then Elem[operand, e, esize] = Elem[input, e, esize]; else Elem[operand, e, esize] = identity; return FPReduce(op, operand, esize, fpcr); J1.1.3.318 FPTrigMAdd fpcr)
```

## J1.1.3.319 FPTrigMAddCoefficient

```
// FPTrigMAddCoefficient() // ======================= bits(N) FPTrigMAddCoefficient[integer index, integer N] assert N IN {16,32,64}; integer result; if N == 16 then case index of when 0 result = 0x3c00; when 1 result = 0xb155; when 2 result = 0x2030; when 3 result = 0x0000; when 4 result = 0x0000; when 5 result = 0x0000; when 6 result = 0x0000; when 7 result = 0x0000; when 8 result = 0x3c00; when 9 result = 0xb800; when 10 result = 0x293a; when 11 result = 0x0000; when 12 result = 0x0000; when 13 result = 0x0000; when 14 result = 0x0000; when 15 result = 0x0000; elsif N == 32 then case index of when 0 result = 0x3f800000; when 1 result = 0xbe2aaaab; when 2 result = 0x3c088886; when 3 result = 0xb95008b9; when 4 result = 0x36369d6d; when 5 result = 0x00000000; when 6 result = 0x00000000; when 7 result = 0x00000000; when 8 result = 0x3f800000; when 9 result = 0xbf000000; when 10 result = 0x3d2aaaa6; when 11 result = 0xbab60705; when 12 result = 0x37cd37cc; when 13 result = 0x00000000; when 14 result = 0x00000000; when 15 result = 0x00000000; else // N == 64 case index of when 0 result = 0x3ff0000000000000; when 1 result = 0xbfc5555555555543; when 2 result = 0x3f8111111110f30c; when 3 result = 0xbf2a01a019b92fc6; when 4 result = 0x3ec71de351f3d22b; when 5 result = 0xbe5ae5e2b60f7b91; when 6 result = 0x3de5d8408868552f; when 7 result = 0x0000000000000000; when 8 result = 0x3ff0000000000000; when 9 result = 0xbfe0000000000000; when 10 result = 0x3fa5555555555536; when 11 result = 0xbf56c16c16c13a0b; when 12 result = 0x3efa01a019b1e8d8; when 13 result = 0xbe927e4f7282f468; when 14 result = 0x3e21ee96d2641b13; when 15 result = 0xbda8f76380fbb401; return result<N-1:0>;
```

## J1.1.3.320 FPTrigSMul

```
// FPTrigSMul() // ============ bits(N) FPTrigSMul(bits(N) op1, bits(N) op2, FPCR_Type assert N IN {16,32,64}; result = FPMul(op1, op1, fpcr); fpexc = FALSE; (fptype, sign, value) = FPUnpack(result, fpcr, fpexc); if ! fptype IN {FPType_QNaN, FPType_SNaN} then result<N-1> = op2<0>; return result;
```

## fpcr) J1.1.3.321 FPTrigSSel // FPTrigSSel() // ============ bits(N) FPTrigSSel(bits(N) op1, bits(N) op2) assert N IN {16,32,64}; bits(N) result; if op2&lt;0&gt; == '1' then result = FPOne(op2&lt;1&gt;, N); elsif op2&lt;1&gt; == '1' then result = FPNeg(op1, EffectiveFPCR()); else result = op1; return result; J1.1.3.322 FirstActive // FirstActive() // ============= bit FirstActive(bits(N) mask, bits(N) x, integer esize) constant integer elements = N DIV (esize DIV 8); for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then return PredicateElement(x, e, esize); return '0'; J1.1.3.323 Getter

```
// Getter for SVCR // =============== // Returns PSTATE.<ZA, SM> SVCR_Type SVCR constant SVCR_Type value = Zeros(62) : PSTATE.ZA return value;
```

```
: PSTATE.SM;
```

## J1.1.3.324 HaveSVE2FP8DOT2

```
// HaveSVE2FP8DOT2() // ================= // Returns TRUE if SVE2 FP8 dot product to half-precision instructions // are implemented, FALSE otherwise. boolean HaveSVE2FP8DOT2() return ((IsFeatureImplemented(FEAT_SVE2) && IsFeatureImplemented(FEAT_FP8DOT2)) || IsFeatureImplemented(FEAT_SSVE_FP8DOT2));
```

## J1.1.3.325 HaveSVE2FP8DOT4

```
// HaveSVE2FP8DOT4() // ================= // Returns TRUE if SVE2 FP8 dot product to single-precision instructions // are implemented, FALSE otherwise. boolean HaveSVE2FP8DOT4() return ((IsFeatureImplemented(FEAT_SVE2) && IsFeatureImplemented(FEAT_FP8DOT4)) || IsFeatureImplemented(FEAT_SSVE_FP8DOT4));
```

## J1.1.3.326 HaveSVE2FP8FMA

```
// HaveSVE2FP8FMA() // ================ // Returns TRUE if SVE2 FP8 multiply-accumulate to half-precision and single-precision // instructions are implemented, FALSE otherwise. boolean HaveSVE2FP8FMA() return ((IsFeatureImplemented(FEAT_SVE2) && IsFeatureImplemented(FEAT_FP8FMA)) || IsFeatureImplemented(FEAT_SSVE_FP8FMA));
```

## J1.1.3.327 ImplementedSMEVectorLength

```
// ImplementedSMEVectorLength() // ============================ // Reduce SVE/SME vector length to a supported value (power of two) VecLen ImplementedSMEVectorLength(integer nbits_in) constant VecLen maxbits = MaxImplementedSVL(); assert 128 <= maxbits && maxbits <= 2048 && IsPow2(maxbits); integer nbits = Min(nbits_in, maxbits); assert 128 <= nbits && nbits <= 2048 && Align(nbits, 128) == nbits; // Search for a supported power-of-two VL less than or equal to nbits while nbits > 128 && !SupportedPowerTwoSVL(nbits) do nbits = nbits - 128; // Return the smallest supported power-of-two VL while nbits < maxbits && !SupportedPowerTwoSVL(nbits) do nbits = nbits * 2; return nbits;
```

## J1.1.3.328 ImplementedSVEVectorLength

```
// ImplementedSVEVectorLength() // ============================ // Reduce SVE vector length to a supported value (power of two) VecLen ImplementedSVEVectorLength(integer nbits_in) constant integer maxbits = MaxImplementedVL(); assert 128 <= maxbits && maxbits <= 2048 && IsPow2(maxbits); integer nbits = Min(nbits_in, maxbits); assert 128 <= nbits && nbits <= 2048 && Align(nbits, 128) == while !IsPow2(nbits) do nbits = nbits - 128; return nbits;
```

```
// IntReducePredicated() // ===================== bits(esize) IntReducePredicated(ReduceOp op, bits(N) input, bits(M) mask, bits(esize) identity) assert(N == M * 8); assert IsPow2(N); bits(N) operand; constant integer elements = N DIV esize; for e = 0 to elements-1 if e * esize < N && ActivePredicateElement(mask, e, esize) then Elem[operand, e, esize] = Elem[input, e, esize]; else Elem[operand, e, esize] = identity; return IntReduce(op, operand, esize);
```

```
// IsFPEnabled() // ============= // Returns TRUE if accesses to the Advanced SIMD and floating-point // registers are enabled at the target exception level in the // execution state and FALSE otherwise. boolean IsFPEnabled(bits(2) el) if ELUsingAArch32(el) then return AArch32.IsFPEnabled(el); else return AArch64.IsFPEnabled(el);
```

## nbits; J1.1.3.329 InStreamingMode // InStreamingMode() // ================= boolean InStreamingMode() return IsFeatureImplemented(FEAT\_SME) &amp;&amp; PSTATE.SM == '1'; J1.1.3.330 IntReducePredicated J1.1.3.331 IsFPEnabled current

## J1.1.3.332 IsFullA64Enabled

```
// IsFullA64Enabled() // ================== // Returns TRUE if full A64 is enabled in Streaming mode and FALSE othersise. boolean IsFullA64Enabled() if !IsFeatureImplemented(FEAT_SME_FA64) then return FALSE; // Check if full A64 disabled in SMCR_EL1 if PSTATE.EL IN {EL0, EL1} && !IsInHost() then // Check full A64 at EL0/EL1 if SMCR_EL1.FA64 == '0' then return FALSE; // Check if full A64 disabled in SMCR_EL2 if PSTATE.EL IN {EL0, EL1, EL2} && EL2Enabled() then if SMCR_EL2.FA64 == '0' then return FALSE; // Check if full A64 disabled in SMCR_EL3 if HaveEL(EL3) then if SMCR_EL3.FA64 == '0' then return FALSE; return TRUE;
```

## J1.1.3.333 IsOriginalSVEEnabled

```
// IsOriginalSVEEnabled() // ====================== // Returns TRUE if access to SVE functionality is enabled at the target // exception level and FALSE otherwise. boolean IsOriginalSVEEnabled(bits(2) el) boolean disabled; if ELUsingAArch32(el) then return FALSE; // Check if access disabled in CPACR_EL1 if el IN {EL0, EL1} && !IsInHost() then // Check SVE at EL0/EL1 case CPACR_EL1.ZEN of when 'x0' disabled = TRUE; when '01' disabled = el == EL0; when '11' disabled = FALSE; if disabled then return FALSE; // Check if access disabled in CPTR_EL2 if el IN {EL0, EL1, EL2} && EL2Enabled() then if ELIsInHost(EL2) then case CPTR_EL2.ZEN of when 'x0' disabled = TRUE; when '01' disabled = el == EL0 && HCR_EL2.TGE == '1'; when '11' disabled = FALSE; if disabled then return FALSE; else if CPTR_EL2.TZ == '1' then return FALSE; // Check if access disabled in CPTR_EL3 if HaveEL(EL3) then if CPTR_EL3.EZ == '0' then return FALSE; return TRUE;
```

## J1.1.3.334 IsSMEEnabled

```
// IsSMEEnabled() // ============== // Returns TRUE if access to SME functionality is enabled at the target // exception level and FALSE otherwise. boolean IsSMEEnabled(bits(2) el) boolean disabled; if ELUsingAArch32(el) then return FALSE; // Check if access disabled in CPACR_EL1 if el IN {EL0, EL1} && !IsInHost() then // Check SME at EL0/EL1 case CPACR_EL1.SMEN of when 'x0' disabled = TRUE; when '01' disabled = el == EL0; when '11' disabled = FALSE; if disabled then return FALSE; // Check if access disabled in CPTR_EL2 if el IN {EL0, EL1, EL2} && EL2Enabled() then if ELIsInHost(EL2) then case CPTR_EL2.SMEN of when 'x0' disabled = TRUE; when '01' disabled = el == EL0 && HCR_EL2.TGE == '1'; when '11' disabled = FALSE; if disabled then return FALSE; else if CPTR_EL2.TSM == '1' then return FALSE; // Check if access disabled in CPTR_EL3 if HaveEL(EL3) then if CPTR_EL3.ESM == '0' then return FALSE; return TRUE;
```

## J1.1.3.335 IsSVEEnabled

```
// IsSVEEnabled() // ============== // Returns TRUE if access to SVE registers is enabled at the target exception // level and FALSE otherwise. boolean IsSVEEnabled(bits(2) el) if IsFeatureImplemented(FEAT_SME) && PSTATE.SM == '1' then return IsSMEEnabled(el); elsif IsFeatureImplemented(FEAT_SVE) then return IsOriginalSVEEnabled(el); else return FALSE;
```

## J1.1.3.336 LastActive

```
// LastActive() // ============ bit LastActive(bits(N) mask, bits(N) x, integer esize) constant integer elements = N DIV (esize DIV 8); for e = elements-1 downto 0 if ActivePredicateElement(mask, e, esize) then return PredicateElement(x, e, esize);
```

```
return '0';
```

## J1.1.3.337 LastActiveElement

```
// LastActiveElement() // =================== integer LastActiveElement(bits(N) mask, integer esize) constant integer elements = N DIV (esize DIV 8); for e = elements-1 downto 0 if ActivePredicateElement(mask, e, esize) then return return -1;
```

## J1.1.3.338 MaxImplementedAnyVL

```
// MaxImplementedAnyVL() // ===================== integer MaxImplementedAnyVL() if IsFeatureImplemented(FEAT_SME) && IsFeatureImplemented(FEAT_SVE) then return Max(MaxImplementedVL(), MaxImplementedSVL()); if IsFeatureImplemented(FEAT_SME) then return MaxImplementedSVL(); return MaxImplementedVL();
```

## J1.1.3.339 MaxImplementedSVL

```
// MaxImplementedSVL() // =================== VecLen MaxImplementedSVL() return integer IMPLEMENTATION_DEFINED "Max implemented SVL";
```

## J1.1.3.340 MaxImplementedVL

```
// MaxImplementedVL() // ================== integer MaxImplementedVL() return integer IMPLEMENTATION_DEFINED "Max implemented VL";
```

## J1.1.3.341 MaybeZeroSVEUppers

```
// MaybeZeroSVEUppers() // ==================== MaybeZeroSVEUppers(bits(2) target_el) boolean lower_enabled; if UInt(target_el) <= UInt(PSTATE.EL) || !IsSVEEnabled(target_el) then return; if target_el == EL3 then if EL2Enabled() then lower_enabled = IsFPEnabled(EL2); else lower_enabled = IsFPEnabled(EL1); elsif target_el == EL2 then
```

```
e;
```

```
assert EL2Enabled() && !ELUsingAArch32(EL2); if HCR_EL2.TGE == '0' then lower_enabled = IsFPEnabled(EL1); else lower_enabled = IsFPEnabled(EL0); else assert target_el == EL1 && !ELUsingAArch32(EL1); lower_enabled = IsFPEnabled(EL0); if lower_enabled then constant integer VL = if IsSVEEnabled(PSTATE.EL) then CurrentVL else constant integer PL = VL DIV 8; for n = 0 to 31 if ConstrainUnpredictableBool(Unpredictable_SVEZEROUPPER) then _Z[n] = ZeroExtend(_Z[n]<VL-1:0>, MAX_VL); for n = 0 to 15 if ConstrainUnpredictableBool(Unpredictable_SVEZEROUPPER) then _P[n] = ZeroExtend(_P[n]<PL-1:0>, MAX_PL); if ConstrainUnpredictableBool(Unpredictable_SVEZEROUPPER) then _FFR = ZeroExtend(_FFR<PL-1:0>, MAX_PL); if IsFeatureImplemented(FEAT_SME) && PSTATE.ZA == '1' then constant integer SVL = CurrentSVL; constant integer accessiblevecs = SVL DIV 8; constant integer allvecs = MaxImplementedSVL() DIV 8; for n = 0 to accessiblevecs - 1 if ConstrainUnpredictableBool(Unpredictable_SMEZEROUPPER) then _ZA[n] = ZeroExtend(_ZA[n]<SVL-1:0>, MAX_VL); for n = accessiblevecs to allvecs - 1 if ConstrainUnpredictableBool(Unpredictable_SMEZEROUPPER) then _ZA[n] = Zeros(MAX_VL);
```

## J1.1.3.342

```
// MemNF -getter // ============== (bits(8*size), boolean) MemNF[bits(64) address, integer size, AccessDescriptor accdesc] assert size IN {1, 2, 4, 8, 16}; bits(8*size) value; boolean bad; boolean aligned = IsAligned(address, size); if !aligned && AlignmentEnforced() then return (bits(8*size) UNKNOWN, TRUE); constant boolean atomic = aligned || size == 1; if !atomic then (value<7:0>, bad) = MemSingleNF[address, 1, accdesc, aligned]; if bad then return (bits(8*size) UNKNOWN, TRUE); // For subsequent bytes, if they cross to a new translation page which assigns // Device memory type, it is CONSTRAINED UNPREDICTABLE whether an unaligned // will generate an Alignment Fault. if !aligned then c = ConstrainUnpredictable(Unpredictable_DEVPAGE2); assert c IN {Constraint_FAULT, Constraint_NONE}; if c == Constraint_NONE then aligned = TRUE; for i = 1 to size-1
```

```
128; MemNF access
```

```
(Elem[value, i, 8], bad) = MemSingleNF[address+i, 1, accdesc, aligned]; if bad then return (bits(8*size) UNKNOWN, TRUE); else (value, bad) = MemSingleNF[address, size, accdesc, aligned]; if bad then return (bits(8*size) UNKNOWN, TRUE); if BigEndian(accdesc.acctype) then value = BigEndianReverse(value); return (value, FALSE); MemSingleNF
```

## J1.1.3.343

```
// MemSingleNF -getter // ==================== (bits(8*size), boolean) MemSingleNF[bits(64) address, integer size, AccessDescriptor accdesc_in, boolean aligned] assert accdesc_in.acctype == AccessType_SVE; assert accdesc_in.nonfault || (accdesc_in.firstfault && !accdesc_in.first); bits(8*size) value; AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; AccessDescriptor accdesc = accdesc_in; FaultRecord fault = NoFault(accdesc, address); // Implementation may suppress NF load for any reason if ConstrainUnpredictableBool(Unpredictable_NONFAULT) then return (bits(8*size) UNKNOWN, TRUE); // If the instruction encoding permits tag checking, confer with system register configuration // which may override this. if accdesc.tagchecked then accdesc.tagchecked = AArch64.AccessIsTagChecked(address, accdesc); // MMU or MPU memaddrdesc = AArch64.TranslateAddress(address, accdesc, aligned, size); // Non-fault load from Device memory must not be performed externally if memaddrdesc.memattrs.memtype == MemType_Device then return (bits(8*size) UNKNOWN, TRUE); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then return (bits(8*size) UNKNOWN, TRUE); if accdesc.tagchecked then constant bits(4) ltag = AArch64.LogicalAddressTag(address); fault = AArch64.CheckTag(memaddrdesc, accdesc, size, ltag); if fault.statuscode != Fault_None then return (bits(8*size) UNKNOWN, TRUE); (memstatus, value) = PhysMemRead(memaddrdesc, size, accdesc); if IsFault(memstatus) then constant boolean iswrite = FALSE; if IsExternalAbortTakenSynchronously(memstatus, iswrite, memaddrdesc, size, accdesc) then return (bits(8*size) UNKNOWN, TRUE); fault.merrorstate = memstatus.merrorstate; fault.extflag = memstatus.extflag; fault.statuscode = memstatus.statuscode; PendSErrorInterrupt(fault);
```

```
return (value, FALSE);
```

```
// NoneActive() // ============ bit NoneActive(bits(N) mask, bits(N) x, integer esize) constant integer elements = N DIV (esize DIV 8); for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) && ActivePredicateElement(x, e, esize) then return '0'; return '1';
```

```
// PredTest() // ========== bits(4) PredTest(bits(N) mask, bits(N) result, integer constant bit n = FirstActive(mask, result, esize); constant bit z = NoneActive(mask, result, esize); constant bit c = NOT LastActive(mask, result, esize); constant bit v = '0'; return n:z:c:v;
```

## J1.1.3.344 NoneActive J1.1.3.345 P // P -getter // ========== bits(width) P[integer n, integer width] assert n &gt;= 0 &amp;&amp; n &lt;= 31; assert width == CurrentVL DIV 8; return \_P[n]&lt;width-1:0&gt;; // P -setter // ========== P[integer n, integer width] = bits(width) value assert n &gt;= 0 &amp;&amp; n &lt;= 31; assert width == CurrentVL DIV 8; if ConstrainUnpredictableBool(Unpredictable\_SVEZEROUPPER) then \_P[n] = ZeroExtend(value, MAX\_PL); else \_P[n]&lt;width-1:0&gt; = value; J1.1.3.346 PredLen // PredLen // ======= type PredLen = integer; J1.1.3.347 PredTest esize)

## J1.1.3.348 PredicateElement

```
// PredicateElement() // ================== // Returns the predicate bit bit PredicateElement(bits(N) pred, integer e, integer esize) assert esize IN {8, 16, 32, 64, 128}; constant integer n = e * (esize DIV 8); assert n >= 0 && n < N; return pred<n>;
```

## J1.1.3.349 ResetSMEState

```
// ResetSMEState() // =============== ResetSMEState(bit newenable) constant integer vectors = MAX_VL DIV 8; if newenable == '1' then for n = 0 to vectors - 1 _ZA[n] = Zeros(MAX_VL); if IsFeatureImplemented(FEAT_SME2) then _ZT0 = Zeros(ZT0_LEN); else for n = 0 to vectors - 1 _ZA[n] = bits(MAX_VL) UNKNOWN; if IsFeatureImplemented(FEAT_SME2) then _ZT0 = bits(ZT0_LEN) UNKNOWN;
```

## J1.1.3.350 ResetSVERegisters

```
// ResetSVERegisters() // =================== ResetSVERegisters() for n = 0 to 31 _Z[n] = bits(MAX_VL) UNKNOWN; for n = 0 to 15 _P[n] = bits(MAX_PL) UNKNOWN; _FFR = bits(MAX_PL) UNKNOWN;
```

## J1.1.3.351 ResetSVEState

```
// ResetSVEState() // =============== ResetSVEState() for n = 0 to 31 _Z[n] = Zeros(MAX_VL); for n = 0 to 15 _P[n] = Zeros(MAX_PL); _FFR = Zeros(MAX_PL); FPSR = ZeroExtend(0x0800009f<31:0>, 64); FPMR = Zeros(64);
```

## J1.1.3.352 SMEAccessTrap

```
// SMEAccessTrap() // =============== // Trapped access to SME registers due to CPACR_EL1, CPTR_EL2, or CPTR_EL3. SMEAccessTrap(SMEExceptionType etype, bits(2) target_el_in) bits(2) target_el = target_el_in; assert UInt(target_el) >= UInt(PSTATE.EL); if target_el == EL0 then target_el = EL1; boolean route_to_el2; route_to_el2 = PSTATE.EL == EL0 && target_el == EL1 && EL2Enabled() && HCR_EL2.TGE == except = ExceptionSyndrome(Exception_SMEAccessTrap); constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; case etype of when SMEExceptionType_AccessTrap except.syndrome.iss<2:0> = '000'; when SMEExceptionType_Streaming except.syndrome.iss<2:0> = '001'; when SMEExceptionType_NotStreaming except.syndrome.iss<2:0> = '010'; when SMEExceptionType_InactiveZA except.syndrome.iss<2:0> = '011'; when SMEExceptionType_InaccessibleZT0 except.syndrome.iss<2:0> = '100'; if route_to_el2 then AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset); else AArch64.TakeException(target_el, except, preferred_exception_return, vect_offset);
```

```
// SVEAccessTrap() // =============== // Trapped access to SVE registers due to CPACR_EL1, CPTR_EL2, or CPTR_EL3. SVEAccessTrap(bits(2) target_el) assert UInt(target_el) >= UInt(PSTATE.EL) && target_el != EL0 && route_to_el2 = target_el == EL1 && EL2Enabled() && HCR_EL2.TGE == '1'; except = ExceptionSyndrome(Exception_SVEAccessTrap); constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; if route_to_el2 then AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset);
```

## '1'; J1.1.3.353 SMEExceptionType // SMEExceptionType // ================ enumeration SMEExceptionType { SMEExceptionType\_AccessTrap, // SME functionality trapped or disabled SMEExceptionType\_Streaming, // Illegal instruction in Streaming SVE mode SMEExceptionType\_NotStreaming, // Illegal instruction not in Streaming SVE mode SMEExceptionType\_InactiveZA, // Illegal instruction when ZA is inactive SMEExceptionType\_InaccessibleZT0, // Access to ZT0 is disabled }; J1.1.3.354 SVEAccessTrap HaveEL(target\_el);

else

AArch64.TakeException(target\_el, except, preferred\_exception\_return, vect\_offset);

## J1.1.3.355 SVEMoveMaskPreferred

```
// SVEMoveMaskPreferred() // ====================== // Return FALSE if a bitmask immediate encoding would generate an immediate // value that could also be represented by a single DUP instruction. // Used as a condition for the preferred MOV<-DUPM alias. boolean SVEMoveMaskPreferred(bits(13) imm13) bits(64) imm; (imm, -) = DecodeBitMasks(imm13<12>, imm13<5:0>, imm13<11:6>, TRUE, 64); // Check for 8 bit immediates if !IsZero(imm<7:0>) then // Check for 'ffffffffffffffxy' or '00000000000000xy' if IsZero(imm<63:7>) || IsOnes(imm<63:7>) then return FALSE; // Check for 'ffffffxyffffffxy' or '000000xy000000xy' if imm<63:32> == imm<31:0> && (IsZero(imm<31:7>) || IsOnes(imm<31:7>)) then return FALSE; // Check for 'ffxyffxyffxyffxy' or '00xy00xy00xy00xy' if (imm<63:32> == imm<31:0> && imm<31:16> == imm<15:0> && (IsZero(imm<15:7>) || IsOnes(imm<15:7>))) then return FALSE; // Check for 'xyxyxyxyxyxyxyxy' if imm<63:32> == imm<31:0> && imm<31:16> == imm<15:0> && (imm<15:8> == imm<7:0>) return FALSE; // Check for 16 bit immediates else // Check for 'ffffffffffffxy00' or '000000000000xy00' if IsZero(imm<63:15>) || IsOnes(imm<63:15>) then return FALSE; // Check for 'ffffxy00ffffxy00' or '0000xy000000xy00' if imm<63:32> == imm<31:0> && (IsZero(imm<31:7>) || IsOnes(imm<31:7>)) then return FALSE; // Check for 'xy00xy00xy00xy00' if imm<63:32> == imm<31:0> && imm<31:16> == imm<15:0> then return FALSE; return TRUE;
```

## J1.1.3.356 SetPSTATE\_SM

```
// SetPSTATE_SM() // ============== SetPSTATE_SM(bit value) if PSTATE.SM != value then ResetSVEState(); PSTATE.SM = value;
```

```
then
```

## J1.1.3.357 SetPSTATE\_ZA

```
// SetPSTATE_ZA() // ============== SetPSTATE_ZA(bit value) if PSTATE.ZA != value then ResetSMEState(value); PSTATE.ZA = value;
```

## J1.1.3.358 Setter

```
// Setter for SVCR // =============== // Sets PSTATE.<ZA, SM> SVCR = SVCR_Type value SetPSTATE_SM(value<0>); SetPSTATE_ZA(value<1>); return;
```

## J1.1.3.359 SupportedPowerTwoSVL

```
// SupportedPowerTwoSVL() // ====================== // Return an IMPLEMENTATION DEFINED specific value // returns TRUE if SVL is supported and is a power of two, FALSE otherwise boolean SupportedPowerTwoSVL(integer nbits);
```

## J1.1.3.360 System

```
// System Registers // ================ constant VecLen MAX_VL = 2048; constant PredLen MAX_PL = 256; constant integer ZT0_LEN = 512; bits(MAX_PL) _FFR; array bits(MAX_VL) _Z[0..31]; array bits(MAX_PL) _P[0..15];
```

## J1.1.3.361 VecLen

```
// VecLen // ====== type VecLen = integer;
```

## J1.1.3.362 Z

```
// Z -getter // ========== bits(width) Z[integer n, integer width] assert n >= 0 && n <= 31; assert width == CurrentVL; return _Z[n]<width-1:0>; // Z -setter // ========== Z[integer n, integer width] = bits(width) value assert n >= 0 && n <= 31; assert width == CurrentVL; if ConstrainUnpredictableBool(Unpredictable_SVEZEROUPPER) then _Z[n] = ZeroExtend(value, MAX_VL); else _Z[n]<width-1:0> = value;
```

## J1.1.3.363 SystemHintOp

```
// SystemHintOp // ============ // System Hint instruction types. enumeration SystemHintOp { SystemHintOp_NOP, SystemHintOp_YIELD, SystemHintOp_WFE, SystemHintOp_WFI, SystemHintOp_SEV, SystemHintOp_SEVL, SystemHintOp_DGH, SystemHintOp_ESB, SystemHintOp_PSB, SystemHintOp_TSB, SystemHintOp_BTI, SystemHintOp_WFET, SystemHintOp_WFIT, SystemHintOp_CLRBHB, SystemHintOp_GCSB, SystemHintOp_CHKFEAT, SystemHintOp_STSHH, SystemHintOp_CSDB };
```

## J1.1.3.364 SysLOp

```
// SysLOp() // ======== SystemLOp SysLOp(bits(3) op1, bits(4) CRn, bits(4) CRm, case op1:CRn:CRm:op2 of otherwise return Sysl_SYSL;
```

```
bits(3) op2)
```

## J1.1.3.365 SystemLOp

```
// SystemLOp // ========= // System instruction with result enumeration SystemLOp { Sysl_SYSL };
```

## J1.1.3.366 SysOp

```
// SysOp() // ======= SystemOp SysOp(bits(3) op1, bits(4) CRn, bits(4) CRm, bits(3) op2) case op1:CRn:CRm:op2 of when '000 0111 1000 000' return Sys_AT; // S1E1R when '000 0111 1000 001' return Sys_AT; // S1E1W when '000 0111 1000 010' return Sys_AT; // S1E0R when '000 0111 1000 011' return Sys_AT; // S1E0W when '000 0111 1001 000' return Sys_AT; // S1E1RP when '000 0111 1001 001' return Sys_AT; // S1E1WP when '000 0111 1001 010' return Sys_AT; // S1E1A when '100 0111 1000 000' return Sys_AT; // S1E2R when '100 0111 1000 001' return Sys_AT; // S1E2W when '100 0111 1001 010' return Sys_AT; // S1E2A when '100 0111 1000 100' return Sys_AT; // S12E1R when '100 0111 1000 101' return Sys_AT; // S12E1W when '100 0111 1000 110' return Sys_AT; // S12E0R when '100 0111 1000 111' return Sys_AT; // S12E0W when '110 0111 1000 000' return Sys_AT; // S1E3R when '110 0111 1000 001' return Sys_AT; // S1E3W when '110 0111 1001 010' return Sys_AT; // S1E3A when '001 0111 0010 100' return Sys_BRB; // IALL when '001 0111 0010 101' return Sys_BRB; // INJ when '000 0111 0110 001' return Sys_DC; // IVAC when '000 0111 0110 010' return Sys_DC; // ISW when '000 0111 0110 011' return Sys_DC; // IGVAC when '000 0111 0110 100' return Sys_DC; // IGSW when '000 0111 0110 101' return Sys_DC; // IGDVAC when '000 0111 0110 110' return Sys_DC; // IGDSW when '000 0111 1010 010' return Sys_DC; // CSW when '000 0111 1010 100' return Sys_DC; // CGSW when '000 0111 1010 110' return Sys_DC; // CGDSW when '000 0111 1110 010' return Sys_DC; // CISW when '000 0111 1110 100' return Sys_DC; // CIGSW when '000 0111 1110 110' return Sys_DC; // CIGDSW when '011 0111 0100 001' return Sys_DC; // ZVA when '011 0111 0100 011' return Sys_DC; // GVA when '011 0111 0100 100' return Sys_DC; // GZVA when '011 0111 1010 001' return Sys_DC; // CVAC when '011 0111 1010 011' return Sys_DC; // CGVAC when '011 0111 1010 101' return Sys_DC; // CGDVAC when '011 0111 1011 001' return Sys_DC; // CVAU when '011 0111 1100 001' return Sys_DC; // CVAP when '011 0111 1100 011' return Sys_DC; // CGVAP when '011 0111 1100 101' return Sys_DC; // CGDVAP when '011 0111 1101 001' return Sys_DC; // CVADP when '011 0111 1101 011' return Sys_DC; // CGVADP when '011 0111 1101 101' return Sys_DC; // CGDVADP when '011 0111 1110 001' return Sys_DC; // CIVAC when '011 0111 1110 011' return Sys_DC; // CIGVAC when '011 0111 1110 101' return Sys_DC; // CIGDVAC
```

```
types.
```

```
when '100 0111 1110 000' return Sys_DC; // CIPAE when '100 0111 1110 111' return Sys_DC; // CIGDPAE when '110 0111 1110 001' return Sys_DC; // CIPAPA when '110 0111 1110 101' return Sys_DC; // CIGDPAPA when '000 0111 1111 001' return Sys_DC; // CIVAPS when '000 0111 1111 101' return Sys_DC; // CIGDVAPS when '000 0111 0001 000' return Sys_IC; // IALLUIS when '000 0111 0101 000' return Sys_IC; // IALLU when '011 0111 0101 001' return Sys_IC; // IVAU when '000 1000 0001 000' return Sys_TLBI; // VMALLE1OS when '000 1000 0001 001' return Sys_TLBI; // VAE1OS when '000 1000 0001 010' return Sys_TLBI; // ASIDE1OS when '000 1000 0001 011' return Sys_TLBI; // VAAE1OS when '000 1000 0001 101' return Sys_TLBI; // VALE1OS when '000 1000 0001 111' return Sys_TLBI; // VAALE1OS when '000 1000 0010 001' return Sys_TLBI; // RVAE1IS when '000 1000 0010 011' return Sys_TLBI; // RVAAE1IS when '000 1000 0010 101' return Sys_TLBI; // RVALE1IS when '000 1000 0010 111' return Sys_TLBI; // RVAALE1IS when '000 1000 0011 000' return Sys_TLBI; // VMALLE1IS when '000 1000 0011 001' return Sys_TLBI; // VAE1IS when '000 1000 0011 010' return Sys_TLBI; // ASIDE1IS when '000 1000 0011 011' return Sys_TLBI; // VAAE1IS when '000 1000 0011 101' return Sys_TLBI; // VALE1IS when '000 1000 0011 111' return Sys_TLBI; // VAALE1IS when '000 1000 0101 001' return Sys_TLBI; // RVAE1OS when '000 1000 0101 011' return Sys_TLBI; // RVAAE1OS when '000 1000 0101 101' return Sys_TLBI; // RVALE1OS when '000 1000 0101 111' return Sys_TLBI; // RVAALE1OS when '000 1000 0110 001' return Sys_TLBI; // RVAE1 when '000 1000 0110 011' return Sys_TLBI; // RVAAE1 when '000 1000 0110 101' return Sys_TLBI; // RVALE1 when '000 1000 0110 111' return Sys_TLBI; // RVAALE1 when '000 1000 0111 000' return Sys_TLBI; // VMALLE1 when '000 1000 0111 001' return Sys_TLBI; // VAE1 when '000 1000 0111 010' return Sys_TLBI; // ASIDE1 when '000 1000 0111 011' return Sys_TLBI; // VAAE1 when '000 1000 0111 101' return Sys_TLBI; // VALE1 when '000 1000 0111 111' return Sys_TLBI; // VAALE1 when '000 1001 0001 000' return Sys_TLBI; // VMALLE1OSNXS when '000 1001 0001 001' return Sys_TLBI; // VAE1OSNXS when '000 1001 0001 010' return Sys_TLBI; // ASIDE1OSNXS when '000 1001 0001 011' return Sys_TLBI; // VAAE1OSNXS when '000 1001 0001 101' return Sys_TLBI; // VALE1OSNXS when '000 1001 0001 111' return Sys_TLBI; // VAALE1OSNXS when '000 1001 0010 001' return Sys_TLBI; // RVAE1ISNXS when '000 1001 0010 011' return Sys_TLBI; // RVAAE1ISNXS when '000 1001 0010 101' return Sys_TLBI; // RVALE1ISNXS when '000 1001 0010 111' return Sys_TLBI; // RVAALE1ISNXS when '000 1001 0011 000' return Sys_TLBI; // VMALLE1ISNXS when '000 1001 0011 001' return Sys_TLBI; // VAE1ISNXS when '000 1001 0011 010' return Sys_TLBI; // ASIDE1ISNXS when '000 1001 0011 011' return Sys_TLBI; // VAAE1ISNXS when '000 1001 0011 101' return Sys_TLBI; // VALE1ISNXS when '000 1001 0011 111' return Sys_TLBI; // VAALE1ISNXS when '000 1001 0101 001' return Sys_TLBI; // RVAE1OSNXS when '000 1001 0101 011' return Sys_TLBI; // RVAAE1OSNXS when '000 1001 0101 101' return Sys_TLBI; // RVALE1OSNXS when '000 1001 0101 111' return Sys_TLBI; // RVAALE1OSNXS when '000 1001 0110 001' return Sys_TLBI; // RVAE1NXS when '000 1001 0110 011' return Sys_TLBI; // RVAAE1NXS when '000 1001 0110 101' return Sys_TLBI; // RVALE1NXS when '000 1001 0110 111' return Sys_TLBI; // RVAALE1NXS when '000 1001 0111 000' return Sys_TLBI; // VMALLE1NXS when '000 1001 0111 001' return Sys_TLBI; // VAE1NXS when '000 1001 0111 010' return Sys_TLBI; // ASIDE1NXS
```

```
when '000 1001 0111 011' return Sys_TLBI; // VAAE1NXS when '000 1001 0111 101' return Sys_TLBI; // VALE1NXS when '000 1001 0111 111' return Sys_TLBI; // VAALE1NXS when '100 1000 0000 001' return Sys_TLBI; // IPAS2E1IS when '100 1000 0000 010' return Sys_TLBI; // RIPAS2E1IS when '100 1000 0000 101' return Sys_TLBI; // IPAS2LE1IS when '100 1000 0000 110' return Sys_TLBI; // RIPAS2LE1IS when '100 1000 0001 000' return Sys_TLBI; // ALLE2OS when '100 1000 0001 001' return Sys_TLBI; // VAE2OS when '100 1000 0001 100' return Sys_TLBI; // ALLE1OS when '100 1000 0001 101' return Sys_TLBI; // VALE2OS when '100 1000 0001 110' return Sys_TLBI; // VMALLS12E1OS when '100 1000 0010 001' return Sys_TLBI; // RVAE2IS when '100 1000 0010 101' return Sys_TLBI; // RVALE2IS when '100 1000 0011 000' return Sys_TLBI; // ALLE2IS when '100 1000 0011 001' return Sys_TLBI; // VAE2IS when '100 1000 0011 100' return Sys_TLBI; // ALLE1IS when '100 1000 0011 101' return Sys_TLBI; // VALE2IS when '100 1000 0011 110' return Sys_TLBI; // VMALLS12E1IS when '100 1000 0100 000' return Sys_TLBI; // IPAS2E1OS when '100 1000 0100 001' return Sys_TLBI; // IPAS2E1 when '100 1000 0100 010' return Sys_TLBI; // RIPAS2E1 when '100 1000 0100 011' return Sys_TLBI; // RIPAS2E1OS when '100 1000 0100 100' return Sys_TLBI; // IPAS2LE1OS when '100 1000 0100 101' return Sys_TLBI; // IPAS2LE1 when '100 1000 0100 110' return Sys_TLBI; // RIPAS2LE1 when '100 1000 0100 111' return Sys_TLBI; // RIPAS2LE1OS when '100 1000 0101 001' return Sys_TLBI; // RVAE2OS when '100 1000 0101 101' return Sys_TLBI; // RVALE2OS when '100 1000 0110 001' return Sys_TLBI; // RVAE2 when '100 1000 0110 101' return Sys_TLBI; // RVALE2 when '100 1000 0111 000' return Sys_TLBI; // ALLE2 when '100 1000 0111 001' return Sys_TLBI; // VAE2 when '100 1000 0111 100' return Sys_TLBI; // ALLE1 when '100 1000 0111 101' return Sys_TLBI; // VALE2 when '100 1000 0111 110' return Sys_TLBI; // VMALLS12E1 when '100 1001 0000 001' return Sys_TLBI; // IPAS2E1ISNXS when '100 1001 0000 010' return Sys_TLBI; // RIPAS2E1ISNXS when '100 1001 0000 101' return Sys_TLBI; // IPAS2LE1ISNXS when '100 1001 0000 110' return Sys_TLBI; // RIPAS2LE1ISNXS when '100 1001 0001 000' return Sys_TLBI; // ALLE2OSNXS when '100 1001 0001 001' return Sys_TLBI; // VAE2OSNXS when '100 1001 0001 100' return Sys_TLBI; // ALLE1OSNXS when '100 1001 0001 101' return Sys_TLBI; // VALE2OSNXS when '100 1001 0001 110' return Sys_TLBI; // VMALLS12E1OSNXS when '100 1001 0010 001' return Sys_TLBI; // RVAE2ISNXS when '100 1001 0010 101' return Sys_TLBI; // RVALE2ISNXS when '100 1001 0011 000' return Sys_TLBI; // ALLE2ISNXS when '100 1001 0011 001' return Sys_TLBI; // VAE2ISNXS when '100 1001 0011 100' return Sys_TLBI; // ALLE1ISNXS when '100 1001 0011 101' return Sys_TLBI; // VALE2ISNXS when '100 1001 0011 110' return Sys_TLBI; // VMALLS12E1ISNXS when '100 1001 0100 000' return Sys_TLBI; // IPAS2E1OSNXS when '100 1001 0100 001' return Sys_TLBI; // IPAS2E1NXS when '100 1001 0100 010' return Sys_TLBI; // RIPAS2E1NXS when '100 1001 0100 011' return Sys_TLBI; // RIPAS2E1OSNXS when '100 1001 0100 100' return Sys_TLBI; // IPAS2LE1OSNXS when '100 1001 0100 101' return Sys_TLBI; // IPAS2LE1NXS when '100 1001 0100 110' return Sys_TLBI; // RIPAS2LE1NXS when '100 1001 0100 111' return Sys_TLBI; // RIPAS2LE1OSNXS when '100 1001 0101 001' return Sys_TLBI; // RVAE2OSNXS when '100 1001 0101 101' return Sys_TLBI; // RVALE2OSNXS when '100 1001 0110 001' return Sys_TLBI; // RVAE2NXS when '100 1001 0110 101' return Sys_TLBI; // RVALE2NXS when '100 1001 0111 000' return Sys_TLBI; // ALLE2NXS when '100 1001 0111 001' return Sys_TLBI; // VAE2NXS
```

```
when '100 1001 0111 100' return Sys_TLBI; // ALLE1NXS when '100 1001 0111 101' return Sys_TLBI; // VALE2NXS when '100 1001 0111 110' return Sys_TLBI; // VMALLS12E1NXS when '110 1000 0001 000' return Sys_TLBI; // ALLE3OS when '110 1000 0001 001' return Sys_TLBI; // VAE3OS when '110 1000 0001 100' return Sys_TLBI; // PAALLOS when '110 1000 0001 101' return Sys_TLBI; // VALE3OS when '110 1000 0010 001' return Sys_TLBI; // RVAE3IS when '110 1000 0010 101' return Sys_TLBI; // RVALE3IS when '110 1000 0011 000' return Sys_TLBI; // ALLE3IS when '110 1000 0011 001' return Sys_TLBI; // VAE3IS when '110 1000 0011 101' return Sys_TLBI; // VALE3IS when '110 1000 0100 011' return Sys_TLBI; // RPAOS when '110 1000 0100 111' return Sys_TLBI; // RPALOS when '110 1000 0101 001' return Sys_TLBI; // RVAE3OS when '110 1000 0101 101' return Sys_TLBI; // RVALE3OS when '110 1000 0110 001' return Sys_TLBI; // RVAE3 when '110 1000 0110 101' return Sys_TLBI; // RVALE3 when '110 1000 0111 000' return Sys_TLBI; // ALLE3 when '110 1000 0111 001' return Sys_TLBI; // VAE3 when '110 1000 0111 100' return Sys_TLBI; // PAALL when '110 1000 0111 101' return Sys_TLBI; // VALE3 when '110 1001 0001 000' return Sys_TLBI; // ALLE3OSNXS when '110 1001 0001 001' return Sys_TLBI; // VAE3OSNXS when '110 1001 0001 101' return Sys_TLBI; // VALE3OSNXS when '110 1001 0010 001' return Sys_TLBI; // RVAE3ISNXS when '110 1001 0010 101' return Sys_TLBI; // RVALE3ISNXS when '110 1001 0011 000' return Sys_TLBI; // ALLE3ISNXS when '110 1001 0011 001' return Sys_TLBI; // VAE3ISNXS when '110 1001 0011 101' return Sys_TLBI; // VALE3ISNXS when '110 1001 0101 001' return Sys_TLBI; // RVAE3OSNXS when '110 1001 0101 101' return Sys_TLBI; // RVALE3OSNXS when '110 1001 0110 001' return Sys_TLBI; // RVAE3NXS when '110 1001 0110 101' return Sys_TLBI; // RVALE3NXS when '110 1001 0111 000' return Sys_TLBI; // ALLE3NXS when '110 1001 0111 001' return Sys_TLBI; // VAE3NXS when '110 1001 0111 101' return Sys_TLBI; // VALE3NXS otherwise return Sys_SYS;
```

## J1.1.3.367 SystemOp

```
// SystemOp // ======== // System instruction enumeration SystemOp { Sys_AT, Sys_BRB, Sys_DC, Sys_IC, Sys_TLBI, Sys_SYS };
```

```
types.
```

## J1.1.3.368 SysOp128

```
// SysOp128() // ========== SystemOp128 SysOp128(bits(3) op1, bits(4) CRn, bits(4) CRm, bits(3) op2) case op1:CRn:CRm:op2 of when '000 1000 0001 001' return Sys_TLBIP; // VAE1OS when '000 1000 0001 011' return Sys_TLBIP; // VAAE1OS
```

```
when '000 1000 0001 101' return Sys_TLBIP; // VALE1OS when '000 1000 0001 111' return Sys_TLBIP; // VAALE1OS when '000 1000 0011 001' return Sys_TLBIP; // VAE1IS when '000 1000 0011 011' return Sys_TLBIP; // VAAE1IS when '000 1000 0011 101' return Sys_TLBIP; // VALE1IS when '000 1000 0011 111' return Sys_TLBIP; // VAALE1IS when '000 1000 0111 001' return Sys_TLBIP; // VAE1 when '000 1000 0111 011' return Sys_TLBIP; // VAAE1 when '000 1000 0111 101' return Sys_TLBIP; // VALE1 when '000 1000 0111 111' return Sys_TLBIP; // VAALE1 when '000 1001 0001 001' return Sys_TLBIP; // VAE1OSNXS when '000 1001 0001 011' return Sys_TLBIP; // VAAE1OSNXS when '000 1001 0001 101' return Sys_TLBIP; // VALE1OSNXS when '000 1001 0001 111' return Sys_TLBIP; // VAALE1OSNXS when '000 1001 0011 001' return Sys_TLBIP; // VAE1ISNXS when '000 1001 0011 011' return Sys_TLBIP; // VAAE1ISNXS when '000 1001 0011 101' return Sys_TLBIP; // VALE1ISNXS when '000 1001 0011 111' return Sys_TLBIP; // VAALE1ISNXS when '000 1001 0111 001' return Sys_TLBIP; // VAE1NXS when '000 1001 0111 011' return Sys_TLBIP; // VAAE1NXS when '000 1001 0111 101' return Sys_TLBIP; // VALE1NXS when '000 1001 0111 111' return Sys_TLBIP; // VAALE1NXS when '100 1000 0001 001' return Sys_TLBIP; // VAE2OS when '100 1000 0001 101' return Sys_TLBIP; // VALE2OS when '100 1000 0011 001' return Sys_TLBIP; // VAE2IS when '100 1000 0011 101' return Sys_TLBIP; // VALE2IS when '100 1000 0111 001' return Sys_TLBIP; // VAE2 when '100 1000 0111 101' return Sys_TLBIP; // VALE2 when '100 1001 0001 001' return Sys_TLBIP; // VAE2OSNXS when '100 1001 0001 101' return Sys_TLBIP; // VALE2OSNXS when '100 1001 0011 001' return Sys_TLBIP; // VAE2ISNXS when '100 1001 0011 101' return Sys_TLBIP; // VALE2ISNXS when '100 1001 0111 001' return Sys_TLBIP; // VAE2NXS when '100 1001 0111 101' return Sys_TLBIP; // VALE2NXS when '110 1000 0001 001' return Sys_TLBIP; // VAE3OS when '110 1000 0001 101' return Sys_TLBIP; // VALE3OS when '110 1000 0011 001' return Sys_TLBIP; // VAE3IS when '110 1000 0011 101' return Sys_TLBIP; // VALE3IS when '110 1000 0111 001' return Sys_TLBIP; // VAE3 when '110 1000 0111 101' return Sys_TLBIP; // VALE3 when '110 1001 0001 001' return Sys_TLBIP; // VAE3OSNXS when '110 1001 0001 101' return Sys_TLBIP; // VALE3OSNXS when '110 1001 0011 001' return Sys_TLBIP; // VAE3ISNXS when '110 1001 0011 101' return Sys_TLBIP; // VALE3ISNXS when '110 1001 0111 001' return Sys_TLBIP; // VAE3NXS when '110 1001 0111 101' return Sys_TLBIP; // VALE3NXS when '100 1000 0000 001' return Sys_TLBIP; // IPAS2E1IS when '100 1000 0000 101' return Sys_TLBIP; // IPAS2LE1IS when '100 1000 0100 000' return Sys_TLBIP; // IPAS2E1OS when '100 1000 0100 001' return Sys_TLBIP; // IPAS2E1 when '100 1000 0100 100' return Sys_TLBIP; // IPAS2LE1OS when '100 1000 0100 101' return Sys_TLBIP; // IPAS2LE1 when '100 1001 0000 001' return Sys_TLBIP; // IPAS2E1ISNXS when '100 1001 0000 101' return Sys_TLBIP; // IPAS2LE1ISNXS when '100 1001 0100 000' return Sys_TLBIP; // IPAS2E1OSNXS when '100 1001 0100 001' return Sys_TLBIP; // IPAS2E1NXS when '100 1001 0100 100' return Sys_TLBIP; // IPAS2LE1OSNXS when '100 1001 0100 101' return Sys_TLBIP; // IPAS2LE1NXS when '000 1000 0010 001' return Sys_TLBIP; // RVAE1IS when '000 1000 0010 011' return Sys_TLBIP; // RVAAE1IS when '000 1000 0010 101' return Sys_TLBIP; // RVALE1IS when '000 1000 0010 111' return Sys_TLBIP; // RVAALE1IS when '000 1000 0101 001' return Sys_TLBIP; // RVAE1OS when '000 1000 0101 011' return Sys_TLBIP; // RVAAE1OS when '000 1000 0101 101' return Sys_TLBIP; // RVALE1OS when '000 1000 0101 111' return Sys_TLBIP; // RVAALE1OS
```

```
when '000 1000 0110 001' return Sys_TLBIP; // RVAE1 when '000 1000 0110 011' return Sys_TLBIP; // RVAAE1 when '000 1000 0110 101' return Sys_TLBIP; // RVALE1 when '000 1000 0110 111' return Sys_TLBIP; // RVAALE1 when '000 1001 0010 001' return Sys_TLBIP; // RVAE1ISNXS when '000 1001 0010 011' return Sys_TLBIP; // RVAAE1ISNXS when '000 1001 0010 101' return Sys_TLBIP; // RVALE1ISNXS when '000 1001 0010 111' return Sys_TLBIP; // RVAALE1ISNXS when '000 1001 0101 001' return Sys_TLBIP; // RVAE1OSNXS when '000 1001 0101 011' return Sys_TLBIP; // RVAAE1OSNXS when '000 1001 0101 101' return Sys_TLBIP; // RVALE1OSNXS when '000 1001 0101 111' return Sys_TLBIP; // RVAALE1OSNXS when '000 1001 0110 001' return Sys_TLBIP; // RVAE1NXS when '000 1001 0110 011' return Sys_TLBIP; // RVAAE1NXS when '000 1001 0110 101' return Sys_TLBIP; // RVALE1NXS when '000 1001 0110 111' return Sys_TLBIP; // RVAALE1NXS when '100 1000 0010 001' return Sys_TLBIP; // RVAE2IS when '100 1000 0010 101' return Sys_TLBIP; // RVALE2IS when '100 1000 0101 001' return Sys_TLBIP; // RVAE2OS when '100 1000 0101 101' return Sys_TLBIP; // RVALE2OS when '100 1000 0110 001' return Sys_TLBIP; // RVAE2 when '100 1000 0110 101' return Sys_TLBIP; // RVALE2 when '100 1001 0010 001' return Sys_TLBIP; // RVAE2ISNXS when '100 1001 0010 101' return Sys_TLBIP; // RVALE2ISNXS when '100 1001 0101 001' return Sys_TLBIP; // RVAE2OSNXS when '100 1001 0101 101' return Sys_TLBIP; // RVALE2OSNXS when '100 1001 0110 001' return Sys_TLBIP; // RVAE2NXS when '100 1001 0110 101' return Sys_TLBIP; // RVALE2NXS when '110 1000 0010 001' return Sys_TLBIP; // RVAE3IS when '110 1000 0010 101' return Sys_TLBIP; // RVALE3IS when '110 1000 0101 001' return Sys_TLBIP; // RVAE3OS when '110 1000 0101 101' return Sys_TLBIP; // RVALE3OS when '110 1000 0110 001' return Sys_TLBIP; // RVAE3 when '110 1000 0110 101' return Sys_TLBIP; // RVALE3 when '110 1001 0010 001' return Sys_TLBIP; // RVAE3ISNXS when '110 1001 0010 101' return Sys_TLBIP; // RVALE3ISNXS when '110 1001 0101 001' return Sys_TLBIP; // RVAE3OSNXS when '110 1001 0101 101' return Sys_TLBIP; // RVALE3OSNXS when '110 1001 0110 001' return Sys_TLBIP; // RVAE3NXS when '110 1001 0110 101' return Sys_TLBIP; // RVALE3NXS when '100 1000 0000 010' return Sys_TLBIP; // RIPAS2E1IS when '100 1000 0000 110' return Sys_TLBIP; // RIPAS2LE1IS when '100 1000 0100 010' return Sys_TLBIP; // RIPAS2E1 when '100 1000 0100 011' return Sys_TLBIP; // RIPAS2E1OS when '100 1000 0100 110' return Sys_TLBIP; // RIPAS2LE1 when '100 1000 0100 111' return Sys_TLBIP; // RIPAS2LE1OS when '100 1001 0000 010' return Sys_TLBIP; // RIPAS2E1ISNXS when '100 1001 0000 110' return Sys_TLBIP; // RIPAS2LE1ISNXS when '100 1001 0100 010' return Sys_TLBIP; // RIPAS2E1NXS when '100 1001 0100 011' return Sys_TLBIP; // RIPAS2E1OSNXS when '100 1001 0100 110' return Sys_TLBIP; // RIPAS2LE1NXS when '100 1001 0100 111' return Sys_TLBIP; // RIPAS2LE1OSNXS otherwise return Sys_SYSP;
```

## J1.1.3.369 SystemOp128

```
// SystemOp128() // ============= // System instruction types. enumeration SystemOp128
```

```
{Sys_TLBIP, Sys_SYSP};
```

## J1.1.3.370 ELR\_EL

```
// ELR_EL -getter // =============== bits(64) ELR_EL[bits(2) el] bits(64) r; case el of when EL1 r = ELR_EL1; when EL2 r = ELR_EL2; when EL3 r = ELR_EL3; otherwise Unreachable(); return r; // ELR_EL -setter // =============== ELR_EL[bits(2) el] = bits(64) value constant bits(64) r = value; case el of when EL1 ELR_EL1 = r; when EL2 ELR_EL2 = r; when EL3 ELR_EL3 = r; otherwise Unreachable(); return;
```

## J1.1.3.371 ELR\_ELx

```
// ELR_ELx - getter // ================ bits(64) ELR_ELx[] assert PSTATE.EL != EL0; return ELR_EL[PSTATE.EL]; // ELR_ELx - setter // ================ ELR_ELx[] = bits(64) value assert PSTATE.EL != EL0; ELR_EL[PSTATE.EL] = value; return;
```

## J1.1.3.372 ESR\_EL

```
// ESR_EL -getter // =============== ESRType ESR_EL[bits(2) regime] bits(64) r; case regime of when EL1 r = ESR_EL1; when EL2 r = ESR_EL2; when EL3 r = ESR_EL3; otherwise Unreachable(); return r; // ESR_EL -setter // =============== ESR_EL[bits(2) regime] = ESRType value constant bits(64) r = value; case regime of
```

```
when EL1 ESR_EL1 = r; when EL2 ESR_EL2 = r; when EL3 ESR_EL3 = r; otherwise Unreachable(); return;
```

## J1.1.3.373 ESR\_ELx

```
// ESR_ELx - getter // ================ ESRType ESR_ELx[] return ESR_EL[S1TranslationRegime()]; // ESR_ELx - setter // ================ ESR_ELx[] = ESRType value ESR_EL[S1TranslationRegime()] = value;
```

## J1.1.3.374 FAR\_EL

```
// FAR_EL -getter // =============== bits(64) FAR_EL[bits(2) regime] bits(64) r; case regime of when EL1 r = FAR_EL1; when EL2 r = FAR_EL2; when EL3 r = FAR_EL3; otherwise Unreachable(); return r; // FAR_EL -setter // =============== FAR_EL[bits(2) regime] = bits(64) value constant bits(64) r = value; case regime of when EL1 FAR_EL1 = r; when EL2 FAR_EL2 = r; when EL3 FAR_EL3 = r; otherwise Unreachable(); return;
```

## J1.1.3.375 FAR\_ELx

```
// FAR_ELx - getter // ================ bits(64) FAR_ELx[] return FAR_EL[S1TranslationRegime()]; // FAR_ELx - setter // ================ FAR_ELx[] = bits(64) value FAR_EL[S1TranslationRegime()] = value; return;
```

## J1.1.3.376 PFAR\_EL

```
// PFAR_EL - getter // ================ bits(64) PFAR_EL[bits(2) regime] assert (IsFeatureImplemented(FEAT_PFAR) || (regime == EL3 && IsFeatureImplemented(FEAT_RME))); bits(64) r; case regime of when EL1 r = PFAR_EL1; when EL2 r = PFAR_EL2; when EL3 r = MFAR_EL3; otherwise Unreachable(); return r; // PFAR_EL - setter // ================ PFAR_EL[bits(2) regime] = bits(64) value constant bits(64) r = value; assert (IsFeatureImplemented(FEAT_PFAR) || (IsFeatureImplemented(FEAT_RME) && regime == EL3)); case regime of when EL1 PFAR_EL1 = r; when EL2 PFAR_EL2 = r; when EL3 MFAR_EL3 = r; otherwise Unreachable(); return;
```

## J1.1.3.377 PFAR\_ELx

```
// PFAR_ELx - getter // ================= bits(64) PFAR_ELx[] return PFAR_EL[S1TranslationRegime()]; // PFAR_ELx - setter // ================= PFAR_ELx[] = bits(64) value PFAR_EL[S1TranslationRegime()] = value; return;
```

## J1.1.3.378 SCTLR\_EL

```
// SCTLR_EL - getter // ================= SCTLRType SCTLR_EL[bits(2) regime] bits(64) r; case regime of when EL1 r = SCTLR_EL1; when EL2 r = SCTLR_EL2; when EL3 r = SCTLR_EL3; otherwise Unreachable(); return r;
```

## J1.1.3.379 SCTLR\_ELx

```
// SCTLR_ELx - getter // ================== SCTLRType SCTLR_ELx[] return SCTLR_EL[S1TranslationRegime()];
```

## J1.1.3.380 VBAR\_EL

```
// VBAR_EL - getter // ================ bits(64) VBAR_EL[bits(2) regime] bits(64) r; case regime of when EL1 r = VBAR_EL1; when EL2 r = VBAR_EL2; when EL3 r = VBAR_EL3; otherwise Unreachable(); return r;
```

## J1.1.3.381 VBAR\_ELx

```
// VBAR_ELx - getter // ================= bits(64) VBAR_ELx[] return VBAR_EL[S1TranslationRegime()];
```

## J1.1.3.382 AArch64.CheckDAIFAccess

```
// AArch64.CheckDAIFAccess() // ========================= // Check that an AArch64 MSR/MRS access to the DAIF flags is permitted. AArch64.CheckDAIFAccess(PSTATEField field) if PSTATE.EL == EL0 && field IN {PSTATEField_DAIFSet, PSTATEField_DAIFClr} then if IsInHost() || SCTLR_EL1.UMA == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18);
```

## J1.1.3.383 AArch64.ChooseNonExcludedTag

```
// AArch64.ChooseNonExcludedTag() // ============================== // Return a tag derived from the start and the offset values, excluding // any tags in the given mask. bits(4) AArch64.ChooseNonExcludedTag(bits(4) tag_in, bits(4) offset_in, bits(16) exclude) bits(4) tag = tag_in; bits(4) offset = offset_in; if IsOnes(exclude) then return '0000'; if offset == '0000' then
```

```
while exclude<UInt(tag)> == '1' do tag = tag + '0001'; while offset != '0000' do offset = offset - '0001'; tag = tag + '0001'; while exclude<UInt(tag)> == '1' do tag = tag + '0001'; return tag;
```

## J1.1.3.384 AArch64.ChooseNonExludedTagOrZero

```
// AArch64.ChooseNonExludedTagOrZero() // =================================== // Return a tag derived from the start and the offset values, excluding any // tags in the given mask, or zero if Allocation Tag access is not enabled. bits(4) AArch64.ChooseNonExcludedTagOrZero(bits(4) tag, bits(4) offset, bits(16) exclude) if IsMTEEnabled(PSTATE.EL) then return AArch64.ChooseNonExcludedTag(tag, offset, exclude); else return '0000';
```

## J1.1.3.385 AArch64.ChooseTagOrZero

```
// AArch64.ChooseTagOrZero() // ========================= // Return a tag, excluding any tags in the given mask, , or zero if Allocation // Tag access is not enabled. bits(4) AArch64.ChooseTagOrZero(bits(16) exclude) if IsMTEEnabled(PSTATE.EL) then if GCR_EL1.RRND == '1' then if IsOnes(exclude) then return '0000'; else return ChooseRandomNonExcludedTag(exclude); else constant bits(4) start_tag = RGSR_EL1.TAG; constant bits(4) offset = AArch64.RandomTag(); RGSR_EL1.TAG = AArch64.ChooseNonExcludedTag(start_tag, offset, exclude); return RGSR_EL1.TAG; else return '0000';
```

## J1.1.3.386 AArch64.ExecutingERETInstr

```
// AArch64.ExecutingERETInstr() // ============================ // Returns TRUE if current instruction is ERET. boolean AArch64.ExecutingERETInstr() instr = ThisInstr(); return instr<31:12> == '11010110100111110000';
```

## J1.1.3.387 AArch64.ImpDefSysInstr

```
// AArch64.ImpDefSysInstr() // ======================== // Execute an implementation-defined system instruction with write (source operand). AArch64.ImpDefSysInstr(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t);
```

```
// AArch64.ImpDefSysInstr128() // =========================== // Execute an implementation-defined system instruction with write (128-bit source operand). AArch64.ImpDefSysInstr128(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t, integer t2);
```

```
// AArch64.ImpDefSysInstrWithResult() // ================================== // Execute an implementation-defined system instruction with read (result operand). AArch64.ImpDefSysInstrWithResult(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t);
```

```
// AArch64.ImpDefSysRegRead() // ========================== // Read from an implementation-defined System register and write the contents of the register // to X[t]. AArch64.ImpDefSysRegRead(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t);
```

```
// AArch64.ImpDefSysRegRead128() // ============================= // Read from an 128-bit implementation-defined System register // and write the contents of the register to X[t], X[t+1]. AArch64.ImpDefSysRegRead128(bits(2) op0, bits(3) op1, bits(4) bits(4) crm, bits(3) op2, integer t, integer t2);
```

## J1.1.3.388 AArch64.ImpDefSysInstr128 J1.1.3.389 AArch64.ImpDefSysInstrWithResult J1.1.3.390 AArch64.ImpDefSysRegRead J1.1.3.391 AArch64.ImpDefSysRegRead128 J1.1.3.392 AArch64.ImpDefSysRegWrite

```
crn,
```

```
// AArch64.ImpDefSysRegWrite() // =========================== // Write to an implementation-defined System register. AArch64.ImpDefSysRegWrite(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, integer t);
```

```
bits(3) op2,
```

## J1.1.3.393 AArch64.ImpDefSysRegWrite128

```
// AArch64.ImpDefSysRegWrite128() // ============================== // Write the contents of X[t], X[t+1] to an 128-bit implementation-defined System register. AArch64.ImpDefSysRegWrite128(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t, integer t2);
```

## J1.1.3.394 AArch64.InterruptPending

```
// AArch64.InterruptPending() // ========================== // Returns TRUE if there are any pending physical, virtual, or delegated // interrupts, and FALSE otherwise. boolean AArch64.InterruptPending() (irq_pending, -) = IRQPending(); (fiq_pending, -) = FIQPending(); constant boolean pending_physical_interrupt = (irq_pending || fiq_pending || IsPhysicalSErrorPending()); boolean pending_virtual_interrupt = FALSE; if EL2Enabled() && PSTATE.EL IN {EL0, EL1} && HCR_EL2.TGE == '0' then constant boolean virq_pending = (HCR_EL2.IMO == '1' && (VirtualIRQPending() || HCR_EL2.VI == '1')); constant boolean vfiq_pending = (HCR_EL2.FMO == '1' && (VirtualFIQPending() || HCR_EL2.VF == '1')); constant boolean vsei_pending = ((HCR_EL2.AMO == '1' || (IsFeatureImplemented(FEAT_DoubleFault2) && IsHCRXEL2Enabled() && HCRX_EL2.TMEA == '1')) && (IsVirtualSErrorPending() || HCR_EL2.VSE == '1')); pending_virtual_interrupt = vsei_pending || virq_pending || vfiq_pending; constant boolean pending_delegated_interrupt = (IsFeatureImplemented(FEAT_E3DSE) && PSTATE.EL != EL3 && SCR_EL3.<EnDSE,DSE> == '11'); return pending_physical_interrupt || pending_virtual_interrupt || pending_delegated_interrupt;
```

## J1.1.3.395 AArch64.NextRandomTagBit

```
// AArch64.NextRandomTagBit() // ========================== // Generate a random bit suitable for generating a random Allocation Tag. bit AArch64.NextRandomTagBit() assert GCR_EL1.RRND == '0'; constant bits(16) lfsr = RGSR_EL1.SEED<15:0>; constant bit top = lfsr<5> EOR lfsr<3> EOR lfsr<2> EOR lfsr<0>; RGSR_EL1.SEED<15:0> = top:lfsr<15:1>; return top;
```

## J1.1.3.396 AArch64.RandomTag

```
// AArch64.RandomTag() // =================== // Generate a random Allocation Tag.
```

```
bits(4) AArch64.RandomTag() bits(4) tag; for i = 0 to 3 tag<i> = AArch64.NextRandomTagBit(); return tag;
```

## J1.1.3.397 AArch64.SysInstr

```
// AArch64.SysInstr() // ================== // Execute a system instruction with write (source operand). AArch64.SysInstr(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t);
```

## J1.1.3.398 AArch64.SysInstrWithResult

```
// AArch64.SysInstrWithResult() // ============================ // Execute a system instruction with read (result operand). // Writes the result of the instruction to X[t]. AArch64.SysInstrWithResult(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm,
```

```
bits(3) op2, integer t);
```

## J1.1.3.399 AArch64.SysRegRead

```
// AArch64.SysRegRead() // ==================== // Read from a System register and write the contents of the register to X[t]. AArch64.SysRegRead(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t);
```

## J1.1.3.400 AArch64.SysRegWrite

```
// AArch64.SysRegWrite() // ===================== // Write to a System register. AArch64.SysRegWrite(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t);
```

## J1.1.3.401 BTypeCompatible

```
// BTypeCompatible // =============== // Records the branch target compatibility. // Returns TRUE if the branch target is compatible with PSTATE.BTYPE, else FALSE. boolean BTypeCompatible;
```

## J1.1.3.402 BTypeCompatible\_BTI

```
// BTypeCompatible_BTI // =================== // This function determines whether a given hint encoding is compatible with the current value of // PSTATE.BTYPE. A value of TRUE here indicates a valid Branch Target Identification instruction. boolean BTypeCompatible_BTI(bits(2) hintcode) case hintcode of when '00' return PSTATE.BTYPE == '00'; when '01' return PSTATE.BTYPE != '11'; when '10' return PSTATE.BTYPE != '10'; when '11' return TRUE;
```

```
// BTypeCompatible_PAC() // ===================== // Returns TRUE if PACIxSP or PACIxSPPC instructions are implicitly compatible with PSTATE.BTYPE, // FALSE otherwise. boolean BTypeCompatible_PAC(PACInstType pacinst) if PSTATE.BTYPE != '11' then return TRUE; else index = if PSTATE.EL == EL0 then 35 else 36; return SCTLR_ELx[]<index> == '0';
```

```
// BTypeCompatible_PACIXSP() // ========================= // Returns TRUE if PACIASP or PACIBSP instructions are implicitly compatible with PSTATE.BTYPE, // FALSE otherwise. boolean BTypeCompatible_PACIXSP() constant PACInstType pacinst = PACIxSP; return BTypeCompatible_PAC(pacinst);
```

## J1.1.3.403 BTypeCompatible\_PAC J1.1.3.404 BTypeCompatible\_PACIXSP J1.1.3.405 BTypeNext

```
// BTypeNext // ========= // Updated every cycle with a value that depends upon the instruction being executed. Assigned to // PSTATE.BTYPE at the end of each cycle and then cleared to zero. Allows SPSR save/restore of // BTYPE for the current instruction being executed. bits(2) BTypeNext;
```

## J1.1.3.406 ChooseRandomNonExcludedTag

```
// ChooseRandomNonExcludedTag() // ============================ // The ChooseRandomNonExcludedTag function is used when GCR_EL1.RRND == '1' to generate random // Allocation Tags. // // The resulting Allocation Tag is selected from the set [0,15], excluding any Allocation Tag where // exclude[tag_value] == 1. If 'exclude' is all Ones, the returned Allocation Tag is '0000'. // // This function is permitted to generate a non-deterministic selection from the set of non-excluded // Allocation Tags. A reasonable implementation should select a tag from a uniform distribution and // avoid common pitfalls such as modulo bias. // // This function can read RGSR_EL1 and/or write RGSR_EL1 to an IMPLEMENTATION DEFINED value. // If it is not capable of writing RGSR_EL1.SEED[15:0] to zero from a previous nonzero // RGSR_EL1.SEED value, it is IMPLEMENTATION DEFINED whether the randomness is significantly // impacted if RGSR_EL1.SEED[15:0] is set to zero.
```

## bits(4) ChooseRandomNonExcludedTag(bits(16) exclude\_in); J1.1.3.407 EffectiveBADDR // EffectiveBADDR() // ================ // Check if the given VA, held in a register BADDR field, is RESS and apply // CONSTRAINED UNPREDICTABLE behaviour if it is not. bits(64) EffectiveBADDR(bits(64) baddr\_in, boolean directread) bits(64) baddr = baddr\_in; // Determine top bit position based on feature support. constant integer n = (if IsFeatureImplemented(FEAT\_LVA3) then 57 elsif IsFeatureImplemented(FEAT\_LVA) then 53 else 49); // Check if the upper bits of the base address form a valid sign extension. if baddr&lt;63:n&gt; != Replicate(baddr&lt;n-1&gt;, 64-n) then c = ConstrainUnpredictable(Unpredictable\_BADDR\_RESS); assert c IN {Constraint\_RESS, Constraint\_ALLRESS, Constraint\_FAULT}; if c == Constraint\_ALLRESS || (!directread &amp;&amp; c == Constraint\_RESS) then baddr&lt;63:n&gt; = Replicate(baddr&lt;n-1&gt;, 64-n); // If c == Constraint\_FAULT, baddr will cause an Address Size fault when used. return baddr; J1.1.3.408 EffectiveICC\_SRE\_EL3\_Enable // EffectiveICC\_SRE\_EL3\_Enable() // ============================= // Returns the Effective value of ICC\_SRE\_EL3.Enable bit EffectiveICC\_SRE\_EL3\_Enable() return ICC\_SRE\_EL3.Enable; J1.1.3.409 InGuardedPage // InGuardedPage // ============= // Records whether the currently fetched instruction was retrieved from a guarded page, will be // TRUE if the GP bit in the page or block descriptor for the current instruction fetch was equal

```
// to one. boolean InGuardedPage;
```

## J1.1.3.410 IsHCRXEL2Enabled

```
// IsHCRXEL2Enabled() // ================== // Returns TRUE if access to HCRX_EL2 register is enabled, and FALSE otherwise. // Indirect read of HCRX_EL2 returns 0 when access is not enabled. boolean IsHCRXEL2Enabled() if !IsFeatureImplemented(FEAT_HCX) then return FALSE; if HaveEL(EL3) && SCR_EL3.HXEn == '0' then return FALSE; return EL2Enabled();
```

## J1.1.3.411 IsMTEEnabled

```
// IsMTEEnabled() // ============== // Returns TRUE if the currently selected MTE mechanism is enabled, and FALSE otherwise. boolean IsMTEEnabled(bits(2) el) constant Regime regime = TranslationRegime(el); boolean selected = FALSE; if IsPMTESelected(el) then if HaveEL(EL3) && SCR_EL3.ATA == '0' && el IN {EL0, EL1, EL2} then return FALSE; if EL2Enabled() && !ELIsInHost(EL0) && HCR_EL2.ATA == '0' && el IN {EL0, EL1} then return FALSE; selected = TRUE; if selected then case regime of when Regime_EL3 return SCTLR_EL3.ATA == '1'; when Regime_EL2 return SCTLR_EL2.ATA == '1'; when Regime_EL20 return if el == EL0 then SCTLR_EL2.ATA0 == '1' else SCTLR_EL2.ATA == '1'; when Regime_EL10 return if el == EL0 then SCTLR_EL1.ATA0 == '1' else SCTLR_EL1.ATA == '1'; otherwise Unreachable(); return FALSE;
```

## J1.1.3.412 IsPMTESelected

```
// IsPMTESelected() // ================ // Returns TRUE if Physical MTE is selected for the translation regime // associated with the EL, and FALSE otherwise boolean IsPMTESelected(bits(2) el) if !IsFeatureImplemented(FEAT_MTE2) then return FALSE;
```

```
return TRUE;
```

## J1.1.3.413 IsSCTLR2EL1Enabled

```
// IsSCTLR2EL1Enabled() // ==================== // Returns TRUE if access to SCTLR2_EL1 register is enabled, and FALSE otherwise. // Indirect read of SCTLR2_EL1 returns 0 when access is not enabled. boolean IsSCTLR2EL1Enabled() if !IsFeatureImplemented(FEAT_SCTLR2) then return FALSE; if HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then return FALSE; elsif (EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SCTLR2En == '0')) then return FALSE; else return TRUE;
```

## J1.1.3.414 IsSCTLR2EL2Enabled

```
// IsSCTLR2EL2Enabled() // ==================== // Returns TRUE if access to SCTLR2_EL2 register is enabled, and FALSE otherwise. // Indirect read of SCTLR2_EL2 returns 0 when access is not enabled. boolean IsSCTLR2EL2Enabled() if !IsFeatureImplemented(FEAT_SCTLR2) then return FALSE; if HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then return FALSE; return EL2Enabled();
```

## J1.1.3.415 IsTCR2EL1Enabled

```
// IsTCR2EL1Enabled() // ================== // Returns TRUE if access to TCR2_EL1 register is enabled, and FALSE otherwise. // Indirect read of TCR2_EL1 returns 0 when access is not enabled. boolean IsTCR2EL1Enabled() if !IsFeatureImplemented(FEAT_TCR2) then return FALSE; if HaveEL(EL3) && SCR_EL3.TCR2En == '0' then return FALSE; elsif (EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.TCR2En == '0')) then return FALSE; else return TRUE;
```

## J1.1.3.416 IsTCR2EL2Enabled

```
// IsTCR2EL2Enabled() // ================== // Returns TRUE if access to TCR2_EL2 register is enabled, and FALSE otherwise. // Indirect read of TCR2_EL2 returns 0 when access is not enabled. boolean IsTCR2EL2Enabled() if !IsFeatureImplemented(FEAT_TCR2) then return FALSE; if HaveEL(EL3) && SCR_EL3.TCR2En == '0' then return FALSE;
```

```
return EL2Enabled();
```

## J1.1.3.417 PACInstType // PACInstType // =========== enumeration PACInstType { PACIxSP, PACIxSPPC, }; J1.1.3.418 SetBTypeCompatible // SetBTypeCompatible() // ==================== // Sets the value of BTypeCompatible global variable used by BTI SetBTypeCompatible(boolean x) BTypeCompatible = x; J1.1.3.419 SetBTypeNext // SetBTypeNext() // ============== // Set the value of BTypeNext global variable used by BTI SetBTypeNext(bits(2) x) BTypeNext = x; J1.1.3.420 SetInGuardedPage // SetInGuardedPage() // ================== // Global state updated to denote if memory access is from a guarded page. SetInGuardedPage(boolean guardedpage) InGuardedPage = guardedpage; J1.1.3.421 AArch64.SysInstr128 // AArch64.SysInstr128() // ===================== // Execute a system instruction with write (2 64-bit source operands). AArch64.SysInstr128(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t, integer t2); J1.1.3.422 AArch64.SysRegRead128 X[t2].

```
// AArch64.SysRegRead128() // ======================= // Read from a 128-bit System register and write the contents of the register to X[t] and AArch64.SysRegRead128(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t, integer t2);
```

## J1.1.3.423 AArch64.SysRegWrite128

```
// AArch64.SysRegWrite128() // ======================== // Read the contents of X[t] and X[t2] and write the contents to a 128-bit System register. AArch64.SysRegWrite128(bits(2) op0, bits(3) op1, bits(4) crn, bits(4) crm, bits(3) op2, integer t, integer t2);
```

## J1.1.3.424 AArch64.TLBIP\_IPAS2

```
// AArch64.TLBIP_IPAS2() // ===================== // Invalidate by IPA all stage 2 only TLB entries in the indicated broadcast // domain matching the indicated VMID in the indicated regime with the indicated security state. // Note: stage 1 and stage 2 combined entries are not in the scope of this operation. // IPA and related parameters of the are derived from Xt. AArch64.TLBIP_IPAS2(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(128) Xt) assert PSTATE.EL IN {EL3, EL2}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_IPAS2; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = TRUE; r.level = level; r.attr = attr; r.ttl = Xt<47:44>; r.address = ZeroExtend(Xt<107:64> : Zeros(12), 64); r.d64 = r.ttl == '00xx'; r.d128 = TRUE; case security of when SS_NonSecure r.ipaspace = PAS_NonSecure; when SS_Secure r.ipaspace = if Xt<63> == '1' then PAS_NonSecure else PAS_Secure; when SS_Realm r.ipaspace = PAS_Realm; otherwise // Root security state does not have stage 2 translation Unreachable(); TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.425 AArch64.TLBIP\_RIPAS2

```
// AArch64.TLBIP_RIPAS2() // ====================== // Range invalidate by IPA all stage 2 only TLB entries in the indicated // broadcast domain matching the indicated VMID in the indicated regime with the indicated // security state. // Note: stage 1 and stage 2 combined entries are not in the scope of this operation. // The range of IPA and related parameters of the are derived from Xt.
```

```
AArch64.TLBIP_RIPAS2(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(128) Xt) assert PSTATE.EL IN {EL3, EL2, EL1}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_RIPAS2; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = TRUE; r.level = level; r.attr = attr; r.ttl<1:0> = Xt<38:37>; r.d64 = r.ttl<1:0> == '00'; r.d128 = TRUE; boolean valid; (valid, r.tg, r.address, r.end_address) = TLBIPRange(regime, Xt); if !valid then return; case security of when SS_NonSecure r.ipaspace = PAS_NonSecure; when SS_Secure r.ipaspace = if Xt<63> == '1' then PAS_NonSecure else PAS_Secure; when SS_Realm r.ipaspace = PAS_Realm; otherwise // Root security state does not have stage 2 translation Unreachable(); TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.426 AArch64.TLBIP\_RVA

```
// AArch64.TLBIP_RVA() // =================== // Range invalidate by VA range all stage 1 TLB entries in the indicated // broadcast domain matching the indicated VMID and ASID (where regime // supports VMID, ASID) in the indicated regime with the indicated security state. // ASID, and range related parameters are derived from Xt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch64.TLBIP_RVA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(128) Xt) assert PSTATE.EL IN {EL3, EL2, EL1}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_RVA; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.asid = Xt<63:48>; r.ttl<1:0> = Xt<38:37>;
```

```
r.d64 = r.ttl<1:0> == '00'; r.d128 = TRUE; boolean valid; (valid, r.tg, r.address, r.end_address) = TLBIPRange(regime, Xt); if !valid then return; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.427 AArch64.TLBIP\_RVAA

```
// AArch64.TLBIP_RVAA() // ==================== // Range invalidate by VA range all stage 1 TLB entries in the indicated // broadcast domain matching the indicated VMID (where regimesupports VMID) // and all ASID in the indicated regime with the indicated security state. // VA range related parameters are derived from Xt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch64.TLBIP_RVAA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(128) Xt) assert PSTATE.EL IN {EL3, EL2, EL1}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_RVAA; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.ttl<1:0> = Xt<38:37>; r.d64 = r.ttl<1:0> == '00'; r.d128 = TRUE; boolean valid; (valid, r.tg, r.address, r.end_address) = TLBIPRange(regime, Xt); if !valid then return; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.428 AArch64.TLBIP\_VA

```
// AArch64.TLBIP_VA() // ================== // Invalidate by VA all stage 1 TLB entries in the indicated broadcast domain // matching the indicated VMID and ASID (where regime supports VMID, ASID) in the indicated regime // with the indicated security state. // ASID, VA and related parameters are derived from Xt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch64.TLBIP_VA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(128) Xt) assert PSTATE.EL IN {EL3, EL2, EL1};
```

```
Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_VA; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.asid = Xt<63:48>; r.ttl = Xt<47:44>; r.address = ZeroExtend(Xt<107:64> : Zeros(12), 64); r.d64 = r.ttl == '00xx'; r.d128 = TRUE; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, return;
```

```
// AArch64.TLBI_ALL() // ================== // Invalidate all entries for the indicated translation regime with the // the indicated security state for all TLBs within the indicated broadcast // Invalidation applies to all applicable stage 1 and stage 2 entries.
```

```
r); J1.1.3.429 AArch64.TLBIP_VAA // AArch64.TLBIP_VAA() // =================== // Invalidate by VA all stage 1 TLB entries in the indicated broadcast domain // matching the indicated VMID (where regime supports VMID) and all ASID in the indicated regime // with the indicated security state. // VA and related parameters are derived from Xt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch64.TLBIP_VAA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(128) Xt) assert PSTATE.EL IN {EL3, EL2, EL1}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_VAA; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.ttl = Xt<47:44>; r.address = ZeroExtend(Xt<107:64> : Zeros(12), 64); r.d64 = r.ttl == '00xx'; r.d128 = TRUE; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return; J1.1.3.430 AArch64.TLBI_ALL domain.
```

```
AArch64.TLBI_ALL(SecurityState security, Regime regime, Broadcast broadcast_in, TLBIMemAttr attr, bits(64) Xt) assert PSTATE.EL IN {EL3, EL2}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_ALL; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.level = TLBILevel_Any; r.attr = attr; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.431 AArch64.TLBI\_ASID

```
// AArch64.TLBI_ASID() // =================== // Invalidate all stage 1 entries matching the indicated VMID (where regime supports) // and ASID in the parameter Xt in the indicated translation regime with the // indicated security state for all TLBs within the indicated broadcast domain. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch64.TLBI_ASID(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBIMemAttr attr, bits(64) Xt) assert PSTATE.EL IN {EL3, EL2, EL1}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_ASID; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = TLBILevel_Any; r.attr = attr; r.asid = Xt<63:48>; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.432 AArch64.TLBI\_IPAS2

```
// AArch64.TLBI_IPAS2() // ==================== // Invalidate by IPA all stage 2 only TLB entries in the indicated broadcast // domain matching the indicated VMID in the indicated regime with the indicated security state. // Note: stage 1 and stage 2 combined entries are not in the scope of this operation. // IPA and related parameters of the are derived from Xt. AArch64.TLBI_IPAS2(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(64) Xt) assert PSTATE.EL IN {EL3, EL2}; Broadcast broadcast = broadcast_in; TLBIRecord r;
```

```
r.op = TLBIOp_IPAS2; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = TRUE; r.level = level; r.attr = attr; r.ttl = Xt<47:44>; r.address = ZeroExtend(Xt<39:0> : Zeros(12), 64); r.d64 = TRUE; r.d128 = r.ttl == '00xx'; case security of when SS_NonSecure r.ipaspace = PAS_NonSecure; when SS_Secure r.ipaspace = if Xt<63> == '1' then PAS_NonSecure else PAS_Secure; when SS_Realm r.ipaspace = PAS_Realm; otherwise // Root security state does not have stage 2 translation Unreachable(); TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.433 AArch64.TLBI\_PAALL

```
// AArch64.TLBI_PAALL() // ==================== // TLB Invalidate ALL GPT Information. // Invalidates cached copies of GPT entries from TLBs in the indicated // Shareabilty domain. // The invalidation applies to all TLB entries containing GPT information. AArch64.TLBI_PAALL(Broadcast broadcast) assert IsFeatureImplemented(FEAT_RME) && PSTATE.EL == EL3; TLBIRecord r; // r.security and r.regime do not apply for TLBI by PA operations r.op = TLBIOp_PAALL; r.level = TLBILevel_Any; r.attr = TLBI_AllAttr; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.434 AArch64.TLBI\_RIPAS2

```
// AArch64.TLBI_RIPAS2() // ===================== // Range invalidate by IPA all stage 2 only TLB entries in the indicated // broadcast domain matching the indicated VMID in the indicated regime with the indicated // security state. // Note: stage 1 and stage 2 combined entries are not in the scope of this operation. // The range of IPA and related parameters of the are derived from Xt. AArch64.TLBI_RIPAS2(SecurityState security, Regime regime, bits(16) vmid,
```

```
Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(64) Xt) assert PSTATE.EL IN {EL3, EL2, EL1}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_RIPAS2; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = TRUE; r.level = level; r.attr = attr; r.ttl<1:0> = Xt<38:37>; r.d64 = TRUE; r.d128 = r.ttl<1:0> == '00'; boolean valid; (valid, r.tg, r.address, r.end_address) = TLBIRange(regime, Xt); if !valid then return; case security of when SS_NonSecure r.ipaspace = PAS_NonSecure; when SS_Secure r.ipaspace = if Xt<63> == '1' then PAS_NonSecure else PAS_Secure; when SS_Realm r.ipaspace = PAS_Realm; otherwise // Root security state does not have stage 2 translation Unreachable(); TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return; J1.1.3.435 AArch64.TLBI_RPA
```

```
// AArch64.TLBI_RPA() // ================== // TLB Range Invalidate GPT Information by PA. // Invalidates cached copies of GPT entries from TLBs in the indicated // Shareabilty domain. // The invalidation applies to TLB entries containing GPT information relating // to the indicated physical address range. // When the indicated level is // TLBILevel_Any : this applies to TLB entries containing GPT information // from all levels of the GPT walk // TLBILevel_Last : this applies to TLB entries containing GPT information // from the last level of the GPT walk AArch64.TLBI_RPA(TLBILevel level, bits(64) Xt, Broadcast broadcast) assert IsFeatureImplemented(FEAT_RME) && PSTATE.EL == EL3; TLBIRecord r; AddressSize range_bits; AddressSize p; // r.security and r.regime do not apply for TLBI by PA operations r.op = TLBIOp_RPA; r.level = level; r.attr = TLBI_AllAttr; // SIZE field
```

```
case Xt<47:44> of when '0000' range_bits = 12; // 4KB when '0001' range_bits = 14; // 16KB when '0010' range_bits = 16; // 64KB when '0011' range_bits = 21; // 2MB when '0100' range_bits = 25; // 32MB when '0101' range_bits = 29; // 512MB when '0110' range_bits = 30; // 1GB when '0111' range_bits = 34; // 16GB when '1000' range_bits = 36; // 64GB when '1001' range_bits = 39; // 512GB otherwise return; // Reserved encoding, no TLB entries are required to be invalidated // If SIZE selects a range smaller than PGS, then PGS is used instead case DecodePGS(GPCCR_EL3.PGS) of when PGS_4KB p = 12; when PGS_16KB p = 14; when PGS_64KB p = 16; otherwise return; // Reserved encoding, no TLB entries are required to be invalidated if range_bits < p then range_bits = p; bits(52) BaseADDR = Zeros(52); case GPCCR_EL3.PGS of when '00' BaseADDR<51:12> = Xt<39:0>; // 4KB when '10' BaseADDR<51:14> = Xt<39:2>; // 16KB when '01' BaseADDR<51:16> = Xt<39:4>; // 64KB // The calculation here automatically aligns BaseADDR to the size of // the region specififed in SIZE. However, the architecture does not // require this alignment and if BaseADDR is not aligned to the region // specified by SIZE then no entries are required to be invalidated. constant integer range_pbits = range_bits; constant bits(52) start_addr = BaseADDR AND NOT ZeroExtend(Ones(range_pbits), 52); constant bits(52) end_addr = start_addr + ZeroExtend(Ones(range_pbits), 52); // PASpace is not considered in TLBI by PA operations r.address = ZeroExtend(start_addr, 64); r.end_address = ZeroExtend(end_addr, 64); TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.436 AArch64.TLBI\_RVA

```
// AArch64.TLBI_RVA() // ================== // Range invalidate by VA range all stage 1 TLB entries in the indicated // broadcast domain matching the indicated VMID and ASID (where regime // supports VMID, ASID) in the indicated regime with the indicated security state. // ASID, and range related parameters are derived from Xt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch64.TLBI_RVA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(64) assert PSTATE.EL IN {EL3, EL2, EL1}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_RVA; r.from_aarch64 = TRUE; r.security = security; r.regime = regime;
```

```
Xt)
```

```
r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.asid = Xt<63:48>; r.ttl<1:0> = Xt<38:37>; r.d64 = TRUE; r.d128 = r.ttl<1:0> == '00'; boolean valid; (valid, r.tg, r.address, r.end_address) = if !valid then return; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

```
// AArch64.TLBI_VA() // ================= // Invalidate by VA all stage 1 TLB entries in the indicated broadcast domain // matching the indicated VMID and ASID (where regime supports VMID, ASID) in the indicated // with the indicated security state. // ASID, VA and related parameters are derived from Xt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation.
```

```
TLBIRange(regime, Xt); J1.1.3.437 AArch64.TLBI_RVAA // AArch64.TLBI_RVAA() // =================== // Range invalidate by VA range all stage 1 TLB entries in the indicated // broadcast domain matching the indicated VMID (where regimesupports VMID) // and all ASID in the indicated regime with the indicated security state. // VA range related parameters are derived from Xt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch64.TLBI_RVAA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBILevel level, TLBIMemAttr attr, bits(64) Xt) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_RVAA; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.ttl<1:0> = Xt<38:37>; r.d64 = TRUE; r.d128 = r.ttl<1:0> == '00'; boolean valid; (valid, r.tg, r.address, r.end_address) = TLBIRange(regime, Xt); if !valid then return; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return; J1.1.3.438 AArch64.TLBI_VA regime
```

```
AArch64.TLBI_VA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(64) assert PSTATE.EL IN {EL3, EL2, EL1}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_VA; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.asid = Xt<63:48>; r.ttl = Xt<47:44>; r.address = ZeroExtend(Xt<43:0> : Zeros(12), 64); r.d64 = TRUE; r.d128 = r.ttl == '00xx'; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.439 AArch64.TLBI\_VAA

```
// AArch64.TLBI_VAA() // ================== // Invalidate by VA all stage 1 TLB entries in the indicated broadcast domain // matching the indicated VMID (where regime supports VMID) and all ASID in the indicated regime // with the indicated security state. // VA and related parameters are derived from Xt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch64.TLBI_VAA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBILevel level, TLBIMemAttr attr, bits(64) Xt) assert PSTATE.EL IN {EL3, EL2, EL1}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_VAA; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.ttl = Xt<47:44>; r.address = ZeroExtend(Xt<43:0> : Zeros(12), 64); r.d64 = TRUE; r.d128 = r.ttl == '00xx'; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.440 AArch64.TLBI\_VMALL

```
Xt)
```

```
// AArch64.TLBI_VMALL() // ==================== // Invalidate all stage 1 entries for the indicated translation regime with the // the indicated security state for all TLBs within the indicated broadcast // domain that match the indicated VMID (where applicable). // Note: stage 1 and stage 2 combined entries are in the scope of this operation. // Note: stage 2 only entries are not in the scope of this operation. AArch64.TLBI_VMALL(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBIMemAttr attr, bits(64) Xt) assert PSTATE.EL IN {EL3, EL2, EL1}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_VMALL; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.level = TLBILevel_Any; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.attr = attr; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.441 AArch64.TLBI\_VMALLS12

```
// AArch64.TLBI_VMALLS12() // ======================= // Invalidate all stage 1 and stage 2 entries for the indicated translation // regime with the indicated security state for all TLBs within the indicated // broadcast domain that match the indicated VMID. AArch64.TLBI_VMALLS12(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBIMemAttr attr, bits(64) Xt) assert PSTATE.EL IN {EL3, EL2}; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_VMALLS12; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.level = TLBILevel_Any; r.vmid = vmid; r.use_vmid = TRUE; r.attr = attr; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.1.3.442 AArch64.TLBI\_VMALLWS2

```
// AArch64.TLBI_VMALLWS2() // ======================= // Remove stage 2 dirty state from entries for the indicated translation regime
```

```
// with the indicated security state for all TLBs within the indicated broadcast // domain that match the indicated VMID. AArch64.TLBI_VMALLWS2(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast_in, TLBIMemAttr attr, bits(64) Xt) assert PSTATE.EL IN {EL3, EL2}; assert regime == Regime_EL10; if security == SS_Secure && HaveEL(EL3) && SCR_EL3.EEL2 == '0' then return; Broadcast broadcast = broadcast_in; TLBIRecord r; r.op = TLBIOp_VMALLWS2; r.from_aarch64 = TRUE; r.security = security; r.regime = regime; r.level = TLBILevel_Any; r.vmid = vmid; r.use_vmid = TRUE; r.attr = attr; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return; J1.1.3.443 DecodeTLBITG // DecodeTLBITG() // ============== // Decode translation granule size in TLBI range instructions TGx DecodeTLBITG(bits(2) tg) case tg of when '01' return TGx_4KB; when '10' return TGx_16KB; when '11' return TGx_64KB; J1.1.3.444 GPTTLBIMatch // GPTTLBIMatch() // ============== // Determine whether the GPT TLB entry lies within the scope of invalidation boolean GPTTLBIMatch(TLBIRecord tlbi, GPTEntry gpt_entry) assert tlbi.op IN {TLBIOp_RPA, TLBIOp_PAALL}; boolean match; constant bits(64) entry_size_mask = ZeroExtend(Ones(gpt_entry.size), 64); constant bits(64) entry_end_address = (ZeroExtend(gpt_entry.pa<55:0> OR entry_size_mask<55:0>, 64)); constant bits(64) entry_start_address = (ZeroExtend(gpt_entry.pa<55:0> AND NOT entry_size_mask<55:0>, 64)); case tlbi.op of when TLBIOp_RPA match = (UInt(tlbi.address<55:0>) <= UInt(entry_end_address<55:0>) && UInt(tlbi.end_address<55:0>) > UInt(entry_start_address<55:0>) && (tlbi.level == TLBILevel_Any || gpt_entry.level == 1)); when TLBIOp_PAALL match = TRUE;
```

```
return match;
```

## J1.1.3.445 HasLargeAddress // HasLargeAddress() // ================= // Returns TRUE if the regime is configured for 52 bit addresses, FALSE otherwise. boolean HasLargeAddress(Regime regime) if !IsFeatureImplemented(FEAT\_LPA2) then return FALSE; case regime of when Regime\_EL3 return TCR\_EL3.DS == '1'; when Regime\_EL2 return TCR\_EL2.DS == '1'; when Regime\_EL20 return TCR\_EL2.DS == '1'; when Regime\_EL10 return TCR\_EL1.DS == '1'; otherwise Unreachable(); J1.1.3.446 ResTLBIRTTL // ResTLBIRTTL() // ============= // Determine whether the TTL field in TLBI instructions that do apply // to a range of addresses contains a reserved value boolean ResTLBIRTTL(bits(2) tg, bits(2) ttl) case ttl of when '00' return TRUE; when '01' return DecodeTLBITG(tg) == TGx\_16KB &amp;&amp; !IsFeatureImplemented(FEAT\_LPA2); otherwise return FALSE; J1.1.3.447 ResTLBITTL // ResTLBITTL() // ============ // Determine whether the TTL field in TLBI instructions that do not apply // to a range of addresses contains a reserved value boolean ResTLBITTL(bits(4) ttl) case ttl of when '00xx' return TRUE; when '0100' return !IsFeatureImplemented(FEAT\_LPA2); when '1000' return TRUE; when '1001' return !IsFeatureImplemented(FEAT\_LPA2); when '1100' return TRUE; otherwise return FALSE; J1.1.3.448 TGBits Granule.

```
// TGBits() // ======== // Return the number of least-significant address bits within a single Translation AddressSize TGBits(bits(2) tg)
```

```
case tg of when '01' return 12; // 4KB when '10' return 14; // 16KB when '11' return 16; // 64KB otherwise Unreachable();
```

## J1.1.3.449 TLBIMatch

```
// TLBIMatch() // =========== // Determine whether the TLB entry lies within the scope of invalidation boolean TLBIMatch(TLBIRecord tlbi, TLBRecord tlb_entry) boolean match; constant bits(64) entry_block_mask = ZeroExtend(Ones(tlb_entry.blocksize), 64); bits(64) entry_end_address = tlb_entry.context.ia OR entry_block_mask; bits(64) entry_start_address = tlb_entry.context.ia AND NOT entry_block_mask; case tlbi.op of when TLBIOp_DALL, TLBIOp_IALL match = (tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime); when TLBIOp_DASID, TLBIOp_IASID match = (tlb_entry.context.includes_s1 && tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime && tlbi.use_vmid == tlb_entry.context.use_vmid && (!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid) && (UseASID(tlb_entry.context) && tlb_entry.context.nG == '1' && tlbi.asid == tlb_entry.context.asid)); when TLBIOp_DVA, TLBIOp_IVA boolean regime_match; boolean context_match; boolean address_match; boolean level_match; regime_match = (tlb_entry.context.includes_s1 && tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime); context_match = (tlbi.use_vmid == tlb_entry.context.use_vmid && (!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid) && (!UseASID(tlb_entry.context) || tlbi.asid == tlb_entry.context.asid || tlb_entry.context.nG == '0')); constant integer addr_lsb = tlb_entry.blocksize; address_match = tlbi.address<55:addr_lsb> == tlb_entry.context.ia<55:addr_lsb>; level_match = (tlbi.level == TLBILevel_Any || !tlb_entry.walkstate.istable); match = regime_match && context_match && address_match && level_match; when TLBIOp_ALL relax_regime = (tlbi.from_aarch64 && tlbi.regime IN {Regime_EL20, Regime_EL2} && tlb_entry.context.regime IN {Regime_EL20, Regime_EL2}); match = (tlbi.security == tlb_entry.context.ss && (tlbi.regime == tlb_entry.context.regime || relax_regime)); when TLBIOp_ASID match = (tlb_entry.context.includes_s1 && tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime && tlbi.use_vmid == tlb_entry.context.use_vmid && (!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid) && (UseASID(tlb_entry.context) && tlb_entry.context.nG == '1' && tlbi.asid == tlb_entry.context.asid)); when TLBIOp_IPAS2, TLBIPOp_IPAS2 constant integer addr_lsb = tlb_entry.blocksize; match = (!tlb_entry.context.includes_s1 && tlb_entry.context.includes_s2 && tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime &&
```

```
(!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid) && tlbi.ipaspace == tlb_entry.context.ipaspace && tlbi.address<55:addr_lsb> == tlb_entry.context.ia<55:addr_lsb> && (!tlbi.from_aarch64 || ResTLBITTL(tlbi.ttl) || ( DecodeTLBITG(tlbi.ttl<3:2>) == tlb_entry.context.tg && UInt(tlbi.ttl<1:0>) == tlb_entry.walkstate.level) ) && ((tlbi.d128 && tlb_entry.context.isd128) || (tlbi.d64 && !tlb_entry.context.isd128) || (tlbi.d64 && tlbi.d128)) && (tlbi.level == TLBILevel_Any || !tlb_entry.walkstate.istable)); when TLBIOp_VAA, TLBIPOp_VAA constant integer addr_lsb = tlb_entry.blocksize; match = (tlb_entry.context.includes_s1 && tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime && tlbi.use_vmid == tlb_entry.context.use_vmid && (!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid) && tlbi.address<55:addr_lsb> == tlb_entry.context.ia<55:addr_lsb> && (!tlbi.from_aarch64 || ResTLBITTL(tlbi.ttl) || ( DecodeTLBITG(tlbi.ttl<3:2>) == tlb_entry.context.tg && UInt(tlbi.ttl<1:0>) == tlb_entry.walkstate.level) ) && ((tlbi.d128 && tlb_entry.context.isd128) || (tlbi.d64 && !tlb_entry.context.isd128) || (tlbi.d64 && tlbi.d128)) && (tlbi.level == TLBILevel_Any || !tlb_entry.walkstate.istable)); when TLBIOp_VA, TLBIPOp_VA constant integer addr_lsb = tlb_entry.blocksize; match = (tlb_entry.context.includes_s1 && tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime && tlbi.use_vmid == tlb_entry.context.use_vmid && (!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid) && (!UseASID(tlb_entry.context) || tlbi.asid == tlb_entry.context.asid || tlb_entry.context.nG == '0') && tlbi.address<55:addr_lsb> == tlb_entry.context.ia<55:addr_lsb> && (!tlbi.from_aarch64 || ResTLBITTL(tlbi.ttl) || ( DecodeTLBITG(tlbi.ttl<3:2>) == tlb_entry.context.tg && UInt(tlbi.ttl<1:0>) == tlb_entry.walkstate.level) ) && ((tlbi.d128 && tlb_entry.context.isd128) || (tlbi.d64 && !tlb_entry.context.isd128) || (tlbi.d64 && tlbi.d128)) && (tlbi.level == TLBILevel_Any || !tlb_entry.walkstate.istable)); when TLBIOp_VMALL match = (tlb_entry.context.includes_s1 && tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime && tlbi.use_vmid == tlb_entry.context.use_vmid && (!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid)); when TLBIOp_VMALLS12 match = (tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime && (!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid)); when TLBIOp_RIPAS2, TLBIPOp_RIPAS2 match = (!tlb_entry.context.includes_s1 && tlb_entry.context.includes_s2 && tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime && (!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid) && tlbi.ipaspace == tlb_entry.context.ipaspace && (tlbi.tg != '00' && DecodeTLBITG(tlbi.tg) == tlb_entry.context.tg) && (!tlbi.from_aarch64 || ResTLBIRTTL(tlbi.tg, tlbi.ttl<1:0>) || UInt(tlbi.ttl<1:0>) == tlb_entry.walkstate.level) && ((tlbi.d128 && tlb_entry.context.isd128) || (tlbi.d64 && !tlb_entry.context.isd128) ||
```

```
(tlbi.d64 && tlbi.d128)) && UInt(tlbi.address<55:0>) <= UInt(entry_end_address<55:0>) && UInt(tlbi.end_address<55:0>) > UInt(entry_start_address<55:0>)); when TLBIOp_RVAA, TLBIPOp_RVAA match = (tlb_entry.context.includes_s1 && tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime && tlbi.use_vmid == tlb_entry.context.use_vmid && (!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid) && (tlbi.tg != '00' && DecodeTLBITG(tlbi.tg) == tlb_entry.context.tg) && (!tlbi.from_aarch64 || ResTLBIRTTL(tlbi.tg, tlbi.ttl<1:0>) || UInt(tlbi.ttl<1:0>) == tlb_entry.walkstate.level) && ((tlbi.d128 && tlb_entry.context.isd128) || (tlbi.d64 && !tlb_entry.context.isd128) || (tlbi.d64 && tlbi.d128)) && UInt(tlbi.address<55:0>) <= UInt(entry_end_address<55:0>) && UInt(tlbi.end_address<55:0>) > UInt(entry_start_address<55:0>)); when TLBIOp_RVA, TLBIPOp_RVA match = (tlb_entry.context.includes_s1 && tlbi.security == tlb_entry.context.ss && tlbi.regime == tlb_entry.context.regime && tlbi.use_vmid == tlb_entry.context.use_vmid && (!tlb_entry.context.use_vmid || tlbi.vmid == tlb_entry.context.vmid) && (!UseASID(tlb_entry.context) || tlbi.asid == tlb_entry.context.asid || tlb_entry.context.nG == '0') && (tlbi.tg != '00' && DecodeTLBITG(tlbi.tg) == tlb_entry.context.tg) && (!tlbi.from_aarch64 || ResTLBIRTTL(tlbi.tg, tlbi.ttl<1:0>) || UInt(tlbi.ttl<1:0>) == tlb_entry.walkstate.level) && ((tlbi.d128 && tlb_entry.context.isd128) || (tlbi.d64 && !tlb_entry.context.isd128) || (tlbi.d64 && tlbi.d128)) && UInt(tlbi.address<55:0>) <= UInt(entry_end_address<55:0>) && UInt(tlbi.end_address<55:0>) > UInt(entry_start_address<55:0>)); when TLBIOp_RPA entry_end_address<55:0> = (tlb_entry.walkstate.baseaddress.address<55:0> OR entry_block_mask<55:0>); entry_start_address<55:0> = (tlb_entry.walkstate.baseaddress.address<55:0> AND NOT entry_block_mask<55:0>); match = (tlb_entry.context.includes_gpt && UInt(tlbi.address<55:0>) <= UInt(entry_end_address<55:0>) && UInt(tlbi.end_address<55:0>) > UInt(entry_start_address<55:0>)); when TLBIOp_PAALL match = tlb_entry.context.includes_gpt; if tlbi.attr == TLBI_ExcludeXS && tlb_entry.context.xs == '1' then match = FALSE; return match; J1.1.3.450 TLBIPRange Xt)
```

```
// TLBIPRange() // ============ // Extract the input address range information from encoded Xt. (boolean, bits(2), bits(64), bits(64)) TLBIPRange(Regime regime, bits(128) constant boolean valid = TRUE; bits(64) start_address = Zeros(64); bits(64) end_address = Zeros(64); constant bits(2) tg = Xt<47:46>; constant integer scale = UInt(Xt<45:44>); constant integer num = UInt(Xt<43:39>); if tg == '00' then
```

```
return (FALSE, tg, start_address, end_address); constant AddressSize tg_bits = TGBits(tg); // The more-significant bits of the start_address is not updated, // as they are not used when performing address matching in TLB start_address<55:tg_bits> = Xt<107:64+(tg_bits-12)>; constant integer range = (num+1) << (5*scale + 1 + tg_bits); end_address = start_address + range<63:0>; if end_address<55> != start_address<55> then // overflow, saturate it end_address = Replicate(start_address<55>, 9) : Ones(55); return (valid, tg, start_address, end_address);
```

## J1.1.3.451 TLBIRange

```
// TLBIRange() // =========== // Extract the input address range information from encoded Xt. (boolean, bits(2), bits(64), bits(64)) TLBIRange(Regime regime, bits(64) Xt) constant boolean valid = TRUE; bits(64) start_address = Zeros(64); bits(64) end_address = Zeros(64); constant bits(2) tg = Xt<47:46>; constant integer scale = UInt(Xt<45:44>); constant integer num = UInt(Xt<43:39>); integer tg_bits; if tg == '00' then return (FALSE, tg, start_address, end_address); case tg of when '01' // 4KB tg_bits = 12; if HasLargeAddress(regime) then start_address<52:16> = Xt<36:0>; start_address<63:53> = Replicate(Xt<36>, 11); else start_address<48:12> = Xt<36:0>; start_address<63:49> = Replicate(Xt<36>, 15); when '10' // 16KB tg_bits = 14; if HasLargeAddress(regime) then start_address<52:16> = Xt<36:0>; start_address<63:53> = Replicate(Xt<36>, 11); else start_address<50:14> = Xt<36:0>; start_address<63:51> = Replicate(Xt<36>, 13); when '11' // 64KB tg_bits = 16; start_address<52:16> = Xt<36:0>; start_address<63:53> = Replicate(Xt<36>, 11); otherwise Unreachable(); constant integer range = (num+1) << (5*scale + 1 + tg_bits); end_address = start_address + range<63:0>; if IsFeatureImplemented(FEAT_LVA3) && end_address<56> != start_address<56> then // overflow, saturate it end_address = Replicate(start_address<56>, 8) : Ones(56);
```

```
elsif end_address<52> != start_address<52> then // overflow, saturate it end_address = Replicate(start_address<52>, 12) : Ones(52); return (valid, tg, start_address, end_address);
```

## J1.1.3.452 VBitOp

```
// VBitOp // ====== // Vector bit select instruction types. enumeration VBitOp {VBitOp_VBIF, VBitOp_VBIT, VBitOp_VBSL, VBitOp_VEOR};
```

## J1.1.4 aarch64/translation

This section includes the following pseudocode functions:

- AArch64.MAIRAttr
- AArch64.CheckBreakpoint
- AArch64.CheckDebug
- AArch64.CheckWatchpoint
- AppendToHDBSS
- CanAppendToHDBSS
- CreateHDBSSEntry
- AArch64.IASize
- AArch64.NextTableBase
- AArch64.PhysicalAddressSize
- AArch64.S1LeafBase
- AArch64.S1SLTTEntryAddress
- AArch64.S1StartLevel
- AArch64.S1TTBaseAddress
- AArch64.S1TTEntryAddress
- AArch64.S2LeafBase
- AArch64.S2SLTTEntryAddress
- AArch64.S2StartLevel
- AArch64.S2TTBaseAddress
- AArch64.S2TTEntryAddress
- AArch64.AddrTop
- AArch64.ContiguousBitFaults
- AArch64.IPAIsOutOfRange
- AArch64.OAOutOfRange
- AArch64.PermissionOverlaysApplied
- AArch64.S1CheckPermissions
- AArch64.S1ComputePermissions
- AArch64.S1DirectBasePermissions
- AArch64.S1HasAlignmentFaultDueToMemType
- AArch64.S1IndirectBasePermissions
- AArch64.S1OAOutOfRange
- AArch64.S1OverlayPermissions

- AArch64.S1TxSZFaults
- AArch64.S2CheckPermissions
- AArch64.S2ComputePermissions
- AArch64.S2DirectBasePermissions
- AArch64.S2HasAlignmentFaultDueToMemType
- AArch64.S2InconsistentSL
- AArch64.S2IndirectBasePermissions
- AArch64.S2InvalidSL
- AArch64.S2OAOutOfRange
- AArch64.S2OverlayPermissions
- AArch64.S2TxSZFaults
- AArch64.VAIsOutOfRange
- AArch64.S2ApplyFWBMemAttrs
- AArch64.GetS1TLBContext
- AArch64.GetS2TLBContext
- AArch64.TLBContextEL10
- AArch64.TLBContextEL2
- AArch64.TLBContextEL20
- AArch64.TLBContextEL3
- AArch64.FullTranslate

•

AArch64.MemSwapTableDesc

- AArch64.S1DisabledOutput
- AArch64.S1Translate
- AArch64.S1TreatAsNormalNC
- AArch64.S2Translate
- AArch64.S2TreatAsNormalNC
- AArch64.SetAccessFlag
- AArch64.SetDirtyState
- AArch64.SettingAccessFlagPermitted
- AArch64.SettingDirtyStatePermitted
- AArch64.TranslateAddress
- AArch64.TranslateTagAddress
- AArch64.BlockDescSupported
- AArch64.ContiguousBit
- AArch64.DecodeDescriptorType
- AArch64.S1ApplyOutputPerms
- AArch64.S1ApplyTablePerms
- AArch64.S2ApplyOutputPerms
- AArch64.nTFaults
- AArch64.S1InitialTTWState
- AArch64.S1NextWalkStateLeaf
- AArch64.S1NextWalkStateTable
- AArch64.S1Walk
- AArch64.S2InitialTTWState
- AArch64.S2NextWalkStateLeaf
- AArch64.S2NextWalkStateTable
- AArch64.S2Walk

- AArch64.SS2InitialTTWState
- AArch64.SS2OutputPASpace
- AArch64.GetS1TTWParams
- AArch64.GetS2TTWParams
- AArch64.GetVARange
- AArch64.HaveS1TG
- AArch64.HaveS2TG
- AArch64.MaxTxSZ
- AArch64.NSS2TTWParams
- AArch64.PAMax
- AArch64.RLS2TTWParams
- AArch64.S1DCacheEnabled
- AArch64.S1DecodeTG0
- AArch64.S1DecodeTG1
- AArch64.S1E0POEnabled
- AArch64.S1EPD
- AArch64.S1Enabled
- AArch64.S1ICacheEnabled
- AArch64.S1MinTxSZ
- AArch64.S1POEnabled
- AArch64.S1POR
- AArch64.S1TTBR
- AArch64.S1TTWParamsEL10
- AArch64.S1TTWParamsEL2
- AArch64.S1TTWParamsEL20
- AArch64.S1TTWParamsEL3
- AArch64.S2DecodeTG0
- AArch64.S2MinTxSZ
- AArch64.SS2TTWParams
- S2DCacheEnabled

## J1.1.4.1 AArch64.MAIRAttr

```
// AArch64.MAIRAttr() // ================== // Retrieve the memory attribute encoding indexed in the given MAIR bits(8) AArch64.MAIRAttr(integer index, MAIRType mair2, MAIRType mair) assert (index < 8 || (IsFeatureImplemented(FEAT_AIE) && (index < 16))); if (index > 7) then return Elem[mair2, index-8, 8]; // Read from LSB at MAIR2 else return Elem[mair, index, 8];
```

## J1.1.4.2 AArch64.CheckBreakpoint

```
// AArch64.CheckBreakpoint() // ========================= // Called before executing the instruction of length "size" bytes at "vaddress" in an AArch64 // translation regime, when either debug exceptions are enabled, or halting debug is enabled // and halting is allowed.
```

```
FaultRecord AArch64.CheckBreakpoint(FaultRecord fault_in, bits(64) vaddress, AccessDescriptor accdesc, integer size) assert !ELUsingAArch32(S1TranslationRegime()); assert (UsingAArch32() && size IN {2,4}) || size == 4; FaultRecord fault = fault_in; boolean match = FALSE; boolean addr_match_bp = FALSE; // Default assumption that all address match breakpoints // are inactive or disabled. boolean addr_mismatch_bp = FALSE; // Default assumption that all address mismatch // breakpoints are inactive or disabled. boolean addr_match = FALSE; boolean addr_mismatch = TRUE; // Default assumption that the given virtual address is // outside the range of all address mismatch breakpoints boolean ctxt_match = FALSE; for i = 0 to NumBreakpointsImplemented() - 1 constant BreakpointInfo brkptinfo = AArch64.BreakpointMatch(i, vaddress, accdesc, size); if brkptinfo.bptype == BreakpointType_AddrMatch then addr_match_bp = TRUE; addr_match = addr_match || brkptinfo.match; elsif brkptinfo.bptype == BreakpointType_AddrMismatch then addr_mismatch_bp = TRUE; addr_mismatch = addr_mismatch && !brkptinfo.match; elsif brkptinfo.bptype == BreakpointType_CtxtMatch then ctxt_match = ctxt_match || brkptinfo.match; if addr_match_bp && addr_mismatch_bp then match = addr_match && addr_mismatch; else match = (addr_match_bp && addr_match) || (addr_mismatch_bp && addr_mismatch); match = match || ctxt_match; if match then fault.statuscode = Fault_Debug; fault.vaddress = vaddress; if HaltOnBreakpointOrWatchpoint() then reason = DebugHalt_Breakpoint; Halt(reason); return fault;
```

## J1.1.4.3 AArch64.CheckDebug

```
// AArch64.CheckDebug() // ==================== // Called on each access to check for a debug exception or entry to Debug state. FaultRecord AArch64.CheckDebug(bits(64) vaddress, AccessDescriptor accdesc, integer size) FaultRecord fault = NoFault(accdesc, vaddress); boolean generate_exception; constant boolean d_side = IsWatchpointableAccess(accdesc); constant boolean i_side = (accdesc.acctype == AccessType_IFETCH); if accdesc.acctype == AccessType_NV2 then mask = '0'; ss = CurrentSecurityState(); generate_exception = (AArch64.GenerateDebugExceptionsFrom(EL2, ss, mask) && MDSCR_EL1.MDE == '1'); else generate_exception = AArch64.GenerateDebugExceptions() && MDSCR_EL1.MDE == '1'; halt = HaltOnBreakpointOrWatchpoint();
```

```
if generate_exception || halt then if d_side then fault = AArch64.CheckWatchpoint(fault, vaddress, accdesc, size); elsif i_side then fault = AArch64.CheckBreakpoint(fault, vaddress, accdesc, size); return fault;
```

## J1.1.4.4 AArch64.CheckWatchpoint

```
// AArch64.CheckWatchpoint() // ========================= // Called before accessing the memory location of "size" bytes at "address", // when either debug exceptions are enabled for the access, or halting debug // is enabled and halting is allowed. FaultRecord AArch64.CheckWatchpoint(FaultRecord fault_in, bits(64) vaddress_in, AccessDescriptor accdesc, integer size_in) assert !ELUsingAArch32(S1TranslationRegime()); FaultRecord fault = fault_in; FaultRecord fault_match = fault_in; FaultRecord fault_mismatch = fault_in; bits(64) vaddress = vaddress_in; integer size = size_in; boolean rounded_match = FALSE; constant bits(64) original_vaddress = vaddress; constant integer original_size = size; boolean addr_match_wp = FALSE; // Default assumption that all address match watchpoints // are inactive or disabled. boolean addr_mismatch_wp = FALSE; // Default assumption that all address mismatch // watchpoints are inactive or disabled. boolean addr_match = FALSE; boolean addr_mismatch = TRUE; // Default assumption that the given virtual address is // outside the range of all address mismatch watchpoints // For memory accesses of below type // - Contiguous SVE access // - SME access // - SIMD&FP access when the PE is in Streaming SVE mode // each call to this function is such that: // - the lowest accessed address is rounded down to the nearest multiple of 16 bytes // - the highest accessed address is rounded up to the nearest multiple of 16 bytes // Since the WPF field is set if the implementation does rounding, regardless of true or // false match, it would be acceptable to return TRUE for either/both of the first and last // access. if IsRelaxedWatchpointAccess(accdesc) then integer upper_vaddress = UInt(original_vaddress) + original_size; if ConstrainUnpredictableBool(Unpredictable_16BYTEROUNDEDDOWNACCESS) then vaddress = Align(vaddress, 16); rounded_match = TRUE; if ConstrainUnpredictableBool(Unpredictable_16BYTEROUNDEDUPACCESS) then upper_vaddress = Align((upper_vaddress)+((16)-1), 16); rounded_match = TRUE; size = upper_vaddress -UInt(vaddress); for i = 0 to NumWatchpointsImplemented() - 1 constant WatchpointInfo watchptinfo = AArch64.WatchpointMatch(i, vaddress, size, accdesc); if watchptinfo.wptype == WatchpointType_AddrMatch then addr_match_wp = TRUE; addr_match = addr_match || watchptinfo.value_match; if watchptinfo.value_match then fault_match.statuscode = Fault_Debug; if DBGWCR_EL1[i].LSC<0> == '1' && accdesc.read then fault_match.write = FALSE; elsif DBGWCR_EL1[i].LSC<1> == '1' && accdesc.write then
```

```
fault_match.write = TRUE; fault_match.watchptinfo = watchptinfo; elsif watchptinfo.wptype == WatchpointType_AddrMismatch then addr_mismatch_wp = TRUE; addr_mismatch = addr_mismatch && !watchptinfo.value_match; if !watchptinfo.value_match then fault_mismatch.statuscode = Fault_Debug; if DBGWCR_EL1[i].LSC<0> == '1' && accdesc.read then fault_mismatch.write = FALSE; elsif DBGWCR_EL1[i].LSC<1> == '1' && accdesc.write then fault_mismatch.write = TRUE; fault_mismatch.watchptinfo = watchptinfo; if ((addr_match_wp && addr_mismatch_wp && addr_match && addr_mismatch) || (addr_match_wp && !addr_mismatch_wp && addr_match)) then fault = fault_match; elsif !addr_match_wp && addr_mismatch_wp && addr_mismatch then fault = fault_mismatch; fault.vaddress = vaddress; fault.watchptinfo.maybe_false_match = rounded_match; if (fault.statuscode == Fault_Debug && HaltOnBreakpointOrWatchpoint() && !accdesc.nonfault && !(accdesc.firstfault && !accdesc.first)) then reason = DebugHalt_Watchpoint; EDWAR = fault.vaddress; is_async = FALSE; Halt(reason, is_async, fault); return fault;
```

## J1.1.4.5 AppendToHDBSS

```
// AppendToHDBSS() // =============== // Appends an entry to the HDBSS when the dirty state of a stage 2 descriptor is updated // from writable-clean to writable-dirty by hardware. FaultRecord AppendToHDBSS(FaultRecord fault_in, FullAddress ipa_in, AccessDescriptor accdesc, S2TTWParams walkparams, integer level) assert CanAppendToHDBSS(); FaultRecord fault = fault_in; FullAddress ipa = ipa_in; constant integer hdbss_size = UInt(HDBSSBR_EL2.SZ); AddressDescriptor hdbss_addrdesc; bits(56) baddr = HDBSSBR_EL2.BADDR<43 : 0> : Zeros(12); baddr<11 + hdbss_size : 12> = Zeros(hdbss_size); hdbss_addrdesc.paddress.address = baddr + (8 * UInt(HDBSSPROD_EL2.INDEX)); constant bit nse2 = '0'; // NSE2 has the Effective value of 0 within a PE. hdbss_addrdesc.paddress.paspace = DecodePASpace(nse2, EffectiveSCR_EL3_NSE(), EffectiveSCR_EL3_NS()); // Accesses to the HDBSS use the same memory attributes as used for stage 2 translation walks. hdbss_addrdesc.memattrs = WalkMemAttrs(walkparams.sh, walkparams.irgn, walkparams.orgn); constant AccessDescriptor hdbss_access = CreateAccDescHDBSS(accdesc); hdbss_addrdesc.mecid = AArch64.S2TTWalkMECID(walkparams.emec, accdesc.ss); if IsFeatureImplemented(FEAT_RME) then fault.gpcf = GranuleProtectionCheck(hdbss_addrdesc, hdbss_access); if fault.gpcf.gpf != GPCF_None then if (boolean IMPLEMENTATION_DEFINED "GPC fault on HDBSSS write reported in HDBSSPROD_EL2") then HDBSSPROD_EL2.FSC = '101000'; else
```

```
fault.statuscode = Fault_GPCFOnWalk; fault.paddress = hdbss_addrdesc.paddress; fault.level = level; fault.gpcfs2walk = TRUE; fault.hdbssf = TRUE; return fault; // The reported IPA must be aligned to the size of the translation. constant AddressSize lsb = TranslationSize(walkparams.d128, walkparams.tgx, ipa.address = ipa.address<55:lsb> : Zeros(lsb); bits(64) hdbss_entry = CreateHDBSSEntry(ipa, hdbss_access.ss, level); if walkparams.ee == '1' then hdbss_entry = BigEndianReverse(hdbss_entry); constant PhysMemRetStatus memstatus = PhysMemWrite(hdbss_addrdesc, 8, hdbss_entry); if IsFault(memstatus) then if (boolean IMPLEMENTATION_DEFINED "External Abort on HDBSS write reported in HDBSSPROD_EL2") then HDBSSPROD_EL2.FSC = '010000'; else constant boolean iswrite = TRUE; fault = HandleExternalTTWAbort(memstatus, iswrite, hdbss_addrdesc, hdbss_access, 8, fault); fault.level = level; fault.hdbssf = TRUE; else HDBSSPROD_EL2.INDEX = HDBSSPROD_EL2.INDEX + 1; return fault;
```

## level); hdbss\_access, J1.1.4.6 CanAppendToHDBSS // CanAppendToHDBSS() // ================== // Return TRUE if HDBSS can be appended. boolean CanAppendToHDBSS() if !IsFeatureImplemented(FEAT\_HDBSS) then return FALSE; assert EL2Enabled(); // The PE cannot append entries to the HDBSS if HDBSSPROD\_EL2.FSC is // any other value than 0b000000, or HDBSS buffer is full. if ((UInt(HDBSSPROD\_EL2.INDEX) &gt;= ((2 ^ (UInt(HDBSSBR\_EL2.SZ) + 12)) DIV 8)) || (HDBSSPROD\_EL2.FSC != '000000')) then return FALSE; else return TRUE; J1.1.4.7 CreateHDBSSEntry // CreateHDBSSEntry() // ================== // Returns a HDBSS entry. bits(64) CreateHDBSSEntry(FullAddress ipa, SecurityState ss, integer level) constant bit ns\_ipa = if ss == SS\_Secure &amp;&amp; ipa.paspace == PAS\_NonSecure then '1' else '0'; return ZeroExtend(ipa.address&lt;55:12&gt; : ns\_ipa : Zeros(7) : level&lt;2:0&gt; : '1', 64);

## J1.1.4.8 AArch64.IASize

```
// AArch64.IASize() // ================ // Retrieve the number of bits containing the AddressSize AArch64.IASize(bits(6) txsz) return 64 UInt(txsz);
```

## J1.1.4.9 AArch64.NextTableBase

```
// AArch64.NextTableBase() // ======================= // Extract the address embedded in a table descriptor pointing to the base of // the next level table of descriptors bits(56) AArch64.NextTableBase(bits(N) descriptor, bit d128, bits(2) skl, bit ds, TGx tgx) bits(56) tablebase = Zeros(56); constant AddressSize granulebits = TGxGranuleBits(tgx); integer tablesize; if d128 == '1' then constant integer descsizelog2 = 4; constant integer stride = granulebits - descsizelog2; tablesize = stride*(1 + UInt(skl)) + descsizelog2; else tablesize = granulebits; case tgx of when TGx_4KB tablebase<47:12> = descriptor<47:12>; when TGx_16KB tablebase<47:14> = descriptor<47:14>; when TGx_64KB tablebase<47:16> = descriptor<47:16>; tablebase = Align(tablebase, 2^tablesize); if d128 == '1' then tablebase<55:48> = descriptor<55:48>; elsif tgx == TGx_64KB && (AArch64.PAMax() >= 52 || boolean IMPLEMENTATION_DEFINED "descriptor[15:12] for 64KB granule are OA[51:48]") then tablebase<51:48> = descriptor<15:12>; elsif ds == '1' then tablebase<51:48> = descriptor<9:8>:descriptor<49:48>; return tablebase;
```

## J1.1.4.10 AArch64.PhysicalAddressSize

```
// AArch64.PhysicalAddressSize() // ============================= // Retrieve the number of bits bounding the physical address AddressSize AArch64.PhysicalAddressSize(bit d128, bit ds, bits(3) encoded_ps, TGx tgx) integer ps; integer max_ps; case encoded_ps of when '000' ps = 32; when '001' ps = 36; when '010' ps = 40; when '011' ps = 42; when '100' ps = 44; when '101' ps = 48; when '110' ps = 52;
```

```
input address
```

```
when '111' ps = 56; if d128 == '1' then max_ps = AArch64.PAMax(); elsif IsFeatureImplemented(FEAT_LPA) && (tgx == TGx_64KB || ds == '1') then max_ps = Min(52, AArch64.PAMax()); else max_ps = Min(48, AArch64.PAMax()); return Min(ps, max_ps);
```

## J1.1.4.11 AArch64.S1LeafBase

```
// AArch64.S1LeafBase() // ==================== // Extract the address embedded in a block and page descriptor pointing to the // base of a memory block bits(56) AArch64.S1LeafBase(bits(N) descriptor, S1TTWParams walkparams, integer level) bits(56) leafbase = Zeros(56); granulebits = TGxGranuleBits(walkparams.tgx); descsizelog2 = if walkparams.d128 == '1' then 4 else 3; constant integer stride = granulebits -descsizelog2; constant integer leafsize = granulebits + stride * (FINAL_LEVEL - level); leafbase<47:0> = Align(descriptor<47:0>, 2^leafsize); if walkparams.d128 == '1' then leafbase<55:48> = descriptor<55:48>; elsif walkparams.tgx == TGx_64KB && (AArch64.PAMax() >= 52 || boolean IMPLEMENTATION_DEFINED "descriptor[15:12] for 64KB granule are OA[51:48]") then leafbase<51:48> = descriptor<15:12>; elsif walkparams.ds == '1' then leafbase<51:48> = descriptor<9:8,49:48>; return leafbase;
```

## J1.1.4.12

```
// AArch64.S1SLTTEntryAddress() // ============================ // Compute the first stage 1 translation table descriptor address within the // table pointed to by the base at the start level FullAddress AArch64.S1SLTTEntryAddress(integer level, S1TTWParams bits(64) ia, FullAddress tablebase) // Input Address size iasize = AArch64.IASize(walkparams.txsz); granulebits = TGxGranuleBits(walkparams.tgx); constant integer descsizelog2 = if walkparams.d128 == '1' then 4 else 3; stride = granulebits -descsizelog2; levels = FINAL_LEVEL -level; bits(56) index; constant AddressSize lsb = levels*stride + granulebits; constant AddressSize msb = iasize - 1; index = ZeroExtend(ia<msb:lsb>:Zeros(descsizelog2), 56); FullAddress descaddress; descaddress.address = tablebase.address OR index; descaddress.paspace = tablebase.paspace;
```

```
AArch64.S1SLTTEntryAddress walkparams,
```

return descaddress;

## J1.1.4.13 AArch64.S1StartLevel

```
// AArch64.S1StartLevel() // ====================== // Compute the initial lookup level when performing a stage 1 translation // table walk integer AArch64.S1StartLevel(S1TTWParams walkparams) // Input Address size iasize = AArch64.IASize(walkparams.txsz); granulebits = TGxGranuleBits(walkparams.tgx); constant integer descsizelog2 = if walkparams.d128 == '1' then 4 else 3; constant integer stride = granulebits -descsizelog2; integer s1startlevel = FINAL_LEVEL - (((iasize-1) granulebits) DIV stride); if walkparams.d128 == '1' then s1startlevel = s1startlevel + UInt(walkparams.skl); return s1startlevel;
```

## J1.1.4.14 AArch64.S1TTBaseAddress

```
// AArch64.S1TTBaseAddress() // ========================= // Retrieve the PA/IPA pointing to the base of the initial translation table of stage 1 bits(56) AArch64.S1TTBaseAddress(S1TTWParams walkparams, Regime regime, bits(N) ttbr) bits(56) tablebase = Zeros(56); // Input Address size iasize = AArch64.IASize(walkparams.txsz); granulebits = TGxGranuleBits(walkparams.tgx); descsizelog2 = if walkparams.d128 == '1' then 4 else 3; stride = granulebits - descsizelog2; startlevel = AArch64.S1StartLevel(walkparams); levels = FINAL_LEVEL -startlevel; // Base address is aligned to size of the initial translation table in bytes tsize = (iasize - (levels*stride + granulebits)) + descsizelog2; if walkparams.d128 == '1' then tsize = Max(tsize, 5); if regime == Regime_EL3 then tablebase<55:5> = ttbr<55:5>; else tablebase<55:5> = ttbr<87:80>:ttbr<47:5>; elsif walkparams.ds == '1' || (walkparams.tgx == TGx_64KB && walkparams.ps == '110' && (IsFeatureImplemented(FEAT_LPA) || boolean IMPLEMENTATION_DEFINED "BADDR expresses 52 bits for 64KB granule")) then tsize = Max(tsize, 6); tablebase<51:6> = ttbr<5:2>:ttbr<47:6>; else tablebase<47:1> = ttbr<47:1>; tablebase = Align(tablebase, 2^tsize); return tablebase;
```

## J1.1.4.15 AArch64.S1TTEntryAddress

```
// AArch64.S1TTEntryAddress() // ========================== // Compute translation table descriptor address within the table pointed to by
```

## // the table base FullAddress AArch64.S1TTEntryAddress(integer level, S1TTWParams walkparams, bits(2) skl, bits(64) ia, FullAddress tablebase, bits(N) descriptor) // Input Address size iasize = AArch64.IASize(walkparams.txsz); granulebits = TGxGranuleBits(walkparams.tgx); constant descsizelog2 = if walkparams.d128 == '1' then 4 else 3; stride = granulebits - descsizelog2; levels = FINAL\_LEVEL -level; bits(56) index; constant AddressSize lsb = levels*stride + granulebits; constant integer nstride = if walkparams.d128 == '1' then UInt(skl) + 1 else 1; constant AddressSize msb = (lsb + (stride * nstride)) 1; index = ZeroExtend(ia&lt;msb:lsb&gt;:Zeros(descsizelog2), 56); FullAddress descaddress; descaddress.address = tablebase.address OR index; descaddress.paspace = tablebase.paspace; return descaddress; J1.1.4.16 AArch64.S2LeafBase // AArch64.S2LeafBase() // ==================== // Extract the address embedded in a block and page descriptor pointing to the // base of a memory block bits(56) AArch64.S2LeafBase(bits(N) descriptor, S2TTWParams walkparams, integer level) bits(56) leafbase = Zeros(56); granulebits = TGxGranuleBits(walkparams.tgx); descsizelog2 = if walkparams.d128 == '1' then 4 else 3; constant integer stride = granulebits -descsizelog2; constant integer leafsize = granulebits + stride * (FINAL\_LEVEL - level); leafbase&lt;47:0&gt; = Align(descriptor&lt;47:0&gt;, 2^leafsize); if walkparams.d128 == '1' then leafbase&lt;55:48&gt; = descriptor&lt;55:48&gt;; elsif walkparams.tgx == TGx\_64KB &amp;&amp; (AArch64.PAMax() &gt;= 52 || (boolean IMPLEMENTATION\_DEFINED "descriptor[15:12] for 64KB granule are OA[51:48]")) then leafbase&lt;51:48&gt; = descriptor&lt;15:12&gt;; elsif walkparams.ds == '1' then leafbase&lt;51:48&gt; = descriptor&lt;9:8&gt;:descriptor&lt;49:48&gt;; return leafbase; J1.1.4.17 AArch64.S2SLTTEntryAddress the ipa,

```
// AArch64.S2SLTTEntryAddress() // ============================ // Compute the first stage 2 translation table descriptor address within // table pointed to by the base at the start level FullAddress AArch64.S2SLTTEntryAddress(S2TTWParams walkparams, bits(56) FullAddress tablebase) startlevel = AArch64.S2StartLevel(walkparams); iasize = AArch64.IASize(walkparams.txsz);
```

```
granulebits = TGxGranuleBits(walkparams.tgx); constant descsizelog2 = if walkparams.d128 == '1' then 4 else 3; stride = granulebits -descsizelog2; levels = FINAL_LEVEL -startlevel; bits(56) index; constant AddressSize lsb = levels*stride + granulebits; constant AddressSize msb = iasize - 1; index = ZeroExtend(ipa<msb:lsb>:Zeros(descsizelog2), 56); FullAddress descaddress; descaddress.address = tablebase.address OR index; descaddress.paspace = tablebase.paspace; return descaddress;
```

## J1.1.4.18 AArch64.S2StartLevel

```
// AArch64.S2StartLevel() // ====================== // Determine the initial lookup level when performing a stage 2 translation // table walk integer AArch64.S2StartLevel(S2TTWParams walkparams) if walkparams.d128 == '1' then iasize = AArch64.IASize(walkparams.txsz); granulebits = TGxGranuleBits(walkparams.tgx); descsizelog2 = 4; constant integer stride = granulebits - descsizelog2; integer s2startlevel = FINAL_LEVEL - (((iasize-1) granulebits) DIV stride); s2startlevel = s2startlevel + UInt(walkparams.skl); return s2startlevel; case walkparams.tgx of when TGx_4KB case walkparams.sl2:walkparams.sl0 of when '000' return 2; when '001' return 1; when '010' return 0; when '011' return 3; when '100' return -1; when TGx_16KB case walkparams.sl0 of when '00' return 3; when '01' return 2; when '10' return 1; when '11' return 0; when TGx_64KB case walkparams.sl0 of when '00' return 3; when '01' return 2; when '10' return 1;
```

## J1.1.4.19 AArch64.S2TTBaseAddress

```
// AArch64.S2TTBaseAddress() // ========================= // Retrieve the PA/IPA pointing to the base of the initial translation table of stage 2 bits(56) AArch64.S2TTBaseAddress(S2TTWParams walkparams, PASpace paspace, bits(N) ttbr) bits(56) tablebase = Zeros(56);
```

```
// Input Address size iasize = AArch64.IASize(walkparams.txsz); granulebits = TGxGranuleBits(walkparams.tgx); descsizelog2 = if walkparams.d128 == '1' then 4 else 3; stride = granulebits - descsizelog2; startlevel = AArch64.S2StartLevel(walkparams); levels = FINAL_LEVEL -startlevel; // Base address is aligned to size of the initial translation table in bytes tsize = (iasize - (levels*stride + granulebits)) + descsizelog2; if walkparams.d128 == '1' then tsize = Max(tsize, 5); if paspace == PAS_Secure then tablebase<55:5> = ttbr<55:5>; else tablebase<55:5> = ttbr<87:80>:ttbr<47:5>; elsif walkparams.ds == '1' || (walkparams.tgx == TGx_64KB && walkparams.ps == '110' && (IsFeatureImplemented(FEAT_LPA) || boolean IMPLEMENTATION_DEFINED "BADDR expresses 52 bits for 64KB granule")) then tsize = Max(tsize, 6); tablebase<51:6> = ttbr<5:2>:ttbr<47:6>; else tablebase<47:1> = ttbr<47:1>; tablebase = Align(tablebase, 2^tsize); return tablebase;
```

## J1.1.4.20 AArch64.S2TTEntryAddress // AArch64.S2TTEntryAddress() // ========================== // Compute translation table descriptor address within the table pointed to by // the table base FullAddress AArch64.S2TTEntryAddress(integer level, S2TTWParams walkparams, bits(2) skl, bits(56) ipa, FullAddress tablebase) ipasize = AArch64.IASize(walkparams.txsz); granulebits = TGxGranuleBits(walkparams.tgx); constant descsizelog2 = if walkparams.d128 == '1' then 4 else 3; stride = granulebits - descsizelog2; levels = FINAL\_LEVEL -level; bits(56) index; constant AddressSize lsb = levels*stride + granulebits; constant integer nstride = if walkparams.d128 == '1' then UInt(skl) + 1 else 1; constant AddressSize msb = (lsb + (stride * nstride)) 1; index = ZeroExtend(ipa&lt;msb:lsb&gt;:Zeros(descsizelog2), 56); FullAddress descaddress; descaddress.address = tablebase.address OR index; descaddress.paspace = tablebase.paspace; return descaddress; J1.1.4.21 AArch64.AddrTop process.

```
// AArch64.AddrTop() // ================= // Get the top bit position of the virtual address. // Bits above are not accounted as part of the translation AddressSize AArch64.AddrTop(bit tbid, AccessType acctype, bit tbi)
```

```
if tbid == '1' && acctype == AccessType_IFETCH then return 63; if tbi == '1' then return 55; else return 63;
```

## J1.1.4.22 AArch64.ContiguousBitFaults

```
// AArch64.ContiguousBitFaults() // ============================= // If contiguous bit is set, returns whether the translation size exceeds the // input address size and if the implementation generates a fault boolean AArch64.ContiguousBitFaults(bit d128, bits(6) txsz, TGx tgx, integer level) // Input Address size iasize = AArch64.IASize(txsz); // Translation size tsize = TranslationSize(d128, tgx, level) + ContiguousSize(d128, tgx, level); return (tsize > iasize && boolean IMPLEMENTATION_DEFINED "Translation fault on misprogrammed contiguous bit");
```

## J1.1.4.23 AArch64.IPAIsOutOfRange

```
// AArch64.IPAIsOutOfRange() // ========================= // Check bits not resolved by translation are ZERO boolean AArch64.IPAIsOutOfRange(bits(56) ipa, S2TTWParams walkparams) //Input Address size constant integer iasize = AArch64.IASize(walkparams.txsz); if iasize < 56 then return !IsZero(ipa<55:iasize>); else return FALSE;
```

## J1.1.4.24 AArch64.OAOutOfRange

```
// AArch64.OAOutOfRange() // ====================== // Returns whether output address is expressed in the configured size number of bits boolean AArch64.OAOutOfRange(bits(56) address, bit d128, bit ds, bits(3) ps, TGx tgx) // Output Address size constant integer oasize = AArch64.PhysicalAddressSize(d128, ds, ps, tgx); if oasize < 56 then return !IsZero(address<55:oasize>); else return FALSE;
```

## J1.1.4.25 AArch64.PermissionOverlaysApplied

```
// AArch64.PermissionOverlaysApplied() // =================================== // Returns TRUE if Permission overlays are applied for the given access type. boolean AArch64.PermissionsOverlaysApplied(AccessType acctype) case acctype of otherwise return TRUE;
```

## J1.1.4.26 AArch64.S1CheckPermissions

```
// AArch64.S1CheckPermissions() // ============================ // Checks whether stage 1 access violates permissions of target memory // and returns a fault record FaultRecord AArch64.S1CheckPermissions(FaultRecord fault_in, bits(64) va, integer size, Regime regime, TTWState walkstate, S1TTWParams walkparams, AccessDescriptor accdesc) FaultRecord fault = fault_in; constant Permissions permissions = walkstate.permissions; S1AccessControls s1perms = AArch64.S1ComputePermissions(regime, walkstate, walkparams, accdesc); if accdesc.acctype == AccessType_IFETCH then // Flag the access is from a guarded page SetInGuardedPage(walkstate.guardedpage == '1' && s1perms.x == '1'); if s1perms.overlay && s1perms.ox == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif (walkstate.memattrs.memtype == MemType_Device && ConstrainUnpredictable(Unpredictable_INSTRDEVICE) == Constraint_FAULT) then fault.statuscode = Fault_Permission; elsif s1perms.x == '0' then fault.statuscode = Fault_Permission; elsif accdesc.acctype == AccessType_DC then if accdesc.cacheop == CacheOp_Invalidate then if s1perms.overlay && s1perms.ow == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif s1perms.w == '0' then fault.statuscode = Fault_Permission; elsif (walkparams.hd != '1' && walkparams.pie == '1' && permissions.ndirty == '1') then fault.statuscode = Fault_Permission; fault.dirtybit = TRUE; // DC from privileged context which clean cannot generate a Permission fault elsif accdesc.el == EL0 then if s1perms.overlay && s1perms.or == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif (walkparams.cmow == '1' && accdesc.cacheop == CacheOp_CleanInvalidate && s1perms.overlay && s1perms.ow == '0') then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif s1perms.r == '0' then fault.statuscode = Fault_Permission; elsif (walkparams.cmow == '1' && accdesc.cacheop == CacheOp_CleanInvalidate && s1perms.w == '0') then fault.statuscode = Fault_Permission; elsif (walkparams.cmow == '1' && walkparams.hd != '1' && walkparams.pie == '1' &&
```

```
permissions.ndirty == '1' && accdesc.cacheop == CacheOp_CleanInvalidate) then fault.statuscode = Fault_Permission; fault.dirtybit = TRUE; elsif accdesc.acctype == AccessType_IC then // IC from privileged context cannot generate Permission fault if accdesc.el == EL0 then if (s1perms.overlay && s1perms.or == '0' && boolean IMPLEMENTATION_DEFINED "Permission fault on EL0 IC_IVAU execution") then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif walkparams.cmow == '1' && s1perms.overlay && s1perms.ow == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif (s1perms.r == '0' && boolean IMPLEMENTATION_DEFINED "Permission fault on EL0 IC_IVAU execution") then fault.statuscode = Fault_Permission; elsif walkparams.cmow == '1' && s1perms.w == '0' then fault.statuscode = Fault_Permission; elsif (walkparams.cmow == '1' && walkparams.hd != '1' && walkparams.pie == '1' && permissions.ndirty == '1') then fault.statuscode = Fault_Permission; fault.dirtybit = TRUE; elsif IsFeatureImplemented(FEAT_GCS) && accdesc.acctype == AccessType_GCS then if s1perms.gcs == '0' then fault.statuscode = Fault_Permission; elsif accdesc.write && walkparams.hd != '1' && permissions.ndirty == '1' then fault.statuscode = Fault_Permission; fault.dirtybit = TRUE; fault.write = TRUE; elsif accdesc.read && s1perms.overlay && s1perms.or == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; fault.write = FALSE; elsif accdesc.write && s1perms.overlay && s1perms.ow == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; fault.write = TRUE; elsif accdesc.read && s1perms.r == '0' then fault.statuscode = Fault_Permission; fault.write = FALSE; elsif accdesc.write && s1perms.w == '0' then fault.statuscode = Fault_Permission; fault.write = TRUE; elsif (accdesc.write && accdesc.tagaccess && walkstate.memattrs.tags == MemTag_CanonicallyTagged) then fault.statuscode = Fault_Permission; fault.write = TRUE; fault.s1tagnotdata = TRUE; elsif (accdesc.write && walkparams.hd != '1' && walkparams.pie == '1' && permissions.ndirty == '1') then fault.statuscode = Fault_Permission; fault.dirtybit = TRUE; fault.write = TRUE; return fault;
```

## J1.1.4.27 AArch64.S1ComputePermissions

```
// AArch64.S1ComputePermissions() // ============================== // Computes the overall stage 1 permissions S1AccessControls AArch64.S1ComputePermissions(Regime regime, TTWState walkstate, S1TTWParams walkparams, AccessDescriptor accdesc) constant Permissions permissions = walkstate.permissions;
```

```
S1AccessControls s1perms; if walkparams.pie == '1' then s1perms = AArch64.S1IndirectBasePermissions(regime, walkstate, walkparams, accdesc); else s1perms = AArch64.S1DirectBasePermissions(regime, walkstate, walkparams, accdesc); if accdesc.el == EL0 && !AArch64.S1E0POEnabled(regime, walkparams.nv1) then s1perms.overlay = FALSE; elsif accdesc.el != EL0 && !AArch64.S1POEnabled(regime) then s1perms.overlay = FALSE; if s1perms.overlay then s1overlay_perms = AArch64.S1OverlayPermissions(regime, walkstate, accdesc); s1perms.or = s1overlay_perms.or; s1perms.ow = s1overlay_perms.ow; s1perms.ox = s1overlay_perms.ox; if s1perms.overlay then // If WXN and the overlay X permission is present, the overlay W permission is removed. s1perms.ow = s1perms.ow AND NOT(s1perms.wxn AND s1perms.ox); else // If WXN and the W and X permissions are present, the X permission is removed. // The W and X permissions are factored into the WXN computation. s1perms.x = s1perms.x AND NOT(s1perms.wxn); return s1perms;
```

```
J1.1.4.28 AArch64.S1DirectBasePermissions accdesc)
```

```
// AArch64.S1DirectBasePermissions() // ================================= // Computes the stage 1 direct base permissions S1AccessControls AArch64.S1DirectBasePermissions(Regime regime, TTWState walkstate, S1TTWParams walkparams, AccessDescriptor bit r, w, x; bit pr, pw, px; bit ur, uw, ux; Permissions permissions = walkstate.permissions; S1AccessControls s1perms; // Descriptors marked with DBM set have the effective value of AP[2] cleared. // This implies no Permission faults caused by lack of write permissions are // reported, and the Dirty bit can be set. if permissions.dbm == '1' && walkparams.hd == '1' then permissions.ap<2> = '0'; if HasUnprivileged(regime) then // Apply leaf permissions case permissions.ap<2:1> of when '00' (pr,pw,ur,uw) = ('1','1','0','0'); // Privileged access when '01' (pr,pw,ur,uw) = ('1','1','1','1'); // No effect when '10' (pr,pw,ur,uw) = ('1','0','0','0'); // Read-only, privileged access when '11' (pr,pw,ur,uw) = ('1','0','1','0'); // Read-only // Apply hierarchical permissions case permissions.ap_table of when '00' (pr,pw,ur,uw) = ( pr, pw, ur, uw); // No effect when '01' (pr,pw,ur,uw) = ( pr, pw,'0','0'); // Privileged access when '10' (pr,pw,ur,uw) = ( pr,'0', ur,'0'); // Read-only when '11' (pr,pw,ur,uw) = ( pr,'0','0','0'); // Read-only, privileged access // Locations writable by unprivileged cannot be executed by privileged px = NOT(permissions.pxn OR permissions.pxn_table OR uw); ux = NOT(permissions.uxn OR permissions.uxn_table);
```

```
if (IsFeatureImplemented(FEAT_PAN) && accdesc.pan && !(regime == Regime_EL10 && walkparams.nv1 == '1')) then bit pan; if (boolean IMPLEMENTATION_DEFINED "SCR_EL3.SIF affects EPAN" && accdesc.ss == SS_Secure && walkstate.baseaddress.paspace == PAS_NonSecure && walkparams.sif == '1') then ux = '0'; if (boolean IMPLEMENTATION_DEFINED "Realm EL2&0 regime affects EPAN" && accdesc.ss == SS_Realm && regime == Regime_EL20 && walkstate.baseaddress.paspace != PAS_Realm) then ux = '0'; pan = PSTATE.PAN AND (ur OR uw OR (walkparams.epan AND ux)); pr = pr AND NOT(pan); pw = pw AND NOT(pan); else // Apply leaf permissions case permissions.ap<2> of when '0' (pr,pw) = ('1','1'); // No effect when '1' (pr,pw) = ('1','0'); // Read-only // Apply hierarchical permissions case permissions.ap_table<1> of when '0' (pr,pw) = ( pr, pw); // No effect when '1' (pr,pw) = ( pr,'0'); // Read-only px = NOT(permissions.xn OR permissions.xn_table); (r,w,x) = if accdesc.el == EL0 then (ur,uw,ux) else (pr,pw,px); // Compute WXN value wxn = walkparams.wxn AND w AND x; // Prevent execution from Non-secure space by PE in secure state if SIF is set if accdesc.ss == SS_Secure && walkstate.baseaddress.paspace == PAS_NonSecure then x = x AND NOT(walkparams.sif); // Prevent execution from non-Root space by Root if accdesc.ss == SS_Root && walkstate.baseaddress.paspace != PAS_Root then x = '0'; // Prevent execution from non-Realm space by Realm EL2 and Realm EL2&0 if (accdesc.ss == SS_Realm && regime IN {Regime_EL2, Regime_EL20} && walkstate.baseaddress.paspace != PAS_Realm) then x = '0'; s1perms.r = r; s1perms.w = w; s1perms.x = x; s1perms.gcs = '0'; s1perms.wxn = wxn; s1perms.overlay = TRUE; return s1perms;
```

## J1.1.4.29 AArch64.S1HasAlignmentFaultDueToMemType

```
// AArch64.S1HasAlignmentFaultDueToMemType() // ========================================= // Returns whether stage 1 output fails alignment requirement on data accesses due to memory type boolean AArch64.S1HasAlignmentFaultDueToMemType(Regime regime, AccessDescriptor accdesc, boolean aligned, bit ntlsmd,
```

```
if accdesc.exclusive || accdesc.atomicop || accdesc.acqsc || accdesc.acqpc || accdesc.relsc then if (!aligned && !(IsWBShareable(memattrs) && AArch64.S1DCacheEnabled(regime)) && ConstrainUnpredictableBool(Unpredictable_LSE2_ALIGNMENT_FAULT)) then return TRUE; if memattrs.memtype != MemType_Device then return FALSE; elsif ((accdesc.acctype == AccessType_DCZero && accdesc.cachetype == CacheType_Tag) || accdesc.stzgm) then return ConstrainUnpredictable(Unpredictable_DEVICETAGSTORE) == Constraint_FAULT; elsif accdesc.a32lsmd && ntlsmd == '0' then return memattrs.device != DeviceType_GRE; elsif accdesc.acctype == AccessType_DCZero then return TRUE; elsif !aligned then return !(boolean IMPLEMENTATION_DEFINED "Device location supports unaligned access"); else return FALSE;
```

```
J1.1.4.30 AArch64.S1IndirectBasePermissions // AArch64.S1IndirectBasePermissions() // =================================== // Computes the stage 1 indirect base permissions S1AccessControls AArch64.S1IndirectBasePermissions(Regime regime, TTWState walkstate, S1TTWParams walkparams, AccessDescriptor accdesc) bit r, w, x, gcs, wxn, overlay; bit pr, pw, px, pgcs, pwxn, p_overlay; bit ur, uw, ux, ugcs, uwxn, u_overlay; constant Permissions permissions = walkstate.permissions; S1AccessControls s1perms; // Apply privileged indirect permissions case permissions.ppi of when '0000' (pr,pw,px,pgcs) = ('0','0','0','0'); // No access when '0001' (pr,pw,px,pgcs) = ('1','0','0','0'); // Privileged read when '0010' (pr,pw,px,pgcs) = ('0','0','1','0'); // Privileged execute when '0011' (pr,pw,px,pgcs) = ('1','0','1','0'); // Privileged read and execute when '0100' (pr,pw,px,pgcs) = ('0','0','0','0'); // Reserved when '0101' (pr,pw,px,pgcs) = ('1','1','0','0'); // Privileged read and write when '0110' (pr,pw,px,pgcs) = ('1','1','1','0'); // Privileged read, write and execute when '0111' (pr,pw,px,pgcs) = ('1','1','1','0'); // Privileged read, write and execute when '1000' (pr,pw,px,pgcs) = ('1','0','0','0'); // Privileged read when '1001' (pr,pw,px,pgcs) = ('1','0','0','1'); // Privileged read and gcs when '1010' (pr,pw,px,pgcs) = ('1','0','1','0'); // Privileged read and execute when '1011' (pr,pw,px,pgcs) = ('0','0','0','0'); // Reserved when '1100' (pr,pw,px,pgcs) = ('1','1','0','0'); // Privileged read and write when '1101' (pr,pw,px,pgcs) = ('0','0','0','0'); // Reserved when '1110' (pr,pw,px,pgcs) = ('1','1','1','0'); // Privileged read, write and execute when '1111' (pr,pw,px,pgcs) = ('0','0','0','0'); // Reserved p_overlay = NOT(permissions.ppi<3>); pwxn = if permissions.ppi == '0110' then '1' else '0'; if HasUnprivileged(regime) then // Apply unprivileged indirect permissions case permissions.upi of when '0000' (ur,uw,ux,ugcs) = ('0','0','0','0'); // No access when '0001' (ur,uw,ux,ugcs) = ('1','0','0','0'); // Unprivileged read when '0010' (ur,uw,ux,ugcs) = ('0','0','1','0'); // Unprivileged execute
```

```
when '0011' (ur,uw,ux,ugcs) = ('1','0','1','0'); // Unprivileged read and execute when '0100' (ur,uw,ux,ugcs) = ('0','0','0','0'); // Reserved when '0101' (ur,uw,ux,ugcs) = ('1','1','0','0'); // Unprivileged read and write when '0110' (ur,uw,ux,ugcs) = ('1','1','1','0'); // Unprivileged read, write and execute when '0111' (ur,uw,ux,ugcs) = ('1','1','1','0'); // Unprivileged read, write and execute when '1000' (ur,uw,ux,ugcs) = ('1','0','0','0'); // Unprivileged read when '1001' (ur,uw,ux,ugcs) = ('1','0','0','1'); // Unprivileged read and gcs when '1010' (ur,uw,ux,ugcs) = ('1','0','1','0'); // Unprivileged read and execute when '1011' (ur,uw,ux,ugcs) = ('0','0','0','0'); // Reserved when '1100' (ur,uw,ux,ugcs) = ('1','1','0','0'); // Unprivileged read and write when '1101' (ur,uw,ux,ugcs) = ('0','0','0','0'); // Reserved when '1110' (ur,uw,ux,ugcs) = ('1','1','1','0'); // Unprivileged read,write and execute when '1111' (ur,uw,ux,ugcs) = ('0','0','0','0'); // Reserved u_overlay = NOT(permissions.upi<3>); uwxn = if permissions.upi == '0110' then '1' else '0'; // If the decoded permissions has either px or pgcs along with either uw or ugcs, // then all effective Stage 1 Base Permissions are set to 0 if ((px == '1' || pgcs == '1') && (uw == '1' || ugcs == '1')) then (pr,pw,px,pgcs) = ('0','0','0','0'); (ur,uw,ux,ugcs) = ('0','0','0','0'); if (IsFeatureImplemented(FEAT_PAN) && accdesc.pan && !(regime == Regime_EL10 && walkparams.nv1 == '1')) then if PSTATE.PAN == '1' && (permissions.upi != '0000') then (pr,pw) = ('0','0'); if accdesc.el == EL0 then (r,w,x,gcs,wxn,overlay) = (ur,uw,ux,ugcs,uwxn,u_overlay); else (r,w,x,gcs,wxn,overlay) = (pr,pw,px,pgcs,pwxn,p_overlay); // Prevent execution from Non-secure space by PE in secure state if SIF is set if accdesc.ss == SS_Secure && walkstate.baseaddress.paspace == PAS_NonSecure then x = x AND NOT(walkparams.sif); gcs = '0'; // Prevent execution from non-Root space by Root if accdesc.ss == SS_Root && walkstate.baseaddress.paspace != PAS_Root then x = '0'; gcs = '0'; // Prevent execution from non-Realm space by Realm EL2 and Realm EL2&0 if (accdesc.ss == SS_Realm && regime IN {Regime_EL2, Regime_EL20} && walkstate.baseaddress.paspace != PAS_Realm) then x = '0'; gcs = '0'; s1perms.r = r; s1perms.w = w; s1perms.x = x; s1perms.gcs = gcs; s1perms.wxn = wxn; s1perms.overlay = overlay == '1'; return s1perms;
```

## J1.1.4.31 AArch64.S1OAOutOfRange

```
// AArch64.S1OAOutOfRange() // ======================== // Returns whether stage 1 output address is expressed in the configured size number of bits boolean AArch64.S1OAOutOfRange(bits(56) address, S1TTWParams walkparams) return AArch64.OAOutOfRange(address, walkparams.d128, walkparams.ds, walkparams.ps, walkparams.tgx);
```

## J1.1.4.32 AArch64.S1OverlayPermissions

```
// AArch64.S1OverlayPermissions() // ============================== // Computes the stage 1 overlay permissions S1AccessControls AArch64.S1OverlayPermissions(Regime regime, TTWState walkstate, AccessDescriptor accdesc) bit r, w, x; bit pr, pw, px; bit ur, uw, ux; constant Permissions permissions = walkstate.permissions; S1AccessControls s1overlay_perms; constant S1PORType por = AArch64.S1POR(regime); constant integer bit_index = 4 * UInt(permissions.po_index); constant bits(4) ppo = por<bit_index+3:bit_index>; // Apply privileged overlay permissions case ppo of when '0000' (pr,pw,px) = ('0','0','0'); // No access when '0001' (pr,pw,px) = ('1','0','0'); // Privileged read when '0010' (pr,pw,px) = ('0','0','1'); // Privileged execute when '0011' (pr,pw,px) = ('1','0','1'); // Privileged read and execute when '0100' (pr,pw,px) = ('0','1','0'); // Privileged write when '0101' (pr,pw,px) = ('1','1','0'); // Privileged read and write when '0110' (pr,pw,px) = ('0','1','1'); // Privileged write and execute when '0111' (pr,pw,px) = ('1','1','1'); // Privileged read, write and execute when '1xxx' (pr,pw,px) = ('0','0','0'); // Reserved if HasUnprivileged(regime) then bits(4) upo = '0000'; if !(HaveEL(EL3) && SCR_EL3.PIEn == '0' && boolean IMPLEMENTATION_DEFINED "SCR_EL3.PIEn forces PIE/POE_ELx to zero") then upo = POR_EL0<bit_index+3:bit_index>; // Apply unprivileged overlay permissions case upo of when '0000' (ur,uw,ux) = ('0','0','0'); // No access when '0001' (ur,uw,ux) = ('1','0','0'); // Unprivileged read when '0010' (ur,uw,ux) = ('0','0','1'); // Unprivileged execute when '0011' (ur,uw,ux) = ('1','0','1'); // Unprivileged read and execute when '0100' (ur,uw,ux) = ('0','1','0'); // Unprivileged write when '0101' (ur,uw,ux) = ('1','1','0'); // Unprivileged read and write when '0110' (ur,uw,ux) = ('0','1','1'); // Unprivileged write and execute when '0111' (ur,uw,ux) = ('1','1','1'); // Unprivileged read, write and execute when '1xxx' (ur,uw,ux) = ('0','0','0'); // Reserved (r,w,x) = if accdesc.el == EL0 then (ur,uw,ux) else (pr,pw,px); s1overlay_perms.or = r; s1overlay_perms.ow = w; s1overlay_perms.ox = x; return s1overlay_perms;
```

## J1.1.4.33 AArch64.S1TxSZFaults

// AArch64.S1TxSZFaults()

```
// ====================== // Detect whether configuration of stage 1 TxSZ field generates a fault boolean AArch64.S1TxSZFaults(Regime regime, S1TTWParams walkparams) mintxsz = AArch64.S1MinTxSZ(regime, walkparams); maxtxsz = AArch64.MaxTxSZ(walkparams.tgx); if UInt(walkparams.txsz) < mintxsz then return (IsFeatureImplemented(FEAT_LVA) || boolean IMPLEMENTATION_DEFINED "Fault on TxSZ value below minimum"); if UInt(walkparams.txsz) > maxtxsz then return boolean IMPLEMENTATION_DEFINED "Fault on TxSZ value above maximum"; return FALSE;
```

## J1.1.4.34 AArch64.S2CheckPermissions // AArch64.S2CheckPermissions() // ============================ // Verifies (FaultRecord, boolean) ipa,

```
memory access with available permissions. AArch64.S2CheckPermissions(FaultRecord fault_in, TTWState walkstate, S2TTWParams walkparams, AddressDescriptor AccessDescriptor accdesc) constant MemType memtype = walkstate.memattrs.memtype; constant Permissions permissions = walkstate.permissions; FaultRecord fault = fault_in; constant S2AccessControls s2perms = AArch64.S2ComputePermissions(permissions, walkparams, accdesc); bit r, w; bit or, ow; if accdesc.acctype == AccessType_TTW then r = s2perms.r_mmu; w = s2perms.w_mmu; or = s2perms.or_mmu; ow = s2perms.ow_mmu; elsif accdesc.rcw then r = s2perms.r_rcw; w = s2perms.w_rcw; or = s2perms.or_rcw; ow = s2perms.ow_rcw; else r = s2perms.r; w = s2perms.w; or = s2perms.or; ow = s2perms.ow; if accdesc.acctype == AccessType_TTW then if (accdesc.toplevel && accdesc.varange == VARange_LOWER && ((walkparams.tl0 == '1' && s2perms.toplevel0 == '0') || (walkparams.tl1 == '1' && s2perms.<toplevel1,toplevel0> == '10'))) then fault.statuscode = Fault_Permission; fault.toplevel = TRUE; elsif (accdesc.toplevel && accdesc.varange == VARange_UPPER && ((walkparams.tl1 == '1' && s2perms.toplevel1 == '0') || (walkparams.tl0 == '1' && s2perms.<toplevel1,toplevel0> == '01'))) then fault.statuscode = Fault_Permission; fault.toplevel = TRUE; // Stage 2 Permission fault due to AssuredOnly check elsif (walkstate.s2assuredonly == '1' && !ipa.s1assured) then fault.statuscode = Fault_Permission; fault.assuredonly = TRUE;
```

```
elsif s2perms.overlay && or == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif accdesc.write && s2perms.overlay && ow == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif walkparams.ptw == '1' && memtype == MemType_Device then fault.statuscode = Fault_Permission; // Prevent translation table walks in Non-secure space by Realm state elsif accdesc.ss == SS_Realm && walkstate.baseaddress.paspace != PAS_Realm then fault.statuscode = Fault_Permission; elsif r == '0' then fault.statuscode = Fault_Permission; elsif accdesc.write && w == '0' then fault.statuscode = Fault_Permission; fault.hdbssf = walkparams.hdbss == '1' && !CanAppendToHDBSS() && permissions.dbm == '1'; elsif (accdesc.write && (walkparams.hd != '1' || (walkparams.hdbss == '1' && !CanAppendToHDBSS())) && walkparams.s2pie == '1' && permissions.s2dirty == '0') then fault.statuscode = Fault_Permission; fault.dirtybit = TRUE; fault.hdbssf = walkparams.hdbss == '1' && !CanAppendToHDBSS(); // Stage 2 Permission fault due to AssuredOnly check elsif ((walkstate.s2assuredonly == '1' && !ipa.s1assured) || (walkstate.s2assuredonly != '1' && IsFeatureImplemented(FEAT_GCS) && VTCR_EL2.GCSH == '1' && accdesc.acctype == AccessType_GCS && accdesc.el != EL0)) then fault.statuscode = Fault_Permission; fault.assuredonly = TRUE; elsif accdesc.acctype == AccessType_IFETCH then if s2perms.overlay && s2perms.ox == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif (memtype == MemType_Device && ConstrainUnpredictable(Unpredictable_INSTRDEVICE) == Constraint_FAULT) then fault.statuscode = Fault_Permission; // Prevent execution from Non-secure space by Realm state elsif accdesc.ss == SS_Realm && walkstate.baseaddress.paspace != PAS_Realm then fault.statuscode = Fault_Permission; elsif s2perms.x == '0' then fault.statuscode = Fault_Permission; elsif accdesc.acctype == AccessType_DC then if accdesc.cacheop == CacheOp_Invalidate then if !ELUsingAArch32(EL1) && s2perms.overlay && ow == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif !ELUsingAArch32(EL1) && w == '0' then fault.statuscode = Fault_Permission; elsif (walkparams.hd != '1' && walkparams.s2pie == '1' && permissions.s2dirty == '0') then fault.statuscode = Fault_Permission; fault.dirtybit = TRUE; elsif !ELUsingAArch32(EL1) && accdesc.el == EL0 && s2perms.overlay && or == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif (walkparams.cmow == '1' && accdesc.cacheop == CacheOp_CleanInvalidate && s2perms.overlay && ow == '0') then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif !ELUsingAArch32(EL1) && accdesc.el == EL0 && r == '0' then fault.statuscode = Fault_Permission; elsif (walkparams.cmow == '1' && accdesc.cacheop == CacheOp_CleanInvalidate &&
```

```
w == '0') then fault.statuscode = Fault_Permission; elsif (walkparams.cmow == '1' && accdesc.cacheop == CacheOp_CleanInvalidate && walkparams.hd != '1' && walkparams.s2pie == '1' && permissions.s2dirty == '0') then fault.statuscode = Fault_Permission; fault.dirtybit = TRUE; elsif accdesc.acctype == AccessType_IC then if (!ELUsingAArch32(EL1) && accdesc.el == EL0 && s2perms.overlay && or == '0' && boolean IMPLEMENTATION_DEFINED "Permission fault on EL0 IC_IVAU execution") then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif walkparams.cmow == '1' && s2perms.overlay && ow == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; elsif (!ELUsingAArch32(EL1) && accdesc.el == EL0 && r == '0' && boolean IMPLEMENTATION_DEFINED "Permission fault on EL0 IC_IVAU execution") then fault.statuscode = Fault_Permission; elsif walkparams.cmow == '1' && w == '0' then fault.statuscode = Fault_Permission; elsif (walkparams.cmow == '1' && walkparams.hd != '1' && walkparams.s2pie == '1' && permissions.s2dirty == '0') then fault.statuscode = Fault_Permission; fault.dirtybit = TRUE; elsif accdesc.read && s2perms.overlay && or == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; fault.write = FALSE; elsif accdesc.write && s2perms.overlay && ow == '0' then fault.statuscode = Fault_Permission; fault.overlay = TRUE; fault.write = TRUE; elsif accdesc.read && r == '0' then fault.statuscode = Fault_Permission; fault.write = FALSE; elsif accdesc.write && w == '0' then fault.statuscode = Fault_Permission; fault.write = TRUE; fault.hdbssf = walkparams.hdbss == '1' && !CanAppendToHDBSS() && permissions.dbm == '1'; elsif (IsFeatureImplemented(FEAT_MTE_PERM) && ((accdesc.tagchecked && AArch64.EffectiveTCF(accdesc.el, accdesc.read) != TCFType_Ignore) || accdesc.tagaccess) && ipa.memattrs.tags == MemTag_AllocationTagged && permissions.s2tag_na == '1' && S2DCacheEnabled()) then fault.statuscode = Fault_Permission; fault.tagaccess = TRUE; fault.write = accdesc.tagaccess && accdesc.write; elsif (accdesc.write && (walkparams.hd != '1' || (walkparams.hdbss == '1' && !CanAppendToHDBSS())) && walkparams.s2pie == '1' && permissions.s2dirty == '0') then fault.statuscode = Fault_Permission; fault.dirtybit = TRUE; fault.write = TRUE; fault.hdbssf = walkparams.hdbss == '1' && !CanAppendToHDBSS(); // MRO* allows only RCW and MMU writes boolean mro; if s2perms.overlay then mro = (s2perms.<w,w_rcw,w_mmu> AND s2perms.<ow,ow_rcw,ow_mmu>) == '011'; else mro = s2perms.<w,w_rcw,w_mmu> == '011'; return (fault, mro);
```

## J1.1.4.35 AArch64.S2ComputePermissions

```
// AArch64.S2ComputePermissions() // ============================== // Compute the overall stage 2 permissions. S2AccessControls AArch64.S2ComputePermissions(Permissions permissions, S2TTWParams walkparams, AccessDescriptor accdesc) S2AccessControls s2perms; if walkparams.s2pie == '1' then s2perms = AArch64.S2IndirectBasePermissions(permissions, accdesc); s2perms.overlay = IsFeatureImplemented(FEAT_S2POE) && VTCR_EL2.S2POE == '1'; if s2perms.overlay then s2overlay_perms = AArch64.S2OverlayPermissions(permissions, accdesc); s2perms.or = s2overlay_perms.or; s2perms.ow = s2overlay_perms.ow; s2perms.ox = s2overlay_perms.ox; s2perms.or_rcw = s2overlay_perms.or_rcw; s2perms.ow_rcw = s2overlay_perms.ow_rcw; s2perms.or_mmu = s2overlay_perms.or_mmu; s2perms.ow_mmu = s2overlay_perms.ow_mmu; // Toplevel is applicable only when the effective S2 permissions is MRO if ((s2perms.<w,w_rcw,w_mmu> AND s2perms.<ow,ow_rcw,ow_mmu>) == '011') then s2perms.toplevel0 = s2perms.toplevel0 OR s2overlay_perms.toplevel0; s2perms.toplevel1 = s2perms.toplevel1 OR s2overlay_perms.toplevel1; else s2perms.toplevel0 = '0'; s2perms.toplevel1 = '0'; else s2perms = AArch64.S2DirectBasePermissions(permissions, accdesc, walkparams); return s2perms; J1.1.4.36 AArch64.S2DirectBasePermissions walkparams)
```

```
// AArch64.S2DirectBasePermissions() // ================================= // Computes the stage 2 direct base permissions. S2AccessControls AArch64.S2DirectBasePermissions(Permissions permissions, AccessDescriptor accdesc, S2TTWParams S2AccessControls s2perms; bit w; constant bit r = permissions.s2ap<0>; if permissions.s2ap<1> == '1' then w = '1'; // Descriptors marked with DBM set have the effective value of S2AP[1] set. // This implies no Permission faults caused by lack of write permissions are // reported, and the Dirty bit can be set. elsif permissions.dbm == '1' && walkparams.hd == '1' then // An update occurs here, conditional to being able to append to HDBSS if walkparams.hdbss == '1' then w = if CanAppendToHDBSS() then '1' else '0'; else w = '1'; else w = '0'; bit px, ux; case (permissions.s2xn:permissions.s2xnx) of
```

```
when '00' (px,ux) = ('1','1'); when '01' (px,ux) = ('0','1'); when '10' (px,ux) = ('0','0'); when '11' (px,ux) = ('1','0'); x = if accdesc.el == EL0 then ux else s2perms.r = r; s2perms.w = w; s2perms.x = x; s2perms.r_rcw = r; s2perms.w_rcw = w; s2perms.r_mmu = r; s2perms.w_mmu = w; s2perms.toplevel0 = '0'; s2perms.toplevel1 = '0'; s2perms.overlay = FALSE; return s2perms;
```

```
// AArch64.S2InconsistentSL() // ========================== // Detect inconsistent configuration of stage 2 TxSZ and SL fields boolean AArch64.S2InconsistentSL(S2TTWParams walkparams) startlevel = AArch64.S2StartLevel(walkparams); levels = FINAL_LEVEL -startlevel; granulebits = TGxGranuleBits(walkparams.tgx); descsizelog2 = 3; stride = granulebits -descsizelog2; // Input address size must at least be large enough to be resolved from the start sl_min_iasize = ( levels * stride // Bits resolved by table walk, except initial level + granulebits // Bits directly mapped to output address + 1); // At least 1 more bit to be decoded by initial level
```

```
px; J1.1.4.37 AArch64.S2HasAlignmentFaultDueToMemType // AArch64.S2HasAlignmentFaultDueToMemType() // ========================================= // Returns whether stage 2 output fails alignment requirement on data accesses due to memory type boolean AArch64.S2HasAlignmentFaultDueToMemType(AccessDescriptor accdesc, boolean aligned, MemoryAttributes memattrs) if accdesc.exclusive || accdesc.atomicop || accdesc.acqsc || accdesc.acqpc || accdesc.relsc then if (!aligned && !(IsWBShareable(memattrs) && S2DCacheEnabled()) && ConstrainUnpredictableBool(Unpredictable_LSE2_ALIGNMENT_FAULT)) then return TRUE; if memattrs.memtype != MemType_Device then return FALSE; elsif ((accdesc.acctype == AccessType_DCZero && accdesc.cachetype == CacheType_Tag) || accdesc.stzgm) then return ConstrainUnpredictable(Unpredictable_DEVICETAGSTORE) == Constraint_FAULT; elsif accdesc.acctype == AccessType_DCZero then return TRUE; elsif !aligned then return !(boolean IMPLEMENTATION_DEFINED "Device location supports unaligned access"); else return FALSE; J1.1.4.38 AArch64.S2InconsistentSL level
```

```
// Can accomodate 1 more stride in the level + concatenation of up to sl_max_iasize = sl_min_iasize + (stride-1) + 4; // Configured Input Address size iasize = AArch64.IASize(walkparams.txsz); return iasize < sl_min_iasize || iasize > sl_max_iasize;
```

## J1.1.4.39 AArch64.S2IndirectBasePermissions

```
// AArch64.S2IndirectBasePermissions() // =================================== // Computes the stage 2 indirect base permissions. S2AccessControls AArch64.S2IndirectBasePermissions(Permissions permissions, AccessDescriptor accdesc) bit r, w; bit r_rcw, w_rcw; bit r_mmu, w_mmu; bit px, ux; bit toplevel0, toplevel1; S2AccessControls s2perms; constant bits(4) s2pi = permissions.s2pi; case s2pi of when '0000' (r,w,px,ux,w_rcw,w_mmu) = ('0','0','0','0','0','0'); // No Access when '0001' (r,w,px,ux,w_rcw,w_mmu) = ('0','0','0','0','0','0'); // Reserved when '0010' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','0','1','1'); // MRO when '0011' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','0','1','1'); // MRO-TL1 when '0100' (r,w,px,ux,w_rcw,w_mmu) = ('0','1','0','0','0','0'); // Write Only when '0101' (r,w,px,ux,w_rcw,w_mmu) = ('0','0','0','0','0','0'); // Reserved when '0110' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','0','1','1'); // MRO-TL0 when '0111' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','0','1','1'); // MRO-TL01 when '1000' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','0','0','0'); // Read Only when '1001' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','1','0','0'); // Read, Unpriv Execute when '1010' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','1','0','0','0'); // Read, Priv Execute when '1011' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','1','1','0','0'); // Read, All Execute when '1100' (r,w,px,ux,w_rcw,w_mmu) = ('1','1','0','0','1','1'); // RW when '1101' (r,w,px,ux,w_rcw,w_mmu) = ('1','1','0','1','1','1'); // RW, Unpriv Execute when '1110' (r,w,px,ux,w_rcw,w_mmu) = ('1','1','1','0','1','1'); // RW, Priv Execute when '1111' (r,w,px,ux,w_rcw,w_mmu) = ('1','1','1','1','1','1'); // RW, All Execute x = if accdesc.el == EL0 then ux else px; // RCW and MMU read permissions. (r_rcw, r_mmu) = (r, r); // Stage 2 Top Level Permission Attributes. case s2pi of when '0110' (toplevel0,toplevel1) = ('1','0'); when '0011' (toplevel0,toplevel1) = ('0','1'); when '0111' (toplevel0,toplevel1) = ('1','1'); otherwise (toplevel0,toplevel1) = ('0','0'); s2perms.r = r; s2perms.w = w; s2perms.x = x; s2perms.r_rcw = r_rcw; s2perms.r_mmu = r_mmu; s2perms.w_rcw = w_rcw; s2perms.w_mmu = w_mmu; s2perms.toplevel0 = toplevel0; s2perms.toplevel1 = toplevel1; return s2perms;
```

```
2^4 tables
```

## J1.1.4.40 AArch64.S2InvalidSL

```
// AArch64.S2InvalidSL() // ===================== // Detect invalid configuration of SL field boolean AArch64.S2InvalidSL(S2TTWParams walkparams) case walkparams.tgx of when TGx_4KB case walkparams.sl2:walkparams.sl0 of when '1x1' return TRUE; when '11x' return TRUE; when '100' return AArch64.PAMax() < 52; when '010' return AArch64.PAMax() < 44; when '011' return !IsFeatureImplemented(FEAT_TTST); otherwise return FALSE; when TGx_16KB case walkparams.sl0 of when '11' return walkparams.ds == '0' || when '10' return AArch64.PAMax() < 42; otherwise return FALSE; when TGx_64KB case walkparams.sl0 of when '11' return TRUE; when '10' return AArch64.PAMax() < 44; otherwise return FALSE;
```

```
// AArch64.S2OverlayPermissions() // ============================== // Computes the stage 2 overlay permissions. S2AccessControls AArch64.S2OverlayPermissions(Permissions permissions, AccessDescriptor bit r, w; bit r_rcw, w_rcw; bit r_mmu, w_mmu; bit px, ux; bit toplevel0, toplevel1; S2AccessControls s2overlay_perms; constant integer index = 4 * UInt(permissions.s2po_index); bits(4) s2po = '0000'; if !(HaveEL(EL3) && SCR_EL3.PIEn == '0' && boolean IMPLEMENTATION_DEFINED "SCR_EL3.PIEn forces PIE/POE_ELx to zero") then s2po = S2POR_EL1<index+3:index>; case s2po of when '0000' (r,w,px,ux,w_rcw,w_mmu) = ('0','0','0','0','0','0'); // No Access when '0001' (r,w,px,ux,w_rcw,w_mmu) = ('0','0','0','0','0','0'); // Reserved when '0010' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','0','1','1'); // MRO
```

## AArch64.PAMax() &lt; 52; J1.1.4.41 AArch64.S2OAOutOfRange // AArch64.S2OAOutOfRange() // ======================== // Returns whether stage 2 output address is expressed in the configured size number of bits boolean AArch64.S2OAOutOfRange(bits(56) address, S2TTWParams walkparams) return AArch64.OAOutOfRange(address, walkparams.d128, walkparams.ds, walkparams.ps, walkparams.tgx); J1.1.4.42 AArch64.S2OverlayPermissions accdesc)

```
when '0011' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','0','1','1'); // MRO-TL1 when '0100' (r,w,px,ux,w_rcw,w_mmu) = ('0','1','0','0','0','0'); // Write Only when '0101' (r,w,px,ux,w_rcw,w_mmu) = ('0','0','0','0','0','0'); // Reserved when '0110' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','0','1','1'); // MRO-TL0 when '0111' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','0','1','1'); // MRO-TL01 when '1000' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','0','0','0'); // Read Only when '1001' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','0','1','0','0'); // Read, Unpriv Execute when '1010' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','1','0','0','0'); // Read, Priv Execute when '1011' (r,w,px,ux,w_rcw,w_mmu) = ('1','0','1','1','0','0'); // Read, All Execute when '1100' (r,w,px,ux,w_rcw,w_mmu) = ('1','1','0','0','1','1'); // RW when '1101' (r,w,px,ux,w_rcw,w_mmu) = ('1','1','0','1','1','1'); // RW, Unpriv Execute when '1110' (r,w,px,ux,w_rcw,w_mmu) = ('1','1','1','0','1','1'); // RW, Priv Execute when '1111' (r,w,px,ux,w_rcw,w_mmu) = ('1','1','1','1','1','1'); // RW, All Execute x = if accdesc.el == EL0 then ux else px; // RCW and MMU read permissions. (r_rcw, r_mmu) = (r, r); // Stage 2 Top Level Permission Attributes. case s2po of when '0110' (toplevel0,toplevel1) = ('1','0'); when '0011' (toplevel0,toplevel1) = ('0','1'); when '0111' (toplevel0,toplevel1) = ('1','1'); otherwise (toplevel0,toplevel1) = ('0','0'); s2overlay_perms.or = r; s2overlay_perms.ow = w; s2overlay_perms.ox = x; s2overlay_perms.or_rcw = r_rcw; s2overlay_perms.ow_rcw = w_rcw; s2overlay_perms.or_mmu = r_mmu; s2overlay_perms.ow_mmu = w_mmu; s2overlay_perms.toplevel0 = toplevel0; s2overlay_perms.toplevel1 = toplevel1; return s2overlay_perms;
```

## J1.1.4.43 AArch64.S2TxSZFaults // AArch64.S2TxSZFaults() // ====================== // Detect whether configuration of stage 2 TxSZ field generates a fault boolean AArch64.S2TxSZFaults(S2TTWParams walkparams, boolean s1aarch64) mintxsz = AArch64.S2MinTxSZ(walkparams, s1aarch64); maxtxsz = AArch64.MaxTxSZ(walkparams.tgx); if UInt(walkparams.txsz) &lt; mintxsz then return (IsFeatureImplemented(FEAT\_LPA) || boolean IMPLEMENTATION\_DEFINED "Fault on TxSZ value below minimum"); if UInt(walkparams.txsz) &gt; maxtxsz then return boolean IMPLEMENTATION\_DEFINED "Fault on TxSZ value above maximum"; return FALSE; J1.1.4.44 AArch64.VAIsOutOfRange value

```
// AArch64.VAIsOutOfRange() // ======================== // Check bits not resolved by translation are identical and of accepted boolean AArch64.VAIsOutOfRange(bits(64) va_in, AccessType acctype,
```

```
Regime regime, S1TTWParams walkparams) bits(64) va = va_in; constant AddressSize addrtop = AArch64.AddrTop(walkparams.tbid, acctype, walkparams.tbi); // If the VA has a Logical Address Tag then the bits holding the Logical Address Tag are // ignored when checking if the address is out of range. if walkparams.mtx == '1' && acctype != AccessType_IFETCH then va<59:56> = if AArch64.GetVARange(va) == VARange_UPPER then '1111' else '0000'; // Input Address size constant integer iasize = AArch64.IASize(walkparams.txsz); // The min value of TxSZ can be 8, with LVA3 implemented. // If TxSZ is set to 8 iasize becomes 64 -8 = 56 // If tbi is also set, addrtop becomes 55 // Then the return statements check va<56:55> // The check here is to guard against this corner case. if addrtop < iasize then return FALSE; if HasUnprivileged(regime) then if AArch64.GetVARange(va) == VARange_LOWER then return !IsZero(va<addrtop:iasize>); else return !IsOnes(va<addrtop:iasize>); else return !IsZero(va<addrtop:iasize>);
```

## J1.1.4.45 AArch64.S2ApplyFWBMemAttrs

```
// AArch64.S2ApplyFWBMemAttrs() // ============================ // Apply stage 2 forced Write-Back on stage 1 memory attributes. MemoryAttributes AArch64.S2ApplyFWBMemAttrs(MemoryAttributes s1_memattrs, S2TTWParams walkparams, bits(N) descriptor) MemoryAttributes memattrs; s2_attr = descriptor<5:2>; s2_sh = if walkparams.ds == '1' then walkparams.sh else descriptor<9:8>; s2_fnxs = descriptor<11>; if s2_attr<2> == '0' then // S2 Device, S1 any s2_device = DecodeDevice(s2_attr<1:0>); memattrs.memtype = MemType_Device; if s1_memattrs.memtype == MemType_Device then memattrs.device = S2CombineS1Device(s1_memattrs.device, s2_device); else memattrs.device = s2_device; memattrs.xs = s1_memattrs.xs; elsif s2_attr<1:0> == '11' then // S2 attr = S1 attr memattrs = s1_memattrs; elsif s2_attr<1:0> == '10' then // Force writeback memattrs.memtype = MemType_Normal; memattrs.inner.attrs = MemAttr_WB; memattrs.outer.attrs = MemAttr_WB; if (s1_memattrs.memtype == MemType_Normal && s1_memattrs.inner.attrs != MemAttr_NC) then memattrs.inner.hints = s1_memattrs.inner.hints; memattrs.inner.transient = s1_memattrs.inner.transient; else
```

```
memattrs.inner.hints = MemHint_RWA; memattrs.inner.transient = FALSE; if (s1_memattrs.memtype == MemType_Normal && s1_memattrs.outer.attrs != MemAttr_NC) then memattrs.outer.hints = s1_memattrs.outer.hints; memattrs.outer.transient = s1_memattrs.outer.transient; else memattrs.outer.hints = MemHint_RWA; memattrs.outer.transient = FALSE; memattrs.xs = '0'; else // Non-cacheable unless S1 is device if s1_memattrs.memtype == MemType_Device then memattrs = s1_memattrs; else MemAttrHints cacheability_attr; cacheability_attr.attrs = MemAttr_NC; memattrs.memtype = MemType_Normal; memattrs.inner = cacheability_attr; memattrs.outer = cacheability_attr; memattrs.xs = s1_memattrs.xs; s2_shareability = DecodeShareability(s2_sh); memattrs.shareability = S2CombineS1Shareability(s1_memattrs.shareability, s2_shareability); memattrs.tags = S2MemTagType(memattrs, s1_memattrs.tags); memattrs.notagaccess = (s2_attr<3:1> == '111' && memattrs.tags == MemTag_AllocationTagged); if s2_fnxs == '1' then memattrs.xs = '0'; memattrs.shareability = EffectiveShareability(memattrs); return memattrs;
```

```
J1.1.4.46 AArch64.GetS1TLBContext
```

```
// AArch64.GetS1TLBContext() // ========================= // Gather translation context for accesses with VA to match against TLB entries TLBContext AArch64.GetS1TLBContext(Regime regime, SecurityState ss, bits(64) va, TGx tg) TLBContext tlbcontext; case regime of when Regime_EL3 tlbcontext = AArch64.TLBContextEL3(ss, va, tg); when Regime_EL2 tlbcontext = AArch64.TLBContextEL2(ss, va, tg); when Regime_EL20 tlbcontext = AArch64.TLBContextEL20(ss, va, tg); when Regime_EL10 tlbcontext = AArch64.TLBContextEL10(ss, va, tg); otherwise Unreachable(); tlbcontext.includes_s1 = TRUE; // The following may be amended for EL1&0 Regime if caching of stage 2 is successful tlbcontext.includes_s2 = FALSE; tlbcontext.use_vmid = UseVMID(regime); // The following may be amended if Granule Protection Check passes tlbcontext.includes_gpt = FALSE; return tlbcontext;
```

## J1.1.4.47 AArch64.GetS2TLBContext

```
// AArch64.GetS2TLBContext() // ========================= // Gather translation context for accesses with IPA to match against TLB entries TLBContext AArch64.GetS2TLBContext(SecurityState ss, FullAddress ipa, TGx tg) assert EL2Enabled(); TLBContext tlbcontext; tlbcontext.ss = ss; tlbcontext.regime = Regime_EL10; tlbcontext.ipaspace = ipa.paspace; tlbcontext.vmid = VMID[]; tlbcontext.tg = tg; tlbcontext.ia = ZeroExtend(ipa.address, 64); if IsFeatureImplemented(FEAT_TTCNP) then tlbcontext.cnp = if ipa.paspace == PAS_Secure then VSTTBR_EL2.CnP else VTTBR_EL2.CnP; else tlbcontext.cnp = '0'; tlbcontext.includes_s1 = FALSE; tlbcontext.includes_s2 = TRUE; tlbcontext.use_vmid = TRUE; // This amy be amended if Granule Protection Check passes tlbcontext.includes_gpt = FALSE; return tlbcontext;
```

```
J1.1.4.48 AArch64.TLBContextEL10
```

```
// AArch64.TLBContextEL10() // ======================== // Gather translation context for accesses under EL10 regime to match against TLB entries TLBContext AArch64.TLBContextEL10(SecurityState ss, bits(64) va, TGx tg) TLBContext tlbcontext; tlbcontext.ss = ss; tlbcontext.regime = Regime_EL10; tlbcontext.vmid = VMID[]; if IsFeatureImplemented(FEAT_ASID2) && IsTCR2EL1Enabled() && TCR2_EL1.A2 == '1' then constant VARange varange = AArch64.GetVARange(va); tlbcontext.asid = if varange == VARange_LOWER then TTBR0_EL1.ASID else TTBR1_EL1.ASID; else tlbcontext.asid = if TCR_EL1.A1 == '0' then TTBR0_EL1.ASID else TTBR1_EL1.ASID; if TCR_EL1.AS == '0' then tlbcontext.asid<15:8> = Zeros(8); tlbcontext.tg = tg; tlbcontext.ia = va; if IsFeatureImplemented(FEAT_TTCNP) then if AArch64.GetVARange(va) == VARange_LOWER then tlbcontext.cnp = TTBR0_EL1.CnP; else tlbcontext.cnp = TTBR1_EL1.CnP; else tlbcontext.cnp = '0'; return tlbcontext;
```

## J1.1.4.49 AArch64.TLBContextEL2

```
// AArch64.TLBContextEL2() // ======================= // Gather translation context for accesses under EL2 regime to match against TLB entries TLBContext AArch64.TLBContextEL2(SecurityState ss, bits(64) va, TGx tg) TLBContext tlbcontext; tlbcontext.ss = ss; tlbcontext.regime = Regime_EL2; tlbcontext.tg = tg; tlbcontext.ia = va; tlbcontext.cnp = if IsFeatureImplemented(FEAT_TTCNP) then TTBR0_EL2.CnP else '0'; return tlbcontext;
```

## J1.1.4.50 AArch64.TLBContextEL20

```
// AArch64.TLBContextEL20() // ======================== // Gather translation context for accesses under EL20 regime to match against TLB entries TLBContext AArch64.TLBContextEL20(SecurityState ss, bits(64) va, TGx tg) TLBContext tlbcontext; tlbcontext.ss = ss; tlbcontext.regime = Regime_EL20; if IsFeatureImplemented(FEAT_ASID2) && IsTCR2EL2Enabled() && TCR2_EL2.A2 == '1' then constant VARange varange = AArch64.GetVARange(va); tlbcontext.asid = if varange == VARange_LOWER then TTBR0_EL2.ASID else TTBR1_EL2.ASID; else tlbcontext.asid = if TCR_EL2.A1 == '0' then TTBR0_EL2.ASID else TTBR1_EL2.ASID; if TCR_EL2.AS == '0' then tlbcontext.asid<15:8> = Zeros(8); tlbcontext.tg = tg; tlbcontext.ia = va; if IsFeatureImplemented(FEAT_TTCNP) then if AArch64.GetVARange(va) == VARange_LOWER then tlbcontext.cnp = TTBR0_EL2.CnP; else tlbcontext.cnp = TTBR1_EL2.CnP; else tlbcontext.cnp = '0'; return tlbcontext;
```

## J1.1.4.51 AArch64.TLBContextEL3

```
// AArch64.TLBContextEL3() // ======================= // Gather translation context for accesses under EL3 regime to match against TLB entries TLBContext AArch64.TLBContextEL3(SecurityState ss, bits(64) va, TGx tg) TLBContext tlbcontext; tlbcontext.ss = ss; tlbcontext.regime = Regime_EL3; tlbcontext.tg = tg; tlbcontext.ia = va;
```

```
tlbcontext.cnp = if IsFeatureImplemented(FEAT_TTCNP) then TTBR0_EL3.CnP else '0'; return tlbcontext;
```

## J1.1.4.52 AArch64.FullTranslate

```
// AArch64.FullTranslate() // ======================= // Address translation as specified by VMSA // Alignment check NOT due to memory type is expected to be done before translation AddressDescriptor AArch64.FullTranslate(bits(64) va, integer size, AccessDescriptor accdesc, boolean aligned) constant Regime regime = TranslationRegime(accdesc.el); FaultRecord fault = NoFault(accdesc, va); AddressDescriptor ipa; (fault, ipa) = AArch64.S1Translate(fault, regime, va, size, aligned, accdesc); if fault.statuscode != Fault_None then return CreateFaultyAddressDescriptor(fault); if accdesc.ss == SS_Realm then assert EL2Enabled(); if regime == Regime_EL10 && EL2Enabled() then s1aarch64 = TRUE; AddressDescriptor pa; (fault, pa) = AArch64.S2Translate(fault, ipa, s1aarch64, aligned, accdesc); if fault.statuscode != Fault_None then return CreateFaultyAddressDescriptor(fault); else return pa; else return ipa;
```

## J1.1.4.53 AArch64.MemSwapTableDesc

```
// AArch64.MemSwapTableDesc() // ========================== // Perform HW update of table descriptor as an atomic operation (FaultRecord, bits(N)) AArch64.MemSwapTableDesc(FaultRecord fault_in, bits(N) prev_desc, bits(N) new_desc, bit ee, AccessDescriptor descaccess, AddressDescriptor descpaddr, integer N) assert descaccess.acctype == AccessType_TTW; FaultRecord fault = fault_in; boolean iswrite; if IsFeatureImplemented(FEAT_RME) then fault.gpcf = GranuleProtectionCheck(descpaddr, descaccess); if fault.gpcf.gpf != GPCF_None then fault.statuscode = Fault_GPCFOnWalk; fault.paddress = descpaddr.paddress; fault.gpcfs2walk = fault.secondstage; return (fault, bits(N) UNKNOWN); // All observers in the shareability domain observe the // following memory read and write accesses atomically. bits(N) mem_desc; PhysMemRetStatus memstatus; (memstatus, mem_desc) = PhysMemRead(descpaddr, N DIV 8, descaccess);
```

```
if ee == '1' then mem_desc = BigEndianReverse(mem_desc); if IsFault(memstatus) then iswrite = FALSE; fault = HandleExternalTTWAbort(memstatus, iswrite, descpaddr, descaccess, N if IsFault(fault.statuscode) then return (fault, bits(N) UNKNOWN); if mem_desc == prev_desc then ordered_new_desc = if ee == '1' then BigEndianReverse(new_desc) else new_desc; memstatus = PhysMemWrite(descpaddr, N DIV 8, descaccess, ordered_new_desc); if IsFault(memstatus) then iswrite = TRUE; fault = HandleExternalTTWAbort(memstatus, iswrite, descpaddr, descaccess, N DIV 8, fault); if IsFault(fault.statuscode) then return (fault, bits(N) UNKNOWN); // Reflect what is now in memory (in little endian format) mem_desc = new_desc; return (fault, mem_desc);
```

```
// AArch64.S1DisabledOutput() // ========================== // Map the VA to IPA/PA and assign default memory attributes (FaultRecord, AddressDescriptor) AArch64.S1DisabledOutput(FaultRecord fault_in, Regime regime, bits(64) va_in, AccessDescriptor boolean aligned) bits(64) va = va_in; walkparams = AArch64.GetS1TTWParams(regime, accdesc.el, accdesc.ss, va); FaultRecord fault = fault_in; // No memory page is guarded when stage 1 address translation is disabled SetInGuardedPage(FALSE); // Output Address FullAddress oa; oa.address = va<55:0>; case accdesc.ss of when SS_Secure oa.paspace = PAS_Secure; when SS_NonSecure oa.paspace = PAS_NonSecure; when SS_Root oa.paspace = PAS_Root; when SS_Realm oa.paspace = PAS_Realm; MemoryAttributes memattrs; if regime == Regime_EL10 && EL2Enabled() && walkparams.dc == '1' then MemAttrHints default_cacheability; default_cacheability.attrs = MemAttr_WB; default_cacheability.hints = MemHint_RWA; default_cacheability.transient = FALSE; memattrs.memtype = MemType_Normal; memattrs.outer = default_cacheability; memattrs.inner = default_cacheability; memattrs.shareability = Shareability_NSH; if walkparams.dct == '1' then memattrs.tags = MemTag_AllocationTagged;
```

```
DIV 8, fault); J1.1.4.54 AArch64.S1DisabledOutput accdesc,
```

```
elsif IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS) && walkparams.mtx == '1' then memattrs.tags = MemTag_CanonicallyTagged; else memattrs.tags = MemTag_Untagged; memattrs.xs = '0'; elsif accdesc.acctype == AccessType_IFETCH then MemAttrHints i_cache_attr; if AArch64.S1ICacheEnabled(regime) then i_cache_attr.attrs = MemAttr_WT; i_cache_attr.hints = MemHint_RA; i_cache_attr.transient = FALSE; else i_cache_attr.attrs = MemAttr_NC; memattrs.memtype = MemType_Normal; memattrs.outer = i_cache_attr; memattrs.inner = i_cache_attr; memattrs.shareability = Shareability_OSH; memattrs.tags = MemTag_Untagged; memattrs.xs = '1'; elsif accdesc.acctype == AccessType_SPE && EffectivePMBLIMITR_EL1_nVM() == '1' then memattrs = S1DecodeMemAttrs(PMBMAR_EL1.Attr, PMBMAR_EL1.SH, TRUE, walkparams, accdesc.acctype); elsif accdesc.acctype == AccessType_TRBE && EffectiveTRBLIMITR_EL1_nVM() == '1' then memattrs = S1DecodeMemAttrs(TRBMAR_EL1.Attr, TRBMAR_EL1.SH, TRUE, walkparams, accdesc.acctype); else memattrs.memtype = MemType_Device; memattrs.device = DeviceType_nGnRnE; memattrs.shareability = Shareability_OSH; if IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS) && walkparams.mtx == '1' then memattrs.tags = MemTag_CanonicallyTagged; else memattrs.tags = MemTag_Untagged; memattrs.xs = '1'; memattrs.notagaccess = FALSE; if walkparams.mtx == '1' && walkparams.tbi == '0' && accdesc.acctype != AccessType_IFETCH then // For the purpose of the checks in this function, the MTE tag bits are ignored. va<59:56> = if HasUnprivileged(regime) then Replicate(va<55>, 4) else '0000'; fault.level = 0; constant AddressSize addrtop = AArch64.AddrTop(walkparams.tbid, accdesc.acctype, walkparams.tbi); constant AddressSize pamax = AArch64.PAMax(); if !IsZero(va<addrtop:pamax>) then fault.statuscode = Fault_AddressSize; elsif AArch64.S1HasAlignmentFaultDueToMemType(regime, accdesc, aligned, walkparams.ntlsmd, memattrs) then fault.statuscode = Fault_Alignment; elsif ((accdesc.exclusive || accdesc.atomicop) && !(regime == Regime_EL10 && EL2Enabled() && HCR_EL2.DC == '1') && ConstrainUnpredictableBool(Unpredictable_Atomic_MMU_IMPDEF_FAULT)) then fault.statuscode = Fault_Exclusive; if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN); else ipa = CreateAddressDescriptor(va_in, oa, memattrs, accdesc); ipa.mecid = AArch64.S1DisabledOutputMECID(walkparams, regime, ipa.paddress.paspace); return (fault, ipa);
```

## J1.1.4.55 AArch64.S1Translate

```
// AArch64.S1Translate() // ===================== // Translate VA to IPA/PA depending on the regime (FaultRecord, AddressDescriptor) AArch64.S1Translate(FaultRecord fault_in, Regime regime, bits(64) va, integer size, boolean aligned, AccessDescriptor accdesc) FaultRecord fault = fault_in; // Prepare fault fields in case a fault is detected fault.secondstage = FALSE; fault.s2fs1walk = FALSE; if !AArch64.S1Enabled(regime, accdesc.acctype) then return AArch64.S1DisabledOutput(fault, regime, va, accdesc, aligned); walkparams = AArch64.GetS1TTWParams(regime, accdesc.el, accdesc.ss, va); constant integer s1mintxsz = AArch64.S1MinTxSZ(regime, walkparams); constant integer s1maxtxsz = AArch64.MaxTxSZ(walkparams.tgx); if AArch64.S1TxSZFaults(regime, walkparams) then fault.statuscode = Fault_Translation; fault.level = 0; return (fault, AddressDescriptor UNKNOWN); elsif UInt(walkparams.txsz) < s1mintxsz then walkparams.txsz = s1mintxsz<5:0>; elsif UInt(walkparams.txsz) > s1maxtxsz then walkparams.txsz = s1maxtxsz<5:0>; if AArch64.VAIsOutOfRange(va, accdesc.acctype, regime, walkparams) then fault.statuscode = Fault_Translation; fault.level = 0; return (fault, AddressDescriptor UNKNOWN); if accdesc.el == EL0 && walkparams.e0pd == '1' then fault.statuscode = Fault_Translation; fault.level = 0; return (fault, AddressDescriptor UNKNOWN); if (IsFeatureImplemented(FEAT_SVE) && accdesc.el == EL0 && walkparams.nfd == '1' && ((accdesc.nonfault && accdesc.contiguous) || (accdesc.firstfault && !accdesc.first && !accdesc.contiguous))) then fault.statuscode = Fault_Translation; fault.level = 0; return (fault, AddressDescriptor UNKNOWN); AddressDescriptor descipaddr; TTWState walkstate; bits(128) descriptor; if walkparams.d128 == '1' then (fault, descipaddr, walkstate, descriptor) = AArch64.S1Walk(fault, walkparams, va, regime, accdesc, 128); else (fault, descipaddr, walkstate, descriptor<63:0>) = AArch64.S1Walk(fault, walkparams, va, regime, accdesc, 64); descriptor<127:64> = Zeros(64); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN); if AArch64.S1HasAlignmentFaultDueToMemType(regime, accdesc, aligned, walkparams.ntlsmd, walkstate.memattrs) then fault.statuscode = Fault_Alignment; constant FaultRecord fault_perm = AArch64.S1CheckPermissions(fault, va, size, regime, walkstate, walkparams, accdesc); bits(128) mem_desc;
```

```
bits(128) new_desc = descriptor; if AArch64.SetAccessFlag(walkparams.ha, accdesc, fault) then // Set descriptor AF bit new_desc<10> = '1'; // If HW update of dirty bit is enabled, the walk state permissions // will already reflect a configuration permitting writes. // The update of the descriptor occurs only if the descriptor bits in // memory do not reflect that and the access instigates a write. if AArch64.SetDirtyState(walkparams.hd, (walkparams.pie OR descriptor<51>), accdesc, fault, fault_perm) then // Clear descriptor AP[2]/nDirty bit permitting stage 1 writes new_desc<7> = '0'; if fault.statuscode == Fault_None && fault_perm.statuscode != Fault_None then fault = fault_perm; // Either the access flag was clear or AP[2]/nDirty is set if new_desc != descriptor then AddressDescriptor descpaddr; descaccess = CreateAccDescTTEUpdate(accdesc); if regime == Regime_EL10 && EL2Enabled() then FaultRecord s2fault; s1aarch64 = TRUE; s2aligned = TRUE; (s2fault, descpaddr) = AArch64.S2Translate(fault, descipaddr, s1aarch64, s2aligned, descaccess); if s2fault.statuscode != Fault_None then return (s2fault, AddressDescriptor UNKNOWN); else descpaddr = descipaddr; if walkparams.d128 == '1' then (fault, mem_desc) = AArch64.MemSwapTableDesc(fault, descriptor, new_desc, walkparams.ee, descaccess, descpaddr, 128); else (fault, mem_desc<63:0>) = AArch64.MemSwapTableDesc(fault, descriptor<63:0>, new_desc<63:0>, walkparams.ee, descaccess, descpaddr, 64); mem_desc<127:64> = Zeros(64); if fault.statuscode != Fault_None then if (accdesc.acctype == AccessType_AT && !(boolean IMPLEMENTATION_DEFINED "AT reports the HW update fault")) then // Mask the fault fault.statuscode = Fault_None; else return (fault, AddressDescriptor UNKNOWN); elsif new_desc != descriptor && mem_desc != new_desc then // HW update of Dirty state or AF was not successful due to the descriptor being updated // not matching the descriptor used for translation. Due to this, the walk is restarted. return AArch64.S1Translate(fault_in, regime, va, size, aligned, accdesc); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN); // Output Address oa = StageOA(va, walkparams.d128, walkparams.tgx, walkstate); MemoryAttributes memattrs; if AArch64.S1TreatAsNormalNC(walkstate, regime, accdesc) then // Treat memory attributes as Normal Non-Cacheable memattrs = NormalNCMemAttr(); memattrs.xs = walkstate.memattrs.xs;
```

```
// The effect of SCTLR_ELx.C when '0' is Constrained UNPREDICTABLE on the Tagged attribute // when the memory region is Allocation Tagged. if (IsFeatureImplemented(FEAT_MTE2) && walkstate.memattrs.tags == MemTag_AllocationTagged && ConstrainUnpredictableBool(Unpredictable_S1CTAGGED)) then memattrs.tags = MemTag_AllocationTagged; // SCTLR_ELx.C has no effect on whether the memory region is treated as Canonically Tagged. elsif (IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS) && walkstate.memattrs.tags == MemTag_CanonicallyTagged) then memattrs.tags = MemTag_CanonicallyTagged; else memattrs = walkstate.memattrs; // Shareability value of stage 1 translation subject to stage 2 is IMPLEMENTATION DEFINED // to be either effective value or descriptor value if (regime == Regime_EL10 && EL2Enabled() && HCR_EL2.VM == '1' && !(boolean IMPLEMENTATION_DEFINED "Apply effective shareability at stage 1")) then memattrs.shareability = walkstate.memattrs.shareability; else memattrs.shareability = EffectiveShareability(memattrs); ipa = CreateAddressDescriptor(va, oa, memattrs, accdesc); ipa.s1assured = walkstate.s1assured; varange = AArch64.GetVARange(va); ipa.mecid = AArch64.S1OutputMECID(walkparams, regime, varange, ipa.paddress.paspace, descriptor); if (accdesc.atomicop && !IsWBShareable(memattrs) && ConstrainUnpredictableBool(Unpredictable_Atomic_MMU_IMPDEF_FAULT)) then fault.statuscode = Fault_Exclusive; return (fault, ipa); if accdesc.ls64 && memattrs.memtype == MemType_Normal then if IsFeatureImplemented(FEAT_LS64WB) && !accdesc.withstatus then if (!IsWBShareable(memattrs) && !(memattrs.inner.attrs == MemAttr_NC && memattrs.outer.attrs == MemAttr_NC) && (boolean IMPLEMENTATION_DEFINED "LD64B or ST64B faults to cacheable non-iWBoWB memory")) then fault.statuscode = Fault_Exclusive; return (fault, ipa); elsif !(memattrs.inner.attrs == MemAttr_NC && memattrs.outer.attrs == MemAttr_NC) then fault.statuscode = Fault_Exclusive; return (fault, ipa); return (fault, ipa);
```

## J1.1.4.56 AArch64.S1TreatAsNormalNC

```
// AArch64.S1TreatAsNormalNC() // =========================== // Returns TRUE if stage 1 memory attributes should be treated as Normal Non-Cacheable boolean AArch64.S1TreatAsNormalNC(TTWState walkstate, Regime regime, AccessDescriptor accdesc) return ((accdesc.acctype == AccessType_IFETCH && (walkstate.memattrs.memtype == MemType_Device || !AArch64.S1ICacheEnabled(regime))) || (accdesc.acctype != AccessType_IFETCH && !AArch64.S1DCacheEnabled(regime) && walkstate.memattrs.memtype == MemType_Normal));
```

## J1.1.4.57 AArch64.S2Translate

```
// AArch64.S2Translate() // ===================== // Translate stage 1 IPA to PA and combine memory attributes (FaultRecord, AddressDescriptor) AArch64.S2Translate(FaultRecord fault_in, AddressDescriptor ipa, boolean s1aarch64, boolean aligned, AccessDescriptor accdesc) walkparams = AArch64.GetS2TTWParams(accdesc.ss, ipa.paddress.paspace, s1aarch64); FaultRecord fault = fault_in; boolean s2fs1mro; // Prepare fault fields in case a fault is detected fault.statuscode = Fault_None; // Ignore any faults from stage 1 fault.dirtybit = FALSE; fault.overlay = FALSE; fault.tagaccess = FALSE; fault.s1tagnotdata = FALSE; fault.secondstage = TRUE; fault.s2fs1walk = accdesc.acctype == AccessType_TTW; fault.ipaddress = ipa.paddress; if walkparams.vm != '1' then // Stage 2 translation is disabled return (fault, ipa); constant integer s2mintxsz = AArch64.S2MinTxSZ(walkparams, s1aarch64); constant integer s2maxtxsz = AArch64.MaxTxSZ(walkparams.tgx); if AArch64.S2TxSZFaults(walkparams, s1aarch64) then fault.statuscode = Fault_Translation; fault.level = 0; return (fault, AddressDescriptor UNKNOWN); elsif UInt(walkparams.txsz) < s2mintxsz then walkparams.txsz = s2mintxsz<5:0>; elsif UInt(walkparams.txsz) > s2maxtxsz then walkparams.txsz = s2maxtxsz<5:0>; if (walkparams.d128 == '0' && (AArch64.S2InvalidSL(walkparams) || AArch64.S2InconsistentSL(walkparams))) then fault.statuscode = Fault_Translation; fault.level = 0; return (fault, AddressDescriptor UNKNOWN); if AArch64.IPAIsOutOfRange(ipa.paddress.address, walkparams) then fault.statuscode = Fault_Translation; fault.level = 0; return (fault, AddressDescriptor UNKNOWN); AddressDescriptor descpaddr; TTWState walkstate; bits(128) descriptor; if walkparams.d128 == '1' then (fault, descpaddr, walkstate, descriptor) = AArch64.S2Walk(fault, ipa, walkparams, accdesc, 128); else (fault, descpaddr, walkstate, descriptor<63:0>) = AArch64.S2Walk(fault, ipa, walkparams, accdesc, 64); descriptor<127:64> = Zeros(64); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN); if AArch64.S2HasAlignmentFaultDueToMemType(accdesc, aligned, walkstate.memattrs) then fault.statuscode = Fault_Alignment; FaultRecord fault_perm; (fault_perm, s2fs1mro) = AArch64.S2CheckPermissions(fault, walkstate, walkparams, ipa, accdesc);
```

```
bits(128) mem_desc; bits(128) new_desc = descriptor; if AArch64.SetAccessFlag(walkparams.ha, accdesc, fault) then // Set descriptor AF bit new_desc<10> = '1'; // If HW update of dirty bit is enabled, the walk state permissions // will already reflect a configuration permitting writes. // The update of the descriptor occurs only if the descriptor bits in // memory do not reflect that and the access instigates a write. if AArch64.SetDirtyState(walkparams.hd, (walkparams.s2pie OR descriptor<51>), accdesc, fault, fault_perm) then // Set descriptor S2AP[1]/Dirty bit permitting stage 2 writes new_desc<7> = '1'; if fault.statuscode == Fault_None && fault_perm.statuscode != Fault_None then fault = fault_perm; // Either the access flag was clear or S2AP[1]/Dirty is clear if new_desc != descriptor then if walkparams.hdbss == '1' && descriptor<7> == '0' && new_desc<7> == '1' then fault = AppendToHDBSS(fault, ipa.paddress, accdesc, walkparams, walkstate.level); // If an error, other than a synchronous External abort, occurred on the HDBSS update, // stage 2 hardware update of dirty state is not permitted. if (HDBSSPROD_EL2.FSC != '101000' && (!fault.hdbssf || IsExternalAbort(fault.statuscode))) then constant AccessDescriptor descaccess = CreateAccDescTTEUpdate(accdesc); if walkparams.d128 == '1' then (fault, mem_desc) = AArch64.MemSwapTableDesc(fault, descriptor, new_desc, walkparams.ee, descaccess, descpaddr, 128); else (fault, mem_desc<63:0>) = AArch64.MemSwapTableDesc(fault, descriptor<63:0>, new_desc<63:0>, walkparams.ee, descaccess, descpaddr, 64); mem_desc<127:64> = Zeros(64); if fault.statuscode != Fault_None then if (accdesc.acctype == AccessType_AT && !(boolean IMPLEMENTATION_DEFINED "AT reports the HW update fault")) then // Mask the fault fault.statuscode = Fault_None; else return (fault, AddressDescriptor UNKNOWN); elsif new_desc != descriptor && mem_desc != new_desc then // HW update of Dirty state or AF was not successful due to the descriptor being updated // not matching the descriptor used for translation. Due to this, the walk is restarted. return AArch64.S2Translate(fault_in, ipa, s1aarch64, aligned, accdesc); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN); ipa_64 = ZeroExtend(ipa.paddress.address, 64); // Output Address oa = StageOA(ipa_64, walkparams.d128, walkparams.tgx, walkstate); MemoryAttributes s2_memattrs; if AArch64.S2TreatAsNormalNC(walkstate, walkparams, accdesc) then // Treat memory attributes as Normal Non-Cacheable s2_memattrs = NormalNCMemAttr(); s2_memattrs.xs = walkstate.memattrs.xs; if walkstate.memattrs.tags == MemTag_CanonicallyTagged then
```

```
s2_memattrs.tags = MemTag_CanonicallyTagged; else s2_memattrs = walkstate.memattrs; s2aarch64 = TRUE; MemoryAttributes memattrs; if walkparams.fwb == '0' then memattrs = S2CombineS1MemAttrs(ipa.memattrs, s2_memattrs, s2aarch64); else memattrs = s2_memattrs; pa = CreateAddressDescriptor(ipa.vaddress, oa, memattrs, accdesc); pa.s2fs1mro = s2fs1mro; pa.mecid = AArch64.S2OutputMECID(walkparams, pa.paddress.paspace, descriptor); if (accdesc.atomicop && !IsWBShareable(s2_memattrs) && ConstrainUnpredictableBool(Unpredictable_Atomic_MMU_IMPDEF_FAULT)) then fault.statuscode = Fault_Exclusive; return (fault, pa); if accdesc.ls64 && s2_memattrs.memtype == MemType_Normal then if IsFeatureImplemented(FEAT_LS64WB) && !accdesc.withstatus then if (!IsWBShareable(s2_memattrs) && !(s2_memattrs.inner.attrs == MemAttr_NC && s2_memattrs.outer.attrs == MemAttr_NC) && (boolean IMPLEMENTATION_DEFINED "LD64B or ST64B faults to cacheable non-iWBoWB memory")) then fault.statuscode = Fault_Exclusive; return (fault, ipa); elsif !(s2_memattrs.inner.attrs == MemAttr_NC && s2_memattrs.outer.attrs == MemAttr_NC) then fault.statuscode = Fault_Exclusive; return (fault, ipa); return (fault, pa);
```

```
J1.1.4.58 AArch64.S2TreatAsNormalNC // AArch64.S2TreatAsNormalNC() // =========================== // Returns TRUE if stage 2 memory attributes should be treated as Normal Non-cacheable boolean AArch64.S2TreatAsNormalNC(TTWState walkstate, S2TTWParams walkparams, AccessDescriptor accdesc) return ((accdesc.acctype == AccessType_TTW && walkstate.memattrs.memtype == MemType_Device && walkparams.ptw == '0') || (accdesc.acctype == AccessType_IFETCH && (walkstate.memattrs.memtype == MemType_Device || HCR_EL2.ID == '1')) || (accdesc.acctype != AccessType_IFETCH && walkstate.memattrs.memtype == MemType_Normal && !S2DCacheEnabled())); J1.1.4.59 AArch64.SetAccessFlag // AArch64.SetAccessFlag() // ======================= // Determine whether the access flag could be set by HW given the fault status boolean AArch64.SetAccessFlag(bit ha, AccessDescriptor accdesc, FaultRecord fault) if ha == '0' || !AArch64.SettingAccessFlagPermitted(fault) then return FALSE; elsif accdesc.acctype == AccessType_AT then return boolean IMPLEMENTATION_DEFINED "AT updates AF"; elsif accdesc.acctype IN {AccessType_DC, AccessType_IC} then return boolean IMPLEMENTATION_DEFINED "Generate access flag fault on IC/DC operations";
```

```
else // Set descriptor AF bit return TRUE;
```

## J1.1.4.60 AArch64.SetDirtyState

```
// AArch64.SetDirtyState() // ======================= // Determine whether dirty state is required to be updated by HW given the fault status boolean AArch64.SetDirtyState(bits(1) hd, bits(1) dbm, AccessDescriptor accdesc, FaultRecord fault, FaultRecord fault_perm) if hd == '0' then return FALSE; elsif !AArch64.SettingDirtyStatePermitted(fault, fault_perm) then return FALSE; elsif accdesc.acctype IN {AccessType_AT, AccessType_IC, AccessType_DC} then return FALSE; elsif !accdesc.write then return FALSE; else return dbm == '1';
```

## J1.1.4.61 AArch64.SettingAccessFlagPermitted

```
// AArch64.SettingAccessFlagPermitted() // ==================================== // Determine whether the access flag could be set by HW given the fault status boolean AArch64.SettingAccessFlagPermitted(FaultRecord fault) if fault.statuscode == Fault_None then return TRUE; elsif fault.statuscode IN {Fault_Alignment, Fault_Permission} then return ConstrainUnpredictableBool(Unpredictable_AFUPDATE); else return FALSE;
```

## J1.1.4.62 AArch64.SettingDirtyStatePermitted

```
// AArch64.SettingDirtyStatePermitted() // ==================================== // Determine whether the dirty state could be set by HW given the fault status boolean AArch64.SettingDirtyStatePermitted(FaultRecord fault, FaultRecord fault_perm) if fault_perm.statuscode != Fault_None then return FALSE; elsif fault.statuscode == Fault_None then return TRUE; elsif fault.statuscode == Fault_Alignment then return ConstrainUnpredictableBool(Unpredictable_DBUPDATE); else return FALSE;
```

## J1.1.4.63 AArch64.TranslateAddress

```
// AArch64.TranslateAddress() // ========================== // Main entry point for translating an address AddressDescriptor AArch64.TranslateAddress(bits(64) va, AccessDescriptor
```

accdesc,

```
boolean aligned, integer size) if (SPESampleInFlight && !(accdesc.acctype IN {AccessType_IFETCH, AccessType_SPE, AccessType_TRBE})) then SPEStartCounter(SPECounterPosTranslationLatency); AddressDescriptor result = AArch64.FullTranslate(va, size, accdesc, aligned); if !IsFault(result) && accdesc.acctype != AccessType_IFETCH then // For an instruction fetch, CheckDebug will be called // after the instruction is read from memory result.fault = AArch64.CheckDebug(va, accdesc, size); if (IsFeatureImplemented(FEAT_RME) && !IsFault(result) && IsGranuleProtectionCheckedAccess(accdesc)) then result.fault.gpcf = GranuleProtectionCheck(result, accdesc); if result.fault.gpcf.gpf != GPCF_None then result.fault.statuscode = Fault_GPCFOnOutput; result.fault.paddress = result.paddress; result.fault.vaddress = result.vaddress; if SPESampleInFlight && !(accdesc.acctype IN {AccessType_IFETCH, AccessType_TRBE, AccessType_SPE}) then SPEStopCounter(SPECounterPosTranslationLatency); // Update virtual address for abort functions result.vaddress = ZeroExtend(va, 64); return result; J1.1.4.64 AArch64.TranslateTagAddress // AArch64.TranslateTagAddress() // ============================= // Translate an address for accessing an Allocation Tag. (MemTagType, AddressDescriptor) AArch64.TranslateTagAddress(bits(64) va, AccessDescriptor accdesc_in, boolean aligned, integer size) AccessDescriptor accdesc = accdesc_in; constant AddressDescriptor taddrdesc = AArch64.TranslateAddress(va, accdesc, aligned, size); return (taddrdesc.memattrs.tags, taddrdesc); J1.1.4.65 AArch64.BlockDescSupported // AArch64.BlockDescSupported() // ============================ // Determine whether a block descriptor is valid for the given granule size // and level boolean AArch64.BlockDescSupported(bit d128, bit ds, TGx tgx, integer level) case tgx of when TGx_4KB return ((level == 0 && (ds == '1' || d128 == '1')) || level == 1 || level == 2); when TGx_16KB return ((level == 1 && (ds == '1' || d128 == '1')) || level == 2); when TGx_64KB return ((level == 1 && (d128 == '1' || AArch64.PAMax() >= 52)) || level == 2); return FALSE;
```

## J1.1.4.66 AArch64.ContiguousBit

```
// AArch64.ContiguousBit() // ======================= // Get the value of the contiguous bit bit AArch64.ContiguousBit(TGx tgx, bit d128, integer level, bits(N) descriptor) if boolean IMPLEMENTATION_DEFINED "Treat Contiguous bit as 0" then return '0'; if d128 == '1' then if (tgx == TGx_64KB && level == 1) || (tgx == TGx_4KB && level == 0) return '0'; // RES0 else return descriptor<111>; // When using TGx 64KB then the Contiguous bit is RES0 for Block // descriptors at level 1. For VMSAv8-64, level 1 Block descriptors // can exist only if FEAT_LPA is implemented. if tgx == TGx_64KB && level == 1 then return '0'; // RES0 // When the Effective value of TCR_ELx.DS is '1', // the Contiguous bit is RES0 for all the following: // * For TGx 4KB, Block descriptors at level 0 // * For TGx 16KB, Block descriptors at level 1 // For VMSAv8-64, the above Block descriptors at the specified // levels can exist only if the Effective value of TCR_ELx.DS is 1. if tgx == TGx_16KB && level == 1 then return '0'; // RES0 if tgx == TGx_4KB && level == 0 then return '0'; // RES0 return descriptor<52>;
```

```
then J1.1.4.67 AArch64.DecodeDescriptorType // AArch64.DecodeDescriptorType() // ============================== // Determine whether the descriptor is a page, block or table DescriptorType AArch64.DecodeDescriptorType(bits(N) descriptor, bit d128, bit ds, TGx tgx, integer level) if descriptor<0> == '0' then return DescriptorType_Invalid; elsif d128 == '1' then constant bits(2) skl = descriptor<110:109>; if tgx IN {TGx_16KB, TGx_64KB} && UInt(skl) == 3 then return DescriptorType_Invalid; constant integer effective_level = level + UInt(skl); if effective_level > FINAL_LEVEL then return DescriptorType_Invalid; elsif effective_level == FINAL_LEVEL then return DescriptorType_Leaf; else return DescriptorType_Table; else if descriptor<1> == '1' then if level == FINAL_LEVEL then return DescriptorType_Leaf; else
```

```
return DescriptorType_Table; elsif descriptor<1> == '0' then if AArch64.BlockDescSupported(d128, ds, tgx, level) then return DescriptorType_Leaf; else return DescriptorType_Invalid; Unreachable();
```

## J1.1.4.68 AArch64.S1ApplyOutputPerms

```
// AArch64.S1ApplyOutputPerms() // ============================ // Apply output permissions encoded in stage 1 page/block descriptors Permissions AArch64.S1ApplyOutputPerms(Permissions permissions_in, bits(N) descriptor, Regime regime, S1TTWParams walkparams) Permissions permissions = permissions_in; bits (4) pi_index; if walkparams.pie == '1' then if walkparams.d128 == '1' then pi_index = descriptor<118:115>; else pi_index = descriptor<54:53>:descriptor<51>:descriptor<6>; permissions.ppi = Elem[walkparams.pir, UInt(pi_index), 4]; permissions.upi = Elem[walkparams.pire0, UInt(pi_index), 4]; permissions.ndirty = descriptor<7>; else if regime == Regime_EL10 && EL2Enabled() && walkparams.nv1 == '1' then permissions.ap<2:1> = descriptor<7>:'0'; permissions.pxn = descriptor<54>; elsif HasUnprivileged(regime) then permissions.ap<2:1> = descriptor<7:6>; permissions.uxn = descriptor<54>; permissions.pxn = descriptor<53>; else permissions.ap<2:1> = descriptor<7>:'1'; permissions.xn = descriptor<54>; permissions.dbm = descriptor<51>; if IsFeatureImplemented(FEAT_S1POE) then if walkparams.d128 == '1' then permissions.po_index<3:0> = descriptor<124:121>; else permissions.po_index<3:0> = '0':descriptor<62:60>; return permissions;
```

## J1.1.4.69 AArch64.S1ApplyTablePerms

```
// AArch64.S1ApplyTablePerms() // =========================== // Apply hierarchical permissions encoded in stage 1 table descriptors Permissions AArch64.S1ApplyTablePerms(Permissions permissions_in, bits(64) descriptor, Regime regime, S1TTWParams walkparams) Permissions permissions = permissions_in; bits(2) ap_table; bit pxn_table; bit uxn_table; bit xn_table; if regime == Regime_EL10 && EL2Enabled() && walkparams.nv1 == '1' then ap_table = descriptor<62>:'0'; pxn_table = descriptor<60>;
```

```
permissions.ap_table = permissions.ap_table OR ap_table; permissions.pxn_table = permissions.pxn_table OR pxn_table; elsif HasUnprivileged(regime) then ap_table = descriptor<62:61>; uxn_table = descriptor<60>; pxn_table = descriptor<59>; permissions.ap_table = permissions.ap_table OR ap_table; permissions.uxn_table = permissions.uxn_table OR uxn_table; permissions.pxn_table = permissions.pxn_table OR pxn_table; else ap_table = descriptor<62>:'0'; xn_table = descriptor<60>; permissions.ap_table = permissions.ap_table OR ap_table; permissions.xn_table = permissions.xn_table OR xn_table; return permissions;
```

## J1.1.4.70 AArch64.S2ApplyOutputPerms

```
// AArch64.S2ApplyOutputPerms() // ============================ // Apply output permissions encoded in stage 2 page/block descriptors Permissions AArch64.S2ApplyOutputPerms(bits(N) descriptor, S2TTWParams walkparams) Permissions permissions; bits(4) s2pi_index; if walkparams.s2pie == '1' then if walkparams.d128 == '1' then s2pi_index = descriptor<118:115>; else s2pi_index = descriptor<54:53,51,6>; permissions.s2pi = Elem[walkparams.s2pir, UInt(s2pi_index), 4]; permissions.s2dirty = descriptor<7>; else permissions.s2ap = descriptor<7:6>; if walkparams.d128 == '1' then permissions.s2xn = descriptor<118>; else permissions.s2xn = descriptor<54>; if IsFeatureImplemented(FEAT_XNX) then if walkparams.d128 == '1' then permissions.s2xnx = descriptor<117>; else permissions.s2xnx = descriptor<53>; else permissions.s2xnx = '0'; permissions.dbm = descriptor<51>; if IsFeatureImplemented(FEAT_S2POE) then if walkparams.d128 == '1' then permissions.s2po_index = descriptor<124:121>; else permissions.s2po_index = descriptor<62:59>; return permissions;
```

## J1.1.4.71 AArch64.nTFaults

```
// AArch64.nTFaults() // ================== // Identify whether the nT bit in a block or table descriptor is effectively set // causing a translation fault
```

```
boolean AArch64.nTFaults(bit d128, bits(N) descriptor) if !IsFeatureImplemented(FEAT_BBML1) then return FALSE; constant bit nT = if d128 == '1' then descriptor<6> else descriptor<16>; return nT == '1' && boolean IMPLEMENTATION_DEFINED "nT bit causes Translation Fault";
```

## J1.1.4.72 AArch64.S1InitialTTWState

```
// AArch64.S1InitialTTWState() // =========================== // Set properties of first access to translation tables in stage 1 TTWState AArch64.S1InitialTTWState(S1TTWParams walkparams, bits(64) va, Regime regime, SecurityState ss) TTWState walkstate; FullAddress tablebase; Permissions permissions; bits(128) ttbr; ttbr = AArch64.S1TTBR(regime, va); case ss of when SS_Secure tablebase.paspace = PAS_Secure; when SS_NonSecure tablebase.paspace = PAS_NonSecure; when SS_Root tablebase.paspace = PAS_Root; when SS_Realm tablebase.paspace = PAS_Realm; tablebase.address = AArch64.S1TTBaseAddress(walkparams, regime, ttbr); permissions.ap_table = '00'; if HasUnprivileged(regime) then permissions.uxn_table = '0'; permissions.pxn_table = '0'; else permissions.xn_table = '0'; walkstate.baseaddress = tablebase; walkstate.level = AArch64.S1StartLevel(walkparams); walkstate.istable = TRUE; // In regimes that support global and non-global translations, translation // table entries from lookup levels other than the final level of lookup // are treated as being non-global walkstate.nG = if HasUnprivileged(regime) then '1' else '0'; walkstate.memattrs = WalkMemAttrs(walkparams.sh, walkparams.irgn, walkparams.orgn); walkstate.permissions = permissions; if regime == Regime_EL10 && EL2Enabled() && HCR_EL2.VM == '1' then if ((AArch64.GetVARange(va) == VARange_LOWER && VTCR_EL2.TL0 == '1') || (AArch64.GetVARange(va) == VARange_UPPER && VTCR_EL2.TL1 == '1')) then walkstate.s1assured = TRUE; else walkstate.s1assured = FALSE; else walkstate.s1assured = FALSE; walkstate.disch = walkparams.disch; return walkstate;
```

## J1.1.4.73 AArch64.S1NextWalkStateLeaf

```
// AArch64.S1NextWalkStateLeaf() // ============================= // Decode stage 1 page or block descriptor as output to this stage of translation
```

```
TTWState AArch64.S1NextWalkStateLeaf(TTWState currentstate, boolean s2fs1mro, Regime regime, AccessDescriptor accdesc, S1TTWParams walkparams, bits(N) descriptor) TTWState nextstate; FullAddress baseaddress; baseaddress.address = AArch64.S1LeafBase(descriptor, walkparams, currentstate.level); if currentstate.baseaddress.paspace == PAS_Secure then // Determine PA space of the block from NS bit constant bit ns = if walkparams.d128 == '1' then descriptor<127> else descriptor<5>; baseaddress.paspace = if ns == '0' then PAS_Secure else PAS_NonSecure; elsif currentstate.baseaddress.paspace == PAS_Root then // Determine PA space of the block from NSE and NS bits constant bit ns = if walkparams.d128 == '1' then descriptor<127> else descriptor<5>; constant bit nse = descriptor<11>; constant bit nse2 = '0'; // NSE2 has the Effective value of 0 within a PE. baseaddress.paspace = DecodePASpace(nse2, nse, ns); // If Secure state is not implemented, but RME is, // force Secure space accesses to Non-secure space if baseaddress.paspace == PAS_Secure && !HaveSecureState() then baseaddress.paspace = PAS_NonSecure; elsif (currentstate.baseaddress.paspace == PAS_Realm && regime IN {Regime_EL2, Regime_EL20}) then // Realm EL2 and EL2&0 regimes have a stage 1 NS bit constant bit ns = if walkparams.d128 == '1' then descriptor<127> else descriptor<5>; baseaddress.paspace = if ns == '0' then PAS_Realm else PAS_NonSecure; elsif currentstate.baseaddress.paspace == PAS_Realm then // Realm EL1&0 regime does not have a stage 1 NS bit baseaddress.paspace = PAS_Realm; else baseaddress.paspace = PAS_NonSecure; nextstate.istable = FALSE; nextstate.level = currentstate.level; nextstate.baseaddress = baseaddress; bits(4) attrindx; if walkparams.aie == '1' then if walkparams.d128 == '1' then attrindx = descriptor<5:2>; else attrindx = descriptor<59,4:2>; else attrindx = '0':descriptor<4:2>; bits(2) sh; if walkparams.d128 == '1' then sh = descriptor<9:8>; elsif walkparams.ds == '1' then sh = walkparams.sh; else sh = descriptor<9:8>; attr = AArch64.MAIRAttr(UInt(attrindx), walkparams.mair2, walkparams.mair); s1aarch64 = TRUE; nextstate.memattrs = S1DecodeMemAttrs(attr, sh, s1aarch64, walkparams, accdesc.acctype); nextstate.permissions = AArch64.S1ApplyOutputPerms(currentstate.permissions, descriptor, regime, walkparams); bit protectedbit; if walkparams.d128 == '1' then protectedbit = descriptor<114>; else protectedbit = if walkparams.pnch == '1' then descriptor<52> else '0';
```

```
if (currentstate.s1assured && s2fs1mro && protectedbit == '1') then nextstate.s1assured = TRUE; else nextstate.s1assured = FALSE; if walkparams.pnch == '1' || currentstate.disch == '1' then nextstate.contiguous = '0'; else nextstate.contiguous = AArch64.ContiguousBit(walkparams.tgx, walkparams.d128, currentstate.level, descriptor); if !HasUnprivileged(regime) then nextstate.nG = '0'; elsif accdesc.ss == SS_Secure && currentstate.baseaddress.paspace == PAS_NonSecure then // In Secure state, a translation must be treated as non-global, // regardless of the value of the nG bit, // if NSTable is set to 1 at any level of the translation table walk nextstate.nG = '1'; elsif walkparams.fng == '1' then // Translations are treated as non-global regardless of the value of the nG bit. nextstate.nG = '1'; elsif (regime == Regime_EL10 && EL2Enabled() && HCR_EL2.VM == '1' && (walkparams.d128 == '1' || walkparams.pnch == '1') && !nextstate.s1assured && walkparams.fngna == '1') then // Translations are treated as non-global regardless of the value of the nG bit. nextstate.nG = '1'; else nextstate.nG = descriptor<11>; if walkparams.d128 == '1' then nextstate.guardedpage = descriptor<113>; else nextstate.guardedpage = descriptor<50>; return nextstate;
```

```
J1.1.4.74 AArch64.S1NextWalkStateTable walkparams.ds,
```

```
// AArch64.S1NextWalkStateTable() // ============================== // Decode stage 1 table descriptor to transition to the next level TTWState AArch64.S1NextWalkStateTable(TTWState currentstate, boolean s2fs1mro, Regime regime, S1TTWParams walkparams, bits(N) descriptor) TTWState nextstate; FullAddress tablebase; constant bits(2) skl = if walkparams.d128 == '1' then descriptor<110:109> else '00'; tablebase.address = AArch64.NextTableBase(descriptor, walkparams.d128, skl, walkparams.tgx); if currentstate.baseaddress.paspace == PAS_Secure then // Determine PA space of the next table from NSTable bit bit nstable; nstable = if walkparams.d128 == '1' then descriptor<127> else descriptor<63>; tablebase.paspace = if nstable == '0' then PAS_Secure else PAS_NonSecure; else // Otherwise bit 63 is RES0 and there is no NSTable bit tablebase.paspace = currentstate.baseaddress.paspace; nextstate.istable = TRUE; nextstate.nG = currentstate.nG; if walkparams.d128 == '1' then nextstate.level = currentstate.level + UInt(skl) + 1; else nextstate.level = currentstate.level + 1; nextstate.baseaddress = tablebase;
```

```
nextstate.memattrs = currentstate.memattrs; if walkparams.hpd == '0' && walkparams.pie == '0' then nextstate.permissions = AArch64.S1ApplyTablePerms(currentstate.permissions, descriptor<63:0>, regime, walkparams); else nextstate.permissions = currentstate.permissions; bit protectedbit; if walkparams.d128 == '1' then protectedbit = descriptor<114>; else protectedbit = if walkparams.pnch == '1' then descriptor<52> else '0'; if (currentstate.s1assured && s2fs1mro && protectedbit == '1') then nextstate.s1assured = TRUE; else nextstate.s1assured = FALSE; nextstate.disch = if walkparams.d128 == '1' then descriptor<112> else '0'; return nextstate;
```

## J1.1.4.75 AArch64.S1Walk

```
// AArch64.S1Walk() // ================ // Traverse stage 1 translation tables obtaining the final descriptor // as well as the address leading to that descriptor (FaultRecord, AddressDescriptor, TTWState, bits(N)) AArch64.S1Walk(FaultRecord fault_in, S1TTWParams walkparams, bits(64) va, Regime regime, AccessDescriptor accdesc, integer N) FaultRecord fault = fault_in; boolean aligned; if HasUnprivileged(regime) && AArch64.S1EPD(regime, va) == '1' then fault.statuscode = Fault_Translation; fault.level = 0; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); walkstate = AArch64.S1InitialTTWState(walkparams, va, regime, accdesc.ss); constant integer startlevel = walkstate.level; if startlevel > 3 then fault.statuscode = Fault_Translation; fault.level = 0; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); bits(N) descriptor; AddressDescriptor walkaddress; bits(2) skl = '00'; walkaddress.vaddress = va; walkaddress.mecid = AArch64.S1TTWalkMECID(walkparams.emec, regime, accdesc.ss); if !AArch64.S1DCacheEnabled(regime) then walkaddress.memattrs = NormalNCMemAttr(); walkaddress.memattrs.xs = walkstate.memattrs.xs; else walkaddress.memattrs = walkstate.memattrs; // Shareability value of stage 1 translation subject to stage 2 is IMPLEMENTATION DEFINED // to be either effective value or descriptor value if (regime == Regime_EL10 && EL2Enabled() && HCR_EL2.VM == '1' && !(boolean IMPLEMENTATION_DEFINED "Apply effective shareability at stage 1")) then walkaddress.memattrs.shareability = walkstate.memattrs.shareability; else
```

```
walkaddress.memattrs.shareability = EffectiveShareability(walkaddress.memattrs); boolean s2fs1mro = FALSE; DescriptorType desctype; FullAddress descaddress = AArch64.S1SLTTEntryAddress(walkstate.level, walkparams, va, walkstate.baseaddress); // Detect Address Size Fault by Descriptor Address if AArch64.S1OAOutOfRange(descaddress.address, walkparams) then fault.statuscode = Fault_AddressSize; fault.level = 0; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); repeat fault.level = walkstate.level; walkaddress.paddress = descaddress; walkaddress.s1assured = walkstate.s1assured; constant boolean toplevel = walkstate.level == startlevel; constant VARange varange = AArch64.GetVARange(va); constant AccessDescriptor walkaccess = CreateAccDescS1TTW(toplevel, varange, accdesc); FaultRecord s2fault; AddressDescriptor s2walkaddress; if regime == Regime_EL10 && EL2Enabled() then constant boolean s1aarch64 = TRUE; aligned = TRUE; (s2fault, s2walkaddress) = AArch64.S2Translate(fault, walkaddress, s1aarch64, aligned, walkaccess); if s2fault.statuscode != Fault_None then return (s2fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); s2fs1mro = s2walkaddress.s2fs1mro; (fault, descriptor) = FetchDescriptor(walkparams.ee, s2walkaddress, walkaccess, fault, N); else (fault, descriptor) = FetchDescriptor(walkparams.ee, walkaddress, walkaccess, fault, N); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); bits(N) new_descriptor; repeat new_descriptor = descriptor; desctype = AArch64.DecodeDescriptorType(descriptor, walkparams.d128, walkparams.ds, walkparams.tgx, walkstate.level); case desctype of when DescriptorType_Table walkstate = AArch64.S1NextWalkStateTable(walkstate, s2fs1mro, regime, walkparams, descriptor); skl = if walkparams.d128 == '1' then descriptor<110:109> else '00'; descaddress = AArch64.S1TTEntryAddress(walkstate.level, walkparams, skl, va, walkstate.baseaddress, descriptor); // Detect Address Size Fault by Descriptor Address if AArch64.S1OAOutOfRange(descaddress.address, walkparams) then fault.statuscode = Fault_AddressSize; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); if walkparams.haft == '1' then new_descriptor<10> = '1';
```

```
if (walkparams.d128 == '1' && skl != '00' && AArch64.nTFaults(walkparams.d128, descriptor)) then fault.statuscode = Fault_Translation; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); when DescriptorType_Leaf walkstate = AArch64.S1NextWalkStateLeaf(walkstate, s2fs1mro, regime, accdesc, walkparams, descriptor); when DescriptorType_Invalid fault.statuscode = Fault_Translation; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); otherwise Unreachable(); if new_descriptor != descriptor then AddressDescriptor descpaddr; constant AccessDescriptor descaccess = CreateAccDescTTEUpdate(accdesc); if regime == Regime_EL10 && EL2Enabled() then constant boolean s1aarch64 = TRUE; aligned = TRUE; (s2fault, descpaddr) = AArch64.S2Translate(fault, walkaddress, s1aarch64, aligned, descaccess); if s2fault.statuscode != Fault_None then return (s2fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); else descpaddr = walkaddress; (fault, descriptor) = AArch64.MemSwapTableDesc(fault, descriptor, new_descriptor, walkparams.ee, descaccess, descpaddr, N); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); until new_descriptor == descriptor; until desctype == DescriptorType_Leaf; constant FullAddress oa = StageOA(va, walkparams.d128, walkparams.tgx, walkstate); if (walkstate.contiguous == '1' && AArch64.ContiguousBitFaults(walkparams.d128, walkparams.txsz, walkparams.tgx, walkstate.level)) then fault.statuscode = Fault_Translation; elsif walkstate.level < FINAL_LEVEL && AArch64.nTFaults(walkparams.d128, descriptor) then fault.statuscode = Fault_Translation; elsif AArch64.S1AMECFault(walkparams, walkstate.baseaddress.paspace, regime, descriptor) then fault.statuscode = Fault_Translation; // Detect Address Size Fault by final output elsif AArch64.S1OAOutOfRange(oa.address, walkparams) then fault.statuscode = Fault_AddressSize; // Check descriptor AF bit elsif (descriptor<10> == '0' && walkparams.ha == '0' && (!accdesc.acctype IN {AccessType_DC, AccessType_IC} || boolean IMPLEMENTATION_DEFINED "Generate access flag fault on IC/DC operations")) then fault.statuscode = Fault_AccessFlag; if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); return (fault, walkaddress, walkstate, descriptor);
```

## J1.1.4.76 AArch64.S2InitialTTWState

```
// AArch64.S2InitialTTWState() // =========================== // Set properties of first access to translation tables in stage 2 TTWState AArch64.S2InitialTTWState(SecurityState ss, S2TTWParams walkparams) TTWState walkstate; FullAddress tablebase; bits(128) ttbr; ttbr = ZeroExtend(VTTBR_EL2, 128); case ss of when SS_NonSecure tablebase.paspace = PAS_NonSecure; when SS_Realm tablebase.paspace = PAS_Realm; tablebase.address = AArch64.S2TTBaseAddress(walkparams, tablebase.paspace, ttbr); walkstate.baseaddress = tablebase; walkstate.level = AArch64.S2StartLevel(walkparams); walkstate.istable = TRUE; walkstate.memattrs = WalkMemAttrs(walkparams.sh, walkparams.irgn, walkparams.orgn); return walkstate; J1.1.4.77 AArch64.S2NextWalkStateLeaf walkparams, descriptor);
```

```
// AArch64.S2NextWalkStateLeaf() // ============================= // Decode stage 2 page or block descriptor as output to this stage of translation TTWState AArch64.S2NextWalkStateLeaf(TTWState currentstate, SecurityState ss, S2TTWParams walkparams, AddressDescriptor ipa, bits(N) descriptor) TTWState nextstate; FullAddress baseaddress; if ss == SS_Secure then baseaddress.paspace = AArch64.SS2OutputPASpace(walkparams, ipa.paddress.paspace); elsif ss == SS_Realm then bit ns; ns = if walkparams.d128 == '1' then descriptor<127> else descriptor<55>; baseaddress.paspace = if ns == '1' then PAS_NonSecure else PAS_Realm; else baseaddress.paspace = PAS_NonSecure; baseaddress.address = AArch64.S2LeafBase(descriptor, walkparams, currentstate.level); nextstate.istable = FALSE; nextstate.level = currentstate.level; nextstate.baseaddress = baseaddress; nextstate.permissions = AArch64.S2ApplyOutputPerms(descriptor, walkparams); s2_attr = descriptor<5:2>; s2_sh = if walkparams.ds == '1' then walkparams.sh else descriptor<9:8>; s2_fnxs = descriptor<11>; if walkparams.fwb == '1' then nextstate.memattrs = AArch64.S2ApplyFWBMemAttrs(ipa.memattrs, if s2_attr<3:1> == '111' then nextstate.permissions.s2tag_na = '1'; else nextstate.permissions.s2tag_na = '0'; else s2aarch64 = TRUE; nextstate.memattrs = S2DecodeMemAttrs(s2_attr, s2_sh, s2aarch64); // FnXS is used later to mask the XS value from stage 1 nextstate.memattrs.xs = NOT s2_fnxs;
```

```
if s2_attr == '0100' then nextstate.permissions.s2tag_na = '1'; else nextstate.permissions.s2tag_na = '0'; nextstate.contiguous = AArch64.ContiguousBit(walkparams.tgx, walkparams.d128, currentstate.level, descriptor); if walkparams.d128 == '1' then nextstate.s2assuredonly = descriptor<114>; else nextstate.s2assuredonly = if walkparams.assuredonly == '1' then descriptor<58> else return nextstate;
```

```
// AArch64.S2Walk() // ================ // Traverse stage 2 translation tables obtaining the final descriptor // as well as the address leading to that descriptor (FaultRecord, AddressDescriptor, TTWState, bits(N)) AArch64.S2Walk(FaultRecord fault_in, AddressDescriptor ipa, S2TTWParams walkparams, AccessDescriptor integer N) FaultRecord fault = fault_in; ipa_64 = ZeroExtend(ipa.paddress.address, 64); TTWState walkstate; if accdesc.ss == SS_Secure then walkstate = AArch64.SS2InitialTTWState(walkparams, ipa.paddress.paspace); else walkstate = AArch64.S2InitialTTWState(accdesc.ss, walkparams); constant integer startlevel = walkstate.level; if startlevel > 3 then
```

```
'0'; J1.1.4.78 AArch64.S2NextWalkStateTable // AArch64.S2NextWalkStateTable() // ============================== // Decode stage 2 table descriptor to transition to the next level TTWState AArch64.S2NextWalkStateTable(TTWState currentstate, S2TTWParams walkparams, bits(N) descriptor) TTWState nextstate; FullAddress tablebase; constant bits(2) skl = if walkparams.d128 == '1' then descriptor<110:109> else '00'; tablebase.address = AArch64.NextTableBase(descriptor, walkparams.d128, skl, walkparams.ds, walkparams.tgx); tablebase.paspace = currentstate.baseaddress.paspace; nextstate.istable = TRUE; if walkparams.d128 == '1' then nextstate.level = currentstate.level + UInt(skl) + 1; else nextstate.level = currentstate.level + 1; nextstate.baseaddress = tablebase; nextstate.memattrs = currentstate.memattrs; return nextstate; J1.1.4.79 AArch64.S2Walk accdesc,
```

```
fault.statuscode = Fault_Translation; fault.level = 0; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); bits(N) descriptor; constant AccessDescriptor walkaccess = CreateAccDescS2TTW(accdesc); AddressDescriptor walkaddress; bits(2) skl = '00'; walkaddress.vaddress = ipa.vaddress; walkaddress.mecid = AArch64.S2TTWalkMECID(walkparams.emec, accdesc.ss); if !S2DCacheEnabled() then walkaddress.memattrs = NormalNCMemAttr(); walkaddress.memattrs.xs = walkstate.memattrs.xs; else walkaddress.memattrs = walkstate.memattrs; walkaddress.memattrs.shareability = EffectiveShareability(walkaddress.memattrs); DescriptorType desctype; // Initial lookup might index into concatenated tables FullAddress descaddress = AArch64.S2SLTTEntryAddress(walkparams, ipa.paddress.address, walkstate.baseaddress); // Detect Address Size Fault by Descriptor Address if AArch64.S2OAOutOfRange(descaddress.address, walkparams) then fault.statuscode = Fault_AddressSize; fault.level = 0; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); repeat fault.level = walkstate.level; walkaddress.paddress = descaddress; (fault, descriptor) = FetchDescriptor(walkparams.ee, walkaddress, walkaccess, fault, N); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); bits(N) new_descriptor; repeat new_descriptor = descriptor; desctype = AArch64.DecodeDescriptorType(descriptor, walkparams.d128, walkparams.ds, walkparams.tgx, walkstate.level); case desctype of when DescriptorType_Table walkstate = AArch64.S2NextWalkStateTable(walkstate, walkparams, descriptor); skl = if walkparams.d128 == '1' then descriptor<110:109> else '00'; descaddress = AArch64.S2TTEntryAddress(walkstate.level, walkparams, skl, ipa.paddress.address, walkstate.baseaddress); // Detect Address Size Fault by table descriptor if AArch64.S2OAOutOfRange(descaddress.address, walkparams) then fault.statuscode = Fault_AddressSize; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); if walkparams.haft == '1' then new_descriptor<10> = '1'; if (walkparams.d128 == '1' && skl != '00' && AArch64.nTFaults(walkparams.d128, descriptor)) then fault.statuscode = Fault_Translation; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN,
```

```
when DescriptorType_Leaf walkstate = AArch64.S2NextWalkStateLeaf(walkstate, accdesc.ss, walkparams, ipa, descriptor); when DescriptorType_Invalid fault.statuscode = Fault_Translation; return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); otherwise Unreachable(); if new_descriptor != descriptor then constant AccessDescriptor descaccess = CreateAccDescTTEUpdate(accdesc); (fault, descriptor) = AArch64.MemSwapTableDesc(fault, descriptor, new_descriptor, walkparams.ee, descaccess, walkaddress, N); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN, TTWState UNKNOWN, bits(N) UNKNOWN); until new_descriptor == descriptor; until desctype == DescriptorType_Leaf; constant FullAddress oa = StageOA(ipa_64, walkparams.d128, walkparams.tgx, walkstate); if (walkstate.contiguous == '1' && AArch64.ContiguousBitFaults(walkparams.d128, walkparams.txsz, walkparams.tgx, walkstate.level)) then fault.statuscode = Fault_Translation; elsif walkstate.level < FINAL_LEVEL && AArch64.nTFaults(walkparams.d128, descriptor) then fault.statuscode = Fault_Translation; // Detect Address Size Fault by final output elsif AArch64.S2OAOutOfRange(oa.address, walkparams) then fault.statuscode = Fault_AddressSize; // Check descriptor AF bit elsif (descriptor<10> == '0' && walkparams.ha == '0' && (!accdesc.acctype IN {AccessType_DC, AccessType_IC} || boolean IMPLEMENTATION_DEFINED "Generate access flag fault on IC/DC operations")) then fault.statuscode = Fault_AccessFlag; return (fault, walkaddress, walkstate, descriptor);
```

```
// AArch64.SS2InitialTTWState() // ============================ // Set properties of first access to translation tables in Secure stage 2 TTWState AArch64.SS2InitialTTWState(S2TTWParams walkparams, PASpace TTWState walkstate; FullAddress tablebase; bits(128) ttbr; if ipaspace == PAS_Secure then ttbr = ZeroExtend(VSTTBR_EL2, 128); else ttbr = ZeroExtend(VTTBR_EL2, 128); if ipaspace == PAS_Secure then if walkparams.sw == '0' then tablebase.paspace = PAS_Secure; else tablebase.paspace = PAS_NonSecure; else if walkparams.nsw == '0' then tablebase.paspace = PAS_Secure; else
```

```
bits(N) UNKNOWN); J1.1.4.80 AArch64.SS2InitialTTWState ipaspace)
```

```
tablebase.paspace = PAS_NonSecure; tablebase.address = AArch64.S2TTBaseAddress(walkparams, tablebase.paspace, ttbr); walkstate.baseaddress = tablebase; walkstate.level = AArch64.S2StartLevel(walkparams); walkstate.istable = TRUE; walkstate.memattrs = WalkMemAttrs(walkparams.sh, walkparams.irgn, walkparams.orgn); return walkstate;
```

## J1.1.4.81 AArch64.SS2OutputPASpace // AArch64.SS2OutputPASpace() // ========================== // Assign PA Space to output of Secure stage 2 translation PASpace AArch64.SS2OutputPASpace(S2TTWParams walkparams, PASpace ipaspace) if ipaspace == PAS\_Secure then if walkparams.&lt;sw,sa&gt; == '00' then return PAS\_Secure; else return PAS\_NonSecure; else if walkparams.&lt;sw,sa,nsw,nsa&gt; == '0000' then return PAS\_Secure; else return PAS\_NonSecure; J1.1.4.82 AArch64.GetS1TTWParams // AArch64.GetS1TTWParams() // ======================== // Returns stage 1 translation table walk parameters from respective controlling // System registers. S1TTWParams AArch64.GetS1TTWParams(Regime regime, bits(2) el, SecurityState ss, bits(64) va) S1TTWParams walkparams; varange = AArch64.GetVARange(va); case regime of when Regime\_EL3 walkparams = AArch64.S1TTWParamsEL3(); when Regime\_EL2 walkparams = AArch64.S1TTWParamsEL2(ss); when Regime\_EL20 walkparams = AArch64.S1TTWParamsEL20(el, ss, varange); when Regime\_EL10 walkparams = AArch64.S1TTWParamsEL10(el, varange); return walkparams; J1.1.4.83 AArch64.GetS2TTWParams boolean s1aarch64)

```
// AArch64.GetS2TTWParams() // ======================== // Gather walk parameters for stage 2 translation S2TTWParams AArch64.GetS2TTWParams(SecurityState ss, PASpace ipaspace, S2TTWParams walkparams; if ss == SS_NonSecure then walkparams = AArch64.NSS2TTWParams(s1aarch64); elsif IsFeatureImplemented(FEAT_SEL2) && ss == SS_Secure then
```

```
walkparams = AArch64.SS2TTWParams(ipaspace, s1aarch64); elsif ss == SS_Realm then walkparams = AArch64.RLS2TTWParams(s1aarch64); else Unreachable(); return walkparams;
```

## J1.1.4.84 AArch64.GetVARange

```
// AArch64.GetVARange() // ==================== // Determines if the VA that is to be translated lies in LOWER or UPPER address range. VARange AArch64.GetVARange(bits(64) va) if va<55> == '0' then return VARange_LOWER; else return VARange_UPPER;
```

## J1.1.4.85 AArch64.HaveS1TG

```
// AArch64.HaveS1TG() // ================== // Determine whether the given translation granule is supported for stage 1 boolean AArch64.HaveS1TG(TGx tgx) case tgx of when TGx_4KB return IsFeatureImplemented(FEAT_TGran4K); when TGx_16KB return IsFeatureImplemented(FEAT_TGran16K); when TGx_64KB return IsFeatureImplemented(FEAT_TGran64K);
```

## J1.1.4.86 AArch64.HaveS2TG

```
// AArch64.HaveS2TG() // ================== // Determine whether the given translation granule is supported for stage 2 boolean AArch64.HaveS2TG(TGx tgx) assert HaveEL(EL2); if IsFeatureImplemented(FEAT_GTG) then case tgx of when TGx_4KB return IsFeatureImplemented(FEAT_S2TGran4K); when TGx_16KB return IsFeatureImplemented(FEAT_S2TGran16K); when TGx_64KB return IsFeatureImplemented(FEAT_S2TGran64K); else return AArch64.HaveS1TG(tgx);
```

## J1.1.4.87 AArch64.MaxTxSZ

```
// AArch64.MaxTxSZ() // ================= // Retrieve the maximum value of TxSZ indicating minimum input address size for both // stages of translation integer AArch64.MaxTxSZ(TGx tgx) if IsFeatureImplemented(FEAT_TTST) then case tgx of when TGx_4KB return 48;
```

```
when TGx_16KB return when TGx_64KB return return 39;
```

```
48; 47;
```

## J1.1.4.88 AArch64.NSS2TTWParams

```
// AArch64.NSS2TTWParams() // ======================= // Gather walk parameters specific for Non-secure stage 2 translation S2TTWParams AArch64.NSS2TTWParams(boolean s1aarch64) S2TTWParams walkparams; walkparams.vm = HCR_EL2.VM OR HCR_EL2.DC; walkparams.tgx = AArch64.S2DecodeTG0(VTCR_EL2.TG0); walkparams.txsz = VTCR_EL2.T0SZ; walkparams.ps = VTCR_EL2.PS; walkparams.irgn = VTCR_EL2.IRGN0; walkparams.orgn = VTCR_EL2.ORGN0; walkparams.sh = VTCR_EL2.SH0; walkparams.ee = SCTLR_EL2.EE; walkparams.d128 = if IsFeatureImplemented(FEAT_D128) then VTCR_EL2.D128 else '0'; if walkparams.d128 == '1' then walkparams.skl = VTTBR_EL2.SKL; else walkparams.sl0 = VTCR_EL2.SL0; walkparams.ptw = if HCR_EL2.TGE == '0' then HCR_EL2.PTW else '0'; walkparams.fwb = if IsFeatureImplemented(FEAT_S2FWB) then HCR_EL2.FWB else '0'; walkparams.ha = if IsFeatureImplemented(FEAT_HAFDBS) then VTCR_EL2.HA else '0'; walkparams.hd = if walkparams.ha == '1' then VTCR_EL2.HD else '0'; if walkparams.tgx IN {TGx_4KB, TGx_16KB} && IsFeatureImplemented(FEAT_LPA2) then walkparams.ds = VTCR_EL2.DS; else walkparams.ds = '0'; if walkparams.tgx == TGx_4KB && IsFeatureImplemented(FEAT_LPA2) then walkparams.sl2 = VTCR_EL2.SL2 AND VTCR_EL2.DS; else walkparams.sl2 = '0'; walkparams.cmow = (if IsFeatureImplemented(FEAT_CMOW) && IsHCRXEL2Enabled() then HCRX_EL2.CMOW else '0'); if walkparams.d128 == '1' then walkparams.s2pie = '1'; else walkparams.s2pie = if IsFeatureImplemented(FEAT_S2PIE) then VTCR_EL2.S2PIE else '0'; if IsFeatureImplemented(FEAT_S2PIE) then if !(HaveEL(EL3) && SCR_EL3.PIEn == '0' && boolean IMPLEMENTATION_DEFINED "SCR_EL3.PIEn forces PIE/POE_ELx to zero") then walkparams.s2pir = S2PIR_EL2; else walkparams.s2pir = Zeros(64); if IsFeatureImplemented(FEAT_THE) && walkparams.d128 != '1' then walkparams.assuredonly = VTCR_EL2.AssuredOnly; else walkparams.assuredonly = '0'; walkparams.tl0 = if IsFeatureImplemented(FEAT_THE) then VTCR_EL2.TL0 else '0'; walkparams.tl1 = if IsFeatureImplemented(FEAT_THE) then VTCR_EL2.TL1 else '0'; if IsFeatureImplemented(FEAT_HAFT) && walkparams.ha == '1' then walkparams.haft = VTCR_EL2.HAFT; else walkparams.haft = '0'; if (IsFeatureImplemented(FEAT_HDBSS) && walkparams.hd == '1' && (!HaveEL(EL3) || SCR_EL3.HDBSSEn == '1')) then walkparams.hdbss = VTCR_EL2.HDBSS;
```

```
else walkparams.hdbss = '0'; return walkparams;
```

## J1.1.4.89 AArch64.PAMax

```
// AArch64.PAMax() // =============== // Returns the IMPLEMENTATION DEFINED maximum number of bits capable of // physical address for this PE AddressSize AArch64.PAMax() return integer IMPLEMENTATION_DEFINED "Maximum Physical Address Size";
```

## J1.1.4.90 AArch64.RLS2TTWParams

```
// AArch64.RLS2TTWParams() // ======================= // Gather walk parameters specific for Realm stage 2 translation S2TTWParams AArch64.RLS2TTWParams(boolean s1aarch64) // Realm stage 2 walk parameters are similar to Non-secure S2TTWParams walkparams = AArch64.NSS2TTWParams(s1aarch64); walkparams.emec = (if IsFeatureImplemented(FEAT_MEC) && IsSCTLR2EL2Enabled() then SCTLR2_EL2.EMEC else return walkparams;
```

## J1.1.4.91 AArch64.S1DCacheEnabled

```
// AArch64.S1DCacheEnabled() // ========================= // Determine cacheability of stage 1 data accesses boolean AArch64.S1DCacheEnabled(Regime regime) case regime of when Regime_EL3 return SCTLR_EL3.C == '1'; when Regime_EL2 return SCTLR_EL2.C == '1'; when Regime_EL20 return SCTLR_EL2.C == '1'; when Regime_EL10 return SCTLR_EL1.C == '1';
```

## J1.1.4.92 AArch64.S1DecodeTG0

```
// AArch64.S1DecodeTG0() // ===================== // Decode stage 1 granule size configuration bits TG0 TGx AArch64.S1DecodeTG0(bits(2) tg0_in) bits(2) tg0 = tg0_in; TGx tgx; if tg0 == '11' then tg0 = bits(2) IMPLEMENTATION_DEFINED "TG0 encoded granule size"; case tg0 of when '00' tgx = TGx_4KB; when '01' tgx = TGx_64KB; when '10' tgx = TGx_16KB; if !AArch64.HaveS1TG(tgx) then
```

```
representing
```

```
'0');
```

```
case bits(2) IMPLEMENTATION_DEFINED "TG0 encoded granule size" of when '00' tgx = TGx_4KB; when '01' tgx = TGx_64KB; when '10' tgx = TGx_16KB; return tgx;
```

## J1.1.4.93 AArch64.S1DecodeTG1

```
// AArch64.S1DecodeTG1() // ===================== // Decode stage 1 granule size configuration bits TG1 TGx AArch64.S1DecodeTG1(bits(2) tg1_in) bits(2) tg1 = tg1_in; TGx tgx; if tg1 == '00' then tg1 = bits(2) IMPLEMENTATION_DEFINED "TG1 encoded granule size"; case tg1 of when '10' tgx = TGx_4KB; when '11' tgx = TGx_64KB; when '01' tgx = TGx_16KB; if !AArch64.HaveS1TG(tgx) then case bits(2) IMPLEMENTATION_DEFINED "TG1 encoded granule size" of when '10' tgx = TGx_4KB; when '11' tgx = TGx_64KB; when '01' tgx = TGx_16KB; return tgx;
```

## J1.1.4.94 AArch64.S1E0POEnabled

```
// AArch64.S1E0POEnabled() // ======================= // Determine whether stage 1 unprivileged permission overlay is enabled boolean AArch64.S1E0POEnabled(Regime regime, bit nv1) assert HasUnprivileged(regime); if !IsFeatureImplemented(FEAT_S1POE) then return FALSE; case regime of when Regime_EL20 return IsTCR2EL2Enabled() && TCR2_EL2.E0POE == '1'; when Regime_EL10 return IsTCR2EL1Enabled() && nv1 == '0' && TCR2_EL1.E0POE == '1';
```

## J1.1.4.95 AArch64.S1EPD

```
// AArch64.S1EPD() // =============== // Determine whether stage 1 translation table walk is allowed for the VA range bit AArch64.S1EPD(Regime regime, bits(64) va) assert HasUnprivileged(regime); varange = AArch64.GetVARange(va); case regime of when Regime_EL20 return if varange == VARange_LOWER then TCR_EL2.EPD0 else TCR_EL2.EPD1; when Regime_EL10 return if varange == VARange_LOWER then TCR_EL1.EPD0 else TCR_EL1.EPD1;
```

## J1.1.4.96 AArch64.S1Enabled

```
// AArch64.S1Enabled() // =================== // Determine if stage 1 is enabled for the access type for this translation regime boolean AArch64.S1Enabled(Regime regime, AccessType acctype) if acctype == AccessType_TRBE && EffectiveTRBLIMITR_EL1_nVM() == '1' then return FALSE; if acctype == AccessType_SPE && EffectivePMBLIMITR_EL1_nVM() == '1' then return FALSE; case regime of when Regime_EL3 return SCTLR_EL3.M == '1'; when Regime_EL2 return SCTLR_EL2.M == '1'; when Regime_EL20 return SCTLR_EL2.M == '1'; when Regime_EL10 return (!EL2Enabled() || HCR_EL2.<DC,TGE> == '00') && SCTLR_EL1.M == '1';
```

## J1.1.4.97 AArch64.S1ICacheEnabled

```
// AArch64.S1ICacheEnabled() // ========================= // Determine cacheability of stage 1 instruction fetches boolean AArch64.S1ICacheEnabled(Regime regime) case regime of when Regime_EL3 return SCTLR_EL3.I == '1'; when Regime_EL2 return SCTLR_EL2.I == '1'; when Regime_EL20 return SCTLR_EL2.I == '1'; when Regime_EL10 return SCTLR_EL1.I == '1';
```

## J1.1.4.98 AArch64.S1MinTxSZ

```
// AArch64.S1MinTxSZ() // =================== // Retrieve the minimum value of TxSZ indicating maximum input address size for stage 1 integer AArch64.S1MinTxSZ(Regime regime, S1TTWParams walkparams) if IsFeatureImplemented(FEAT_LVA3) then if walkparams.d128 == '1' then if HasUnprivileged(regime) then return 9; else return 8; elsif walkparams.tgx == TGx_64KB || walkparams.ds == '1' then return 12; else return 16; if IsFeatureImplemented(FEAT_LVA) then if walkparams.tgx == TGx_64KB || walkparams.ds == '1' || walkparams.d128 == '1' then return 12; else return 16; return 16;
```

## J1.1.4.99 AArch64.S1POEnabled

```
// AArch64.S1POEnabled() // ===================== // Determine whether stage 1 privileged permission overlay is enabled
```

```
boolean AArch64.S1POEnabled(Regime regime) if !IsFeatureImplemented(FEAT_S1POE) then return FALSE; case regime of when Regime_EL3 return TCR_EL3.POE == '1'; when Regime_EL2 return IsTCR2EL2Enabled() && TCR2_EL2.POE == '1'; when Regime_EL20 return IsTCR2EL2Enabled() && TCR2_EL2.POE == '1'; when Regime_EL10 return IsTCR2EL1Enabled() && TCR2_EL1.POE == '1';
```

## J1.1.4.100 AArch64.S1POR

```
// AArch64.S1POR() // =============== // Identify stage 1 permissions overlay register for the acting translation regime S1PORType AArch64.S1POR(Regime regime) if (HaveEL(EL3) && SCR_EL3.PIEn == '0' && regime != Regime_EL3 && boolean IMPLEMENTATION_DEFINED "SCR_EL3.PIEn forces PIE/POE_ELx to zero") then return Zeros(64); case regime of when Regime_EL3 return POR_EL3; when Regime_EL2 return POR_EL2; when Regime_EL20 return POR_EL2; when Regime_EL10 return POR_EL1;
```

## J1.1.4.101 AArch64.S1TTBR

```
// AArch64.S1TTBR() // ================ // Identify stage 1 table base register for the acting translation regime bits(128) AArch64.S1TTBR(Regime regime, bits(64) va) varange = AArch64.GetVARange(va); case regime of when Regime_EL3 return ZeroExtend(TTBR0_EL3, 128); when Regime_EL2 return ZeroExtend(TTBR0_EL2, 128); when Regime_EL20 if varange == VARange_LOWER then return ZeroExtend(TTBR0_EL2, 128); else return ZeroExtend(TTBR1_EL2, 128); when Regime_EL10 if varange == VARange_LOWER then return ZeroExtend(TTBR0_EL1, 128); else return ZeroExtend(TTBR1_EL1, 128);
```

## J1.1.4.102 AArch64.S1TTWParamsEL10

```
// AArch64.S1TTWParamsEL10() // ========================= // Gather stage 1 translation table walk parameters for EL1&0 regime // (with EL2 enabled or disabled) S1TTWParams AArch64.S1TTWParamsEL10(bits(2) el, VARange varange) S1TTWParams walkparams; if IsFeatureImplemented(FEAT_D128) && IsTCR2EL1Enabled() then
```

```
walkparams.d128 = TCR2_EL1.D128; else walkparams.d128 = '0'; constant bits(3) nvs = EffectiveHCR_EL2_NVx(); walkparams.nv1 = nvs<1>; if IsFeatureImplemented(FEAT_AIE) then walkparams.mair2 = MAIR2_EL1; walkparams.aie = (if IsFeatureImplemented(FEAT_AIE) && IsTCR2EL1Enabled() then TCR2_EL1.AIE else '0'); if walkparams.d128 == '1' then walkparams.pie = '1'; else walkparams.pie = (if IsFeatureImplemented(FEAT_S1PIE) && IsTCR2EL1Enabled() then TCR2_EL1.PIE else '0'); if IsFeatureImplemented(FEAT_S1PIE) then if !(HaveEL(EL3) && SCR_EL3.PIEn == '0' && boolean IMPLEMENTATION_DEFINED "SCR_EL3.PIEn forces PIE/POE_ELx to zero") then walkparams.pir = PIR_EL1; if walkparams.nv1 == '1' then walkparams.pire0 = Zeros(64); else walkparams.pire0 = PIRE0_EL1; else walkparams.pir = Zeros(64); walkparams.pire0 = Zeros(64); if varange == VARange_LOWER then walkparams.tgx = AArch64.S1DecodeTG0(TCR_EL1.TG0); walkparams.txsz = TCR_EL1.T0SZ; walkparams.irgn = TCR_EL1.IRGN0; walkparams.orgn = TCR_EL1.ORGN0; walkparams.sh = TCR_EL1.SH0; walkparams.tbi = TCR_EL1.TBI0; walkparams.nfd = if IsFeatureImplemented(FEAT_SVE) then TCR_EL1.NFD0 else '0'; walkparams.tbid = if IsFeatureImplemented(FEAT_PAuth) then TCR_EL1.TBID0 else '0'; walkparams.e0pd = if IsFeatureImplemented(FEAT_E0PD) then TCR_EL1.E0PD0 else '0'; walkparams.hpd = if IsFeatureImplemented(FEAT_HPDS) then TCR_EL1.HPD0 else '0'; if walkparams.hpd == '0' then if walkparams.aie == '1' then walkparams.hpd = '1'; if walkparams.pie == '1' then walkparams.hpd = '1'; if (AArch64.S1POEnabled(Regime_EL10) || AArch64.S1E0POEnabled(Regime_EL10, walkparams.nv1)) then walkparams.hpd = '1'; if (IsFeatureImplemented(FEAT_MTE_NO_ADDRESS_TAGS) || IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS)) then walkparams.mtx = TCR_EL1.MTX0; else walkparams.mtx = '0'; walkparams.skl = if walkparams.d128 == '1' then TTBR0_EL1.SKL else '00'; walkparams.disch = if walkparams.d128 == '1' then TCR2_EL1.DisCH0 else '0'; if IsFeatureImplemented(FEAT_ASID2) && IsTCR2EL1Enabled() then walkparams.fng = TCR2_EL1.FNG0; else walkparams.fng = '0'; if IsFeatureImplemented(FEAT_THE) && IsTCR2EL1Enabled() then walkparams.fngna = TCR2_EL1.FNGNA0; else walkparams.fngna = '0'; else walkparams.tgx = AArch64.S1DecodeTG1(TCR_EL1.TG1); walkparams.txsz = TCR_EL1.T1SZ; walkparams.irgn = TCR_EL1.IRGN1; walkparams.orgn = TCR_EL1.ORGN1; walkparams.sh = TCR_EL1.SH1; walkparams.tbi = TCR_EL1.TBI1;
```

```
walkparams.nfd = if IsFeatureImplemented(FEAT_SVE) then TCR_EL1.NFD1 else '0'; walkparams.tbid = if IsFeatureImplemented(FEAT_PAuth) then TCR_EL1.TBID1 else '0'; walkparams.e0pd = if IsFeatureImplemented(FEAT_E0PD) then TCR_EL1.E0PD1 else '0'; walkparams.hpd = if IsFeatureImplemented(FEAT_HPDS) then TCR_EL1.HPD1 else '0'; if walkparams.hpd == '0' then if walkparams.aie == '1' then walkparams.hpd = '1'; if walkparams.pie == '1' then walkparams.hpd = '1'; if (AArch64.S1POEnabled(Regime_EL10) || AArch64.S1E0POEnabled(Regime_EL10, walkparams.nv1)) then walkparams.hpd = '1'; if (IsFeatureImplemented(FEAT_MTE_NO_ADDRESS_TAGS) || IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS)) then walkparams.mtx = TCR_EL1.MTX1; else walkparams.mtx = '0'; walkparams.skl = if walkparams.d128 == '1' then TTBR1_EL1.SKL else '00'; walkparams.disch = if walkparams.d128 == '1' then TCR2_EL1.DisCH1 else '0'; if IsFeatureImplemented(FEAT_ASID2) && IsTCR2EL1Enabled() then walkparams.fng = TCR2_EL1.FNG1; else walkparams.fng = '0'; if IsFeatureImplemented(FEAT_THE) && IsTCR2EL1Enabled() then walkparams.fngna = TCR2_EL1.FNGNA1; else walkparams.fngna = '0'; walkparams.mair = MAIR_EL1; walkparams.wxn = SCTLR_EL1.WXN; walkparams.ps = TCR_EL1.IPS; walkparams.ee = SCTLR_EL1.EE; if (HaveEL(EL3) && (!IsFeatureImplemented(FEAT_RME) || IsFeatureImplemented(FEAT_SEL2))) then walkparams.sif = SCR_EL3.SIF; else walkparams.sif = '0'; if EL2Enabled() then walkparams.dc = HCR_EL2.DC; walkparams.dct = if IsFeatureImplemented(FEAT_MTE2) then HCR_EL2.DCT else '0'; if IsFeatureImplemented(FEAT_LSMAOC) then walkparams.ntlsmd = SCTLR_EL1.nTLSMD; else walkparams.ntlsmd = '1'; walkparams.cmow = if IsFeatureImplemented(FEAT_CMOW) then SCTLR_EL1.CMOW else '0'; walkparams.ha = if IsFeatureImplemented(FEAT_HAFDBS) then TCR_EL1.HA else '0'; walkparams.hd = if walkparams.ha == '1' then TCR_EL1.HD else '0'; if (walkparams.tgx IN {TGx_4KB, TGx_16KB} && IsFeatureImplemented(FEAT_LPA2) && walkparams.d128 == '0') then walkparams.ds = TCR_EL1.DS; else walkparams.ds = '0'; if IsFeatureImplemented(FEAT_PAN3) then walkparams.epan = if walkparams.pie == '0' then SCTLR_EL1.EPAN else '1'; else walkparams.epan = '0'; if IsFeatureImplemented(FEAT_THE) && walkparams.d128 == '0' && IsTCR2EL1Enabled() then walkparams.pnch = TCR2_EL1.PnCH; else walkparams.pnch = '0'; if IsFeatureImplemented(FEAT_HAFT) && walkparams.ha == '1' && IsTCR2EL1Enabled() then walkparams.haft = TCR2_EL1.HAFT; else walkparams.haft = '0'; walkparams.emec = (if IsFeatureImplemented(FEAT_MEC) && IsSCTLR2EL2Enabled() then SCTLR2_EL2.EMEC else '0');
```

return walkparams;

## J1.1.4.103 AArch64.S1TTWParamsEL2

```
// AArch64.S1TTWParamsEL2() // ======================== // Gather stage 1 translation table walk parameters for EL2 regime S1TTWParams AArch64.S1TTWParamsEL2(SecurityState ss) S1TTWParams walkparams; walkparams.tgx = AArch64.S1DecodeTG0(TCR_EL2.TG0); walkparams.txsz = TCR_EL2.T0SZ; walkparams.ps = TCR_EL2.PS; walkparams.irgn = TCR_EL2.IRGN0; walkparams.orgn = TCR_EL2.ORGN0; walkparams.sh = TCR_EL2.SH0; walkparams.tbi = TCR_EL2.TBI; walkparams.mair = MAIR_EL2; walkparams.pie = (if IsFeatureImplemented(FEAT_S1PIE) && IsTCR2EL2Enabled() then TCR2_EL2.PIE else '0'); if IsFeatureImplemented(FEAT_S1PIE) then if !(HaveEL(EL3) && SCR_EL3.PIEn == '0' && boolean IMPLEMENTATION_DEFINED "SCR_EL3.PIEn forces PIE/POE_ELx to zero") then walkparams.pir = PIR_EL2; else walkparams.pir = Zeros(64); if IsFeatureImplemented(FEAT_AIE) then walkparams.mair2 = MAIR2_EL2; walkparams.aie = (if IsFeatureImplemented(FEAT_AIE) && IsTCR2EL2Enabled() then TCR2_EL2.AIE else '0'); walkparams.wxn = SCTLR_EL2.WXN; walkparams.ee = SCTLR_EL2.EE; if (HaveEL(EL3) && (!IsFeatureImplemented(FEAT_RME) || IsFeatureImplemented(FEAT_SEL2))) then walkparams.sif = SCR_EL3.SIF; else walkparams.sif = '0'; walkparams.tbid = if IsFeatureImplemented(FEAT_PAuth) then TCR_EL2.TBID else '0'; walkparams.hpd = if IsFeatureImplemented(FEAT_HPDS) then TCR_EL2.HPD else '0'; if walkparams.hpd == '0' then if walkparams.aie == '1' then walkparams.hpd = '1'; if walkparams.pie == '1' then walkparams.hpd = '1'; if AArch64.S1POEnabled(Regime_EL2) then walkparams.hpd = '1'; walkparams.ha = if IsFeatureImplemented(FEAT_HAFDBS) then TCR_EL2.HA else '0'; walkparams.hd = if walkparams.ha == '1' then TCR_EL2.HD else '0'; if walkparams.tgx IN {TGx_4KB, TGx_16KB} && IsFeatureImplemented(FEAT_LPA2) then walkparams.ds = TCR_EL2.DS; else walkparams.ds = '0'; if (IsFeatureImplemented(FEAT_MTE_NO_ADDRESS_TAGS) || IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS)) then walkparams.mtx = TCR_EL2.MTX; else walkparams.mtx = '0'; walkparams.pnch = (if IsFeatureImplemented(FEAT_THE) && IsTCR2EL2Enabled() then TCR2_EL2.PnCH else '0'); if IsFeatureImplemented(FEAT_HAFT) && walkparams.ha == '1' && IsTCR2EL2Enabled() then walkparams.haft = TCR2_EL2.HAFT; else walkparams.haft = '0'; walkparams.emec = (if IsFeatureImplemented(FEAT_MEC) &&
```

```
IsSCTLR2EL2Enabled() then SCTLR2_EL2.EMEC else '0'); if IsFeatureImplemented(FEAT_MEC) && ss == SS_Realm && IsTCR2EL2Enabled() then walkparams.amec = TCR2_EL2.AMEC0; else walkparams.amec = '0'; return walkparams;
```

## J1.1.4.104 AArch64.S1TTWParamsEL20

```
// AArch64.S1TTWParamsEL20() // ========================= // Gather stage 1 translation table walk parameters for EL2&0 regime S1TTWParams AArch64.S1TTWParamsEL20(bits(2) el, SecurityState ss, VARange varange) S1TTWParams walkparams; if IsFeatureImplemented(FEAT_D128) && IsTCR2EL2Enabled() then walkparams.d128 = TCR2_EL2.D128; else walkparams.d128 = '0'; if walkparams.d128 == '1' then walkparams.pie = '1'; else walkparams.pie = (if IsFeatureImplemented(FEAT_S1PIE) && IsTCR2EL2Enabled() then TCR2_EL2.PIE else '0'); if IsFeatureImplemented(FEAT_S1PIE) then if !(HaveEL(EL3) && SCR_EL3.PIEn == '0' && boolean IMPLEMENTATION_DEFINED "SCR_EL3.PIEn forces PIE/POE_ELx to zero") then walkparams.pir = PIR_EL2; walkparams.pire0 = PIRE0_EL2; else walkparams.pir = Zeros(64); walkparams.pire0 = Zeros(64); if IsFeatureImplemented(FEAT_AIE) then walkparams.mair2 = MAIR2_EL2; walkparams.aie = (if IsFeatureImplemented(FEAT_AIE) && IsTCR2EL2Enabled() then TCR2_EL2.AIE else '0'); if varange == VARange_LOWER then walkparams.tgx = AArch64.S1DecodeTG0(TCR_EL2.TG0); walkparams.txsz = TCR_EL2.T0SZ; walkparams.irgn = TCR_EL2.IRGN0; walkparams.orgn = TCR_EL2.ORGN0; walkparams.sh = TCR_EL2.SH0; walkparams.tbi = TCR_EL2.TBI0; walkparams.nfd = if IsFeatureImplemented(FEAT_SVE) then TCR_EL2.NFD0 else '0'; walkparams.tbid = if IsFeatureImplemented(FEAT_PAuth) then TCR_EL2.TBID0 else '0'; walkparams.e0pd = if IsFeatureImplemented(FEAT_E0PD) then TCR_EL2.E0PD0 else '0'; walkparams.hpd = if IsFeatureImplemented(FEAT_HPDS) then TCR_EL2.HPD0 else '0'; if walkparams.hpd == '0' then if walkparams.aie == '1' then walkparams.hpd = '1'; if walkparams.pie == '1' then walkparams.hpd = '1'; if AArch64.S1POEnabled(Regime_EL20) || AArch64.S1E0POEnabled(Regime_EL20, '0') then walkparams.hpd = '1'; if (IsFeatureImplemented(FEAT_MTE_NO_ADDRESS_TAGS) || IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS)) then walkparams.mtx = TCR_EL2.MTX0; else walkparams.mtx = '0'; walkparams.skl = if walkparams.d128 == '1' then TTBR0_EL2.SKL else '00'; walkparams.disch = if walkparams.d128 == '1' then TCR2_EL2.DisCH0 else '0'; if IsFeatureImplemented(FEAT_ASID2) && IsTCR2EL2Enabled() then
```

```
walkparams.fng = TCR2_EL2.FNG0; else walkparams.fng = '0'; else walkparams.tgx = AArch64.S1DecodeTG1(TCR_EL2.TG1); walkparams.txsz = TCR_EL2.T1SZ; walkparams.irgn = TCR_EL2.IRGN1; walkparams.orgn = TCR_EL2.ORGN1; walkparams.sh = TCR_EL2.SH1; walkparams.tbi = TCR_EL2.TBI1; walkparams.nfd = if IsFeatureImplemented(FEAT_SVE) then TCR_EL2.NFD1 else '0'; walkparams.tbid = if IsFeatureImplemented(FEAT_PAuth) then TCR_EL2.TBID1 else '0'; walkparams.e0pd = if IsFeatureImplemented(FEAT_E0PD) then TCR_EL2.E0PD1 else '0'; walkparams.hpd = if IsFeatureImplemented(FEAT_HPDS) then TCR_EL2.HPD1 else '0'; if walkparams.hpd == '0' then if walkparams.aie == '1' then walkparams.hpd = '1'; if walkparams.pie == '1' then walkparams.hpd = '1'; if AArch64.S1POEnabled(Regime_EL20) || AArch64.S1E0POEnabled(Regime_EL20, '0') then walkparams.hpd = '1'; if (IsFeatureImplemented(FEAT_MTE_NO_ADDRESS_TAGS) || IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS)) then walkparams.mtx = TCR_EL2.MTX1; else walkparams.mtx = '0'; walkparams.skl = if walkparams.d128 == '1' then TTBR1_EL2.SKL else '00'; walkparams.disch = if walkparams.d128 == '1' then TCR2_EL2.DisCH1 else '0'; if IsFeatureImplemented(FEAT_ASID2) && IsTCR2EL2Enabled() then walkparams.fng = TCR2_EL2.FNG1; else walkparams.fng = '0'; walkparams.mair = MAIR_EL2; walkparams.wxn = SCTLR_EL2.WXN; walkparams.ps = TCR_EL2.IPS; walkparams.ee = SCTLR_EL2.EE; if (HaveEL(EL3) && (!IsFeatureImplemented(FEAT_RME) || IsFeatureImplemented(FEAT_SEL2))) then walkparams.sif = SCR_EL3.SIF; else walkparams.sif = '0'; if IsFeatureImplemented(FEAT_LSMAOC) then walkparams.ntlsmd = SCTLR_EL2.nTLSMD; else walkparams.ntlsmd = '1'; walkparams.cmow = if IsFeatureImplemented(FEAT_CMOW) then SCTLR_EL2.CMOW else '0'; walkparams.ha = if IsFeatureImplemented(FEAT_HAFDBS) then TCR_EL2.HA else '0'; walkparams.hd = if walkparams.ha == '1' then TCR_EL2.HD else '0'; if (walkparams.tgx IN {TGx_4KB, TGx_16KB} && IsFeatureImplemented(FEAT_LPA2) && walkparams.d128 == '0') then walkparams.ds = TCR_EL2.DS; else walkparams.ds = '0'; if IsFeatureImplemented(FEAT_PAN3) then walkparams.epan = if walkparams.pie == '0' then SCTLR_EL2.EPAN else '1'; else walkparams.epan = '0'; if IsFeatureImplemented(FEAT_THE) && walkparams.d128 == '0' && IsTCR2EL2Enabled() then walkparams.pnch = TCR2_EL2.PnCH; else walkparams.pnch = '0'; if IsFeatureImplemented(FEAT_HAFT) && walkparams.ha == '1' && IsTCR2EL2Enabled() then walkparams.haft = TCR2_EL2.HAFT; else walkparams.haft = '0';
```

```
walkparams.emec = (if IsFeatureImplemented(FEAT_MEC) && IsSCTLR2EL2Enabled() then SCTLR2_EL2.EMEC else '0'); if IsFeatureImplemented(FEAT_MEC) && ss == SS_Realm && IsTCR2EL2Enabled() then walkparams.amec = if varange == VARange_LOWER then TCR2_EL2.AMEC0 else TCR2_EL2.AMEC1; else walkparams.amec = '0'; return walkparams;
```

## J1.1.4.105 AArch64.S1TTWParamsEL3

```
// AArch64.S1TTWParamsEL3() // ======================== // Gather stage 1 translation table walk parameters for EL3 regime S1TTWParams AArch64.S1TTWParamsEL3() S1TTWParams walkparams; walkparams.tgx = AArch64.S1DecodeTG0(TCR_EL3.TG0); walkparams.txsz = TCR_EL3.T0SZ; walkparams.ps = TCR_EL3.PS; walkparams.irgn = TCR_EL3.IRGN0; walkparams.orgn = TCR_EL3.ORGN0; walkparams.sh = TCR_EL3.SH0; walkparams.tbi = TCR_EL3.TBI; walkparams.mair = MAIR_EL3; walkparams.d128 = if IsFeatureImplemented(FEAT_D128) then TCR_EL3.D128 else '0'; walkparams.skl = if walkparams.d128 == '1' then TTBR0_EL3.SKL else '00'; walkparams.disch = if walkparams.d128 == '1' then TCR_EL3.DisCH0 else '0'; if walkparams.d128 == '1' then walkparams.pie = '1'; else walkparams.pie = if IsFeatureImplemented(FEAT_S1PIE) then TCR_EL3.PIE else '0'; if IsFeatureImplemented(FEAT_S1PIE) then walkparams.pir = PIR_EL3; if IsFeatureImplemented(FEAT_AIE) then walkparams.mair2 = MAIR2_EL3; walkparams.aie = if IsFeatureImplemented(FEAT_AIE) then TCR_EL3.AIE else '0'; walkparams.wxn = SCTLR_EL3.WXN; walkparams.ee = SCTLR_EL3.EE; walkparams.sif = (if !IsFeatureImplemented(FEAT_RME) || IsFeatureImplemented(FEAT_SEL2) then SCR_EL3.SIF else '0'); walkparams.tbid = if IsFeatureImplemented(FEAT_PAuth) then TCR_EL3.TBID else '0'; walkparams.hpd = if IsFeatureImplemented(FEAT_HPDS) then TCR_EL3.HPD else '0'; if walkparams.hpd == '0' then if walkparams.aie == '1' then walkparams.hpd = '1'; if walkparams.pie == '1' then walkparams.hpd = '1'; if AArch64.S1POEnabled(Regime_EL3) then walkparams.hpd = '1'; walkparams.ha = if IsFeatureImplemented(FEAT_HAFDBS) then TCR_EL3.HA else '0'; walkparams.hd = if walkparams.ha == '1' then TCR_EL3.HD else '0'; if (walkparams.tgx IN {TGx_4KB, TGx_16KB} && IsFeatureImplemented(FEAT_LPA2) && walkparams.d128 == '0') then walkparams.ds = TCR_EL3.DS; else walkparams.ds = '0'; if (IsFeatureImplemented(FEAT_MTE_NO_ADDRESS_TAGS) || IsFeatureImplemented(FEAT_MTE_CANONICAL_TAGS)) then walkparams.mtx = TCR_EL3.MTX; else walkparams.mtx = '0'; if IsFeatureImplemented(FEAT_THE) && walkparams.d128 == '0' then walkparams.pnch = TCR_EL3.PnCH;
```

```
else walkparams.pnch = '0'; if IsFeatureImplemented(FEAT_HAFT) && walkparams.ha == '1' then walkparams.haft = TCR_EL3.HAFT; else walkparams.haft = '0'; walkparams.emec = if IsFeatureImplemented(FEAT_MEC) then SCTLR2_EL3.EMEC else '0'; return walkparams; J1.1.4.106 AArch64.S2DecodeTG0 // AArch64.S2DecodeTG0() // ===================== // Decode stage 2 granule size configuration bits TG0 TGx AArch64.S2DecodeTG0(bits(2) tg0_in) bits(2) tg0 = tg0_in; TGx tgx; if tg0 == '11' then tg0 = bits(2) IMPLEMENTATION_DEFINED "TG0 encoded granule size"; case tg0 of when '00' tgx = TGx_4KB; when '01' tgx = TGx_64KB; when '10' tgx = TGx_16KB; if !AArch64.HaveS2TG(tgx) then case bits(2) IMPLEMENTATION_DEFINED "TG0 encoded granule size" of when '00' tgx = TGx_4KB; when '01' tgx = TGx_64KB; when '10' tgx = TGx_16KB; return tgx; J1.1.4.107 AArch64.S2MinTxSZ // AArch64.S2MinTxSZ() // =================== // Retrieve the minimum value of TxSZ indicating maximum input address size for stage 2 integer AArch64.S2MinTxSZ(S2TTWParams walkparams, boolean s1aarch64) integer ips; if AArch64.PAMax() == 56 then if walkparams.d128 == '1' then ips = 56; elsif walkparams.tgx == TGx_64KB || walkparams.ds == '1' then ips = 52; else ips = 48; elsif AArch64.PAMax() == 52 then if walkparams.tgx == TGx_64KB || walkparams.ds == '1' then ips = 52; else ips = 48; else ips = AArch64.PAMax(); integer min_txsz = 64 -ips; if !s1aarch64 then // EL1 is AArch32
```

```
min_txsz = Min(min_txsz, 24); return min_txsz;
```

## J1.1.4.108 AArch64.SS2TTWParams

```
// AArch64.SS2TTWParams() // ====================== // Gather walk parameters specific for secure stage 2 translation S2TTWParams AArch64.SS2TTWParams(PASpace ipaspace, boolean s1aarch64) S2TTWParams walkparams; walkparams.d128 = if IsFeatureImplemented(FEAT_D128) then VTCR_EL2.D128 else '0'; if ipaspace == PAS_Secure then walkparams.tgx = AArch64.S2DecodeTG0(VSTCR_EL2.TG0); walkparams.txsz = VSTCR_EL2.T0SZ; if walkparams.d128 == '1' then walkparams.skl = VSTTBR_EL2.SKL; else walkparams.sl0 = VSTCR_EL2.SL0; if walkparams.tgx == TGx_4KB && IsFeatureImplemented(FEAT_LPA2) then walkparams.sl2 = VSTCR_EL2.SL2 AND VTCR_EL2.DS; else walkparams.sl2 = '0'; elsif ipaspace == PAS_NonSecure then walkparams.tgx = AArch64.S2DecodeTG0(VTCR_EL2.TG0); walkparams.txsz = VTCR_EL2.T0SZ; if walkparams.d128 == '1' then walkparams.skl = VTTBR_EL2.SKL; else walkparams.sl0 = VTCR_EL2.SL0; if walkparams.tgx == TGx_4KB && IsFeatureImplemented(FEAT_LPA2) then walkparams.sl2 = VTCR_EL2.SL2 AND VTCR_EL2.DS; else walkparams.sl2 = '0'; else Unreachable(); walkparams.sw = VSTCR_EL2.SW; walkparams.nsw = VTCR_EL2.NSW; walkparams.sa = VSTCR_EL2.SA; walkparams.nsa = VTCR_EL2.NSA; walkparams.vm = HCR_EL2.VM OR HCR_EL2.DC; walkparams.ps = VTCR_EL2.PS; walkparams.irgn = VTCR_EL2.IRGN0; walkparams.orgn = VTCR_EL2.ORGN0; walkparams.sh = VTCR_EL2.SH0; walkparams.ee = SCTLR_EL2.EE; walkparams.ptw = if HCR_EL2.TGE == '0' then HCR_EL2.PTW else '0'; walkparams.fwb = if IsFeatureImplemented(FEAT_S2FWB) then HCR_EL2.FWB else '0'; walkparams.ha = if IsFeatureImplemented(FEAT_HAFDBS) then VTCR_EL2.HA else '0'; walkparams.hd = if walkparams.ha == '1' then VTCR_EL2.HD else '0'; if walkparams.tgx IN {TGx_4KB, TGx_16KB} && IsFeatureImplemented(FEAT_LPA2) then walkparams.ds = VTCR_EL2.DS; else walkparams.ds = '0'; walkparams.cmow = (if IsFeatureImplemented(FEAT_CMOW) && IsHCRXEL2Enabled() then HCRX_EL2.CMOW else '0'); if walkparams.d128 == '1' then walkparams.s2pie = '1'; else walkparams.s2pie = if IsFeatureImplemented(FEAT_S2PIE) then VTCR_EL2.S2PIE else '0'; if IsFeatureImplemented(FEAT_S2PIE) then
```

```
if !(HaveEL(EL3) && SCR_EL3.PIEn == '0' && boolean IMPLEMENTATION_DEFINED "SCR_EL3.PIEn forces PIE/POE_ELx to zero") then walkparams.s2pir = S2PIR_EL2; else walkparams.s2pir = Zeros(64); if IsFeatureImplemented(FEAT_THE) && walkparams.d128 != '1' then walkparams.assuredonly = VTCR_EL2.AssuredOnly; else walkparams.assuredonly = '0'; walkparams.tl0 = if IsFeatureImplemented(FEAT_THE) then VTCR_EL2.TL0 else '0'; walkparams.tl1 = if IsFeatureImplemented(FEAT_THE) then VTCR_EL2.TL1 else '0'; if IsFeatureImplemented(FEAT_HAFT) && walkparams.ha == '1' then walkparams.haft = VTCR_EL2.HAFT; else walkparams.haft = '0'; walkparams.emec = '0'; if (IsFeatureImplemented(FEAT_HDBSS) && walkparams.hd == '1' && (!HaveEL(EL3) || SCR_EL3.HDBSSEn == '1')) then walkparams.hdbss = VTCR_EL2.HDBSS; else walkparams.hdbss = '0'; return walkparams;
```

## J1.1.4.109 S2DCacheEnabled

```
// S2DCacheEnabled() // ================= // Returns TRUE if Stage 2 Data access cacheability is enabled boolean S2DCacheEnabled() return HCR_EL2.CD == '0';
```