## J1.2 Pseudocode for AArch32 operation

This section holds the pseudocode for execution in AArch32 state. Functions that are listed in this section are identified as AArch32.FunctionName . Some of these functions have an equivalent AArch64 function, AArch64.FunctionName . This section is organized by functional groups, with the functional groups being indicated by hierarchical path names, for example aarch32/debug/breakpoint .

Note

Many AArch32 pseudocode functions have not been updated to show the constraints on the Armv7 UNPREDICTABLE behaviors that are described in Architectural Constraints on UNPREDICTABLE Behaviors. Where AArch32 pseudocode shows something to be UNPREDICTABLE, check Architectural Constraints on UNPREDICTABLE Behaviors for possible constraints on the permitted behavior.

The top-level sections of the AArch32 pseudocode hierarchy are:

- aarch32/debug.
- aarch32/exceptions.
- aarch32/functions.
- aarch32/translation.

## J1.2.1 aarch32/debug

This section includes the following pseudocode functions:

- AArch32.VCRMatch
- AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled
- AArch32.BreakpointMatch
- AArch32.BreakpointValueMatch
- AArch32.ReservedBreakpointType
- AArch32.StateMatch
- AArch32.GenerateDebugExceptions
- AArch32.GenerateDebugExceptionsFrom
- AArch32.IncrementCycleCounter
- AArch32.IncrementEventCounter
- AArch32.PMUCycle
- AArch32.EnterHypModeInDebugState
- AArch32.EnterModeInDebugState
- AArch32.EnterMonitorModeInDebugState
- AArch32.WatchpointByteMatch
- AArch32.WatchpointMatch

## J1.2.1.1 AArch32.VCRMatch

```
// AArch32.VCRMatch() // ================== boolean AArch32.VCRMatch(bits(32) vaddress) boolean match; if UsingAArch32() && ELUsingAArch32(EL1) && PSTATE.EL != EL2 then // Each bit position in this string corresponds to a bit in DBGVCR and an exception vector. match_word = Zeros(32); ss = CurrentSecurityState();
```

## if vaddress&lt;31:5&gt; == ExcVectorBase()&lt;31:5&gt; then if HaveEL(EL3) &amp;&amp; ss == SS\_NonSecure then match\_word&lt;UInt(vaddress&lt;4:2&gt;) + 24&gt; = '1'; // Non-secure vectors else match\_word&lt;UInt(vaddress&lt;4:2&gt;) + 0&gt; = '1'; // Secure vectors (or no EL3) if (HaveEL(EL3) &amp;&amp; ELUsingAArch32(EL3) &amp;&amp; vaddress&lt;31:5&gt; == MVBAR&lt;31:5&gt; &amp;&amp; ss == SS\_Secure) then match\_word&lt;UInt(vaddress&lt;4:2&gt;) + 8&gt; = '1'; // Monitor vectors // Mask out bits not corresponding to vectors. bits(32) mask; if !HaveEL(EL3) then mask = '00000000':'00000000':'00000000':'11011110'; // DBGVCR[31:8] are RES0 elsif !ELUsingAArch32(EL3) then mask = '11011110':'00000000':'00000000':'11011110'; // DBGVCR[15:8] are RES0 else mask = '11011110':'00000000':'11011100':'11011110'; match\_word = match\_word AND DBGVCR AND mask; match = !IsZero(match\_word); // Check for UNPREDICTABLE case - match on Prefetch Abort and Data Abort vectors if !IsZero(match\_word&lt;28:27,12:11,4:3&gt;) &amp;&amp; DebugTarget() == PSTATE.EL then match = ConstrainUnpredictableBool(Unpredictable\_VCMATCHDAPA); if !IsZero(vaddress&lt;1:0&gt;) &amp;&amp; match then match = ConstrainUnpredictableBool(Unpredictable\_VCMATCHHALF); else match = FALSE; return match; J1.2.1.2 AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled // AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled() // ======================================================== boolean AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled() // The definition of this function is IMPLEMENTATION DEFINED. // In the recommended interface, AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled returns // the state of the (DBGEN AND SPIDEN) signal. if !HaveEL(EL3) &amp;&amp; NonSecureOnlyImplementation() then return FALSE; return DBGEN == HIGH &amp;&amp; SPIDEN == HIGH; J1.2.1.3 AArch32.BreakpointMatch accdesc,

```
// AArch32.BreakpointMatch() // ========================= // Breakpoint matching in an AArch32 translation regime. BreakpointInfo AArch32.BreakpointMatch(integer n, bits(32) vaddress, AccessDescriptor integer size) assert ELUsingAArch32(S1TranslationRegime()); assert n < NumBreakpointsImplemented(); BreakpointInfo brkptinfo; enabled = DBGBCR[n].E == '1'; isbreakpnt = TRUE; linked = DBGBCR[n].BT == '0x01'; linked_to = FALSE; linked_n = UInt(DBGBCR[n].LBN);
```

```
state_match = AArch32.StateMatch(DBGBCR[n].SSC, DBGBCR[n].HMC, DBGBCR[n].PMC, linked, linked_n, isbreakpnt, accdesc); (value_match, value_mismatch) = AArch32.BreakpointValueMatch(n, vaddress, linked_to); if size == 4 then // Check second halfword // If the breakpoint address and BAS of an Address breakpoint match the address of the // second halfword of an instruction, but not the address of the first halfword, it is // CONSTRAINED UNPREDICTABLE whether or not this breakpoint generates a Breakpoint debug // event. (match_i, mismatch_i) = AArch32.BreakpointValueMatch(n, vaddress + 2, linked_to); if !value_match && match_i then value_match = ConstrainUnpredictableBool(Unpredictable_BPMATCHHALF); if value_mismatch && !mismatch_i then value_mismatch = ConstrainUnpredictableBool(Unpredictable_BPMISMATCHHALF); if vaddress<1> == '1' && DBGBCR[n].BAS == '1111' then // The above notwithstanding, if DBGBCR[n].BAS == '1111', then it is CONSTRAINED // UNPREDICTABLE whether or not a Breakpoint debug event is generated for an instruction // at the address DBGBVR[n]+2. if value_match then value_match = ConstrainUnpredictableBool(Unpredictable_BPMATCHHALF); if !value_mismatch then value_mismatch = ConstrainUnpredictableBool(Unpredictable_BPMISMATCHHALF); brkptinfo.match = value_match && state_match && enabled; brkptinfo.mismatch = value_mismatch && state_match && enabled; return brkptinfo;
```

## J1.2.1.4

```
// AArch32.BreakpointValueMatch() // ============================== // The first result is whether an Address Match or Context breakpoint is programmed on the // instruction at "address". The second result is whether an Address Mismatch breakpoint is // programmed on the instruction, that is, whether the instruction should be stepped. (boolean, boolean) AArch32.BreakpointValueMatch(integer n_in, bits(32) vaddress, boolean // "n" is the identity of the breakpoint unit to match against. // "vaddress" is the current instruction address, ignored if linked_to is TRUE and for Context // matching breakpoints. // "linked_to" is TRUE if this is a call from StateMatch for linking. integer n = n_in; Constraint c; // If a non-existent breakpoint then it is CONSTRAINED UNPREDICTABLE whether this gives // no match or the breakpoint is mapped to another UNKNOWN implemented breakpoint. if n >= NumBreakpointsImplemented() then (c, n) = ConstrainUnpredictableInteger(0, NumBreakpointsImplemented() - 1, Unpredictable_BPNOTIMPL); assert c IN {Constraint_DISABLED, Constraint_UNKNOWN}; if c == Constraint_DISABLED then return (FALSE, FALSE); // If this breakpoint is not enabled, it cannot generate a match. // (This could also happen on a call from StateMatch for linking). if DBGBCR[n].E == '0' then return (FALSE, FALSE); dbgtype = DBGBCR[n].BT; (c, dbgtype) = AArch32.ReservedBreakpointType(n, dbgtype); if c == Constraint_DISABLED then return (FALSE, FALSE);
```

```
AArch32.BreakpointValueMatch linked_to)
```

```
// Otherwise the dbgtype value returned by AArch32.ReservedBreakpointType is valid. // Determine what to compare against. match_addr = (dbgtype == '0x0x'); mismatch = (dbgtype == '010x'); match_vmid = (dbgtype == '10xx'); match_cid1 = (dbgtype == 'xx1x'); match_cid2 = (dbgtype == '11xx'); linking_enabled = (dbgtype == 'xxx1'); // If called from StateMatch, is is CONSTRAINED UNPREDICTABLE if the // breakpoint is not programmed with linking enabled. if linked_to && !linking_enabled then if !ConstrainUnpredictableBool(Unpredictable_BPLINKINGDISABLED) then return (FALSE, FALSE); // If called from BreakpointMatch return FALSE for Linked context ID and/or VMID matches. if !linked_to && linking_enabled && !match_addr then return (FALSE, FALSE); boolean bvr_match = FALSE; boolean bxvr_match = FALSE; // Do the comparison. if match_addr then constant integer byte = UInt(vaddress<1:0>); assert byte IN {0,2}; // "vaddress" is halfword aligned constant boolean byte_select_match = (DBGBCR[n].BAS<byte> == '1'); bvr_match = (vaddress<31:2> == DBGBVR[n]<31:2>) && byte_select_match; elsif match_cid1 then bvr_match = (PSTATE.EL != EL2 && CONTEXTIDR == DBGBVR[n]<31:0>); if match_vmid then bits(16) vmid; bits(16) bvr_vmid; if ELUsingAArch32(EL2) then vmid = ZeroExtend(VTTBR.VMID, 16); bvr_vmid = ZeroExtend(DBGBXVR[n]<7:0>, 16); elsif !IsFeatureImplemented(FEAT_VMID16) || VTCR_EL2.VS == '0' then vmid = ZeroExtend(VTTBR_EL2.VMID<7:0>, 16); bvr_vmid = ZeroExtend(DBGBXVR[n]<7:0>, 16); else vmid = VTTBR_EL2.VMID; bvr_vmid = DBGBXVR[n]<15:0>; bxvr_match = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && vmid == bvr_vmid); elsif match_cid2 then bxvr_match = (PSTATE.EL != EL3 && EL2Enabled() && !ELUsingAArch32(EL2) && DBGBXVR[n]<31:0> == CONTEXTIDR_EL2<31:0>); bvr_match_valid = (match_addr || match_cid1); bxvr_match_valid = (match_vmid || match_cid2); match = (!bxvr_match_valid || bxvr_match) && (!bvr_match_valid || bvr_match); return (match && !mismatch, !match && mismatch);
```

## J1.2.1.5 AArch32.ReservedBreakpointType

```
// AArch32.ReservedBreakpointType() // ================================
```

```
// Checks if the given DBGBCR<n>.BT value is reserved and will generate Constrained Unpredictable // behavior, otherwise returns Constraint_NONE. (Constraint, bits(4)) AArch32.ReservedBreakpointType(integer n, bits(4) bt_in) bits(4) bt = bt_in; boolean reserved = FALSE; context_aware = IsContextAwareBreakpoint(n); // Address mismatch if bt == '010x' && HaltOnBreakpointOrWatchpoint() then reserved = TRUE; // Context matching if bt != '0x0x' && !context_aware then reserved = TRUE; // EL2 extension if bt == '1xxx' && !HaveEL(EL2) then reserved = TRUE; // Context matching if (bt IN {'011x','11xx'} && !IsFeatureImplemented(FEAT_VHE) && !IsFeatureImplemented(FEAT_Debugv8p2)) then reserved = TRUE; if reserved then Constraint c; (c, bt) = ConstrainUnpredictableBits(Unpredictable_RESBPTYPE, 4); assert c IN {Constraint_DISABLED, Constraint_UNKNOWN}; if c == Constraint_DISABLED then return (c, bits(4) UNKNOWN); // Otherwise the value returned by ConstrainUnpredictableBits must be a not-reserved value return (Constraint_NONE, bt);
```

```
J1.2.1.6 AArch32.StateMatch register.
```

```
// AArch32.StateMatch() // ==================== // Determine whether a breakpoint or watchpoint is enabled in the current mode and state. boolean AArch32.StateMatch(bits(2) ssc_in, bit hmc_in, bits(2) pxc_in, boolean linked_in, integer linked_n_in, boolean isbreakpnt, AccessDescriptor accdesc) // "ssc_in","hmc_in","pxc_in" are the control fields from the DBGBCR[n] or DBGWCR[n] // "linked_in" is TRUE if this is a linked breakpoint/watchpoint type. // "linked_n_in" is the linked breakpoint number from the DBGBCR[n] or DBGWCR[n] register. // "isbreakpnt" is TRUE for breakpoints, FALSE for watchpoints. // "accdesc" describes the properties of the access being matched. bit hmc = hmc_in; bits(2) ssc = ssc_in; bits(2) pxc = pxc_in; boolean linked = linked_in; integer linked_n = linked_n_in; // If parameters are set to a reserved type, behaves as either disabled or a defined type Constraint c; // SSCE value discarded as there is no SSCE bit in AArch32. (c, ssc, -, hmc, pxc) = CheckValidStateMatch(ssc, '0', hmc, pxc, isbreakpnt); if c == Constraint_DISABLED then return FALSE; // Otherwise the hmc,ssc,pxc values are either valid or the values returned by // CheckValidStateMatch are valid. pl2_match = HaveEL(EL2) && ((hmc == '1' && (ssc:pxc != '1000')) || ssc == '11'); pl1_match = pxc<0> == '1';
```

```
pl0_match = pxc<1> == '1'; ssu_match = isbreakpnt && hmc == '0' && pxc == '00' && ssc != '11'; boolean priv_match; if ssu_match then priv_match = PSTATE.M IN {M32_User,M32_Svc,M32_System}; else case accdesc.el of when EL3 priv_match = pl1_match; // EL3 and EL1 are both PL1 when EL2 priv_match = pl2_match; when EL1 priv_match = pl1_match; when EL0 priv_match = pl0_match; // Security state match boolean ss_match; case ssc of when '00' ss_match = TRUE; // Both when '01' ss_match = accdesc.ss == SS_NonSecure; // Non-secure only when '10' ss_match = accdesc.ss == SS_Secure; // Secure only when '11' ss_match = (hmc == '1' || accdesc.ss == SS_Secure); // HMC=1 -> Both, // HMC=0 -> Secure only boolean linked_match = FALSE; if linked then // "linked_n" must be an enabled context-aware breakpoint unit. // If it is not context-aware then it is CONSTRAINED UNPREDICTABLE whether // this gives no match, gives a match without linking, or linked_n is mapped to some // UNKNOWN breakpoint that is context-aware. if !IsContextAwareBreakpoint(linked_n) then (first_ctx_cmp, last_ctx_cmp) = ContextAwareBreakpointRange(); (c, linked_n) = ConstrainUnpredictableInteger(first_ctx_cmp, last_ctx_cmp, Unpredictable_BPNOTCTXCMP); assert c IN {Constraint_DISABLED, Constraint_NONE, Constraint_UNKNOWN}; case c of when Constraint_DISABLED return FALSE; // Disabled when Constraint_NONE linked = FALSE; // No linking // Otherwise ConstrainUnpredictableInteger returned a context-aware breakpoint vaddress = bits(32) UNKNOWN; linked_to = TRUE; (linked_match,-) = AArch32.BreakpointValueMatch(linked_n, vaddress, linked_to); return priv_match && ss_match && (!linked || linked_match);
```

## J1.2.1.7 AArch32.GenerateDebugExceptions // AArch32.GenerateDebugExceptions() // ================================= boolean AArch32.GenerateDebugExceptions() ss = CurrentSecurityState(); return AArch32.GenerateDebugExceptionsFrom(PSTATE.EL, ss); J1.2.1.8 AArch32.GenerateDebugExceptionsFrom // AArch32.GenerateDebugExceptionsFrom() // ===================================== boolean AArch32.GenerateDebugExceptionsFrom(bits(2) from\_el, SecurityState from\_state) if !ELUsingAArch32(DebugTargetFrom(from\_state)) then mask = '0'; // No PSTATE.D in AArch32 state

```
return AArch64.GenerateDebugExceptionsFrom(from_el, from_state, mask); if DBGOSLSR.OSLK == '1' || DoubleLockStatus() || Halted() then return FALSE; boolean enabled; if HaveEL(EL3) && from_state == SS_Secure then assert from_el != EL2; // Secure EL2 always uses AArch64 if IsSecureEL2Enabled() then // Implies that EL3 and EL2 both using AArch64 enabled = MDCR_EL3.SDD == '0'; else spd = if ELUsingAArch32(EL3) then SDCR.SPD else MDCR_EL3.SPD32; if spd<1> == '1' then enabled = spd<0> == '1'; else // SPD == 0b01 is reserved, but behaves the same as 0b00. enabled = AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled(); if from_el == EL0 then enabled = enabled || SDER.SUIDEN == '1'; else enabled = from_el != EL2; return enabled;
```

```
J1.2.1.9 AArch32.IncrementCycleCounter // AArch32.IncrementCycleCounter() // =============================== // Increment the cycle counter and possibly set overflow bits. AArch32.IncrementCycleCounter() if !CountPMUEvents(CYCLE_COUNTER_ID) then return; bit d = PMCR.D; // Check divide-by-64 bit lc = PMCR.LC; // Effective value of 'D' bit is 0 when Effective value of LC is '1' if lc == '1' then d = '0'; if d == '1' && !HasElapsed64Cycles() then return; constant integer old_value = UInt(PMCCNTR); constant integer new_value = old_value + 1; PMCCNTR = new_value<63:0>; constant integer ovflw = if lc == '1' then 64 else 32; if old_value<64:ovflw> != new_value<64:ovflw> then PMOVSSET.C = '1'; return; J1.2.1.10 AArch32.IncrementEventCounter // AArch32.IncrementEventCounter() // =============================== // Increment the specified event counter 'idx' by the specified amount 'increment'. // 'Vm' is the value event counter 'idx-1' is being incremented by if 'idx' is odd, // zero otherwise. // Returns the amount the counter was incremented by. integer AArch32.IncrementEventCounter(integer idx, integer increment_in, integer Vm) if HaveAArch64() then // Force the counter to be incremented as a 64-bit counter. return AArch64.IncrementEventCounter(idx, increment_in, Vm); // In this model, event counters in an AArch32-only implementation are 32 bits and
```

## // the LP bits are RES0 in this model, even if FEAT\_PMUv3p5 is implemented. integer old\_value; integer new\_value; old\_value = UInt(PMEVCNTR[idx]); constant integer increment = PMUCountValue(idx, increment\_in, Vm); new\_value = old\_value + increment; PMEVCNTR[idx] = new\_value&lt;31:0&gt;; constant integer ovflw = 32; if old\_value&lt;64:ovflw&gt; != new\_value&lt;64:ovflw&gt; then PMOVSSET&lt;idx&gt; = '1'; // Check for the CHAIN event from an even counter if (idx&lt;0&gt; == '0' &amp;&amp; idx + 1 &lt; NUM\_PMU\_COUNTERS &amp;&amp; (GetPMUCounterRange(idx) == GetPMUCounterRange(idx+1) || ConstrainUnpredictableBool(Unpredictable\_COUNT\_CHAIN))) then // If PMU counters idx and idx+1 are not in same range, // it is CONSTRAINED UNPREDICTABLE if CHAIN event is counted PMUEvent(PMU\_EVENT\_CHAIN, 1, idx + 1); return increment; J1.2.1.11 AArch32.PMUCycle // AArch32.PMUCycle() // ================== // Called at the end of each cycle to increment event counters and // check for PMU overflow. In pseudocode, a cycle ends after the // execution of the operational pseudocode. AArch32.PMUCycle() if HaveAArch64() then AArch64.PMUCycle(); return; if !IsFeatureImplemented(FEAT\_PMUv3) then return; PMUEvent(PMU\_EVENT\_CPU\_CYCLES); constant integer counters = NUM\_PMU\_COUNTERS; integer Vm = 0; if counters != 0 then for idx = 0 to counters - 1 if CountPMUEvents(idx) then constant integer accumulated = PMUEventAccumulator[idx]; if (idx MOD 2) == 0 then Vm = 0; Vm = AArch32.IncrementEventCounter(idx, accumulated, Vm); PMUEventAccumulator[idx] = 0; AArch32.IncrementCycleCounter(); CheckForPMUOverflow(); J1.2.1.12 AArch32.EnterHypModeInDebugState ELUsingAArch32(EL2);

```
// AArch32.EnterHypModeInDebugState() // ================================== // Take an exception in Debug state to Hyp mode. AArch32.EnterHypModeInDebugState(ExceptionRecord except) SynchronizeContext(); assert HaveEL(EL2) && CurrentSecurityState() == SS_NonSecure && AArch32.ReportHypEntry(except); AArch32.WriteMode(M32_Hyp); SPSR_curr[] = bits(32) UNKNOWN;
```

```
ELR_hyp = bits(32) UNKNOWN; // In Debug state, the PE always execute T32 instructions when in AArch32 state, and // PSTATE.{SS,A,I,F} are not observable so behave as UNKNOWN. PSTATE.T = '1'; // PSTATE.J is RES0 PSTATE.<SS,A,I,F> = bits(4) UNKNOWN; DLR = bits(32) UNKNOWN; DSPSR = bits(32) UNKNOWN; if IsFeatureImplemented(FEAT_Debugv8p9) then DSPSR2 = bits(32) UNKNOWN; PSTATE.E = HSCTLR.EE; PSTATE.IL = '0'; PSTATE.IT = '00000000'; if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = bit UNKNOWN; EDSCR.ERR = '1'; UpdateEDSCRFields(); EndOfInstruction();
```

## J1.2.1.13 AArch32.EnterModeInDebugState

```
// AArch32.EnterModeInDebugState() // =============================== // Take an exception in Debug state to a mode other than Monitor and Hyp mode. AArch32.EnterModeInDebugState(bits(5) target_mode) SynchronizeContext(); assert ELUsingAArch32(EL1) && PSTATE.EL != EL2; if PSTATE.M == M32_Monitor then SCR.NS = '0'; AArch32.WriteMode(target_mode); SPSR_curr[] = bits(32) UNKNOWN; R[14] = bits(32) UNKNOWN; // In Debug state, the PE always execute T32 instructions when in AArch32 state, and // PSTATE.{SS,A,I,F} are not observable so behave as UNKNOWN. PSTATE.T = '1'; // PSTATE.J is RES0 PSTATE.<SS,A,I,F> = bits(4) UNKNOWN; DLR = bits(32) UNKNOWN; DSPSR = bits(32) UNKNOWN; if IsFeatureImplemented(FEAT_Debugv8p9) then DSPSR2 = bits(32) UNKNOWN; PSTATE.E = SCTLR.EE; PSTATE.IL = '0'; PSTATE.IT = '00000000'; if IsFeatureImplemented(FEAT_PAN) && SCTLR.SPAN == '0' then PSTATE.PAN = '1'; if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = bit UNKNOWN; EDSCR.ERR = '1'; UpdateEDSCRFields(); // Update EDSCR PE state flags. EndOfInstruction();
```

## J1.2.1.14 AArch32.EnterMonitorModeInDebugState

```
// AArch32.EnterMonitorModeInDebugState() // ====================================== // Take an exception in Debug state to Monitor mode. AArch32.EnterMonitorModeInDebugState() SynchronizeContext(); assert HaveEL(EL3) && ELUsingAArch32(EL3); from_secure = CurrentSecurityState() == SS_Secure; if PSTATE.M == M32_Monitor then SCR.NS = '0'; AArch32.WriteMode(M32_Monitor); SPSR_curr[] = bits(32) UNKNOWN;
```

```
R[14] = bits(32) UNKNOWN; // In Debug state, the PE always execute T32 instructions when in AArch32 state, and // PSTATE.{SS,A,I,F} are not observable so behave as UNKNOWN. PSTATE.T = '1'; // PSTATE.J is RES0 PSTATE.<SS,A,I,F> = bits(4) UNKNOWN; PSTATE.E = SCTLR.EE; PSTATE.IL = '0'; PSTATE.IT = '00000000'; if IsFeatureImplemented(FEAT_PAN) then if !from_secure then PSTATE.PAN = '0'; elsif SCTLR.SPAN == '0' then PSTATE.PAN = '1'; if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = bit UNKNOWN; DLR = bits(32) UNKNOWN; DSPSR = bits(32) UNKNOWN; if IsFeatureImplemented(FEAT_Debugv8p9) then DSPSR2 = bits(32) UNKNOWN; EDSCR.ERR = '1'; UpdateEDSCRFields(); // Update EDSCR PE state flags. EndOfInstruction(); AArch32.WatchpointByteMatch
```

## J1.2.1.15

```
// AArch32.WatchpointByteMatch() // ============================= boolean AArch32.WatchpointByteMatch(integer n, bits(32) vaddress) constant integer dbgtop = 31; constant integer cmpbottom = if DBGWVR[n]<2> == '1' then 2 else 3; // Word or doubleword bottom = cmpbottom; constant integer select = UInt(vaddress<cmpbottom-1:0>); byte_select_match = (DBGWCR[n].BAS<select> != '0'); mask = UInt(DBGWCR[n].MASK); // If DBGWCR[n].MASK is a nonzero value and DBGWCR[n].BAS is not set to '11111111', or // DBGWCR[n].BAS specifies a non-contiguous set of bytes behavior is CONSTRAINED // UNPREDICTABLE. if mask > 0 && !IsOnes(DBGWCR[n].BAS) then byte_select_match = ConstrainUnpredictableBool(Unpredictable_WPMASKANDBAS); else LSB = (DBGWCR[n].BAS AND NOT(DBGWCR[n].BAS - 1)); MSB = (DBGWCR[n].BAS + LSB); if !IsZero(MSB AND (MSB - 1)) then // Not contiguous byte_select_match = ConstrainUnpredictableBool(Unpredictable_WPBASCONTIGUOUS); bottom = 3; // For the whole doubleword // If the address mask is set to a reserved value, the behavior is CONSTRAINED UNPREDICTABLE. if mask > 0 && mask <= 2 then Constraint c; (c, mask) = ConstrainUnpredictableInteger(3, 31, Unpredictable_RESWPMASK); assert c IN {Constraint_DISABLED, Constraint_NONE, Constraint_UNKNOWN}; case c of when Constraint_DISABLED return FALSE; // Disabled when Constraint_NONE mask = 0; // No masking // Otherwise the value returned by ConstrainUnpredictableInteger is a not-reserved value constant integer cmpmsb = dbgtop; constant integer cmplsb = if mask > bottom then mask else bottom; constant integer bottombit = bottom; boolean WVR_match = (vaddress<cmpmsb:cmplsb> == DBGWVR[n]<cmpmsb:cmplsb>); if mask > bottom then // If masked bits of DBGWVR[n] are not zero, the behavior is CONSTRAINED UNPREDICTABLE. if WVR_match && !IsZero(DBGWVR[n]<cmplsb-1:bottombit>) then WVR_match = ConstrainUnpredictableBool(Unpredictable_WPMASKEDBITS);
```

```
return (WVR_match && byte_select_match);
```

## J1.2.1.16 AArch32.WatchpointMatch

```
// AArch32.WatchpointMatch() // ========================= // Watchpoint matching in an AArch32 translation regime. WatchpointInfo AArch32.WatchpointMatch(integer n, bits(32) vaddress, integer size, AccessDescriptor accdesc) assert ELUsingAArch32(S1TranslationRegime()); assert n < NumWatchpointsImplemented(); constant boolean enabled = DBGWCR[n].E == '1'; linked = DBGWCR[n].WT == '1'; isbreakpnt = FALSE; linked_n = UInt(DBGWCR_EL1[n].LBN); state_match = AArch32.StateMatch(DBGWCR[n].SSC, DBGWCR[n].HMC, DBGWCR[n].PAC, linked, linked_n, isbreakpnt, accdesc); WatchpointInfo watchptinfo; boolean ls_match; case DBGWCR[n].LSC<1:0> of when '00' ls_match = FALSE; when '01' ls_match = accdesc.read; when '10' ls_match = accdesc.write || accdesc.acctype == AccessType_DC; when '11' ls_match = TRUE; boolean value_match = FALSE; watchptinfo.vaddress = ZeroExtend(vaddress, 64); for byte = 0 to size - 1 if (!value_match && !AddressInNaturallyAlignedBlock(watchptinfo.vaddress, ZeroExtend(vaddress + byte, 64))) then // Watchpoint should report an address which is in // the naturally aligned block of the matched address. watchptinfo.vaddress = ZeroExtend(vaddress + byte, 64); value_match = value_match || AArch32.WatchpointByteMatch(n, vaddress + byte); watchptinfo.watchpt_num = n; watchptinfo.value_match = value_match && state_match && ls_match && enabled; return watchptinfo;
```

## J1.2.2 aarch32/exceptions

This section includes the following pseudocode functions:

- AArch32.Abort
- AArch32.AbortSyndrome
- AArch32.CheckPCAlignment
- AArch32.CommonFaultStatus
- AArch32.ReportDataAbort
- AArch32.ReportPrefetchAbort
- AArch32.TakeDataAbortException
- AArch32.TakePrefetchAbortException
- AArch32.TakePhysicalFIQException
- AArch32.TakePhysicalIRQException

- AArch32.TakePhysicalSErrorException
- AArch32.TakeVirtualFIQException
- AArch32.TakeVirtualIRQException
- AArch32.TakeVirtualSErrorException
- AArch32.SoftwareBreakpoint
- DebugException
- AArch32.CheckAdvSIMDOrFPRegisterTraps
- AArch32.ExceptionClass
- AArch32.GeneralExceptionsToAArch64
- AArch32.ReportHypEntry
- AArch32.ResetControlRegisters
- AArch32.TakeReset
- ExcVectorBase
- AArch32.FPTrappedException
- AArch32.CallHypervisor
- AArch32.CallSupervisor
- AArch32.TakeHVCException
- AArch32.TakeSMCException
- AArch32.TakeSVCException
- AArch32.EnterHypMode
- AArch32.EnterMode
- AArch32.EnterMonitorMode
- AArch32.CheckAdvSIMDOrFPEnabled
- AArch32.CheckFPAdvSIMDTrap
- AArch32.CheckForSMCUndefOrTrap
- AArch32.CheckForSVCTrap
- AArch32.CheckForWFxTrap
- AArch32.CheckITEnabled
- AArch32.CheckIllegalState
- AArch32.CheckSETENDEnabled
- AArch32.SystemAccessTrap
- AArch32.SystemAccessTrapSyndrome
- AArch32.TakeHypTrapException
- AArch32.TakeMonitorTrapException
- AArch32.TakeUndefInstrException
- AArch32.Undefined

## J1.2.2.1 AArch32.Abort

```
// AArch32.Abort() // =============== // Abort and Debug exception handling in an AArch32 translation regime. AArch32.Abort(FaultRecord fault) // Check if routed to AArch64 state route_to_aarch64 = ((IsExternalAbort(fault) && !ELUsingAArch32(SyncExternalAbortTarget(fault))) || (PSTATE.EL == EL0 && !ELUsingAArch32(EL1))); if !route_to_aarch64 && EL2Enabled() && !ELUsingAArch32(EL2) then
```

## route\_to\_aarch64 = (HCR\_EL2.TGE == '1' || IsSecondStage(fault) || (IsDebugException(fault) &amp;&amp; MDCR\_EL2.TDE == '1')); if route\_to\_aarch64 then AArch64.Abort(fault); if fault.accessdesc.acctype == AccessType\_IFETCH then AArch32.TakePrefetchAbortException(fault); else AArch32.TakeDataAbortException(fault); J1.2.2.2 AArch32.AbortSyndrome // AArch32.AbortSyndrome() // ======================= // Creates an exception syndrome record for Abort exceptions // taken to Hyp mode // from an AArch32 translation regime. ExceptionRecord AArch32.AbortSyndrome(Exception exceptype, FaultRecord fault, bits(2) target\_el) except = ExceptionSyndrome(exceptype); except.syndrome.iss = AArch32.FaultSyndrome(exceptype, fault); if exceptype == Exception\_Watchpoint then except.vaddress = fault.watchptinfo.vaddress; else except.vaddress = ZeroExtend(fault.vaddress, 64); if IPAValid(fault) then except.ipavalid = TRUE; except.NS = if fault.ipaddress.paspace == PAS\_NonSecure then '1' else '0'; except.ipaddress = ZeroExtend(fault.ipaddress.address, 56); else except.ipavalid = FALSE; return except; J1.2.2.3 AArch32.CheckPCAlignment // AArch32.CheckPCAlignment() // ========================== AArch32.CheckPCAlignment() constant bits(32) pc = ThisInstrAddr(32); if (CurrentInstrSet() == InstrSet\_A32 &amp;&amp; pc&lt;1&gt; == '1') || pc&lt;0&gt; == '1' then if AArch32.GeneralExceptionsToAArch64() then AArch64.PCAlignmentFault(); constant AccessDescriptor accdesc = CreateAccDescIFetch(); FaultRecord fault = NoFault(accdesc, ZeroExtend(pc, 64)); // Generate an Alignment fault Prefetch Abort exception fault.statuscode = Fault\_Alignment; AArch32.Abort(fault); J1.2.2.4 AArch32.CommonFaultStatus // AArch32.CommonFaultStatus() // =========================== // Return the common part of the fault status on reporting a Data // or Prefetch Abort. bits(32) AArch32.CommonFaultStatus(FaultRecord fault, boolean long\_format) bits(32) target = Zeros(32);

```
if IsFeatureImplemented(FEAT_RAS) && IsAsyncAbort(fault) then constant ErrorState errstate = PEErrorState(fault); target<15:14> = AArch32.EncodeAsyncErrorSyndrome(errstate); // AET if IsExternalAbort(fault) then target<12> = fault.extflag; // ExT target<9> = if long_format then '1' else '0'; // LPAE if long_format then // Long-descriptor format target<5:0> = EncodeLDFSC(fault.statuscode, fault.level); // STATUS else // Short-descriptor format target<10,3:0> = EncodeSDFSC(fault.statuscode, fault.level); // FS return target;
```

## J1.2.2.5 AArch32.ReportDataAbort

```
// AArch32.ReportDataAbort() // ========================= // Report syndrome information for aborts taken to modes other than Hyp mode. AArch32.ReportDataAbort(boolean route_to_monitor, FaultRecord fault) boolean long_format; if route_to_monitor && CurrentSecurityState() != SS_Secure then long_format = ((TTBCR_S.EAE == '1') || (IsExternalSyncAbort(fault) && ((PSTATE.EL == EL2 || TTBCR.EAE == '1') || (fault.secondstage && (boolean IMPLEMENTATION_DEFINED "Report abort using Long-descriptor format"))))); else long_format = TTBCR.EAE == '1'; bits(32) syndrome = AArch32.CommonFaultStatus(fault, long_format); // bits of syndrome that are not common to I and D side if fault.accessdesc.acctype IN {AccessType_DC, AccessType_IC, AccessType_AT} then syndrome<13> = '1'; // CM syndrome<11> = '1'; // WnR else syndrome<11> = if fault.write then '1' else '0'; // WnR if !long_format then syndrome<7:4> = fault.domain; // Domain if fault.accessdesc.acctype == AccessType_IC then bits(32) i_syndrome; if (!long_format && boolean IMPLEMENTATION_DEFINED "Report I-cache maintenance fault in IFSR") then i_syndrome = syndrome; syndrome<10,3:0> = EncodeSDFSC(Fault_ICacheMaint, 1); else i_syndrome = bits(32) UNKNOWN; if route_to_monitor then IFSR_S = i_syndrome; else IFSR = i_syndrome; if route_to_monitor then DFSR_S = syndrome; DFAR_S = fault.vaddress<31:0>; else DFSR = syndrome; DFAR = fault.vaddress<31:0>; return;
```

## J1.2.2.6 AArch32.ReportPrefetchAbort

```
// AArch32.ReportPrefetchAbort() // ============================= // Report syndrome information for aborts taken to modes other than Hyp mode. AArch32.ReportPrefetchAbort(boolean route_to_monitor, FaultRecord fault) // The encoding used in the IFSR can be Long-descriptor format or Short-descriptor format. // Normally, the current translation table format determines the format. For an abort from // Non-secure state to Monitor mode, the IFSR uses the Long-descriptor format if any of the // following applies: // * The Secure TTBCR.EAE is set to 1. // * It is taken from Hyp mode. // * It is taken from EL1 or EL0, and the Non-secure TTBCR.EAE is set to 1. long_format = FALSE; if route_to_monitor && CurrentSecurityState() != SS_Secure then long_format = TTBCR_S.EAE == '1' || PSTATE.EL == EL2 || TTBCR.EAE == '1'; else long_format = TTBCR.EAE == '1'; constant bits(32) fsr = AArch32.CommonFaultStatus(fault, long_format); if route_to_monitor then IFSR_S = fsr; IFAR_S = fault.vaddress<31:0>; else IFSR = fsr; IFAR = fault.vaddress<31:0>; return;
```

```
J1.2.2.7 AArch32.TakeDataAbortException // AArch32.TakeDataAbortException() // ================================ AArch32.TakeDataAbortException(FaultRecord fault) bits(2) sea_target; if IsExternalAbort(fault) then sea_target = SyncExternalAbortTarget(fault); else sea_target = bits(2) UNKNOWN; route_to_monitor = IsExternalAbort(fault) && sea_target == EL3; route_to_hyp = (EL2Enabled() && PSTATE.EL IN {EL0, EL1} && (HCR.TGE == '1' || (IsExternalAbort(fault) && sea_target == EL2) || (IsDebugException(fault) && HDCR.TDE == '1') || IsSecondStage(fault))); constant bits(32) preferred_exception_return = ThisInstrAddr(32); constant integer vect_offset = 0x10; constant integer lr_offset = 8; if IsDebugException(fault) then DBGDSCRext.MOE = fault.debugmoe; if route_to_monitor then AArch32.ReportDataAbort(route_to_monitor, fault); AArch32.EnterMonitorMode(preferred_exception_return, lr_offset, vect_offset); elsif PSTATE.EL == EL2 || route_to_hyp then except = AArch32.AbortSyndrome(Exception_DataAbort, fault, EL2); if PSTATE.EL == EL2 then AArch32.EnterHypMode(except, preferred_exception_return, vect_offset); else AArch32.EnterHypMode(except, preferred_exception_return, 0x14);
```

```
else AArch32.ReportDataAbort(route_to_monitor, fault); AArch32.EnterMode(M32_Abort, preferred_exception_return, lr_offset, vect_offset);
```

## J1.2.2.8 AArch32.TakePrefetchAbortException

```
// AArch32.TakePrefetchAbortException() // ==================================== AArch32.TakePrefetchAbortException(FaultRecord fault) bits(2) sea_target; if IsExternalAbort(fault) then sea_target = SyncExternalAbortTarget(fault); else sea_target = bits(2) UNKNOWN; route_to_monitor = IsExternalAbort(fault) && sea_target == EL3; route_to_hyp = (EL2Enabled() && PSTATE.EL IN {EL0, EL1} && (HCR.TGE == '1' || (IsExternalAbort(fault) && sea_target == EL2) || (IsDebugException(fault) && HDCR.TDE == '1') || IsSecondStage(fault))); ExceptionRecord except; constant bits(32) preferred_exception_return = ThisInstrAddr(32); vect_offset = 0x0C; lr_offset = 4; if IsDebugException(fault) then DBGDSCRext.MOE = fault.debugmoe; if route_to_monitor then AArch32.ReportPrefetchAbort(route_to_monitor, fault); AArch32.EnterMonitorMode(preferred_exception_return, lr_offset, vect_offset); elsif PSTATE.EL == EL2 || route_to_hyp then if fault.statuscode == Fault_Alignment then // PC Alignment fault except = ExceptionSyndrome(Exception_PCAlignment); except.vaddress = ThisInstrAddr(64); else except = AArch32.AbortSyndrome(Exception_InstructionAbort, fault, EL2); if PSTATE.EL == EL2 then AArch32.EnterHypMode(except, preferred_exception_return, vect_offset); else AArch32.EnterHypMode(except, preferred_exception_return, 0x14); else AArch32.ReportPrefetchAbort(route_to_monitor, fault); AArch32.EnterMode(M32_Abort, preferred_exception_return, lr_offset, vect_offset);
```

## J1.2.2.9 AArch32.TakePhysicalFIQException

```
// AArch32.TakePhysicalFIQException() // ================================== AArch32.TakePhysicalFIQException() // Check if routed to AArch64 state route_to_aarch64 = PSTATE.EL == EL0 && !ELUsingAArch32(EL1); if !route_to_aarch64 && EL2Enabled() && !ELUsingAArch32(EL2) then route_to_aarch64 = HCR_EL2.TGE == '1' || (HCR_EL2.FMO if !route_to_aarch64 && HaveEL(EL3) && !ELUsingAArch32(EL3) then route_to_aarch64 = SCR_EL3.FIQ == '1';
```

```
== '1' && !IsInHost()); if route_to_aarch64 then AArch64.TakePhysicalFIQException();
```

```
route_to_monitor = HaveEL(EL3) && SCR.FIQ == '1'; route_to_hyp = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && (HCR.TGE == '1' || HCR.FMO == '1')); constant bits(32) preferred_exception_return = ThisInstrAddr(32); vect_offset = 0x1C; lr_offset = 4; if route_to_monitor then AArch32.EnterMonitorMode(preferred_exception_return, lr_offset, vect_offset); elsif PSTATE.EL == EL2 || route_to_hyp then except = ExceptionSyndrome(Exception_FIQ); AArch32.EnterHypMode(except, preferred_exception_return, vect_offset); else AArch32.EnterMode(M32_FIQ, preferred_exception_return, lr_offset, vect_offset);
```

## J1.2.2.10 AArch32.TakePhysicalIRQException

```
// AArch32.TakePhysicalIRQException() // ================================== // Take an enabled physical IRQ exception. AArch32.TakePhysicalIRQException() // Check if routed to AArch64 state route_to_aarch64 = PSTATE.EL == EL0 && !ELUsingAArch32(EL1); if !route_to_aarch64 && EL2Enabled() && !ELUsingAArch32(EL2) then route_to_aarch64 = HCR_EL2.TGE == '1' || (HCR_EL2.IMO == '1' && !IsInHost()); if !route_to_aarch64 && HaveEL(EL3) && !ELUsingAArch32(EL3) then route_to_aarch64 = SCR_EL3.IRQ == '1'; if route_to_aarch64 then AArch64.TakePhysicalIRQException(); route_to_monitor = HaveEL(EL3) && SCR.IRQ == '1'; route_to_hyp = (PSTATE.EL IN {EL0, EL1} && EL2Enabled() && (HCR.TGE == '1' || HCR.IMO == '1')); constant bits(32) preferred_exception_return = ThisInstrAddr(32); vect_offset = 0x18; lr_offset = 4; if route_to_monitor then AArch32.EnterMonitorMode(preferred_exception_return, lr_offset, vect_offset); elsif PSTATE.EL == EL2 || route_to_hyp then except = ExceptionSyndrome(Exception_IRQ); AArch32.EnterHypMode(except, preferred_exception_return, vect_offset); else AArch32.EnterMode(M32_IRQ, preferred_exception_return, lr_offset, vect_offset);
```

## J1.2.2.11 AArch32.TakePhysicalSErrorException

```
// AArch32.TakePhysicalSErrorException() // ===================================== AArch32.TakePhysicalSErrorException(boolean implicit_esb) boolean masked; bits(2) target_el; (masked, target_el) = PhysicalSErrorTarget(); assert !masked; // Check if routed to AArch64 state if !ELUsingAArch32(target_el) then AArch64.TakePhysicalSErrorException(implicit_esb); constant bits(32) preferred_exception_return = ThisInstrAddr(32); constant integer vect_offset = 0x10;
```

```
constant FaultRecord fault = GetPendingPhysicalSError(); constant integer lr_offset = 8; except = AArch32.AbortSyndrome(Exception_DataAbort, fault, target_el); route_to_monitor = (target_el == EL3); if IsSErrorEdgeTriggered() then ClearPendingPhysicalSError(); case target_el of when EL3 AArch32.ReportDataAbort(route_to_monitor, fault); AArch32.EnterMonitorMode(preferred_exception_return, lr_offset, vect_offset); when EL2 if PSTATE.EL == EL2 then AArch32.EnterHypMode(except, preferred_exception_return, vect_offset); else AArch32.EnterHypMode(except, preferred_exception_return, 0x14); when EL1 AArch32.ReportDataAbort(route_to_monitor, fault); AArch32.EnterMode(M32_Abort, preferred_exception_return, lr_offset, vect_offset); otherwise Unreachable();
```

## J1.2.2.12 AArch32.TakeVirtualFIQException // AArch32.TakeVirtualFIQException() // ================================= AArch32.TakeVirtualFIQException() assert PSTATE.EL IN {EL0, EL1} &amp;&amp; EL2Enabled(); if ELUsingAArch32(EL2) then // Virtual IRQ enabled if TGE==0 and FMO==1 assert HCR.TGE == '0' &amp;&amp; HCR.FMO == '1'; else assert HCR\_EL2.TGE == '0' &amp;&amp; HCR\_EL2.FMO == '1'; // Check if routed to AArch64 state if PSTATE.EL == EL0 &amp;&amp; !ELUsingAArch32(EL1) then AArch64.TakeVirtualFIQException(); constant bits(32) preferred\_exception\_return = ThisInstrAddr(32); vect\_offset = 0x1C; lr\_offset = 4; AArch32.EnterMode(M32\_FIQ, preferred\_exception\_return, lr\_offset, vect\_offset); J1.2.2.13 AArch32.TakeVirtualIRQException // AArch32.TakeVirtualIRQException() // ================================= AArch32.TakeVirtualIRQException() assert PSTATE.EL IN {EL0, EL1} &amp;&amp; EL2Enabled(); if ELUsingAArch32(EL2) then // Virtual IRQs enabled if TGE==0 and IMO==1 assert HCR.TGE == '0' &amp;&amp; HCR.IMO == '1'; else assert HCR\_EL2.TGE == '0' &amp;&amp; HCR\_EL2.IMO == '1'; // Check if routed to AArch64 state if PSTATE.EL == EL0 &amp;&amp; !ELUsingAArch32(EL1) then AArch64.TakeVirtualIRQException(); constant bits(32) preferred\_exception\_return = ThisInstrAddr(32); vect\_offset = 0x18; lr\_offset = 4;

AArch32.EnterMode(M32\_IRQ, preferred\_exception\_return, lr\_offset, vect\_offset);

## J1.2.2.14 AArch32.TakeVirtualSErrorException

```
// AArch32.TakeVirtualSErrorException() // ==================================== AArch32.TakeVirtualSErrorException() assert PSTATE.EL IN {EL0, EL1} && EL2Enabled(); if ELUsingAArch32(EL2) then // Virtual SError enabled if TGE==0 and AMO==1 assert HCR.TGE == '0' && HCR.AMO == '1'; else assert HCR_EL2.TGE == '0' && HCR_EL2.AMO == '1'; // Check if routed to AArch64 state if PSTATE.EL == EL0 && !ELUsingAArch32(EL1) then AArch64.TakeVirtualSErrorException(); route_to_monitor = FALSE; constant bits(32) preferred_exception_return = ThisInstrAddr(32); vect_offset = 0x10; lr_offset = 8; vaddress = bits(32) UNKNOWN; parity = FALSE; constant Fault fault = Fault_AsyncExternal; constant integer level = integer UNKNOWN; bits(32) fsr = Zeros(32); if IsFeatureImplemented(FEAT_RAS) then if ELUsingAArch32(EL2) then fsr<15:14> = VDFSR.AET; fsr<12> = VDFSR.ExT; else fsr<15:14> = VSESR_EL2.AET; fsr<12> = VSESR_EL2.ExT; else fsr<12> = bit IMPLEMENTATION_DEFINED "Virtual External abort type"; if TTBCR.EAE == '1' then // Long-descriptor format fsr<9> = '1'; fsr<5:0> = EncodeLDFSC(fault, level); else // Short-descriptor format fsr<9> = '0'; fsr<10,3:0> = EncodeSDFSC(fault, level); DFSR = fsr; DFAR = bits(32) UNKNOWN; ClearPendingVirtualSError(); AArch32.EnterMode(M32_Abort, preferred_exception_return, lr_offset, vect_offset); J1.2.2.15 AArch32.SoftwareBreakpoint
```

```
// AArch32.SoftwareBreakpoint() // ============================ AArch32.SoftwareBreakpoint(bits(16) immediate) if (EL2Enabled() && !ELUsingAArch32(EL2) && (HCR_EL2.TGE == '1' || MDCR_EL2.TDE == '1')) || !ELUsingAArch32(EL1) then AArch64.SoftwareBreakpoint(immediate); accdesc = CreateAccDescIFetch(); fault = NoFault(accdesc, bits(64) UNKNOWN); fault.statuscode = Fault_Debug;
```

```
fault.debugmoe = DebugException_BKPT; AArch32.Abort(fault);
```

## J1.2.2.16 DebugException

```
// DebugException // ============== // Reason codes for debug exceptions, taken to AArch32 constant bits(4) DebugException_Breakpoint = '0001'; constant bits(4) DebugException_BKPT = '0011'; constant bits(4) DebugException_VectorCatch = '0101'; constant bits(4) DebugException_Watchpoint = '1010';
```

## J1.2.2.17 AArch32.CheckAdvSIMDOrFPRegisterTraps

```
// AArch32.CheckAdvSIMDOrFPRegisterTraps() // ======================================= // Check if an instruction that accesses an Advanced SIMD and // floating-point System register is trapped by an appropriate HCR.TIDx // ID group trap control. AArch32.CheckAdvSIMDOrFPRegisterTraps(bits(4) reg) if PSTATE.EL == EL1 && EL2Enabled() then tid0 = if ELUsingAArch32(EL2) then HCR.TID0 else HCR_EL2.TID0; tid3 = if ELUsingAArch32(EL2) then HCR.TID3 else HCR_EL2.TID3; if ((tid0 == '1' && reg == '0000') || // FPSID (tid3 == '1' && reg IN {'0101', '0110', '0111'})) then // MVFRx if ELUsingAArch32(EL2) then AArch32.SystemAccessTrap(M32_Hyp, 0x8); else AArch64.AArch32SystemAccessTrap(EL2, 0x8);
```

## J1.2.2.18 AArch32.ExceptionClass

```
// AArch32.ExceptionClass() // ======================== // Returns the Exception Class and Instruction Length fields to be reported in HSR (integer,bit) AArch32.ExceptionClass(Exception exceptype) il_is_valid = TRUE; integer ec; case exceptype of when Exception_Uncategorized ec = 0x00; il_is_valid = FALSE; when Exception_WFxTrap ec = 0x01; when Exception_CP15RTTrap ec = 0x03; when Exception_CP15RRTTrap ec = 0x04; when Exception_CP14RTTrap ec = 0x05; when Exception_CP14DTTrap ec = 0x06; when Exception_AdvSIMDFPAccessTrap ec = 0x07; when Exception_FPIDTrap ec = 0x08; when Exception_PACTrap ec = 0x09; when Exception_GPC ec = 0x1E; when Exception_CP14RRTTrap ec = 0x0C; when Exception_BranchTarget ec = 0x0D; when Exception_IllegalState ec = 0x0E; il_is_valid = FALSE; when Exception_SupervisorCall ec = 0x11; when Exception_HypervisorCall ec = 0x12; when Exception_MonitorCall ec = 0x13; when Exception_InstructionAbort
```

```
ec = if PSTATE.EL == EL2 then 0x21 else 0x20; il_is_valid = FALSE; when Exception_PCAlignment ec = 0x22; il_is_valid = FALSE; when Exception_DataAbort ec = if PSTATE.EL == EL2 then 0x25 else 0x24; when Exception_NV2DataAbort ec = 0x25; when Exception_FPTrappedException ec = 0x28; when Exception_Profiling ec = 0x3D; otherwise Unreachable(); bit il; if il_is_valid then il = if ThisInstrLength() == 32 then '1' else '0'; else il = '1'; return (ec,il); J1.2.2.19 AArch32.GeneralExceptionsToAArch64
```

```
// AArch32.GeneralExceptionsToAArch64() // ==================================== // Returns TRUE if exceptions normally routed to EL1 are being handled at an Exception // level using AArch64, because either EL1 is using AArch64 or TGE is in force and EL2 // is using AArch64. boolean AArch32.GeneralExceptionsToAArch64() return ((PSTATE.EL == EL0 && !ELUsingAArch32(EL1)) || (EL2Enabled() && !ELUsingAArch32(EL2) && HCR_EL2.TGE == '1'));
```

## J1.2.2.20 AArch32.ReportHypEntry

```
// AArch32.ReportHypEntry() // ======================== // Report syndrome information to Hyp mode registers. AArch32.ReportHypEntry(ExceptionRecord except) constant Exception exceptype = except.exceptype; (ec,il) = AArch32.ExceptionClass(exceptype); iss = except.syndrome.iss; iss2 = except.syndrome.iss2; // IL is not valid for Data Abort exceptions without valid instruction syndrome information if ec IN {0x24,0x25} && iss<24> == '0' then il = '1'; HSR = ec<5:0>:il:iss; if exceptype IN {Exception_InstructionAbort, Exception_PCAlignment} then HIFAR = except.vaddress<31:0>; HDFAR = bits(32) UNKNOWN; elsif exceptype == Exception_DataAbort then HIFAR = bits(32) UNKNOWN; HDFAR = except.vaddress<31:0>; if except.ipavalid then HPFAR<31:4> = except.ipaddress<39:12>; else HPFAR<31:4> = bits(28) UNKNOWN; return;
```

## J1.2.2.21 AArch32.ResetControlRegisters

```
// AArch32.ResetControlRegisters() // =============================== // Resets System registers and memory-mapped control registers that have architecturally-defined // reset values to those values. AArch32.ResetControlRegisters(boolean cold_reset);
```

## J1.2.2.22 AArch32.TakeReset

```
// AArch32.TakeReset() // =================== // Reset into AArch32 state AArch32.TakeReset(boolean cold_reset) assert !HaveAArch64(); // Enter the highest implemented Exception level in AArch32 state if HaveEL(EL3) then AArch32.WriteMode(M32_Svc); SCR.NS = '0'; // Secure state elsif HaveEL(EL2) then AArch32.WriteMode(M32_Hyp); else AArch32.WriteMode(M32_Svc); // Reset System registers in the coproc=0b111x encoding space // and other system components AArch32.ResetControlRegisters(cold_reset); FPEXC.EN = '0'; // Reset all other PSTATE fields, including instruction set and endianness according to the // SCTLR values produced by the above call to ResetControlRegisters() PSTATE.<A,I,F> = '111'; // All asynchronous exceptions masked PSTATE.IT = '00000000'; // IT block state reset if HaveEL(EL2) && !HaveEL(EL3) then PSTATE.T = HSCTLR.TE; // Instruction set: TE=0:A32, TE=1:T32. PSTATE.J is RES0. PSTATE.E = HSCTLR.EE; // Endianness: EE=0: little-endian, EE=1: big-endian. else PSTATE.T = SCTLR.TE; // Instruction set: TE=0:A32, TE=1:T32. PSTATE.J is RES0. PSTATE.E = SCTLR.EE; // Endianness: EE=0: little-endian, EE=1: big-endian. PSTATE.IL = '0'; // Clear Illegal Execution state bit // All registers, bits and fields not reset by the above pseudocode or by the BranchTo() call // below are UNKNOWN bitstrings after reset. In particular, the return information registers // R14 or ELR_hyp and SPSR have UNKNOWN values, so that it // is impossible to return from a reset in an architecturally defined way. AArch32.ResetGeneralRegisters(); if IsFeatureImplemented(FEAT_SME) || IsFeatureImplemented(FEAT_SVE) then ResetSVERegisters(); else AArch32.ResetSIMDFPRegisters(); AArch32.ResetSpecialRegisters(); ResetExternalDebugRegisters(cold_reset); bits(32) rv; // IMPLEMENTATION DEFINED reset vector if HaveEL(EL3) then if MVBAR<0> == '1' then // Reset vector in MVBAR rv = MVBAR<31:1>:'0'; else rv = bits(32) IMPLEMENTATION_DEFINED "reset vector address"; else
```

```
rv = RVBAR<31:1>:'0'; // The reset vector must be correctly aligned assert rv<0> == '0' && (PSTATE.T == '1' || rv<1> == '0'); constant boolean branch_conditional = FALSE; EDPRSR.R = '0'; // Leaving Reset State. BranchTo(rv, BranchType_RESET, branch_conditional);
```

## J1.2.2.23 ExcVectorBase

```
// ExcVectorBase() // =============== bits(32) ExcVectorBase() if SCTLR.V == '1' then // Hivecs selected, base = 0xFFFF0000 return Ones(16):Zeros(16); else return VBAR<31:5>:Zeros(5);
```

## J1.2.2.24 AArch32.FPTrappedException

```
// AArch32.FPTrappedException() // ============================ AArch32.FPTrappedException(bits(8) accumulated_exceptions) if AArch32.GeneralExceptionsToAArch64() then is_ase = FALSE; element = 0; AArch64.FPTrappedException(is_ase, accumulated_exceptions); FPEXC.DEX = '1'; FPEXC.TFV = '1'; FPEXC<7,4:0> = accumulated_exceptions<7,4:0>; // IDF,IXF,UFF,OFF,DZF,IOF FPEXC<10:8> = '111'; // VECITR is RES1 AArch32.TakeUndefInstrException();
```

## J1.2.2.25 AArch32.CallHypervisor

```
// AArch32.CallHypervisor() // ======================== // Performs a HVC call AArch32.CallHypervisor(bits(16) immediate) assert HaveEL(EL2); if !ELUsingAArch32(EL2) then AArch64.CallHypervisor(immediate); else AArch32.TakeHVCException(immediate);
```

## J1.2.2.26 AArch32.CallSupervisor

```
// AArch32.CallSupervisor() // ======================== // Calls the Supervisor AArch32.CallSupervisor(bits(16) immediate_in) bits(16) immediate = immediate_in; if CurrentCond() != '1110' then
```

```
immediate = bits(16) UNKNOWN; if AArch32.GeneralExceptionsToAArch64() then AArch64.CallSupervisor(immediate); else AArch32.TakeSVCException(immediate);
```

## J1.2.2.27 AArch32.TakeHVCException

```
// AArch32.TakeHVCException() // ========================== AArch32.TakeHVCException(bits(16) immediate) assert HaveEL(EL2) && ELUsingAArch32(EL2); AArch32.ITAdvance(); SSAdvance(); constant bits(32) preferred_exception_return = NextInstrAddr(32); vect_offset = 0x08; except = ExceptionSyndrome(Exception_HypervisorCall); except.syndrome.iss<15:0> = immediate; if PSTATE.EL == EL2 then AArch32.EnterHypMode(except, preferred_exception_return, vect_offset); else AArch32.EnterHypMode(except, preferred_exception_return, 0x14);
```

## J1.2.2.28 AArch32.TakeSMCException

```
// AArch32.TakeSMCException() // ========================== AArch32.TakeSMCException() assert HaveEL(EL3) && ELUsingAArch32(EL3); AArch32.ITAdvance(); HSAdvance(); SSAdvance(); constant bits(32) preferred_exception_return = NextInstrAddr(32); vect_offset = 0x08; lr_offset = 0; AArch32.EnterMonitorMode(preferred_exception_return, lr_offset, vect_offset);
```

## J1.2.2.29 AArch32.TakeSVCException

```
// AArch32.TakeSVCException() // ========================== AArch32.TakeSVCException(bits(16) immediate) AArch32.ITAdvance(); SSAdvance(); route_to_hyp = PSTATE.EL == EL0 && EL2Enabled() && HCR.TGE == '1'; constant bits(32) preferred_exception_return = NextInstrAddr(32); vect_offset = 0x08; lr_offset = 0; if PSTATE.EL == EL2 || route_to_hyp then except = ExceptionSyndrome(Exception_SupervisorCall); except.syndrome.iss<15:0> = immediate;
```

```
if PSTATE.EL == EL2 then AArch32.EnterHypMode(except, preferred_exception_return, vect_offset); else AArch32.EnterHypMode(except, preferred_exception_return, 0x14); else AArch32.EnterMode(M32_Svc, preferred_exception_return, lr_offset,
```

```
// AArch32.EnterMode() // =================== // Take an exception to a mode other than Monitor and Hyp mode. AArch32.EnterMode(bits(5) target_mode, bits(32) preferred_exception_return, integer integer vect_offset) SynchronizeContext(); assert ELUsingAArch32(EL1) && PSTATE.EL != EL2;
```

```
vect_offset); J1.2.2.30 AArch32.EnterHypMode // AArch32.EnterHypMode() // ====================== // Take an exception to Hyp mode. AArch32.EnterHypMode(ExceptionRecord except, bits(32) preferred_exception_return, integer vect_offset) SynchronizeContext(); assert HaveEL(EL2) && CurrentSecurityState() == SS_NonSecure && ELUsingAArch32(EL2); if Halted() then AArch32.EnterHypModeInDebugState(except); return; constant bits(32) spsr = GetPSRFromPSTATE(AArch32_NonDebugState, 32); if ! except.exceptype IN {Exception_IRQ, Exception_FIQ} then AArch32.ReportHypEntry(except); AArch32.WriteMode(M32_Hyp); SPSR_curr[] = spsr; ELR_hyp = preferred_exception_return; PSTATE.T = HSCTLR.TE; // PSTATE.J is RES0 PSTATE.SS = '0'; if !HaveEL(EL3) then PSTATE.A = '1'; PSTATE.I = '1'; PSTATE.F = '1'; else if ELUsingAArch32(EL3) then if SCR.EA == '0' then PSTATE.A = '1'; if SCR.IRQ == '0' then PSTATE.I = '1'; if SCR.FIQ == '0' then PSTATE.F = '1'; else if SCR_EL3.EA == '0' then PSTATE.A = '1'; if SCR_EL3.IRQ == '0' then PSTATE.I = '1'; if SCR_EL3.FIQ == '0' then PSTATE.F = '1'; PSTATE.E = HSCTLR.EE; PSTATE.IL = '0'; PSTATE.IT = '00000000'; if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = HSCTLR.DSSBS; constant boolean branch_conditional = FALSE; BranchTo(HVBAR<31:5>:vect_offset<4:0>, BranchType_EXCEPTION, branch_conditional); CheckExceptionCatch(TRUE); // Check for debug event on exception entry EndOfInstruction(); J1.2.2.31 AArch32.EnterMode lr_offset,
```

```
if Halted() then AArch32.EnterModeInDebugState(target_mode); return; constant bits(32) spsr = GetPSRFromPSTATE(AArch32_NonDebugState, 32); if PSTATE.M == M32_Monitor then SCR.NS = '0'; AArch32.WriteMode(target_mode); SPSR_curr[] = spsr; R[14] = preferred_exception_return + lr_offset; PSTATE.T = SCTLR.TE; // PSTATE.J is RES0 PSTATE.SS = '0'; if target_mode == M32_FIQ then PSTATE.<A,I,F> = '111'; elsif target_mode IN {M32_Abort, M32_IRQ} then PSTATE.<A,I> = '11'; else PSTATE.I = '1'; PSTATE.E = SCTLR.EE; PSTATE.IL = '0'; PSTATE.IT = '00000000'; if IsFeatureImplemented(FEAT_PAN) && SCTLR.SPAN == '0' then PSTATE.PAN = '1'; if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = SCTLR.DSSBS; constant boolean branch_conditional = FALSE; BranchTo(ExcVectorBase()<31:5>:vect_offset<4:0>, BranchType_EXCEPTION, branch_conditional); CheckExceptionCatch(TRUE); // Check for debug event on exception entry EndOfInstruction();
```

```
J1.2.2.32 AArch32.EnterMonitorMode
```

```
// AArch32.EnterMonitorMode() // ========================== // Take an exception to Monitor mode. AArch32.EnterMonitorMode(bits(32) preferred_exception_return, integer lr_offset, integer vect_offset) SynchronizeContext(); assert HaveEL(EL3) && ELUsingAArch32(EL3); from_secure = CurrentSecurityState() == SS_Secure; if Halted() then AArch32.EnterMonitorModeInDebugState(); return; constant bits(32) spsr = GetPSRFromPSTATE(AArch32_NonDebugState, 32); if PSTATE.M == M32_Monitor then SCR.NS = '0'; AArch32.WriteMode(M32_Monitor); SPSR_curr[] = spsr; R[14] = preferred_exception_return + lr_offset; PSTATE.T = SCTLR.TE; // PSTATE.J is RES0 PSTATE.SS = '0'; PSTATE.<A,I,F> = '111'; PSTATE.E = SCTLR.EE; PSTATE.IL = '0'; PSTATE.IT = '00000000'; if IsFeatureImplemented(FEAT_PAN) then if !from_secure then PSTATE.PAN = '0'; elsif SCTLR.SPAN == '0' then PSTATE.PAN = '1'; if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = SCTLR.DSSBS; constant boolean branch_conditional = FALSE; BranchTo(MVBAR<31:5>:vect_offset<4:0>, BranchType_EXCEPTION, branch_conditional); CheckExceptionCatch(TRUE); // Check for debug event on exception entry
```

EndOfInstruction();

## J1.2.2.33 AArch32.CheckAdvSIMDOrFPEnabled

```
// AArch32.CheckAdvSIMDOrFPEnabled() // ================================= // Check against CPACR, FPEXC, HCPTR, NSACR, and CPTR_EL3. AArch32.CheckAdvSIMDOrFPEnabled(boolean fpexc_check_in, boolean advsimd) boolean fpexc_check = fpexc_check_in; if PSTATE.EL == EL0 && !ELUsingAArch32(EL1) then // When executing at EL0 using AArch32, if EL1 is using AArch64 then the Effective value of // FPEXC.EN is 1. This includes when EL2 is using AArch64 and enabled in the current // Security state, HCR_EL2.TGE is 1, and the Effective value of HCR_EL2.RW is 1. AArch64.CheckFPAdvSIMDEnabled(); else cpacr_asedis = CPACR.ASEDIS; cpacr_cp10 = CPACR.cp10; if HaveEL(EL3) && ELUsingAArch32(EL3) && CurrentSecurityState() == SS_NonSecure then // Check if access disabled in NSACR if NSACR.NSASEDIS == '1' then cpacr_asedis = '1'; if NSACR.cp10 == '0' then cpacr_cp10 = '00'; if PSTATE.EL != EL2 then // Check if Advanced SIMD disabled in CPACR if advsimd && cpacr_asedis == '1' then AArch32.Undefined(); // Check if access disabled in CPACR boolean disabled; case cpacr_cp10 of when '00' disabled = TRUE; when '01' disabled = PSTATE.EL == EL0; when '10' disabled = ConstrainUnpredictableBool(Unpredictable_RESCPACR); when '11' disabled = FALSE; if disabled then AArch32.Undefined(); // If required, check FPEXC enabled bit. if (fpexc_check && PSTATE.EL == EL0 && EL2Enabled() && !ELUsingAArch32(EL2) && HCR_EL2.TGE == '1') then // When executing at EL0 using AArch32, if EL2 is using AArch64 and enabled in the // current Security state, HCR_EL2.TGE is 1, and the Effective value of HCR_EL2.RW is 0 // then it is IMPLEMENTATION DEFINED whether the Effective value of FPEXC.EN is 1 // or the value of FPEXC32_EL2.EN. fpexc_check = (boolean IMPLEMENTATION_DEFINED "Use FPEXC32_EL2.EN value when {TGE,RW} == {1,0}"); if fpexc_check && FPEXC.EN == '0' then AArch32.Undefined(); AArch32.CheckFPAdvSIMDTrap(advsimd); // Also check against HCPTR and CPTR_EL3
```

## J1.2.2.34 AArch32.CheckFPAdvSIMDTrap

```
// AArch32.CheckFPAdvSIMDTrap() // ============================ // Check against CPTR_EL2 and CPTR_EL3. AArch32.CheckFPAdvSIMDTrap(boolean advsimd) if EL2Enabled() && !ELUsingAArch32(EL2) then AArch64.CheckFPAdvSIMDTrap(); else if (HaveEL(EL3) && !ELUsingAArch32(EL3) &&
```

```
CPTR_EL3.TFP == '1' && EL3SDDUndefPriority()) then UNDEFINED; ss = CurrentSecurityState(); if HaveEL(EL2) && ss != SS_Secure then hcptr_tase = HCPTR.TASE; hcptr_cp10 = HCPTR.TCP10; if HaveEL(EL3) && ELUsingAArch32(EL3) then // Check if access disabled in NSACR if NSACR.NSASEDIS == '1' then hcptr_tase = '1'; if NSACR.cp10 == '0' then hcptr_cp10 = '1'; // Check if access disabled in HCPTR if (advsimd && hcptr_tase == '1') || hcptr_cp10 == '1' then except = ExceptionSyndrome(Exception_AdvSIMDFPAccessTrap); except.syndrome.iss<24:20> = ConditionSyndrome(); if advsimd then except.syndrome.iss<5> = '1'; else except.syndrome.iss<5> = '0'; except.syndrome.iss<3:0> = '1010'; // coproc field, always 0xA if PSTATE.EL == EL2 then AArch32.TakeUndefInstrException(except); else AArch32.TakeHypTrapException(except); if HaveEL(EL3) && !ELUsingAArch32(EL3) then // Check if access disabled in CPTR_EL3 if CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AdvSIMDFPAccessTrap(EL3);
```

```
J1.2.2.35 AArch32.CheckForSMCUndefOrTrap // AArch32.CheckForSMCUndefOrTrap() // ================================ // Check for UNDEFINED or trap on SMC instruction AArch32.CheckForSMCUndefOrTrap() if !HaveEL(EL3) || PSTATE.EL == EL0 then UNDEFINED; if EL2Enabled() && !ELUsingAArch32(EL2) then AArch64.CheckForSMCUndefOrTrap(Zeros(16)); else route_to_hyp = EL2Enabled() && PSTATE.EL == EL1 && HCR.TSC == '1'; if route_to_hyp then except = ExceptionSyndrome(Exception_MonitorCall); AArch32.TakeHypTrapException(except); J1.2.2.36 AArch32.CheckForSVCTrap // AArch32.CheckForSVCTrap() // ========================= // Check for trap on SVC instruction AArch32.CheckForSVCTrap(bits(16) immediate) if IsFeatureImplemented(FEAT_FGT) then
```

```
route_to_el2 = FALSE; if PSTATE.EL == EL0 then route_to_el2 = (!ELUsingAArch32(EL1) && EL2Enabled() && HFGITR_EL2.SVC_EL0 == '1' && (!IsInHost() && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1'))); if route_to_el2 then except = ExceptionSyndrome(Exception_SupervisorCall); except.syndrome.iss<15:0> = immediate; except.trappedsyscallinst = TRUE; constant bits(64) preferred_exception_return = ThisInstrAddr(64); vect_offset = 0x0; AArch64.TakeException(EL2, except, preferred_exception_return, vect_offset);
```

## J1.2.2.37 AArch32.CheckForWFxTrap

```
// AArch32.CheckForWFxTrap() // ========================= // Check for trap on WFE or WFI instruction AArch32.CheckForWFxTrap(bits(2) target_el, WFxType wfxtype) assert HaveEL(target_el); // Check for routing to AArch64 if !ELUsingAArch32(target_el) then boolean trap; constant boolean is_wfe = wfxtype == WFxType_WFE; case target_el of when EL1 trap = (if is_wfe then SCTLR_ELx[].nTWE else SCTLR_ELx[].nTWI) == '0'; when EL2 trap = (if is_wfe then HCR_EL2.TWE else HCR_EL2.TWI) == '1'; when EL3 trap = (if is_wfe then SCR_EL3.TWE else SCR_EL3.TWI) == '1'; if trap then if target_el == EL3 && EL3SDDUndef() then UNDEFINED; else AArch64.WFxTrap(wfxtype, target_el); return; constant boolean is_wfe = wfxtype == WFxType_WFE; boolean trap; case target_el of when EL1 trap = (if is_wfe then SCTLR.nTWE else SCTLR.nTWI) == '0'; when EL2 trap = (if is_wfe then HCR.TWE else HCR.TWI) == '1'; when EL3 trap = (if is_wfe then SCR.TWE else SCR.TWI) == '1'; if trap then if target_el == EL1 && EL2Enabled() && !ELUsingAArch32(EL2) && HCR_EL2.TGE == '1' then AArch64.WFxTrap(wfxtype, target_el); if target_el == EL3 && !EL3SDDUndef() then AArch32.TakeMonitorTrapException(); elsif target_el == EL2 then except = ExceptionSyndrome(Exception_WFxTrap); except.syndrome.iss<24:20> = ConditionSyndrome(); except.syndrome.iss<0> = if wfxtype == WFxType_WFI then '0' else '1'; AArch32.TakeHypTrapException(except); else AArch32.TakeUndefInstrException();
```

## J1.2.2.38 AArch32.CheckITEnabled

```
// AArch32.CheckITEnabled() // ======================== // Check whether the T32 IT instruction is disabled. AArch32.CheckITEnabled(bits(4) mask) bit it_disabled; if PSTATE.EL == EL2 then it_disabled = HSCTLR.ITD; else it_disabled = (if ELUsingAArch32(EL1) then SCTLR.ITD else SCTLR_ELx[].ITD); if it_disabled == '1' then if mask != '1000' then UNDEFINED; accdesc = CreateAccDescIFetch(); aligned = TRUE; // Otherwise whether the IT block is allowed depends on hw1 of the next instruction. next_instr = AArch32.MemSingle[NextInstrAddr(32), 2, accdesc, aligned]; if next_instr IN {'11xxxxxxxxxxxxxx', '1011xxxxxxxxxxxx', '10100xxxxxxxxxxx', '01001xxxxxxxxxxx', '010001xxx1111xxx', '010001xx1xxxx111'} then // It is IMPLEMENTATION DEFINED whether the Undefined Instruction exception is // taken on the IT instruction or the next instruction. This is not reflected in // the pseudocode, which always takes the exception on the IT instruction. This // also does not take into account cases where the next instruction is UNPREDICTABLE. UNDEFINED; return;
```

## J1.2.2.39 AArch32.CheckIllegalState

```
// AArch32.CheckIllegalState() // =========================== // Check PSTATE.IL bit and generate Illegal Execution state exception if set. AArch32.CheckIllegalState() if AArch32.GeneralExceptionsToAArch64() then AArch64.CheckIllegalState(); elsif PSTATE.IL == '1' then route_to_hyp = PSTATE.EL == EL0 && EL2Enabled() && HCR.TGE == '1'; constant bits(32) preferred_exception_return = ThisInstrAddr(32); vect_offset = 0x04; if PSTATE.EL == EL2 || route_to_hyp then except = ExceptionSyndrome(Exception_IllegalState); if PSTATE.EL == EL2 then AArch32.EnterHypMode(except, preferred_exception_return, vect_offset); else AArch32.EnterHypMode(except, preferred_exception_return, 0x14); else AArch32.TakeUndefInstrException();
```

## J1.2.2.40 AArch32.CheckSETENDEnabled

```
// AArch32.CheckSETENDEnabled() // ============================ // Check whether the AArch32 SETEND instruction is disabled.
```

```
AArch32.CheckSETENDEnabled() bit setend_disabled; if PSTATE.EL == EL2 then setend_disabled = HSCTLR.SED; else setend_disabled = (if ELUsingAArch32(EL1) then SCTLR.SED else SCTLR_ELx[].SED); if setend_disabled == '1' then UNDEFINED; return;
```

```
J1.2.2.41 AArch32.SystemAccessTrap // AArch32.SystemAccessTrap() // ========================== // Trapped AArch32 System register access. AArch32.SystemAccessTrap(bits(5) mode, integer ec) (valid, target_el) = ELFromM32(mode); assert valid && HaveEL(target_el) && target_el != EL0 && UInt(target_el) >= UInt(PSTATE.EL); if target_el == EL2 then except = AArch32.SystemAccessTrapSyndrome(ThisInstr(), ec); AArch32.TakeHypTrapException(except); else AArch32.TakeUndefInstrException(); J1.2.2.42 AArch32.SystemAccessTrapSyndrome // AArch32.SystemAccessTrapSyndrome() // ================================== // Returns the syndrome information for traps on AArch32 MCR, MCRR, MRC, MRRC, and VMRS, // VMSR instructions, other than traps that are due to HCPTR or CPACR. ExceptionRecord AArch32.SystemAccessTrapSyndrome(bits(32) instr, integer ec) ExceptionRecord except; case ec of when 0x0 except = ExceptionSyndrome(Exception_Uncategorized); when 0x3 except = ExceptionSyndrome(Exception_CP15RTTrap); when 0x4 except = ExceptionSyndrome(Exception_CP15RRTTrap); when 0x5 except = ExceptionSyndrome(Exception_CP14RTTrap); when 0x6 except = ExceptionSyndrome(Exception_CP14DTTrap); when 0x7 except = ExceptionSyndrome(Exception_AdvSIMDFPAccessTrap); when 0x8 except = ExceptionSyndrome(Exception_FPIDTrap); when 0xC except = ExceptionSyndrome(Exception_CP14RRTTrap); otherwise Unreachable(); bits(20) iss = Zeros(20); if except.exceptype == Exception_Uncategorized then return except; elsif except.exceptype IN {Exception_FPIDTrap, Exception_CP14RTTrap, Exception_CP15RTTrap} then // Trapped MRC/MCR, VMRS on FPSID iss<13:10> = instr<19:16>; // CRn, Reg in case of VMRS iss<8:5> = instr<15:12>; // Rt iss<9> = '0'; // RES0 if except.exceptype != Exception_FPIDTrap then // When trap is not for VMRS iss<19:17> = instr<7:5>; // opc2 iss<16:14> = instr<23:21>; // opc1
```

```
ELUsingAArch32(EL2);
```

## iss&lt;4:1&gt; = instr&lt;3:0&gt;; //CRm else //VMRS Access iss&lt;19:17&gt; = '000'; //opc2 -Hardcoded for VMRS iss&lt;16:14&gt; = '111'; //opc1 -Hardcoded for VMRS iss&lt;4:1&gt; = '0000'; //CRm -Hardcoded for VMRS elsif except.exceptype IN {Exception\_CP14RRTTrap, Exception\_AdvSIMDFPAccessTrap, Exception\_CP15RRTTrap} then // Trapped MRRC/MCRR, VMRS/VMSR iss&lt;19:16&gt; = instr&lt;7:4&gt;; // opc1 iss&lt;13:10&gt; = instr&lt;19:16&gt;; // Rt2 iss&lt;8:5&gt; = instr&lt;15:12&gt;; // Rt iss&lt;4:1&gt; = instr&lt;3:0&gt;; // CRm elsif except.exceptype == Exception\_CP14DTTrap then // Trapped LDC/STC iss&lt;19:12&gt; = instr&lt;7:0&gt;; // imm8 iss&lt;4&gt; = instr&lt;23&gt;; // U iss&lt;2:1&gt; = instr&lt;24,21&gt;; // P,W if instr&lt;19:16&gt; == '1111' then // Rn==15, LDC(Literal addressing)/STC iss&lt;8:5&gt; = bits(4) UNKNOWN; iss&lt;3&gt; = '1'; iss&lt;0&gt; = instr&lt;20&gt;; // Direction except.syndrome.iss&lt;24:20&gt; = ConditionSyndrome(); except.syndrome.iss&lt;19:0&gt; = iss; return except; J1.2.2.43 AArch32.TakeHypTrapException // AArch32.TakeHypTrapException() // ============================== // Exceptions routed to Hyp mode as a Hyp Trap exception. AArch32.TakeHypTrapException(integer ec) except = AArch32.SystemAccessTrapSyndrome(ThisInstr(), ec); AArch32.TakeHypTrapException(except); // AArch32.TakeHypTrapException() // ============================== // Exceptions routed to Hyp mode as a Hyp Trap exception. AArch32.TakeHypTrapException(ExceptionRecord except) assert HaveEL(EL2) &amp;&amp; CurrentSecurityState() == SS\_NonSecure &amp;&amp; constant bits(32) preferred\_exception\_return = ThisInstrAddr(32); vect\_offset = 0x14; AArch32.EnterHypMode(except, preferred\_exception\_return, vect\_offset); J1.2.2.44 AArch32.TakeMonitorTrapException // AArch32.TakeMonitorTrapException() // ================================== // Exceptions routed to Monitor mode as a Monitor Trap exception. AArch32.TakeMonitorTrapException() assert HaveEL(EL3) &amp;&amp; ELUsingAArch32(EL3); constant bits(32) preferred\_exception\_return = ThisInstrAddr(32); vect\_offset = 0x04; lr\_offset = if CurrentInstrSet() == InstrSet\_A32 then 4 else 2; AArch32.EnterMonitorMode(preferred\_exception\_return, lr\_offset, vect\_offset);

## J1.2.2.45 AArch32.TakeUndefInstrException

```
// AArch32.TakeUndefInstrException() // ================================= AArch32.TakeUndefInstrException() except = ExceptionSyndrome(Exception_Uncategorized); AArch32.TakeUndefInstrException(except); // AArch32.TakeUndefInstrException() // ================================= AArch32.TakeUndefInstrException(ExceptionRecord except) route_to_hyp = PSTATE.EL == EL0 && EL2Enabled() && HCR.TGE == '1'; constant bits(32) preferred_exception_return = ThisInstrAddr(32); vect_offset = 0x04; lr_offset = if CurrentInstrSet() == InstrSet_A32 then 4 else 2; if PSTATE.EL == EL2 then AArch32.EnterHypMode(except, preferred_exception_return, vect_offset); elsif route_to_hyp then AArch32.EnterHypMode(except, preferred_exception_return, 0x14); else
```

```
AArch32.EnterMode(M32_Undef, preferred_exception_return, lr_offset, vect_offset);
```

## J1.2.2.46 AArch32.Undefined

```
// AArch32.Undefined() // =================== AArch32.Undefined() if AArch32.GeneralExceptionsToAArch64() then AArch32.TakeUndefInstrException();
```

## J1.2.3 aarch32/functions

This section includes the following pseudocode functions:

- AArch32.DomainValid
- AArch32.FaultSyndrome
- AArch32.InstructionSyndromeValid
- EncodeSDFSC
- A32ExpandImm
- A32ExpandImm\_C
- DecodeImmShift
- DecodeRegShift
- RRX
- RRX\_C
- SRType
- Shift
- Shift\_C
- T32ExpandImm
- T32ExpandImm\_C
- VBitOps

```
AArch64.Undefined();
```

- VCGEType
- VCGTtype
- VFPNegMul
- AArch32.CheckCP15InstrCoarseTraps
- AArch32.ExclusiveMonitorsPass
- AArch32.IsExclusiveVA
- AArch32.MarkExclusiveVA
- AArch32.SetExclusiveMonitors
- CheckAdvSIMDEnabled
- CheckAdvSIMDOrVFPEnabled
- CheckCryptoEnabled32
- CheckVFPEnabled
- FPHalvedSub
- FPRSqrtStep
- FPRecipStep
- StandardFPCR
- AArch32.MemSingle
- AArch32.MemSingleRead
- AArch32.MemSingleWrite
- AArch32.UnalignedAccessFaults
- Hint\_PreloadData
- Hint\_PreloadDataForWrite
- Hint\_PreloadInstr
- MemA
- MemO
- MemS
- MemU
- MemU\_unpriv
- Mem\_with\_type
- AArch32.ESBOperation
- AArch32.EncodeAsyncErrorSyndrome

•

AArch32.PhysicalSErrorSyndrome

- AArch32.vESBOperation
- AArch32.ResetGeneralRegisters
- AArch32.ResetSIMDFPRegisters
- AArch32.ResetSpecialRegisters
- AArch32.ResetSystemRegisters
- ALUExceptionReturn
- ALUWritePC
- BXWritePC
- BranchWritePC
- CBWritePC
- D
- Din

•

H

- LR
- LoadWritePC

- LookUpRIndex
- Monitor

•

PC32

- PCStoreValue
- Q
- Qin

•

R

- RBankSelect
- ReadAnyAllocatedRegister
- ReadAnyAllocatedSPSR
- Rmode
- S
- WriteAnyAllocatedRegister
- WriteAnyAllocatedSPSR
- \_Dclone
- AArch32.ExceptionReturn
- AArch32.ExecutingCP10or11Instr
- AArch32.ITAdvance
- AArch32.InterruptPending
- AArch32.SysRegRead
- AArch32.SysRegRead64
- AArch32.SysRegReadCanWriteAPSR
- AArch32.SysRegWrite
- AArch32.SysRegWrite64
- AArch32.SysRegWriteM
- AArch32.WriteMode
- AArch32.WriteModeByInstr
- BadMode
- BankedRegisterAccessValid
- CPSRWriteByInstr
- ConditionPassed
- CurrentCond
- InITBlock
- LastInITBlock
- SPSRWriteByInstr
- SPSRaccessValid
- SelectInstrSet
- AArch32.DTLBI\_ALL
- AArch32.DTLBI\_ASID
- AArch32.DTLBI\_VA
- AArch32.ITLBI\_ALL
- AArch32.ITLBI\_ASID
- AArch32.ITLBI\_VA
- AArch32.TLBI\_ALL
- AArch32.TLBI\_ASID
- AArch32.TLBI\_IPAS2
- AArch32.TLBI\_VA

```
· AArch32.TLBI_VAA · AArch32.TLBI_VMALL · AArch32.TLBI_VMALLS12 · Sat · AArch32.RestrictPrediction
```

## J1.2.3.1 AArch32.DomainValid

```
// AArch32.DomainValid() // ===================== // Returns TRUE if the Domain is valid for a Short-descriptor translation scheme. boolean AArch32.DomainValid(Fault statuscode, integer level) assert statuscode != Fault_None; case statuscode of when Fault_Domain return TRUE; when Fault_Translation, Fault_AccessFlag, Fault_SyncExternalOnWalk, Fault_SyncParityOnWalk return level == 2; otherwise return FALSE;
```

## J1.2.3.2 AArch32.FaultSyndrome

```
// AArch32.FaultSyndrome() // ======================= // Creates an exception syndrome value and updates the virtual address for Abort and Watchpoint // exceptions taken to AArch32 Hyp mode. bits(25) AArch32.FaultSyndrome(Exception exceptype, FaultRecord fault) assert fault.statuscode != Fault_None; IssType isstype; isstype.iss = Zeros(25); constant boolean d_side = exceptype == Exception_DataAbort; if IsFeatureImplemented(FEAT_RAS) && IsAsyncAbort(fault) then constant ErrorState errstate = PEErrorState(fault); isstype.iss<11:10> = AArch32.EncodeAsyncErrorSyndrome(errstate); // AET if d_side then if AArch32.InstructionSyndromeValid(fault) then isstype.iss<24:14> = LSInstructionSyndrome(); if fault.accessdesc.acctype IN {AccessType_DC, AccessType_IC, AccessType_AT} then isstype.iss<8> = '1'; if fault.accessdesc.acctype IN {AccessType_DC, AccessType_IC, AccessType_AT} then isstype.iss<6> = '1'; elsif fault.statuscode IN {Fault_HWUpdateAccessFlag, Fault_Exclusive} then isstype.iss<6> = bit UNKNOWN; elsif fault.accessdesc.atomicop && IsExternalAbort(fault) then isstype.iss<6> = bit UNKNOWN; else isstype.iss<6> = if fault.write then '1' else '0'; if IsExternalAbort(fault) then isstype.iss<9> = fault.extflag; isstype.iss<7> = if fault.s2fs1walk then '1' else '0'; isstype.iss<5:0> = EncodeLDFSC(fault.statuscode, fault.level);
```

```
return isstype.iss;
```

## J1.2.3.3 AArch32.InstructionSyndromeValid

```
// AArch32.InstructionSyndromeValid() // ================================== // Returns TRUE if ESR_ELx.ISV is '1' for the given Fault. boolean AArch32.InstructionSyndromeValid(FaultRecord fault) if IsSecondStage(fault) && !fault.s2fs1walk then return (!IsExternalSyncAbort(fault) || (!IsFeatureImplemented(FEAT_RAS) && IsExternalAbortOnWalk(fault) && boolean IMPLEMENTATION_DEFINED "ISV on second stage translation table walk")); return FALSE;
```

## J1.2.3.4 EncodeSDFSC

```
// EncodeSDFSC() // ============= // Function that gives the Short-descriptor FSR code for different types of Fault bits(5) EncodeSDFSC(Fault statuscode, integer level) bits(5) result; case statuscode of when Fault_AccessFlag assert level IN {1,2}; result = if level == 1 then '00011' else '00110'; when Fault_Alignment result = '00001'; when Fault_Permission assert level IN {1,2}; result = if level == 1 then '01101' else '01111'; when Fault_Domain assert level IN {1,2}; result = if level == 1 then '01001' else '01011'; when Fault_Translation assert level IN {1,2}; result = if level == 1 then '00101' else '00111'; when Fault_SyncExternal result = '01000'; when Fault_SyncExternalOnWalk assert level IN {1,2}; result = if level == 1 then '01100' else '01110'; when Fault_SyncParity result = '11001'; when Fault_SyncParityOnWalk assert level IN {1,2}; result = if level == 1 then '11100' else '11110'; when Fault_AsyncParity result = '11000'; when Fault_AsyncExternal result = '10110'; when Fault_Debug result = '00010'; when Fault_TLBConflict result = '10000'; when Fault_Lockdown result = '10100'; // IMPLEMENTATION DEFINED when Fault_Exclusive result = '10101'; // IMPLEMENTATION DEFINED when Fault_ICacheMaint result = '00100';
```

```
otherwise Unreachable(); return result;
```

## J1.2.3.5 A32ExpandImm

```
// A32ExpandImm() // ============== bits(32) A32ExpandImm(bits(12) imm12) // PSTATE.C argument to following function call does not affect the imm32 result. (imm32, -) = A32ExpandImm_C(imm12, PSTATE.C); return imm32;
```

## J1.2.3.6 A32ExpandImm\_C

```
// A32ExpandImm_C() // ================ (bits(32), bit) A32ExpandImm_C(bits(12) imm12, bit carry_in) unrotated_value = ZeroExtend(imm12<7:0>, 32); (imm32, carry_out) = Shift_C(unrotated_value, SRType_ROR, 2*UInt(imm12<11:8>), carry_in); return (imm32, carry_out);
```

## J1.2.3.7 DecodeImmShift

```
// DecodeImmShift() // ================ (SRType, integer) DecodeImmShift(bits(2) srtype, bits(5) imm5) SRType shift_t; integer shift_n; case srtype of when '00' shift_t = SRType_LSL; shift_n = UInt(imm5); when '01' shift_t = SRType_LSR; shift_n = if imm5 == '00000' then 32 else UInt(imm5); when '10' shift_t = SRType_ASR; shift_n = if imm5 == '00000' then 32 else UInt(imm5); when '11' if imm5 == '00000' then shift_t = SRType_RRX; shift_n = 1; else shift_t = SRType_ROR; shift_n = UInt(imm5); return (shift_t, shift_n);
```

## J1.2.3.8 DecodeRegShift

```
// DecodeRegShift() // ================ SRType DecodeRegShift(bits(2) srtype) SRType shift_t; case srtype of when '00' shift_t = SRType_LSL; when '01' shift_t = SRType_LSR;
```

```
when '10' shift_t = SRType_ASR; when '11' shift_t = SRType_ROR; return shift_t;
```

## J1.2.3.9 RRX

```
// RRX() // ===== bits(N) RRX(bits(N) x, bit carry_in) (result, -) = RRX_C(x, carry_in); return result;
```

## J1.2.3.10 RRX\_C

```
// RRX_C() // ======= (bits(N), bit) RRX_C(bits(N) x, bit carry_in) result = carry_in : x<N-1:1>; carry_out = x<0>; return (result, carry_out);
```

## J1.2.3.11 SRType

```
// SRType // ====== enumeration SRType {SRType_LSL, SRType_LSR, SRType_ASR, SRType_ROR,
```

## J1.2.3.12 Shift

```
// Shift() // ======= bits(N) Shift(bits(N) value, SRType srtype, integer amount, bit carry_in) (result, -) = Shift_C(value, srtype, amount, carry_in); return result;
```

## J1.2.3.13 Shift\_C

```
// Shift_C() // ========= (bits(N), bit) Shift_C(bits(N) value, SRType srtype, integer amount, bit carry_in) assert !(srtype == SRType_RRX && amount != 1); bits(N) result; bit carry_out; if amount == 0 then (result, carry_out) = (value, carry_in); else case srtype of when SRType_LSL (result, carry_out) = LSL_C(value, amount); when SRType_LSR (result, carry_out) = LSR_C(value, amount); when SRType_ASR
```

```
SRType_RRX};
```

```
(result, carry_out) = ASR_C(value, amount); when SRType_ROR (result, carry_out) = ROR_C(value, amount); when SRType_RRX (result, carry_out) = RRX_C(value, return (result, carry_out);
```

## carry\_in); J1.2.3.14 T32ExpandImm // T32ExpandImm() // ============== bits(32) T32ExpandImm(bits(12) imm12) // PSTATE.C argument to following function call does not affect the imm32 result. (imm32, -) = T32ExpandImm\_C(imm12, PSTATE.C); return imm32; J1.2.3.15 T32ExpandImm\_C // T32ExpandImm\_C() // ================ (bits(32), bit) T32ExpandImm\_C(bits(12) imm12, bit carry\_in) bits(32) imm32; bit carry\_out; if imm12&lt;11:10&gt; == '00' then case imm12&lt;9:8&gt; of when '00' imm32 = ZeroExtend(imm12&lt;7:0&gt;, 32); when '01' imm32 = '00000000' : imm12&lt;7:0&gt; : '00000000' : imm12&lt;7:0&gt;; when '10' imm32 = imm12&lt;7:0&gt; : '00000000' : imm12&lt;7:0&gt; : '00000000'; when '11' imm32 = imm12&lt;7:0&gt; : imm12&lt;7:0&gt; : imm12&lt;7:0&gt; : imm12&lt;7:0&gt;; carry\_out = carry\_in; else unrotated\_value = ZeroExtend('1':imm12&lt;6:0&gt;, 32); (imm32, carry\_out) = ROR\_C(unrotated\_value, UInt(imm12&lt;11:7&gt;)); return (imm32, carry\_out); J1.2.3.16 VBitOps // VBitOps // ======= enumeration VBitOps {VBitOps\_VBIF, VBitOps\_VBIT, VBitOps\_VBSL}; J1.2.3.17 VCGEType // VCGEType // ======== enumeration VCGEType {VCGEType\_signed, VCGEType\_unsigned, VCGEType\_fp};

## J1.2.3.18 VCGTtype

```
// VCGTtype // ======== enumeration VCGTtype {VCGTtype_signed,
```

```
VCGTtype_unsigned, VCGTtype_fp};
```

## J1.2.3.19 VFPNegMul // VFPNegMul // ========= enumeration VFPNegMul {VFPNegMul\_VNMLA, VFPNegMul\_VNMLS, VFPNegMul\_VNMUL}; J1.2.3.20 AArch32.CheckCP15InstrCoarseTraps // AArch32.CheckCP15InstrCoarseTraps() // =================================== // Check for coarse-grained traps to System registers in the // coproc=0b1111 encoding space by HSTR and HCR. AArch32.CheckCP15InstrCoarseTraps(integer CRn, integer nreg, integer CRm) if PSTATE.EL == EL0 &amp;&amp; (!ELUsingAArch32(EL1) || (EL2Enabled() &amp;&amp; !ELUsingAArch32(EL2))) then AArch64.CheckCP15InstrCoarseTraps(CRn, nreg, CRm); trapped\_encoding = ((CRn == 9 &amp;&amp; CRm IN {0,1,2, 5,6,7,8 }) || (CRn == 10 &amp;&amp; CRm IN {0,1, 4, 8 }) || (CRn == 11 &amp;&amp; CRm IN {0,1,2,3,4,5,6,7,8,15})); // Check for coarse-grained Hyp traps if PSTATE.EL IN {EL0, EL1} &amp;&amp; EL2Enabled() then major = if nreg == 1 then CRn else CRm; // Check for MCR, MRC, MCRR, and MRRC disabled by HSTR&lt;CRn/CRm&gt; // and MRC and MCR disabled by HCR.TIDCP. if ((! major IN {4,14} &amp;&amp; HSTR&lt;major&gt; == '1') || (HCR.TIDCP == '1' &amp;&amp; nreg == 1 &amp;&amp; trapped\_encoding)) then if (PSTATE.EL == EL0 &amp;&amp; boolean IMPLEMENTATION\_DEFINED "UNDEF unallocated CP15 access at EL0") then UNDEFINED; if ELUsingAArch32(EL2) then AArch32.SystemAccessTrap(M32\_Hyp, 0x3); else AArch64.AArch32SystemAccessTrap(EL2, 0x3); J1.2.3.21 AArch32.ExclusiveMonitorsPass of the addresses

```
// AArch32.ExclusiveMonitorsPass() // =============================== // Return TRUE if the Exclusives monitors for the current PE include all // associated with the virtual address region of size bytes starting at address. // The immediately following memory write must be to the same addresses. // It is IMPLEMENTATION DEFINED whether the detection of memory aborts happens // before or after the check on the local Exclusives monitor. As a result a failure // of the local monitor can occur on some implementations even if the memory // access would give an memory abort. boolean AArch32.ExclusiveMonitorsPass(bits(32) address, integer size) constant boolean acqrel = FALSE; constant boolean privileged = PSTATE.EL != EL0;
```

```
constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescExLDST(MemOp_STORE, acqrel, tagchecked, privileged); constant boolean aligned = IsAligned(address, size); if !aligned then constant FaultRecord fault = AlignmentFault(accdesc, AArch32.Abort(fault); if !AArch32.IsExclusiveVA(address, ProcessorID(), size) then return FALSE; memaddrdesc = AArch32.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then AArch32.Abort(memaddrdesc.fault); passed = IsExclusiveLocal(memaddrdesc.paddress, ProcessorID(), size); ClearExclusiveLocal(ProcessorID()); if passed && memaddrdesc.memattrs.shareability != Shareability_NSH then passed = IsExclusiveGlobal(memaddrdesc.paddress, ProcessorID(), size); return passed;
```

```
ZeroExtend(address, 64)); J1.2.3.22 AArch32.IsExclusiveVA // AArch32.IsExclusiveVA() // ======================= // An optional IMPLEMENTATION DEFINED test for an exclusive access to a virtual // address region of size bytes starting at address. // // It is permitted (but not required) for this function to return FALSE and // cause a store exclusive to fail if the virtual address region is not // totally included within the region recorded by MarkExclusiveVA(). // // It is always safe to return TRUE which will check the physical address only. boolean AArch32.IsExclusiveVA(bits(32) address, integer processorid, integer size); J1.2.3.23 AArch32.MarkExclusiveVA // AArch32.MarkExclusiveVA() // ========================= // Optionally record an exclusive access to the virtual address region of size bytes // starting at address for processorid. AArch32.MarkExclusiveVA(bits(32) address, integer processorid, integer size); J1.2.3.24 AArch32.SetExclusiveMonitors
```

```
// AArch32.SetExclusiveMonitors() // ============================== // Sets the Exclusives monitors for the current PE to record the addresses // with the virtual address region of size bytes starting at address. AArch32.SetExclusiveMonitors(bits(32) address, integer size) constant boolean acqrel = FALSE; constant boolean privileged = PSTATE.EL != EL0;
```

```
associated constant boolean tagchecked = FALSE;
```

```
constant AccessDescriptor accdesc = CreateAccDescExLDST(MemOp_LOAD, acqrel, tagchecked, privileged); constant boolean aligned = IsAligned(address, size); if !aligned then constant FaultRecord fault = AlignmentFault(accdesc, AArch32.Abort(fault); memaddrdesc = AArch32.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then return; if memaddrdesc.memattrs.shareability != Shareability_NSH then MarkExclusiveGlobal(memaddrdesc.paddress, ProcessorID(), size); MarkExclusiveLocal(memaddrdesc.paddress, ProcessorID(), size); AArch32.MarkExclusiveVA(address, ProcessorID(), size);
```

## ZeroExtend(address, 64)); J1.2.3.25 CheckAdvSIMDEnabled // CheckAdvSIMDEnabled() // ===================== CheckAdvSIMDEnabled() fpexc\_check = TRUE; advsimd = TRUE; AArch32.CheckAdvSIMDOrFPEnabled(fpexc\_check, advsimd); // Return from CheckAdvSIMDOrFPEnabled() occurs only if Advanced SIMD access is permitted // Make temporary copy of D registers // \_Dclone[] is used as input data for instruction pseudocode for i = 0 to 31 \_Dclone[i] = D[i]; return; J1.2.3.26 CheckAdvSIMDOrVFPEnabled // CheckAdvSIMDOrVFPEnabled() // ========================== CheckAdvSIMDOrVFPEnabled(boolean include\_fpexc\_check, boolean advsimd) AArch32.CheckAdvSIMDOrFPEnabled(include\_fpexc\_check, advsimd); // Return from CheckAdvSIMDOrFPEnabled() occurs only if VFP access is permitted return; J1.2.3.27 CheckCryptoEnabled32 // CheckCryptoEnabled32() // ====================== CheckCryptoEnabled32() CheckAdvSIMDEnabled(); // Return from CheckAdvSIMDEnabled() occurs only if access is permitted return;

## J1.2.3.28 CheckVFPEnabled

```
// CheckVFPEnabled() // ================= CheckVFPEnabled(boolean include_fpexc_check) advsimd = FALSE; AArch32.CheckAdvSIMDOrFPEnabled(include_fpexc_check, advsimd); // Return from CheckAdvSIMDOrFPEnabled() occurs only if VFP access return;
```

```
is permitted
```

## J1.2.3.29 FPHalvedSub // FPHalvedSub() // ============= bits(N) FPHalvedSub(bits(N) op1, bits(N) op2, FPCR\_Type fpcr) assert N IN {16,32,64}; rounding = FPRoundingMode(fpcr); (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr); if !done then inf1 = (type1 == FPType\_Infinity); inf2 = (type2 == FPType\_Infinity); zero1 = (type1 == FPType\_Zero); zero2 = (type2 == FPType\_Zero); if inf1 &amp;&amp; inf2 &amp;&amp; sign1 == sign2 then result = FPDefaultNaN(fpcr, N); FPProcessException(FPExc\_InvalidOp, fpcr); elsif (inf1 &amp;&amp; sign1 == '0') || (inf2 &amp;&amp; sign2 == '1') then result = FPInfinity('0', N); elsif (inf1 &amp;&amp; sign1 == '1') || (inf2 &amp;&amp; sign2 == '0') then result = FPInfinity('1', N); elsif zero1 &amp;&amp; zero2 &amp;&amp; sign1 != sign2 then result = FPZero(sign1, N); else result\_value = (value1 - value2) / 2.0; if result\_value == 0.0 then // Sign of exact zero result depends on rounding mode result\_sign = if rounding == FPRounding\_NEGINF then '1' else '0'; result = FPZero(result\_sign, N); else result = FPRound(result\_value, fpcr, N); return result; J1.2.3.30 FPRSqrtStep FPType\_Infinity);

```
// FPRSqrtStep() // ============= bits(N) FPRSqrtStep(bits(N) op1, bits(N) op2) assert N IN {16,32}; constant FPCR_Type fpcr = StandardFPCR(); (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr); if !done then inf1 = (type1 == FPType_Infinity); inf2 = (type2 == zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); bits(N) product; if (inf1 && zero2) || (zero1 && inf2) then product = FPZero('0', N); else product = FPMul(op1, op2, fpcr); constant bits(N) three = FPThree('0', N);
```

```
result = FPHalvedSub(three, product, fpcr); return result;
```

## J1.2.3.31 FPRecipStep

```
// FPRecipStep() // ============= bits(N) FPRecipStep(bits(N) op1, bits(N) op2) assert N IN {16,32}; constant FPCR_Type fpcr = StandardFPCR(); (type1,sign1,value1) = FPUnpack(op1, fpcr); (type2,sign2,value2) = FPUnpack(op2, fpcr); (done,result) = FPProcessNaNs(type1, type2, op1, op2, fpcr); if !done then inf1 = (type1 == FPType_Infinity); inf2 = (type2 == FPType_Infinity); zero1 = (type1 == FPType_Zero); zero2 = (type2 == FPType_Zero); bits(N) product; if (inf1 && zero2) || (zero1 && inf2) then product = FPZero('0', N); else product = FPMul(op1, op2, fpcr); constant bits(N) two = FPTwo('0', N); result = FPSub(two, product, fpcr); return result;
```

## J1.2.3.32 StandardFPCR

```
// StandardFPCR() // ============== FPCR_Type StandardFPCR() constant bits(32) value = '00000' : FPSCR.AHP : '110000' : FPSCR.FZ16 : '0000000000000000000'; return ZeroExtend(value, 64);
```

## J1.2.3.33 AArch32.MemSingle

```
// AArch32.MemSingle -non-assignment (read) form // ============================================== // Perform an atomic, little-endian read of 'size' bytes. bits(size*8) AArch32.MemSingle[bits(32) address, integer size, AccessDescriptor accdesc, boolean aligned] bits(size*8) value; AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; (value, memaddrdesc, memstatus) = AArch32.MemSingleRead(address, size, accdesc, aligned); // Check for a fault from translation or the output of translation. if IsFault(memaddrdesc) then AArch32.Abort(memaddrdesc.fault); // Check for external aborts. if IsFault(memstatus) then HandleExternalAbort(memstatus, accdesc.write, memaddrdesc, size, accdesc); return value; // AArch32.MemSingle -assignment (write) form // ===========================================
```

```
// Perform an atomic, little-endian write of 'size' bytes. AArch32.MemSingle[bits(32) address, integer size, AccessDescriptor accdesc, boolean aligned] = bits(size*8) value AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus; (memaddrdesc, memstatus) = AArch32.MemSingleWrite(address, size, accdesc, aligned, value); // Check for a fault from translation or the output of translation. if IsFault(memaddrdesc) then AArch32.Abort(memaddrdesc.fault); // Check for external aborts. if IsFault(memstatus) then HandleExternalWriteAbort(memstatus, memaddrdesc, size, accdesc); return;
```

```
J1.2.3.34 AArch32.MemSingleRead // AArch32.MemSingleRead() // ======================= // Perform an atomic, little-endian read of 'size' bytes. (bits(size*8), AddressDescriptor, PhysMemRetStatus) AArch32.MemSingleRead(bits(32) address, integer size, AccessDescriptor accdesc_in, boolean aligned) assert size IN {1, 2, 4, 8, 16, 32}; bits(size*8) value = bits(size*8) UNKNOWN; PhysMemRetStatus memstatus = PhysMemRetStatus UNKNOWN; AccessDescriptor accdesc = accdesc_in; assert IsAligned(address, size); AddressDescriptor memaddrdesc; memaddrdesc = AArch32.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then return (value, memaddrdesc, memstatus); // Memory array access (memstatus, value) = PhysMemRead(memaddrdesc, size, accdesc); if IsFault(memstatus) then return (value, memaddrdesc, memstatus); if accdesc.acctype == AccessType_IFETCH then if ELUsingAArch32(S1TranslationRegime()) then memaddrdesc.fault = AArch32.CheckDebug(address, accdesc, size); else memaddrdesc.fault = AArch64.CheckDebug(ZeroExtend(address, 64), accdesc, size); return (value, memaddrdesc, memstatus); J1.2.3.35 AArch32.MemSingleWrite // AArch32.MemSingleWrite() // ======================== // Perform an atomic, little-endian write of 'size' bytes. (AddressDescriptor, PhysMemRetStatus) AArch32.MemSingleWrite(bits(32) address, integer size,
```

## AccessDescriptor accdesc\_in, boolean aligned, bits(size*8) value) assert size IN {1, 2, 4, 8, 16, 32}; AccessDescriptor accdesc = accdesc\_in; assert IsAligned(address, size); AddressDescriptor memaddrdesc; PhysMemRetStatus memstatus = PhysMemRetStatus UNKNOWN; memaddrdesc = AArch32.TranslateAddress(address, accdesc, aligned, size); // Check for aborts or debug exceptions if IsFault(memaddrdesc) then return (memaddrdesc, memstatus); // Effect on exclusives if memaddrdesc.memattrs.shareability != Shareability\_NSH then ClearExclusiveByAddress(memaddrdesc.paddress, ProcessorID(), size); memstatus = PhysMemWrite(memaddrdesc, size, accdesc, value); if IsFault(memstatus) then return (memaddrdesc, memstatus); return (memaddrdesc, memstatus); J1.2.3.36 AArch32.UnalignedAccessFaults // AArch32.UnalignedAccessFaults() // =============================== // Determine whether the unaligned access generates an Alignment fault boolean AArch32.UnalignedAccessFaults(AccessDescriptor accdesc) return (AlignmentEnforced() || accdesc.a32lsmd || accdesc.exclusive || accdesc.acqsc || accdesc.relsc); J1.2.3.37 Hint\_PreloadData // Hint\_PreloadData() // ================== Hint\_PreloadData(bits(32) address); J1.2.3.38 Hint\_PreloadDataForWrite // Hint\_PreloadDataForWrite() // ========================== Hint\_PreloadDataForWrite(bits(32) address); J1.2.3.39 Hint\_PreloadInstr // Hint\_PreloadInstr() // =================== Hint\_PreloadInstr(bits(32) address);

## J1.2.3.40 MemA

```
// MemA -getter // ============= bits(8*size) MemA[bits(32) address, integer size] constant boolean acqrel = FALSE; constant boolean privileged = PSTATE.EL != EL0; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescExLDST(MemOp_LOAD, acqrel, tagchecked, privileged); return Mem_with_type[address, size, accdesc]; // MemA -setter // ============= MemA[bits(32) address, integer size] = bits(8*size) value constant boolean acqrel = FALSE; constant boolean privileged = PSTATE.EL != EL0; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = privileged); Mem_with_type[address, size, accdesc] = value; return;
```

```
CreateAccDescExLDST(MemOp_STORE, acqrel, tagchecked, J1.2.3.41 MemO // MemO -getter // ============= bits(8*size) MemO[bits(32) address, integer size] constant boolean acquire = TRUE; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescAcqRel(MemOp_LOAD, tagchecked, acquire); return Mem_with_type[address, size, accdesc]; // MemO -setter // ============= MemO[bits(32) address, integer size] = bits(8*size) value constant boolean acquire = FALSE; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescAcqRel(MemOp_STORE, tagchecked, acquire); Mem_with_type[address, size, accdesc] = value; return; J1.2.3.42 MemS // MemS -getter // ============= // Memory accessor for streaming load multiple instructions bits(8*size) MemS[bits(32) address, integer size] constant AccessDescriptor accdesc = CreateAccDescA32LSMD(MemOp_LOAD); return Mem_with_type[address, size, accdesc]; // MemS -setter // ============= // Memory accessor for streaming store multiple instructions MemS[bits(32) address, integer size] = bits(8*size) value constant AccessDescriptor accdesc = CreateAccDescA32LSMD(MemOp_STORE); Mem_with_type[address, size, accdesc] = value;
```

return;

## J1.2.3.43 MemU

```
// MemU -getter // ============= bits(8*size) MemU[bits(32) address, integer size] constant boolean nontemporal = FALSE; constant boolean privileged = PSTATE.EL != EL0; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked); return Mem_with_type[address, size, accdesc]; // MemU -setter // ============= MemU[bits(32) address, integer size] = bits(8*size) value constant boolean nontemporal = FALSE; constant boolean privileged = PSTATE.EL != EL0; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_STORE, nontemporal, privileged, tagchecked); Mem_with_type[address, size, accdesc] = value; return;
```

## J1.2.3.44 MemU\_unpriv

```
// MemU_unpriv -getter // ==================== bits(8*size) MemU_unpriv[bits(32) address, integer size] constant boolean nontemporal = FALSE; constant boolean privileged = FALSE; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_LOAD, nontemporal, privileged, tagchecked); return Mem_with_type[address, size, accdesc]; // MemU_unpriv -setter // ==================== MemU_unpriv[bits(32) address, integer size] = bits(8*size) value constant boolean nontemporal = FALSE; constant boolean privileged = FALSE; constant boolean tagchecked = FALSE; constant AccessDescriptor accdesc = CreateAccDescGPR(MemOp_STORE, nontemporal, privileged, tagchecked); Mem_with_type[address, size, accdesc] = value; return;
```

## J1.2.3.45

```
// Mem_with_type -non-assignment (read) form // ========================================== // Perform a read of 'size' bytes. The access byte order is reversed for // Instruction fetches would call AArch32.MemSingle directly. bits(size*8) Mem_with_type[bits(32) address, integer size, AccessDescriptor accdesc_in]
```

```
Mem_with_type a big-endian access.
```

```
assert size IN {1, 2, 4, 8, 16, 32}; AccessDescriptor accdesc = accdesc_in; bits(size * 8) value; // Check alignment on size of element accessed, not overall access size constant integer alignment = if accdesc.ispair then size DIV 2 else size; boolean aligned = IsAligned(address, alignment); if !aligned && AArch32.UnalignedAccessFaults(accdesc) then constant FaultRecord fault = AlignmentFault(accdesc, ZeroExtend(address, 64)); AArch32.Abort(fault); if aligned then value = AArch32.MemSingle[address, size, accdesc, aligned]; else assert size > 1; value<7:0> = AArch32.MemSingle[address, 1, accdesc, aligned]; // For subsequent bytes, if they cross to a new translation page which assigns // Device memory type, it is CONSTRAINED UNPREDICTABLE whether an unaligned access // will generate an Alignment Fault. c = ConstrainUnpredictable(Unpredictable_DEVPAGE2); assert c IN {Constraint_FAULT, Constraint_NONE}; if c == Constraint_NONE then aligned = TRUE; for i = 1 to size-1 Elem[value, i, 8] = AArch32.MemSingle[address+i, 1, accdesc, aligned]; if BigEndian(accdesc.acctype) then value = BigEndianReverse(value); return value; // Mem_with_type - assignment (write) form // ======================================= // Perform a write of 'size' bytes. The byte order is reversed for a big-endian access. Mem_with_type[bits(32) address, integer size, AccessDescriptor accdesc_in] = bits(size*8) value_in bits(size*8) value = value_in; AccessDescriptor accdesc = accdesc_in; // Check alignment on size of element accessed, not overall access size constant integer alignment = if accdesc.ispair then size DIV 2 else size; boolean aligned = IsAligned(address, alignment); if !aligned && AArch32.UnalignedAccessFaults(accdesc) then constant FaultRecord fault = AlignmentFault(accdesc, ZeroExtend(address, 64)); AArch32.Abort(fault); if BigEndian(accdesc.acctype) then value = BigEndianReverse(value); if aligned then AArch32.MemSingle[address, size, accdesc, aligned] = value; else assert size > 1; AArch32.MemSingle[address, 1, accdesc, aligned] = value<7:0>; // For subsequent bytes, if they cross to a new translation page which assigns // Device memory type, it is CONSTRAINED UNPREDICTABLE whether an unaligned access // will generate an Alignment Fault. c = ConstrainUnpredictable(Unpredictable_DEVPAGE2); assert c IN {Constraint_FAULT, Constraint_NONE}; if c == Constraint_NONE then aligned = TRUE; for i = 1 to size-1 AArch32.MemSingle[address+i, 1, accdesc, aligned] = Elem[value, i, 8];
```

return;

## J1.2.3.46 AArch32.ESBOperation

```
// AArch32.ESBOperation() // ====================== // Perform the AArch32 ESB operation for ESB executed in AArch32 state. AArch32.ESBOperation() boolean masked; bits(2) target_el; (masked, target_el) = PhysicalSErrorTarget(); // Check if routed to AArch64 state if !masked && !ELUsingAArch32(target_el) then AArch64.ESBOperation(); return; // Check for a masked Physical SError pending that can be synchronized // by an Error synchronization event. if masked && IsSynchronizablePhysicalSErrorPending() then bits(32) syndrome = Zeros(32); syndrome<31> = '1'; // A syndrome<15:0> = AArch32.PhysicalSErrorSyndrome(); DISR = syndrome; ClearPendingPhysicalSError(); return;
```

## J1.2.3.47 AArch32.EncodeAsyncErrorSyndrome

```
// AArch32.EncodeAsyncErrorSyndrome() // ================================== // Return the encoding for specified ErrorState for an SError exception taken // to AArch32 state. bits(2) AArch32.EncodeAsyncErrorSyndrome(ErrorState errorstate) case errorstate of when ErrorState_UC return '00'; when ErrorState_UEU return '01'; when ErrorState_UEO return '10'; when ErrorState_UER return '11'; otherwise Unreachable();
```

## J1.2.3.48 AArch32.PhysicalSErrorSyndrome

```
// AArch32.PhysicalSErrorSyndrome() // ================================ // Generate SError syndrome. bits(16) AArch32.PhysicalSErrorSyndrome() bits(32) syndrome = Zeros(32); constant FaultRecord fault = GetPendingPhysicalSError(); if PSTATE.EL == EL2 then constant ErrorState errstate = PEErrorState(fault); syndrome<11:10> = AArch32.EncodeAsyncErrorSyndrome(errstate); // AET syndrome<9> = fault.extflag; // EA syndrome<5:0> = '010001'; // DFSC else constant boolean long_format = TTBCR.EAE == '1';
```

```
syndrome = AArch32.CommonFaultStatus(fault, long_format); return syndrome<15:0>;
```

## J1.2.3.49 AArch32.vESBOperation

```
// AArch32.vESBOperation() // ======================= // Perform the ESB operation for virtual SError interrupts executed in AArch32 state. // If FEAT_E3DSE is implemented and there is no unmasked virtual SError exception // pending, then AArch64.dESBOperation() is called to perform the AArch64 ESB operation // for a pending delegated SError exception. AArch32.vESBOperation() assert PSTATE.EL IN {EL0, EL1} && EL2Enabled(); // Check for EL2 using AArch64 state if !ELUsingAArch32(EL2) then AArch64.vESBOperation(); return; // If physical SError interrupts are routed to Hyp mode, and TGE is not set, then a virtual // SError interrupt might be pending. vsei_pending = IsVirtualSErrorPending() && HCR.TGE == '0' && HCR.AMO == '1'; vsei_masked = PSTATE.A == '1' || Halted() || ExternalDebugInterruptsDisabled(EL1); // Check for a masked virtual SError pending if vsei_pending && vsei_masked then bits(32) syndrome = Zeros(32); syndrome<31> = '1'; // A syndrome<15:14> = VDFSR<15:14>; // AET syndrome<12> = VDFSR<12>; // ExT syndrome<9> = TTBCR.EAE; // LPAE if TTBCR.EAE == '1' then // Long-descriptor format syndrome<5:0> = '010001'; // STATUS else // Short-descriptor format syndrome<10,3:0> = '10110'; // FS VDISR = syndrome; ClearPendingVirtualSError(); elsif IsFeatureImplemented(FEAT_E3DSE) && !ELUsingAArch32(EL3) then AArch64.dESBOperation(); return;
```

```
J1.2.3.50 AArch32.ResetGeneralRegisters // AArch32.ResetGeneralRegisters() // =============================== AArch32.ResetGeneralRegisters() for i = 0 to 7 R[i] = bits(32) UNKNOWN; for i = 8 to 12 Rmode[i, M32_User] = bits(32) UNKNOWN; Rmode[i, M32_FIQ] = bits(32) UNKNOWN; if HaveEL(EL2) then Rmode[13, M32_Hyp] = bits(32) UNKNOWN; // No R14_hyp for i = 13 to 14 Rmode[i, M32_User] = bits(32) UNKNOWN; Rmode[i, M32_FIQ] = bits(32) UNKNOWN; Rmode[i, M32_IRQ] = bits(32) UNKNOWN; Rmode[i, M32_Svc] = bits(32) UNKNOWN; Rmode[i, M32_Abort] = bits(32) UNKNOWN; Rmode[i, M32_Undef] = bits(32) UNKNOWN;
```

```
if HaveEL(EL3) then Rmode[i, M32_Monitor] = bits(32) UNKNOWN; return;
```

## J1.2.3.51 AArch32.ResetSIMDFPRegisters

```
// AArch32.ResetSIMDFPRegisters() // ============================== UNKNOWN;
```

```
AArch32.ResetSIMDFPRegisters() for i = 0 to 15 Q[i] = bits(128) return;
```

## J1.2.3.52 AArch32.ResetSpecialRegisters

```
// AArch32.ResetSpecialRegisters() // =============================== AArch32.ResetSpecialRegisters() // AArch32 special registers SPSR_fiq<31:0> = bits(32) UNKNOWN; SPSR_irq<31:0> = bits(32) UNKNOWN; SPSR_svc<31:0> = bits(32) UNKNOWN; SPSR_abt<31:0> = bits(32) UNKNOWN; SPSR_und<31:0> = bits(32) UNKNOWN; if HaveEL(EL2) then SPSR_hyp = bits(32) UNKNOWN; ELR_hyp = bits(32) UNKNOWN; if HaveEL(EL3) then SPSR_mon = bits(32) UNKNOWN; // External debug special registers DLR = bits(32) UNKNOWN; DSPSR = bits(32) UNKNOWN; return;
```

## J1.2.3.53 AArch32.ResetSystemRegisters

```
// AArch32.ResetSystemRegisters() // ============================== AArch32.ResetSystemRegisters(boolean cold_reset);
```

## J1.2.3.54 ALUExceptionReturn

```
// ALUExceptionReturn() // ==================== ALUExceptionReturn(bits(32) address) if PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.M IN {M32_User,M32_System} then constant Constraint c = ConstrainUnpredictable(Unpredictable_ALUEXCEPTIONRETURN); assert c IN {Constraint_UNDEF, Constraint_NOP}; case c of
```

```
when Constraint_UNDEF UNDEFINED; when Constraint_NOP ExecuteAsNOP(); else
```

```
AArch32.ExceptionReturn(address, SPSR_curr[]); J1.2.3.55 ALUWritePC // ALUWritePC() // ============ ALUWritePC(bits(32) address) if CurrentInstrSet() == InstrSet_A32 then BXWritePC(address, BranchType_INDIR); else BranchWritePC(address, BranchType_INDIR); J1.2.3.56 BXWritePC // BXWritePC() // =========== BXWritePC(bits(32) address_in, BranchType branch_type) bits(32) address = address_in; if address<0> == '1' then SelectInstrSet(InstrSet_T32); address<0> = '0'; else SelectInstrSet(InstrSet_A32); // For branches to an unaligned PC counter in A32 state, the PE takes the branch // and does one of: // * Forces the address to be aligned // * Leaves the PC unaligned, meaning the target generates a PC Alignment fault. if address<1> == '1' && ConstrainUnpredictableBool(Unpredictable_A32FORCEALIGNPC) then address<1> = '0'; constant boolean branch_conditional = CurrentCond() != '111x'; BranchTo(address, branch_type, branch_conditional); J1.2.3.57 BranchWritePC // BranchWritePC() // =============== BranchWritePC(bits(32) address_in, BranchType branch_type) bits(32) address = address_in; if CurrentInstrSet() == InstrSet_A32 then address<1:0> = '00'; else address<0> = '0'; constant boolean branch_conditional = CurrentCond() != '111x'; BranchTo(address, branch_type, branch_conditional); J1.2.3.58 CBWritePC instruction.
```

```
// CBWritePC() // =========== // Takes a branch from a CBNZ/CBZ CBWritePC(bits(32) address_in)
```

```
bits(32) address = address_in; assert CurrentInstrSet() == InstrSet_T32; address<0> = '0'; constant boolean branch_conditional = TRUE; BranchTo(address, BranchType_DIR, branch_conditional);
```

## J1.2.3.59 D

```
// D -getter // ========== bits(64) D[integer n] assert n >= 0 && n <= 31; constant bits(128) vreg = V[n DIV 2, 128]; return Elem[vreg, n MOD 2, 64]; // D -setter // ========== D[integer n] = bits(64) value assert n >= 0 && n <= 31; bits(128) vreg = V[n DIV 2, 128]; Elem[vreg, n MOD 2, 64] = value; V[n DIV 2, 128] = vreg; return;
```

## J1.2.3.60 Din

```
// Din - getter // ============ // Return the initial value of D input bits(64) Din[integer n] assert n >= 0 && n <= 31; return _Dclone[n];
```

## J1.2.3.61 H

```
// H -getter // ========== bits(16) H[integer n] assert n >= 0 && n <= 31; return S[n]<15:0>; // H -setter // ========== H[integer n] = bits(16) value S[n] = ZeroExtend(value, 32);
```

## J1.2.3.62 LR

```
// LR - setter // =========== LR = bits(32) value R[14] = value; return;
```

```
// LR - getter // =========== bits(32) LR return
```

## R[14]; J1.2.3.63 LoadWritePC // LoadWritePC() // ============= LoadWritePC(bits(32) address) BXWritePC(address, BranchType\_INDIR); J1.2.3.64 LookUpRIndex // LookUpRIndex() // ============== integer LookUpRIndex(integer n, bits(5) mode) assert n &gt;= 0 &amp;&amp; n &lt;= 14; integer result; case n of // Select index by mode: usr fiq irq svc abt und hyp when 8 result = RBankSelect(mode, 8, 24, 8, 8, 8, 8, 8); when 9 result = RBankSelect(mode, 9, 25, 9, 9, 9, 9, 9); when 10 result = RBankSelect(mode, 10, 26, 10, 10, 10, 10, 10); when 11 result = RBankSelect(mode, 11, 27, 11, 11, 11, 11, 11); when 12 result = RBankSelect(mode, 12, 28, 12, 12, 12, 12, 12); when 13 result = RBankSelect(mode, 13, 29, 17, 19, 21, 23, 15); when 14 result = RBankSelect(mode, 14, 30, 16, 18, 20, 22, 14); otherwise result = n; return result; J1.2.3.65 Monitor // Monitor mode registers // ====================== // The Monitor mode registers do not map to X registers, so must be defined separately bits(32) SP\_mon; bits(32) LR\_mon; J1.2.3.66 PC32 // AArch32 program counter // PC32 -getter // ============= // Read 32-bit program counter bits(32) PC32 return R[15]; // This includes the offset from AArch32 state

## J1.2.3.67 PCStoreValue

```
// PCStoreValue() // ============== bits(32) PCStoreValue() // This function returns the PC value. On architecture versions before Armv7, it // is permitted to instead return PC+4, provided it does so consistently. It is // used only to describe A32 instructions, so it returns the address of the current // instruction plus 8 (normally) or 12 (when the alternative is permitted). return PC32;
```

## J1.2.3.68 Q

```
// Q -getter // ========== bits(128) Q[integer n] assert n >= 0 && n <= 15; return V[n, 128]; // Q -setter // ========== Q[integer n] = bits(128) value assert n >= 0 && n <= 15; V[n, 128] = value; return;
```

## J1.2.3.69 Qin

```
// Qin - getter // ============ // Return the initial value of Q input bits(128) Qin[integer n] assert n >= 0 && n <= 15; return Din[2*n+1]:Din[2*n];
```

## J1.2.3.70 R

```
// R -setter // ========== R[integer n] = bits(32) value Rmode[n, PSTATE.M] = value; return; // R -getter // ========== bits(32) R[integer n] if n == 15 then offset = (if CurrentInstrSet() == InstrSet_A32 then 8 else 4); return _PC<31:0> + offset; else return Rmode[n, PSTATE.M]; // R -setter // ==========
```

## R[integer lr, integer hr] = bits(64) value R[lr] = value&lt;0+:32&gt;; R[hr] = value&lt;32+:32&gt;; return; // R -getter // ========== bits(64) R[integer lr, integer hr] return R[hr] : R[lr]; J1.2.3.71 RBankSelect // RBankSelect() // ============= integer RBankSelect(bits(5) mode, integer usr, integer fiq, integer irq, integer svc, integer abt, integer und, integer hyp) integer result; case mode of when M32\_User result = usr; // User mode when M32\_FIQ result = fiq; // FIQ mode when M32\_IRQ result = irq; // IRQ mode when M32\_Svc result = svc; // Supervisor mode when M32\_Abort result = abt; // Abort mode when M32\_Hyp result = hyp; // Hyp mode when M32\_Undef result = und; // Undefined mode when M32\_System result = usr; // System mode uses User mode registers otherwise Unreachable(); // Monitor mode return result; J1.2.3.72 ReadAnyAllocatedRegister // ReadAnyAllocatedRegister() // ========================== bits(32) ReadAnyAllocatedRegister(); J1.2.3.73 ReadAnyAllocatedSPSR // ReadAnyAllocatedSPSR() // ========================== bits(32) ReadAnyAllocatedSPSR(); J1.2.3.74 Rmode M32\_Monitor;

```
// Rmode -getter // ============== bits(32) Rmode[integer n, bits(5) mode] assert n >= 0 && n <= 14; // Check for attempted use of Monitor mode in Non-secure state. if CurrentSecurityState() != SS_Secure then assert mode != assert !BadMode(mode); if mode == M32_Monitor then
```

```
if n == 13 then return SP_mon; elsif n == 14 then return LR_mon; else return _R[n]<31:0>; else return _R[LookUpRIndex(n, mode)]<31:0>; // Rmode -setter // ============== Rmode[integer n, bits(5) mode] = bits(32) value assert n >= 0 && n <= 14; // Check for attempted use of Monitor mode in Non-secure state. if CurrentSecurityState() != SS_Secure then assert mode != M32_Monitor; assert !BadMode(mode); if mode == M32_Monitor then if n == 13 then SP_mon = value; elsif n == 14 then LR_mon = value; else _R[n]<31:0> = value; else // It is CONSTRAINED UNPREDICTABLE whether the upper 32 bits of the X // register are unchanged or set to zero. This is also tested for on // exception entry, as this applies to all AArch32 registers. if HaveAArch64() && ConstrainUnpredictableBool(Unpredictable_ZEROUPPER) then _R[LookUpRIndex(n, mode)] = ZeroExtend(value, 64); else _R[LookUpRIndex(n, mode)]<31:0> = value; return;
```

## J1.2.3.75 S

```
// S -getter // ========== bits(32) S[integer n] assert n >= 0 && n <= 31; constant bits(128) vreg = V[n DIV 4, 128]; return Elem[vreg, n MOD 4, 32]; // S -setter // ========== S[integer n] = bits(32) value assert n >= 0 && n <= 31; bits(128) vreg = V[n DIV 4, 128]; Elem[vreg, n MOD 4, 32] = value; V[n DIV 4, 128] = vreg; return;
```

## J1.2.3.76 WriteAnyAllocatedRegister

```
// WriteAnyAllocatedRegister() // =========================== WriteAnyAllocatedRegister(bits(32)
```

value);

## J1.2.3.77 WriteAnyAllocatedSPSR

```
// WriteAnyAllocatedSPSR() // =========================== WriteAnyAllocatedSPSR(bits(32)
```

```
// _Dclone[] // ========= // Clone the 64-bit Advanced SIMD and VFP extension register bank for use as input to // instruction pseudocode, to avoid read-after-write for Advanced SIMD and VFP array bits(64) _Dclone[0..31];
```

```
operations.
```

```
// AArch32.ExceptionReturn() // ========================= AArch32.ExceptionReturn(bits(32) new_pc_in, bits(32) spsr) bits(32) new_pc = new_pc_in; SynchronizeContext(); // Attempts to change to an illegal mode or state will invoke the Illegal Execution state // mechanism SetPSTATEFromPSR(spsr); ClearExclusiveLocal(ProcessorID()); SendEventLocal(); if PSTATE.IL == '1' then // If the exception return is illegal, PC[1:0] are UNKNOWN new_pc<1:0> = bits(2) UNKNOWN; else // LR[1:0] or LR[0] are treated as being 0, depending on the target instruction set state if PSTATE.T == '1' then new_pc<0> = '0'; // T32 else new_pc<1:0> = '00'; // A32 constant boolean branch_conditional = CurrentCond() != '111x'; BranchTo(new_pc, BranchType_ERET, branch_conditional); CheckExceptionCatch(FALSE); // Check for debug event on exception return
```

## value); J1.2.3.78 \_Dclone J1.2.3.79 AArch32.ExceptionReturn J1.2.3.80 AArch32.ExecutingCP10or11Instr

```
// AArch32.ExecutingCP10or11Instr() // ================================ boolean AArch32.ExecutingCP10or11Instr() instr = ThisInstr(); instr_set = CurrentInstrSet(); assert instr_set IN {InstrSet_A32, InstrSet_T32}; if instr_set == InstrSet_A32 then return ((instr<27:24> == '1110' || instr<27:25> == '110') && instr<11:8> == '101x'); else // InstrSet_T32 return (instr<31:28> == '111x' && (instr<27:24> == '1110' || instr<27:25> == '110') && instr<11:8> == '101x');
```

## J1.2.3.81 AArch32.ITAdvance

```
// AArch32.ITAdvance() // =================== AArch32.ITAdvance() if PSTATE.IT<2:0> == '000' then PSTATE.IT = '00000000'; else PSTATE.IT<4:0> = LSL(PSTATE.IT<4:0>, 1); return;
```

## J1.2.3.82 AArch32.InterruptPending

```
// AArch32.InterruptPending() // ========================== // Returns TRUE if there are any pending physical or virtual interrupts, and FALSE otherwise. boolean AArch32.InterruptPending() if !ELUsingAArch32(EL2) then return AArch64.InterruptPending(); (irq_pending, -) = IRQPending(); (fiq_pending, -) = FIQPending(); constant boolean pending_physical_interrupt = (irq_pending || fiq_pending || IsPhysicalSErrorPending()); boolean pending_virtual_interrupt = FALSE; if EL2Enabled() && PSTATE.EL IN {EL0, EL1} && HCR.TGE == '0' then constant boolean virq_pending = (HCR.IMO == '1' && (VirtualIRQPending() || HCR.VI == '1')); constant boolean vfiq_pending = (HCR.FMO == '1' && (VirtualFIQPending() || HCR.VF == '1')); constant boolean vsei_pending = (HCR.AMO == '1' && (IsVirtualSErrorPending() || HCR.VA == '1')); pending_virtual_interrupt = vsei_pending || virq_pending || vfiq_pending; return pending_physical_interrupt || pending_virtual_interrupt;
```

## J1.2.3.83 AArch32.SysRegRead

```
// AArch32.SysRegRead() // ==================== // Read from a 32-bit AArch32 System register and write the register's contents to R[t]. AArch32.SysRegRead(integer cp_num, bits(32) instr, integer t);
```

## J1.2.3.84 AArch32.SysRegRead64

```
// AArch32.SysRegRead64() // ====================== // Read from a 64-bit AArch32 System register and write the register's contents to R[t] and R[t2]. AArch32.SysRegRead64(integer cp_num, bits(32) instr, integer t, integer t2);
```

## J1.2.3.85 AArch32.SysRegReadCanWriteAPSR

## // AArch32.SysRegReadCanWriteAPSR() // ================================ // Determines whether the AArch32 System register read instruction can write to APSR flags. boolean AArch32.SysRegReadCanWriteAPSR(integer cp\_num, bits(32) instr) assert UsingAArch32(); assert (cp\_num IN {14,15}); assert cp\_num == UInt(instr&lt;11:8&gt;); opc1 = UInt(instr&lt;23:21&gt;); opc2 = UInt(instr&lt;7:5&gt;); CRn = UInt(instr&lt;19:16&gt;); CRm = UInt(instr&lt;3:0&gt;); if cp\_num == 14 &amp;&amp; opc1 == 0 &amp;&amp; CRn == 0 &amp;&amp; CRm == 1 &amp;&amp; opc2 == 0 then // DBGDSCRint return TRUE; return FALSE; J1.2.3.86 AArch32.SysRegWrite // AArch32.SysRegWrite() // ===================== // Read the contents of R[t] and write to a 32-bit AArch32 System register. AArch32.SysRegWrite(integer cp\_num, bits(32) instr, integer t); J1.2.3.87 AArch32.SysRegWrite64 // AArch32.SysRegWrite64() // ======================= // Read the contents of R[t] and R[t2] and write to a 64-bit AArch32 System register. AArch32.SysRegWrite64(integer cp\_num, bits(32) instr, integer t, integer t2); J1.2.3.88 AArch32.SysRegWriteM // AArch32.SysRegWriteM() // ====================== // Read a value from a virtual address and write it to an AArch32 System register. AArch32.SysRegWriteM(integer cp\_num, bits(32) instr, bits(32) address); J1.2.3.89 AArch32.WriteMode only.

```
// AArch32.WriteMode() // =================== // Function for dealing with writes to PSTATE.M from AArch32 state // This ensures that PSTATE.EL and PSTATE.SP are always valid. AArch32.WriteMode(bits(5) mode) (valid,el) = ELFromM32(mode); assert valid; PSTATE.M = mode; PSTATE.EL = el; PSTATE.nRW = '1'; PSTATE.SP = (if mode IN {M32_User,M32_System} then '0' else '1'); return;
```

## J1.2.3.90 AArch32.WriteModeByInstr

```
// AArch32.WriteModeByInstr() // ========================== // Function for dealing with writes to PSTATE.M from an AArch32 instruction, and ensuring that // illegal state changes are correctly flagged in PSTATE.IL. AArch32.WriteModeByInstr(bits(5) mode) (valid,el) = ELFromM32(mode); // 'valid' is set to FALSE if' mode' is invalid for this implementation or the current value // of SCR.NS/SCR_EL3.NS. Additionally, it is illegal for an instruction to write 'mode' to // PSTATE.EL if it would result in any of: // * A change to a mode that would cause entry to a higher Exception level. if UInt(el) > UInt(PSTATE.EL) then valid = FALSE; // * A change to or from Hyp mode. if (PSTATE.M == M32_Hyp || mode == M32_Hyp) && PSTATE.M != mode then valid = FALSE; // * When EL2 is implemented, the value of HCR.TGE is '1', a change to a Non-secure EL1 mode. if PSTATE.M == M32_Monitor && HaveEL(EL2) && el == EL1 && SCR.NS == '1' && HCR.TGE == '1' then valid = FALSE; if !valid then PSTATE.IL = '1'; else AArch32.WriteMode(mode);
```

```
// BadMode() // ========= boolean BadMode(bits(5) mode) // Return TRUE if 'mode' encodes a mode that is not valid for this implementation boolean valid; case mode of when M32_Monitor valid = HaveAArch32EL(EL3); when M32_Hyp valid = HaveAArch32EL(EL2); when M32_FIQ, M32_IRQ, M32_Svc, M32_Abort, M32_Undef, M32_System // If EL3 is implemented and using AArch32, then these modes are EL3 modes in Secure // state, and EL1 modes in Non-secure state. If EL3 is not implemented or is using // AArch64, then these modes are EL1 modes. // Therefore it is sufficient to test this implementation supports EL1 using AArch32. valid = HaveAArch32EL(EL1); when M32_User valid = HaveAArch32EL(EL0); otherwise valid = FALSE; // Passed an illegal mode value return !valid;
```

## J1.2.3.91 BadMode J1.2.3.92 BankedRegisterAccessValid

```
// BankedRegisterAccessValid() // =========================== // Checks for MRS (Banked register) or MSR (Banked register) accesses to registers // other than the SPSRs that are invalid. This includes ELR_hyp accesses. (boolean, Constraint) BankedRegisterAccessValid(bits(5) SYSm, bits(5) mode)
```

```
boolean valid = TRUE; Constraint c = Constraint_NONE; boolean banked_unpred = FALSE; case SYSm of when '000xx', '00100' // R8_usr to R12_usr banked_unpred = mode != M32_FIQ; when '00101' // SP_usr banked_unpred = mode == M32_System; when '00110' // LR_usr banked_unpred = mode IN {M32_Hyp,M32_System}; when '010xx', '0110x', '01110' // R8_fiq to R12_fiq, SP_fiq, LR_fiq banked_unpred = mode == M32_FIQ; when '1000x' // LR_irq, SP_irq banked_unpred = mode == M32_IRQ; when '1001x' // LR_svc, SP_svc banked_unpred = mode == M32_Svc; when '1010x' // LR_abt, SP_abt banked_unpred = mode == M32_Abort; when '1011x' // LR_und, SP_und banked_unpred = mode == M32_Undef; when '1110x' // LR_mon, SP_mon banked_unpred = (!HaveEL(EL3) || CurrentSecurityState() != SS_Secure || mode == M32_Monitor); when '11110' // ELR_hyp, only from Monitor or Hyp mode banked_unpred = !HaveEL(EL2) || ! mode IN {M32_Monitor,M32_Hyp}; when '11111' // SP_hyp, only from Monitor mode banked_unpred = !HaveEL(EL2) || mode != M32_Monitor; otherwise valid = FALSE; c = ConstrainUnpredictable(Unpredictable_UnimplementedRegister); assert c IN {Constraint_UNDEF, Constraint_NOP, Constraint_ANYREG}; if banked_unpred then valid = FALSE; c = ConstrainUnpredictable(Unpredictable_BankedRegister); assert c IN {Constraint_UNDEF, Constraint_NOP, Constraint_UNKNOWN}; return (valid, c);
```

## J1.2.3.93 CPSRWriteByInstr

```
// CPSRWriteByInstr() // ================== // Update PSTATE.<N,Z,C,V,Q,GE,E,A,I,F,M> from a CPSR value written by an MSR instruction. CPSRWriteByInstr(bits(32) value, bits(4) bytemask) privileged = PSTATE.EL != EL0; // PSTATE.<A,I,F,M> are not writable at // Write PSTATE from 'value', ignoring bytes masked by 'bytemask' if bytemask<3> == '1' then PSTATE.<N,Z,C,V,Q> = value<31:27>; // Bits <26:24> are ignored if bytemask<2> == '1' then if IsFeatureImplemented(FEAT_SSBS) then PSTATE.SSBS = value<23>; if privileged then PSTATE.PAN = value<22>; if IsFeatureImplemented(FEAT_DIT) then PSTATE.DIT = value<21>; // Bit <20> is RES0 PSTATE.GE = value<19:16>; if bytemask<1> == '1' then // Bits <15:10> are RES0
```

```
EL0
```

```
PSTATE.E = value<9>; // PSTATE.E is writable at EL0 if privileged then PSTATE.A = value<8>; if bytemask<0> == '1' then if privileged then PSTATE.<I,F> = value<7:6>; // Bit <5> is RES0 // AArch32.WriteModeByInstr() sets PSTATE.IL to 1 if this is an illegal mode change. AArch32.WriteModeByInstr(value<4:0>); return;
```

## J1.2.3.94 ConditionPassed

```
// ConditionPassed() // ================= boolean ConditionPassed() return ConditionHolds(CurrentCond());
```

## J1.2.3.95 CurrentCond

```
// CurrentCond() // ============= // Returns the condition code that applies to the currently executing instruction bits(4) CurrentCond();
```

## J1.2.3.96 InITBlock

```
// InITBlock() // =========== boolean InITBlock() if CurrentInstrSet() == InstrSet_T32 then return PSTATE.IT<3:0> != '0000'; else return FALSE;
```

## J1.2.3.97 LastInITBlock

```
// LastInITBlock() // =============== boolean LastInITBlock() return (PSTATE.IT<3:0> == '1000');
```

## J1.2.3.98 SPSRWriteByInstr

```
// SPSRWriteByInstr() // ================== SPSRWriteByInstr(bits(32) value, bits(4) bytemask) bits(32) new_spsr = SPSR_curr[]; if bytemask<3> == '1' then new_spsr<31:24> = value<31:24>; // N,Z,C,V,Q flags, IT[1:0],J bits
```

```
if bytemask<2> == '1' then new_spsr<23:16> = value<23:16>; // IL bit, GE[3:0] flags if bytemask<1> == '1' then new_spsr<15:8> = value<15:8>; // IT[7:2] bits, E bit, A interrupt mask if bytemask<0> == '1' then new_spsr<7:0> = value<7:0>; // I,F interrupt masks, T bit, Mode bits SPSR_curr[] = new_spsr; // UNPREDICTABLE if User or System mode return;
```

## J1.2.3.99 SPSRaccessValid

```
// SPSRaccessValid() // ================= // Checks for MRS (Banked register) or MSR (Banked register) accesses to the SPSRs // that are UNPREDICTABLE (boolean, Constraint) SPSRaccessValid(bits(5) SYSm, bits(5) mode) boolean valid = TRUE; Constraint c = Constraint_NONE; boolean banked_unpred = FALSE; case SYSm of when '01110' // SPSR_fiq banked_unpred = mode == M32_FIQ; when '10000' // SPSR_irq banked_unpred = mode == M32_IRQ; when '10010' // SPSR_svc banked_unpred = mode == M32_Svc; when '10100' // SPSR_abt banked_unpred = mode == M32_Abort; when '10110' // SPSR_und banked_unpred = mode == M32_Undef; when '11100' // SPSR_mon banked_unpred = (!HaveEL(EL3) || mode == M32_Monitor || CurrentSecurityState() != SS_Secure); when '11110' // SPSR_hyp banked_unpred = !HaveEL(EL2) || mode != M32_Monitor; otherwise valid = FALSE; c = ConstrainUnpredictable(Unpredictable_UnimplementedRegister); assert c IN {Constraint_UNDEF, Constraint_NOP, Constraint_ANYREG}; if banked_unpred then valid = FALSE; c = ConstrainUnpredictable(Unpredictable_BankedRegister); assert c IN {Constraint_UNDEF, Constraint_NOP, Constraint_UNKNOWN}; return (valid, c);
```

## J1.2.3.100 SelectInstrSet

```
// SelectInstrSet() // ================ SelectInstrSet(InstrSet iset) assert CurrentInstrSet() IN {InstrSet_A32, InstrSet_T32}; assert iset IN {InstrSet_A32, InstrSet_T32}; PSTATE.T = if iset == InstrSet_A32 then '0' else '1';
```

return;

## J1.2.3.101 AArch32.DTLBI\_ALL

```
// AArch32.DTLBI_ALL() // =================== // Invalidate all data TLB entries for the indicated translation regime with the // the indicated security state for all TLBs within the indicated broadcast domain. // Invalidation applies to all applicable stage 1 and stage 2 entries. AArch32.DTLBI_ALL(SecurityState security, Regime regime, Broadcast broadcast, TLBIMemAttr attr) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_DALL; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.level = TLBILevel_Any; r.attr = attr; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.2.3.102 AArch32.DTLBI\_ASID

```
// AArch32.DTLBI_ASID() // ==================== // Invalidate all data TLB stage 1 entries matching the indicated VMID (where regime supports) // and ASID in the parameter Rt in the indicated translation regime with the // indicated security state for all TLBs within the indicated broadcast domain. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch32.DTLBI_ASID(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBIMemAttr attr, bits(32) Rt) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_DASID; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = TLBILevel_Any; r.attr = attr; r.asid = Zeros(8) : Rt<7:0>; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.2.3.103 AArch32.DTLBI\_VA

```
// AArch32.DTLBI_VA() // ================== // Invalidate by VA all stage 1 data TLB entries in the indicated broadcast domain // matching the indicated VMID and ASID (where regime supports VMID, ASID) in the indicated regime // with the indicated security state.
```

```
// ASID, VA and related parameters are derived from Rt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch32.DTLBI_VA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBILevel level, TLBIMemAttr attr, bits(32) Rt) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_DVA; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.asid = Zeros(8) : Rt<7:0>; r.address = Zeros(32) : Rt<31:12> : Zeros(12); TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.2.3.104 AArch32.ITLBI\_ALL

```
// AArch32.ITLBI_ALL() // =================== // Invalidate all instruction TLB entries for the indicated translation regime with the // the indicated security state for all TLBs within the indicated broadcast domain. // Invalidation applies to all applicable stage 1 and stage 2 entries. AArch32.ITLBI_ALL(SecurityState security, Regime regime, Broadcast broadcast, TLBIMemAttr attr) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_IALL; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.level = TLBILevel_Any; r.attr = attr; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.2.3.105 AArch32.ITLBI\_ASID

```
// AArch32.ITLBI_ASID() // ==================== // Invalidate all instruction TLB stage 1 entries matching the indicated VMID // (where regime supports) and ASID in the parameter Rt in the indicated translation // regime with the indicated security state for all TLBs within the indicated broadcast domain. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch32.ITLBI_ASID(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBIMemAttr attr, bits(32) Rt) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_IASID; r.from_aarch64 = FALSE;
```

```
r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = TLBILevel_Any; r.attr = attr; r.asid = Zeros(8) : Rt<7:0>; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.2.3.106 AArch32.ITLBI\_VA

```
// AArch32.ITLBI_VA() // ================== // Invalidate by VA all stage 1 instruction TLB entries in the indicated broadcast domain // matching the indicated VMID and ASID (where regime supports VMID, ASID) in the indicated regime // with the indicated security state. // ASID, VA and related parameters are derived from Rt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch32.ITLBI_VA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBILevel level, TLBIMemAttr attr, bits(32) Rt) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_IVA; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.asid = Zeros(8) : Rt<7:0>; r.address = Zeros(32) : Rt<31:12> : Zeros(12); TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.2.3.107 AArch32.TLBI\_ALL

```
// AArch32.TLBI_ALL() // ================== // Invalidate all entries for the indicated translation regime with the // the indicated security state for all TLBs within the indicated broadcast domain. // Invalidation applies to all applicable stage 1 and stage 2 entries. AArch32.TLBI_ALL(SecurityState security, Regime regime, Broadcast broadcast, TLBIMemAttr attr) assert PSTATE.EL IN {EL3, EL2}; TLBIRecord r; r.op = TLBIOp_ALL; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.level = TLBILevel_Any; r.attr = attr; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r);
```

return;

## J1.2.3.108 AArch32.TLBI\_ASID

```
// AArch32.TLBI_ASID() // =================== // Invalidate all stage 1 entries matching the indicated VMID (where regime supports) // and ASID in the parameter Rt in the indicated translation regime with the // indicated security state for all TLBs within the indicated broadcast domain. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch32.TLBI_ASID(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBIMemAttr attr, bits(32) Rt) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_ASID; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = TLBILevel_Any; r.attr = attr; r.asid = Zeros(8) : Rt<7:0>; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.2.3.109 AArch32.TLBI\_IPAS2

```
// AArch32.TLBI_IPAS2() // ==================== // Invalidate by IPA all stage 2 only TLB entries in the indicated broadcast // domain matching the indicated VMID in the indicated regime with the indicated security state. // Note: stage 1 and stage 2 combined entries are not in the scope of this operation. // IPA and related parameters of the are derived from Rt. AArch32.TLBI_IPAS2(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBILevel level, TLBIMemAttr attr, bits(32) Rt) assert PSTATE.EL IN {EL3, EL2}; assert security == SS_NonSecure; TLBIRecord r; r.op = TLBIOp_IPAS2; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = TRUE; r.level = level; r.attr = attr; r.address = Zeros(24) : Rt<27:0> : Zeros(12); r.ipaspace = PAS_NonSecure; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.2.3.110 AArch32.TLBI\_VA

```
// AArch32.TLBI_VA() // ================= // Invalidate by VA all stage 1 TLB entries in the indicated broadcast domain // matching the indicated VMID and ASID (where regime supports VMID, ASID) in the indicated regime // with the indicated security state. // ASID, VA and related parameters are derived from Rt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch32.TLBI_VA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBILevel level, TLBIMemAttr attr, bits(32) Rt) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_VA; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.asid = Zeros(8) : Rt<7:0>; r.address = Zeros(32) : Rt<31:12> : Zeros(12); TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

```
J1.2.3.111 AArch32.TLBI_VAA
```

```
// AArch32.TLBI_VAA() // ================== // Invalidate by VA all stage 1 TLB entries in the indicated broadcast domain // matching the indicated VMID (where regime supports VMID) and all ASID in the indicated regime // with the indicated security state. // VA and related parameters are derived from Rt. // Note: stage 1 and stage 2 combined entries are in the scope of this operation. AArch32.TLBI_VAA(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBILevel level, TLBIMemAttr attr, bits(32) Rt) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_VAA; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.level = level; r.attr = attr; r.address = Zeros(32) : Rt<31:12> : Zeros(12); TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

## J1.2.3.112 AArch32.TLBI\_VMALL

```
// AArch32.TLBI_VMALL() // ==================== // Invalidate all stage 1 entries for the indicated translation regime with the // the indicated security state for all TLBs within the indicated broadcast // domain that match the indicated VMID (where applicable). // Note: stage 1 and stage 2 combined entries are in the scope of this // Note: stage 2 only entries are not in the scope of this operation. AArch32.TLBI_VMALL(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBIMemAttr attr) assert PSTATE.EL IN {EL3, EL2, EL1}; TLBIRecord r; r.op = TLBIOp_VMALL; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.level = TLBILevel_Any; r.vmid = vmid; r.use_vmid = UseVMID(regime); r.attr = attr; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return;
```

```
operation. J1.2.3.113 AArch32.TLBI_VMALLS12 // AArch32.TLBI_VMALLS12() // ======================= // Invalidate all stage 1 and stage 2 entries for the indicated translation // regime with the indicated security state for all TLBs within the indicated // broadcast domain that match the indicated VMID. AArch32.TLBI_VMALLS12(SecurityState security, Regime regime, bits(16) vmid, Broadcast broadcast, TLBIMemAttr attr) assert PSTATE.EL IN {EL3, EL2}; TLBIRecord r; r.op = TLBIOp_VMALLS12; r.from_aarch64 = FALSE; r.security = security; r.regime = regime; r.level = TLBILevel_Any; r.vmid = vmid; r.use_vmid = TRUE; r.attr = attr; TLBI(r); if broadcast != Broadcast_NSH then BroadcastTLBI(broadcast, r); return; J1.2.3.114 Sat // Sat() // ===== bits(N) Sat(integer i, integer N, boolean unsigned) result = if unsigned then UnsignedSat(i, N) else SignedSat(i, N); return result;
```

## J1.2.3.115 AArch32.RestrictPrediction

```
// AArch32.RestrictPrediction() // ============================ // Clear all predictions in the context. AArch32.RestrictPrediction(bits(32) val, RestrictType restriction) ExecutionCntxt c; target_el = val<25:24>; // If the target EL is not implemented or the instruction is executed at an // EL lower than the specified level, the instruction is treated as a NOP. if !HaveEL(target_el) || UInt(target_el) > UInt(PSTATE.EL) then ExecuteAsNOP(); constant bit ns = val<26>; constant bit nse = bit UNKNOWN; ss = TargetSecurityState(ns, nse); c.security = ss; c.target_el = target_el; if EL2Enabled() then if PSTATE.EL IN {EL0, EL1} then c.is_vmid_valid = TRUE; c.all_vmid = FALSE; c.vmid = VMID[]; elsif target_el IN {EL0, EL1} then c.is_vmid_valid = TRUE; c.all_vmid = val<27> == '1'; c.vmid = ZeroExtend(val<23:16>, 16); // Only valid if val<27> == '0'; else c.is_vmid_valid = FALSE; else c.is_vmid_valid = FALSE; if PSTATE.EL == EL0 then c.is_asid_valid = TRUE; c.all_asid = FALSE; c.asid = ASID[]; elsif target_el == EL0 then c.is_asid_valid = TRUE; c.all_asid = val<8> == '1'; c.asid = ZeroExtend(val<7:0>, 16); // Only valid if val<8> == '0'; else c.is_asid_valid = FALSE; c.restriction = restriction; RESTRICT_PREDICTIONS(c);
```

## J1.2.4 aarch32/translation

This section includes the following pseudocode functions:

- AArch32.DefaultTEXDecode
- AArch32.MAIRAttr
- AArch32.RemappedTEXDecode
- AArch32.CheckBreakpoint
- AArch32.CheckDebug

- AArch32.CheckVectorCatch
- AArch32.CheckWatchpoint
- AArch32.IPAIsOutOfRange
- AArch32.S1HasAlignmentFaultDueToMemType
- AArch32.S1LDHasPermissionsFault
- AArch32.S1SDHasPermissionsFault
- AArch32.S2HasAlignmentFaultDueToMemType
- AArch32.S2HasPermissionsFault
- AArch32.S2InconsistentSL
- AArch32.VAIsOutOfRange
- AArch32.GetS1TLBContext
- AArch32.GetS2TLBContext
- AArch32.TLBContextEL10
- AArch32.TLBContextEL2
- AArch32.TLBContextEL30
- AArch32.EL2Enabled
- AArch32.FullTranslate
- AArch32.OutputDomain
- AArch32.S1DisabledOutput
- AArch32.S1Enabled
- AArch32.S1TranslateLD
- AArch32.S1TranslateSD
- AArch32.S2Translate
- AArch32.SDStageOA
- AArch32.TranslateAddress
- SDFSize
- AArch32.DecodeDescriptorTypeLD
- AArch32.DecodeDescriptorTypeSD
- AArch32.S1IASize
- AArch32.S1WalkLD
- AArch32.S1WalkSD
- AArch32.S2IASize
- AArch32.S2StartLevel
- AArch32.S2Walk
- RemapRegsHaveResetValues
- AArch32.GetS1TTWParams
- AArch32.GetS2TTWParams
- AArch32.GetVARange
- AArch32.S1DCacheEnabled
- AArch32.S1ICacheEnabled
- AArch32.S1TTWParamsEL10
- AArch32.S1TTWParamsEL2
- AArch32.S1TTWParamsEL30

## J1.2.4.1 AArch32.DefaultTEXDecode

```
// AArch32.DefaultTEXDecode() // ========================== // Apply short-descriptor format memory region attributes, without TEX remap MemoryAttributes AArch32.DefaultTEXDecode(bits(3) TEX_in, bit c_in, bit b_in, bit s) MemoryAttributes memattrs; bits(3) TEX = TEX_in; bit c = c_in; bit b = b_in; // Reserved values map to allocated values if (TEX == '001' && c:b == '01') || (TEX == '010' && c:b != '00') || TEX == '011' then bits(5) texcb; (-, texcb) = ConstrainUnpredictableBits(Unpredictable_RESTEXCB, 5); TEX = texcb<4:2>; c = texcb<1>; b = texcb<0>; // Distinction between Inner Shareable and Outer Shareable is not supported in this format // A memory region is either Non-shareable or Outer Shareable case TEX:c:b of when '00000' // Device-nGnRnE memattrs.memtype = MemType_Device; memattrs.device = DeviceType_nGnRnE; memattrs.shareability = Shareability_OSH; when '00001', '01000' // Device-nGnRE memattrs.memtype = MemType_Device; memattrs.device = DeviceType_nGnRE; memattrs.shareability = Shareability_OSH; when '00010' // Write-through Read allocate memattrs.memtype = MemType_Normal; memattrs.inner.attrs = MemAttr_WT; memattrs.inner.hints = MemHint_RA; memattrs.outer.attrs = MemAttr_WT; memattrs.outer.hints = MemHint_RA; memattrs.shareability = if s == '1' then Shareability_OSH else Shareability_NSH; when '00011' // Write-back Read allocate memattrs.memtype = MemType_Normal; memattrs.inner.attrs = MemAttr_WB; memattrs.inner.hints = MemHint_RA; memattrs.outer.attrs = MemAttr_WB; memattrs.outer.hints = MemHint_RA; memattrs.shareability = if s == '1' then Shareability_OSH else Shareability_NSH; when '00100' // Non-cacheable memattrs.memtype = MemType_Normal; memattrs.inner.attrs = MemAttr_NC; memattrs.outer.attrs = MemAttr_NC; memattrs.shareability = Shareability_OSH; when '00110' memattrs = MemoryAttributes IMPLEMENTATION_DEFINED; when '00111' // Write-back Read and Write allocate memattrs.memtype = MemType_Normal; memattrs.inner.attrs = MemAttr_WB; memattrs.inner.hints = MemHint_RWA; memattrs.outer.attrs = MemAttr_WB; memattrs.outer.hints = MemHint_RWA; memattrs.shareability = if s == '1' then Shareability_OSH else Shareability_NSH; when '1xxxx' // Cacheable, TEX<1:0> = Outer attrs, {c,b} = Inner attrs memattrs.memtype = MemType_Normal;
```

```
memattrs.inner = DecodeSDFAttr(c:b); memattrs.outer = DecodeSDFAttr(TEX<1:0>); if memattrs.inner.attrs == MemAttr_NC && memattrs.outer.attrs == MemAttr_NC then memattrs.shareability = Shareability_OSH; else memattrs.shareability = if s == '1' then Shareability_OSH else Shareability_NSH; otherwise // Reserved, handled above Unreachable(); // The Transient hint is not supported in this format memattrs.inner.transient = FALSE; memattrs.outer.transient = FALSE; memattrs.tags = MemTag_Untagged; if memattrs.inner.attrs == MemAttr_WB && memattrs.outer.attrs == MemAttr_WB then memattrs.xs = '0'; else memattrs.xs = '1'; return memattrs;
```

```
J1.2.4.2 AArch32.MAIRAttr // AArch32.MAIRAttr() // ================== // Retrieve the memory attribute encoding indexed in the given MAIR bits(8) AArch32.MAIRAttr(integer index, MAIRType mair) assert (index < 8); return Elem[mair, index, 8]; J1.2.4.3 AArch32.RemappedTEXDecode // AArch32.RemappedTEXDecode() // =========================== // Apply short-descriptor format memory region attributes, with TEX remap MemoryAttributes AArch32.RemappedTEXDecode(Regime regime, bits(3) TEX, bit c, bit b, bit s) MemoryAttributes memattrs; PRRR_Type prrr; NMRR_Type nmrr; region = UInt(TEX<0>:c:b); // TEX<2:1> are ignored in this mapping scheme if region == 6 then return MemoryAttributes IMPLEMENTATION_DEFINED; if regime == Regime_EL30 then prrr = PRRR_S; nmrr = NMRR_S; elsif HaveEL(EL3) && ELUsingAArch32(EL3) then prrr = PRRR_NS; nmrr = NMRR_NS; else prrr = PRRR; nmrr = NMRR; constant integer base = 2 * region; attrfield = Elem[prrr, region, 2]; if attrfield == '11' then // Reserved, maps to allocated value
```

```
(-, attrfield) = ConstrainUnpredictableBits(Unpredictable_RESPRRR, 2); case attrfield of when '00' // Device-nGnRnE memattrs.memtype = MemType_Device; memattrs.device = DeviceType_nGnRnE; memattrs.shareability = Shareability_OSH; when '01' // Device-nGnRE memattrs.memtype = MemType_Device; memattrs.device = DeviceType_nGnRE; memattrs.shareability = Shareability_OSH; when '10' NSn = if s == '0' then prrr.NS0 else prrr.NS1; NOSm = prrr<region+24> AND NSn; IRn = nmrr<base+1:base>; ORn = nmrr<base+17:base+16>; memattrs.memtype = MemType_Normal; memattrs.inner = DecodeSDFAttr(IRn); memattrs.outer = DecodeSDFAttr(ORn); if memattrs.inner.attrs == MemAttr_NC && memattrs.outer.attrs == MemAttr_NC then memattrs.shareability = Shareability_OSH; else constant bits(2) sh = NSn:NOSm; memattrs.shareability = DecodeShareability(sh); when '11' Unreachable(); // The Transient hint is not supported in this format memattrs.inner.transient = FALSE; memattrs.outer.transient = FALSE; memattrs.tags = MemTag_Untagged; if memattrs.inner.attrs == MemAttr_WB && memattrs.outer.attrs == MemAttr_WB then memattrs.xs = '0'; else memattrs.xs = '1'; return memattrs;
```

## J1.2.4.4 AArch32.CheckBreakpoint

```
// AArch32.CheckBreakpoint() // ========================= // Called before executing the instruction of length "size" bytes at "vaddress" in an AArch32 // translation regime, when either debug exceptions are enabled, or halting debug is enabled // and halting is allowed. FaultRecord AArch32.CheckBreakpoint(FaultRecord fault_in, bits(32) vaddress, AccessDescriptor accdesc, integer size) assert ELUsingAArch32(S1TranslationRegime()); assert size IN {2,4}; FaultRecord fault = fault_in; match = FALSE; mismatch = FALSE; BreakpointInfo brkptinfo; for i = 0 to NumBreakpointsImplemented() - 1 brkptinfo = AArch32.BreakpointMatch(i, vaddress, accdesc, size); match = match || brkptinfo.match; mismatch = mismatch || brkptinfo.mismatch; if match && HaltOnBreakpointOrWatchpoint() then reason = DebugHalt_Breakpoint;
```

```
Halt(reason); elsif (match || mismatch) then fault.statuscode = Fault_Debug; fault.debugmoe = DebugException_Breakpoint; fault.vaddress = ZeroExtend(vaddress, 64); return fault;
```

## J1.2.4.5 AArch32.CheckDebug

```
// AArch32.CheckDebug() // ==================== // Called on each access to check for a debug exception or entry to Debug state. FaultRecord AArch32.CheckDebug(bits(32) vaddress, AccessDescriptor accdesc, integer size) FaultRecord fault = NoFault(accdesc, ZeroExtend(vaddress, 64)); constant boolean d_side = IsWatchpointableAccess(accdesc); constant boolean i_side = (accdesc.acctype == AccessType_IFETCH); generate_exception = AArch32.GenerateDebugExceptions() && DBGDSCRext.MDBGen == '1'; halt = HaltOnBreakpointOrWatchpoint(); // Relative priority of Vector Catch and Breakpoint exceptions not defined in the architecture vector_catch_first = ConstrainUnpredictableBool(Unpredictable_BPVECTORCATCHPRI); if i_side && vector_catch_first && generate_exception then fault = AArch32.CheckVectorCatch(fault, vaddress, size); if fault.statuscode == Fault_None && (generate_exception || halt) then if d_side then fault = AArch32.CheckWatchpoint(fault, vaddress, accdesc, size); elsif i_side then fault = AArch32.CheckBreakpoint(fault, vaddress, accdesc, size); if fault.statuscode == Fault_None && i_side && !vector_catch_first && generate_exception then return AArch32.CheckVectorCatch(fault, vaddress, size); return fault;
```

## J1.2.4.6 AArch32.CheckVectorCatch

```
// AArch32.CheckVectorCatch() // ========================== // Called before executing the instruction of length "size" bytes at "vaddress" in an AArch32 // translation regime, when debug exceptions are enabled. FaultRecord AArch32.CheckVectorCatch(FaultRecord fault_in, bits(32) vaddress, integer size) assert ELUsingAArch32(S1TranslationRegime()); FaultRecord fault = fault_in; match = AArch32.VCRMatch(vaddress); if size == 4 && !match && AArch32.VCRMatch(vaddress + 2) then match = ConstrainUnpredictableBool(Unpredictable_VCMATCHHALF); if match then fault.statuscode = Fault_Debug; fault.debugmoe = DebugException_VectorCatch; return fault;
```

## J1.2.4.7 AArch32.CheckWatchpoint

```
// AArch32.CheckWatchpoint() // ========================= // Called before accessing the memory location of "size" bytes at "address", // when either debug exceptions are enabled for the access, or halting debug // is enabled and halting is allowed. FaultRecord AArch32.CheckWatchpoint(FaultRecord fault_in, bits(32) vaddress, AccessDescriptor accdesc, integer size) assert ELUsingAArch32(S1TranslationRegime()); FaultRecord fault = fault_in; boolean match = FALSE; if !IsWatchpointableAccess(accdesc) then return fault; for i = 0 to NumWatchpointsImplemented() - 1 constant WatchpointInfo watchptinfo = AArch32.WatchpointMatch(i, vaddress, size, accdesc); match = match || watchptinfo.value_match; if match && HaltOnBreakpointOrWatchpoint() then reason = DebugHalt_Watchpoint; EDWAR = ZeroExtend(vaddress, 64); Halt(reason); elsif match then fault.statuscode = Fault_Debug; fault.debugmoe = DebugException_Watchpoint; fault.vaddress = ZeroExtend(vaddress, 64); return fault;
```

```
J1.2.4.8 AArch32.IPAIsOutOfRange // AArch32.IPAIsOutOfRange() // ========================= // Check intermediate physical address bits not resolved by translation are ZERO boolean AArch32.IPAIsOutOfRange(S2TTWParams walkparams, bits(40) ipa) // Input Address size constant iasize = AArch32.S2IASize(walkparams.t0sz); return iasize < 40 && !IsZero(ipa<39:iasize>); J1.2.4.9 AArch32.S1HasAlignmentFaultDueToMemType // AArch32.S1HasAlignmentFaultDueToMemType() // ========================================= // Returns whether stage 1 output fails alignment requirement on data accesses to memory type boolean AArch32.S1HasAlignmentFaultDueToMemType(AccessDescriptor accdesc, boolean aligned, bit ntlsmd, MemoryAttributes memattrs) if memattrs.memtype != MemType_Device then return FALSE; elsif accdesc.a32lsmd && ntlsmd == '0' then return memattrs.device != DeviceType_GRE; elsif accdesc.acctype == AccessType_DCZero then return TRUE; elsif !aligned then return !(boolean IMPLEMENTATION_DEFINED "Device location supports unaligned access"); else return FALSE;
```

## J1.2.4.10 AArch32.S1LDHasPermissionsFault

```
// AArch32.S1LDHasPermissionsFault() // ================================= // Returns whether an access using stage 1 long-descriptor translation // violates permissions of target memory boolean AArch32.S1LDHasPermissionsFault(Regime regime, S1TTWParams walkparams, Permissions perms, MemType memtype, PASpace paspace, AccessDescriptor accdesc) bit r, w, x; bit pr, pw; bit ur, uw; bit xn; if HasUnprivileged(regime) then // Apply leaf permissions case perms.ap<2:1> of when '00' (pr,pw,ur,uw) = ('1','1','0','0'); // R/W at PL1 only when '01' (pr,pw,ur,uw) = ('1','1','1','1'); // R/W at any PL when '10' (pr,pw,ur,uw) = ('1','0','0','0'); // RO at PL1 only when '11' (pr,pw,ur,uw) = ('1','0','1','0'); // RO at any PL // Apply hierarchical permissions case perms.ap_table of when '00' (pr,pw,ur,uw) = ( pr, pw, ur, uw); // No effect when '01' (pr,pw,ur,uw) = ( pr, pw,'0','0'); // Privileged access when '10' (pr,pw,ur,uw) = ( pr,'0', ur,'0'); // Read-only when '11' (pr,pw,ur,uw) = ( pr,'0','0','0'); // Read-only, privileged access xn = perms.xn OR perms.xn_table; pxn = perms.pxn OR perms.pxn_table; ux = ur AND NOT(xn OR (uw AND walkparams.wxn)); px = pr AND NOT(xn OR pxn OR (pw AND walkparams.wxn) OR (uw AND walkparams.uwxn)); if IsFeatureImplemented(FEAT_PAN) && accdesc.pan then pan = PSTATE.PAN AND (ur OR uw); pr = pr AND NOT(pan); pw = pw AND NOT(pan); (r,w,x) = if accdesc.el == EL0 then (ur,uw,ux) else (pr,pw,px); // Prevent execution from Non-secure space by PE in Secure state if SIF is set if accdesc.ss == SS_Secure && paspace == PAS_NonSecure then x = x AND NOT(walkparams.sif); else // Apply leaf permissions case perms.ap<2> of when '0' (r,w) = ('1','1'); // No effect when '1' (r,w) = ('1','0'); // Read-only // Apply hierarchical permissions case perms.ap_table<1> of when '0' (r,w) = ( r, w ); // No effect when '1' (r,w) = ( r, '0'); // Read-only xn = perms.xn OR perms.xn_table; x = NOT(xn OR (w AND walkparams.wxn)); if accdesc.acctype == AccessType_IFETCH then constraint = ConstrainUnpredictable(Unpredictable_INSTRDEVICE); if constraint == Constraint_FAULT && memtype == MemType_Device then return TRUE; else return x == '0'; elsif accdesc.acctype IN {AccessType_IC, AccessType_DC} then return FALSE;
```

```
elsif accdesc.write then return w == '0'; else return r == '0';
```

## J1.2.4.11 AArch32.S1SDHasPermissionsFault

```
// AArch32.S1SDHasPermissionsFault() // ================================= // Returns whether an access using stage 1 short-descriptor translation // violates permissions of target memory boolean AArch32.S1SDHasPermissionsFault(Regime regime, Permissions perms_in, MemType memtype, PASpace paspace, AccessDescriptor accdesc) Permissions perms = perms_in; bit pr, pw; bit ur, uw; SCTLR_Type sctlr; if regime == Regime_EL30 then sctlr = SCTLR_S; elsif HaveEL(EL3) && ELUsingAArch32(EL3) then sctlr = SCTLR_NS; else sctlr = SCTLR; if sctlr.AFE == '0' then // Map Reserved encoding '100' if perms.ap == '100' then perms.ap = bits(3) IMPLEMENTATION_DEFINED "Reserved short descriptor AP encoding"; case perms.ap of when '000' (pr,pw,ur,uw) = ('0','0','0','0'); // No access when '001' (pr,pw,ur,uw) = ('1','1','0','0'); // R/W at PL1 only when '010' (pr,pw,ur,uw) = ('1','1','1','0'); // R/W at PL1, RO at PL0 when '011' (pr,pw,ur,uw) = ('1','1','1','1'); // R/W at any PL // '100' is reserved when '101' (pr,pw,ur,uw) = ('1','0','0','0'); // RO at PL1 only when '110' (pr,pw,ur,uw) = ('1','0','1','0'); // RO at any PL (deprecated) when '111' (pr,pw,ur,uw) = ('1','0','1','0'); // RO at any PL else // Simplified access permissions model case perms.ap<2:1> of when '00' (pr,pw,ur,uw) = ('1','1','0','0'); // R/W at PL1 only when '01' (pr,pw,ur,uw) = ('1','1','1','1'); // R/W at any PL when '10' (pr,pw,ur,uw) = ('1','0','0','0'); // RO at PL1 only when '11' (pr,pw,ur,uw) = ('1','0','1','0'); // RO at any PL ux = ur AND NOT(perms.xn OR (uw AND sctlr.WXN)); px = pr AND NOT(perms.xn OR perms.pxn OR (pw AND sctlr.WXN) OR (uw AND sctlr.UWXN)); if IsFeatureImplemented(FEAT_PAN) && accdesc.pan then pan = PSTATE.PAN AND (ur OR uw); pr = pr AND NOT(pan); pw = pw AND NOT(pan); (r,w,x) = if accdesc.el == EL0 then (ur,uw,ux) else (pr,pw,px); // Prevent execution from Non-secure space by PE in Secure state if SIF is set if accdesc.ss == SS_Secure && paspace == PAS_NonSecure then x = x AND NOT(if ELUsingAArch32(EL3) then SCR.SIF else SCR_EL3.SIF); if accdesc.acctype == AccessType_IFETCH then if (memtype == MemType_Device && ConstrainUnpredictable(Unpredictable_INSTRDEVICE) == Constraint_FAULT) then return TRUE; else return x == '0';
```

```
elsif accdesc.acctype IN {AccessType_IC, AccessType_DC} then return FALSE; elsif accdesc.write then return w == '0'; else return r == '0';
```

## J1.2.4.12 AArch32.S2HasAlignmentFaultDueToMemType

```
// AArch32.S2HasAlignmentFaultDueToMemType() // ========================================= // Returns whether stage 2 output fails alignment requirement on data accesses due to memory type boolean AArch32.S2HasAlignmentFaultDueToMemType(AccessDescriptor accdesc, boolean aligned, MemoryAttributes memattrs) if memattrs.memtype != MemType_Device then return FALSE; elsif accdesc.acctype == AccessType_DCZero then return TRUE; elsif !aligned then return !(boolean IMPLEMENTATION_DEFINED "Device location supports unaligned access"); else return FALSE;
```

## J1.2.4.13 AArch32.S2HasPermissionsFault

```
// AArch32.S2HasPermissionsFault() // =============================== // Returns whether stage 2 access violates permissions of target memory boolean AArch32.S2HasPermissionsFault(S2TTWParams walkparams, Permissions perms, MemType memtype, AccessDescriptor accdesc) r = perms.s2ap<0>; w = perms.s2ap<1>; bit x; bit ux; bit px; if IsFeatureImplemented(FEAT_XNX) then case perms.s2xn:perms.s2xnx of when '00' (px, ux) = ( r, r ); when '01' (px, ux) = ('0', r ); when '10' (px, ux) = ('0', '0'); when '11' (px, ux) = ( r, '0'); x = if accdesc.el == EL0 then ux else px; else x = r AND NOT(perms.s2xn); if accdesc.acctype == AccessType_TTW then return (walkparams.ptw == '1' && memtype == MemType_Device) || r == '0'; elsif accdesc.acctype == AccessType_IFETCH then constraint = ConstrainUnpredictable(Unpredictable_INSTRDEVICE); return (constraint == Constraint_FAULT && memtype == MemType_Device) || x == '0'; elsif accdesc.acctype IN {AccessType_IC, AccessType_DC} then return FALSE; elsif accdesc.write then return w == '0'; else
```

```
return r == '0';
```

## J1.2.4.14 AArch32.S2InconsistentSL

```
// AArch32.S2InconsistentSL() // ========================== // Detect inconsistent configuration of stage 2 T0SZ and SL fields boolean AArch32.S2InconsistentSL(S2TTWParams walkparams) startlevel = AArch32.S2StartLevel(walkparams.sl0); levels = FINAL_LEVEL -startlevel; granulebits = TGxGranuleBits(walkparams.tgx); stride = granulebits - 3; // Input address size must at least be large enough to be resolved from the start level sl_min_iasize = ( levels * stride // Bits resolved by table walk, except initial level + granulebits // Bits directly mapped to output address + 1); // At least 1 more bit to be decoded by initial level // Can accomodate 1 more stride in the level + concatenation of up to 2^4 tables sl_max_iasize = sl_min_iasize + (stride-1) + 4; // Configured Input Address size iasize = AArch32.S2IASize(walkparams.t0sz); return iasize < sl_min_iasize || iasize > sl_max_iasize;
```

## J1.2.4.15 AArch32.VAIsOutOfRange // AArch32.VAIsOutOfRange() // ======================== // Check virtual address bits not resolved by translation are identical // and of accepted value boolean AArch32.VAIsOutOfRange(Regime regime, S1TTWParams walkparams, bits(32) va) if regime == Regime\_EL2 then // Input Address size constant iasize = AArch32.S1IASize(walkparams.t0sz); return walkparams.t0sz != '000' &amp;&amp; !IsZero(va&lt;31:iasize&gt;); elsif walkparams.t1sz != '000' &amp;&amp; walkparams.t0sz != '000' then // Lower range Input Address size constant lo\_iasize = AArch32.S1IASize(walkparams.t0sz); // Upper range Input Address size constant up\_iasize = AArch32.S1IASize(walkparams.t1sz); return !IsZero(va&lt;31:lo\_iasize&gt;) &amp;&amp; !IsOnes(va&lt;31:up\_iasize&gt;); else return FALSE; J1.2.4.16 AArch32.GetS1TLBContext va)

```
// AArch32.GetS1TLBContext() // ========================= // Gather translation context for accesses with VA to match against TLB entries TLBContext AArch32.GetS1TLBContext(Regime regime, SecurityState ss, bits(32) TLBContext tlbcontext; case regime of when Regime_EL2 tlbcontext = AArch32.TLBContextEL2(va); when Regime_EL10 tlbcontext = AArch32.TLBContextEL10(ss, va); when Regime_EL30 tlbcontext = AArch32.TLBContextEL30(va);
```

```
tlbcontext.includes_s1 = TRUE; // The following may be amended for EL1&0 Regime if caching of stage 2 is successful tlbcontext.includes_s2 = FALSE; return tlbcontext;
```

## J1.2.4.17 AArch32.GetS2TLBContext

```
// AArch32.GetS2TLBContext() // ========================= // Gather translation context for accesses with IPA to match against TLB entries TLBContext AArch32.GetS2TLBContext(FullAddress ipa) assert ipa.paspace == PAS_NonSecure; TLBContext tlbcontext; tlbcontext.ss = SS_NonSecure; tlbcontext.regime = Regime_EL10; tlbcontext.ipaspace = ipa.paspace; tlbcontext.vmid = ZeroExtend(VTTBR.VMID, 16); tlbcontext.tg = TGx_4KB; tlbcontext.includes_s1 = FALSE; tlbcontext.includes_s2 = TRUE; tlbcontext.ia = ZeroExtend(ipa.address, 64); tlbcontext.cnp = if IsFeatureImplemented(FEAT_TTCNP) then VTTBR.CnP else '0'; return tlbcontext;
```

## J1.2.4.18 AArch32.TLBContextEL10

```
// AArch32.TLBContextEL10() // ======================== // Gather translation context for accesses under EL10 regime // (PL10 when EL3 is A64) to match against TLB entries TLBContext AArch32.TLBContextEL10(SecurityState ss, bits(32) va) TLBContext tlbcontext; TTBCR_Type ttbcr; TTBR0_Type ttbr0; TTBR1_Type ttbr1; CONTEXTIDR_Type contextidr; if HaveEL(EL3) && ELUsingAArch32(EL3) then ttbcr = TTBCR_NS; ttbr0 = TTBR0_NS; ttbr1 = TTBR1_NS; contextidr = CONTEXTIDR_NS; else ttbcr = TTBCR; ttbr0 = TTBR0; ttbr1 = TTBR1; contextidr = CONTEXTIDR; tlbcontext.ss = ss; tlbcontext.regime = Regime_EL10; if AArch32.EL2Enabled(ss) then tlbcontext.vmid = ZeroExtend(VTTBR.VMID, 16); if ttbcr.EAE == '1' then tlbcontext.asid = ZeroExtend(if ttbcr.A1 == '0' then ttbr0.ASID else ttbr1.ASID, 16); else
```

```
tlbcontext.asid = ZeroExtend(contextidr.ASID, 16); tlbcontext.tg = TGx_4KB; tlbcontext.ia = ZeroExtend(va, 64); if IsFeatureImplemented(FEAT_TTCNP) && ttbcr.EAE == '1' then if AArch32.GetVARange(va, ttbcr.T0SZ, ttbcr.T1SZ) == VARange_LOWER then tlbcontext.cnp = ttbr0.CnP; else tlbcontext.cnp = ttbr1.CnP; else tlbcontext.cnp = '0'; return tlbcontext;
```

```
J1.2.4.19 AArch32.TLBContextEL2 // AArch32.TLBContextEL2() // ======================= // Gather translation context for accesses under EL2 regime to match against TLB entries TLBContext AArch32.TLBContextEL2(bits(32) va) TLBContext tlbcontext; tlbcontext.ss = SS_NonSecure; tlbcontext.regime = Regime_EL2; tlbcontext.ia = ZeroExtend(va, 64); tlbcontext.tg = TGx_4KB; tlbcontext.cnp = if IsFeatureImplemented(FEAT_TTCNP) then HTTBR.CnP else '0'; return tlbcontext; J1.2.4.20 AArch32.TLBContextEL30
```

```
// AArch32.TLBContextEL30() // ======================== // Gather translation context for accesses under EL30 regime // (PL10 in Secure state and EL3 is A32) to match against TLB entries TLBContext AArch32.TLBContextEL30(bits(32) va) TLBContext tlbcontext; tlbcontext.ss = SS_Secure; tlbcontext.regime = Regime_EL30; if TTBCR_S.EAE == '1' then tlbcontext.asid = ZeroExtend(if TTBCR_S.A1 == '0' then TTBR0_S.ASID else TTBR1_S.ASID, 16); else tlbcontext.asid = ZeroExtend(CONTEXTIDR_S.ASID, 16); tlbcontext.tg = TGx_4KB; tlbcontext.ia = ZeroExtend(va, 64); if IsFeatureImplemented(FEAT_TTCNP) && TTBCR_S.EAE == '1' then if AArch32.GetVARange(va, TTBCR_S.T0SZ, TTBCR_S.T1SZ) == VARange_LOWER then tlbcontext.cnp = TTBR0_S.CnP; else tlbcontext.cnp = TTBR1_S.CnP; else tlbcontext.cnp = '0'; return tlbcontext;
```

## J1.2.4.21 AArch32.EL2Enabled

```
// AArch32.EL2Enabled() // ==================== // Returns whether EL2 is enabled for the given Security State boolean AArch32.EL2Enabled(SecurityState ss) if ss == SS_Secure then if !(HaveEL(EL2) && IsFeatureImplemented(FEAT_SEL2)) then return FALSE; elsif HaveEL(EL3) then return SCR_EL3.EEL2 == '1'; else return boolean IMPLEMENTATION_DEFINED "Secure-only implementation"; else return HaveEL(EL2);
```

## J1.2.4.22 AArch32.FullTranslate

```
// AArch32.FullTranslate() // ======================= // Perform address translation as specified by VMSA-A32 AddressDescriptor AArch32.FullTranslate(bits(32) va, AccessDescriptor accdesc, boolean aligned) // Prepare fault fields in case a fault is detected FaultRecord fault = NoFault(accdesc, ZeroExtend(va, 64)); constant Regime regime = TranslationRegime(accdesc.el); // First Stage Translation AddressDescriptor ipa; if regime == Regime_EL2 || TTBCR.EAE == '1' then (fault, ipa) = AArch32.S1TranslateLD(fault, regime, va, aligned, accdesc); else (fault, ipa, -) = AArch32.S1TranslateSD(fault, regime, va, aligned, accdesc); if fault.statuscode != Fault_None then return CreateFaultyAddressDescriptor(fault); if regime == Regime_EL10 && EL2Enabled() then ipa.vaddress = ZeroExtend(va, 64); AddressDescriptor pa; (fault, pa) = AArch32.S2Translate(fault, ipa, aligned, accdesc); if fault.statuscode != Fault_None then return CreateFaultyAddressDescriptor(fault); else return pa; else return ipa;
```

## J1.2.4.23 AArch32.OutputDomain

```
// AArch32.OutputDomain() // ====================== // Determine the domain the translated output address bits(2) AArch32.OutputDomain(Regime regime, bits(4) domain) bits(2) Dn; if regime == Regime_EL30 then Dn = Elem[DACR_S, UInt(domain), 2]; elsif HaveEL(EL3) && ELUsingAArch32(EL3) then Dn = Elem[DACR_NS, UInt(domain), 2];
```

```
else Dn = Elem[DACR, UInt(domain), 2]; if Dn == '10' then // Reserved value maps to an allocated value (-, Dn) = ConstrainUnpredictableBits(Unpredictable_RESDACR, 2); return Dn;
```

## J1.2.4.24 AArch32.S1DisabledOutput

```
// AArch32.S1DisabledOutput() // ========================== // Flat map the VA to IPA/PA, depending on the regime, assigning default memory attributes (FaultRecord, AddressDescriptor) AArch32.S1DisabledOutput(FaultRecord fault_in, Regime regime, bits(32) va, boolean aligned, AccessDescriptor accdesc) FaultRecord fault = fault_in; // No memory page is guarded when stage 1 address translation is disabled SetInGuardedPage(FALSE); MemoryAttributes memattrs; bit default_cacheable; if regime == Regime_EL10 && AArch32.EL2Enabled(accdesc.ss) then if ELStateUsingAArch32(EL2, accdesc.ss == SS_Secure) then default_cacheable = HCR.DC; else default_cacheable = HCR_EL2.DC; else default_cacheable = '0'; if default_cacheable == '1' then // Use default cacheable settings memattrs.memtype = MemType_Normal; memattrs.inner.attrs = MemAttr_WB; memattrs.inner.hints = MemHint_RWA; memattrs.outer.attrs = MemAttr_WB; memattrs.outer.hints = MemHint_RWA; memattrs.shareability = Shareability_NSH; if (EL2Enabled() && !ELStateUsingAArch32(EL2, accdesc.ss == SS_Secure) && IsFeatureImplemented(FEAT_MTE2) && HCR_EL2.DCT == '1') then memattrs.tags = MemTag_AllocationTagged; else memattrs.tags = MemTag_Untagged; memattrs.xs = '0'; elsif accdesc.acctype == AccessType_IFETCH then memattrs.memtype = MemType_Normal; memattrs.shareability = Shareability_OSH; memattrs.tags = MemTag_Untagged; if AArch32.S1ICacheEnabled(regime) then memattrs.inner.attrs = MemAttr_WT; memattrs.inner.hints = MemHint_RA; memattrs.outer.attrs = MemAttr_WT; memattrs.outer.hints = MemHint_RA; else memattrs.inner.attrs = MemAttr_NC; memattrs.outer.attrs = MemAttr_NC; memattrs.xs = '1'; else // Treat memory region as Device memattrs.memtype = MemType_Device; memattrs.device = DeviceType_nGnRnE; memattrs.shareability = Shareability_OSH;
```

```
memattrs.tags = MemTag_Untagged; memattrs.xs = '1'; bit ntlsmd; if IsFeatureImplemented(FEAT_LSMAOC) then case regime of when Regime_EL30 ntlsmd = SCTLR_S.nTLSMD; when Regime_EL2 ntlsmd = HSCTLR.nTLSMD; when Regime_EL10 if HaveEL(EL3) && ELUsingAArch32(EL3) then ntlsmd = SCTLR_NS.nTLSMD; else ntlsmd = SCTLR.nTLSMD; else ntlsmd = '1'; if AArch32.S1HasAlignmentFaultDueToMemType(accdesc, aligned, ntlsmd, memattrs) then fault.statuscode = Fault_Alignment; return (fault, AddressDescriptor UNKNOWN); elsif (accdesc.exclusive && !(regime == Regime_EL10 && EL2Enabled() && ((!ELUsingAArch32(EL2) && HCR_EL2.DC == '1') || (ELUsingAArch32(EL2) && HCR.DC == '1'))) && ConstrainUnpredictableBool(Unpredictable_Atomic_MMU_IMPDEF_FAULT)) then fault.statuscode = Fault_Exclusive; FullAddress oa; oa.address = ZeroExtend(va, 56); oa.paspace = if accdesc.ss == SS_Secure then PAS_Secure else PAS_NonSecure; ipa = CreateAddressDescriptor(ZeroExtend(va, 64), oa, memattrs, accdesc); return (fault, ipa);
```

```
J1.2.4.25 AArch32.S1Enabled // AArch32.S1Enabled() // =================== // Returns whether stage 1 translation is enabled for the active translation regime boolean AArch32.S1Enabled(Regime regime, SecurityState ss) if regime == Regime_EL2 then return HSCTLR.M == '1'; elsif regime == Regime_EL30 then return SCTLR_S.M == '1'; elsif !AArch32.EL2Enabled(ss) then return (if HaveEL(EL3) && ELUsingAArch32(EL3) then SCTLR_NS.M else SCTLR.M) == '1'; elsif ELStateUsingAArch32(EL2, ss == SS_Secure) then if HaveEL(EL3) && ELUsingAArch32(EL3) then return HCR.<TGE,DC> == '00' && SCTLR_NS.M == '1'; else return HCR.<TGE,DC> == '00' && SCTLR.M == '1'; else return EL2Enabled() && HCR_EL2.<TGE,DC> == '00' && SCTLR.M == '1'; J1.2.4.26 AArch32.S1TranslateLD // AArch32.S1TranslateLD() // ======================= // Perform a stage 1 translation using long-descriptor format mapping VA to IPA/PA // depending on the regime (FaultRecord, AddressDescriptor) AArch32.S1TranslateLD(FaultRecord fault_in, Regime regime, bits(32) va, boolean aligned,
```

AccessDescriptor accdesc)

```
FaultRecord fault = fault_in; if !AArch32.S1Enabled(regime, accdesc.ss) then return AArch32.S1DisabledOutput(fault, regime, va, aligned, accdesc); walkparams = AArch32.GetS1TTWParams(regime, va); if AArch32.VAIsOutOfRange(regime, walkparams, va) then fault.level = 1; fault.statuscode = Fault_Translation; return (fault, AddressDescriptor UNKNOWN); TTWState walkstate; (fault, walkstate) = AArch32.S1WalkLD(fault, regime, walkparams, accdesc, va); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN); SetInGuardedPage(FALSE); // AArch32-VMSA does not guard any pages if AArch32.S1HasAlignmentFaultDueToMemType(accdesc, aligned, walkparams.ntlsmd, walkstate.memattrs) then fault.statuscode = Fault_Alignment; elsif AArch32.S1LDHasPermissionsFault(regime, walkparams, walkstate.permissions, walkstate.memattrs.memtype, walkstate.baseaddress.paspace, accdesc) then fault.statuscode = Fault_Permission; if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN); MemoryAttributes memattrs; if ((accdesc.acctype == AccessType_IFETCH && (walkstate.memattrs.memtype == MemType_Device || !AArch32.S1ICacheEnabled(regime))) || (accdesc.acctype != AccessType_IFETCH && walkstate.memattrs.memtype == MemType_Normal && !AArch32.S1DCacheEnabled(regime))) then // Treat memory attributes as Normal Non-Cacheable memattrs = NormalNCMemAttr(); memattrs.xs = walkstate.memattrs.xs; else memattrs = walkstate.memattrs; // Shareability value of stage 1 translation subject to stage 2 is IMPLEMENTATION DEFINED // to be either effective value or descriptor value if (regime == Regime_EL10 && AArch32.EL2Enabled(accdesc.ss) && (if ELStateUsingAArch32(EL2, accdesc.ss==SS_Secure) then HCR.VM else HCR_EL2.VM) == '1' && !(boolean IMPLEMENTATION_DEFINED "Apply effective shareability at stage 1")) then memattrs.shareability = walkstate.memattrs.shareability; else memattrs.shareability = EffectiveShareability(memattrs); // Output Address oa = StageOA(ZeroExtend(va, 64), walkparams.d128, walkparams.tgx, walkstate); ipa = CreateAddressDescriptor(ZeroExtend(va, 64), oa, memattrs, accdesc); return (fault, ipa);
```

## J1.2.4.27 AArch32.S1TranslateSD

```
// AArch32.S1TranslateSD() // ======================= // Perform a stage 1 translation using short-descriptor format mapping VA to IPA/PA
```

```
// depending on the regime (FaultRecord, AddressDescriptor, SDFType) AArch32.S1TranslateSD(FaultRecord fault_in, Regime regime, bits(32) va, boolean aligned, AccessDescriptor accdesc) FaultRecord fault = fault_in; if !AArch32.S1Enabled(regime, accdesc.ss) then AddressDescriptor ipa; (fault, ipa) = AArch32.S1DisabledOutput(fault, regime, va, aligned, accdesc); return (fault, ipa, SDFType UNKNOWN); TTWState walkstate; (fault, walkstate) = AArch32.S1WalkSD(fault, regime, accdesc, va); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN, SDFType UNKNOWN); domain = AArch32.OutputDomain(regime, walkstate.domain); SetInGuardedPage(FALSE); // AArch32-VMSA does not guard any pages bit ntlsmd; if IsFeatureImplemented(FEAT_LSMAOC) then case regime of when Regime_EL30 ntlsmd = SCTLR_S.nTLSMD; when Regime_EL10 if HaveEL(EL3) && ELUsingAArch32(EL3) then ntlsmd = SCTLR_NS.nTLSMD; else ntlsmd = SCTLR.nTLSMD; else ntlsmd = '1'; if AArch32.S1HasAlignmentFaultDueToMemType(accdesc, aligned, ntlsmd, walkstate.memattrs) then fault.statuscode = Fault_Alignment; elsif (! accdesc.acctype IN {AccessType_IC, AccessType_DC} && domain == Domain_NoAccess) then fault.statuscode = Fault_Domain; elsif domain == Domain_Client then if AArch32.S1SDHasPermissionsFault(regime, walkstate.permissions, walkstate.memattrs.memtype, walkstate.baseaddress.paspace, accdesc) then fault.statuscode = Fault_Permission; if fault.statuscode != Fault_None then fault.domain = walkstate.domain; return (fault, AddressDescriptor UNKNOWN, walkstate.sdftype); MemoryAttributes memattrs; if ((accdesc.acctype == AccessType_IFETCH && (walkstate.memattrs.memtype == MemType_Device || !AArch32.S1ICacheEnabled(regime))) || (accdesc.acctype != AccessType_IFETCH && walkstate.memattrs.memtype == MemType_Normal && !AArch32.S1DCacheEnabled(regime))) then // Treat memory attributes as Normal Non-Cacheable memattrs = NormalNCMemAttr(); memattrs.xs = walkstate.memattrs.xs; else memattrs = walkstate.memattrs; // Shareability value of stage 1 translation subject to stage 2 is IMPLEMENTATION DEFINED // to be either effective value or descriptor value if (regime == Regime_EL10 && AArch32.EL2Enabled(accdesc.ss) && (if ELStateUsingAArch32(EL2, accdesc.ss==SS_Secure) then HCR.VM else HCR_EL2.VM) == '1' && !(boolean IMPLEMENTATION_DEFINED "Apply effective shareability at stage 1")) then memattrs.shareability = walkstate.memattrs.shareability;
```

```
else memattrs.shareability = EffectiveShareability(memattrs); // Output Address oa = AArch32.SDStageOA(walkstate.baseaddress, va, walkstate.sdftype); ipa = CreateAddressDescriptor(ZeroExtend(va, 64), oa, memattrs, accdesc); return (fault, ipa, walkstate.sdftype);
```

## J1.2.4.28 AArch32.S2Translate

```
// AArch32.S2Translate() // ===================== // Perform a stage 2 translation mapping an IPA to a PA (FaultRecord, AddressDescriptor) AArch32.S2Translate(FaultRecord fault_in, AddressDescriptor ipa, boolean aligned, AccessDescriptor accdesc) FaultRecord fault = fault_in; assert IsZero(ipa.paddress.address<55:40>); if !ELStateUsingAArch32(EL2, accdesc.ss == SS_Secure) then s1aarch64 = FALSE; return AArch64.S2Translate(fault, ipa, s1aarch64, aligned, accdesc); // Prepare fault fields in case a fault is detected fault.statuscode = Fault_None; fault.secondstage = TRUE; fault.s2fs1walk = accdesc.acctype == AccessType_TTW; fault.ipaddress = ipa.paddress; walkparams = AArch32.GetS2TTWParams(); if walkparams.vm == '0' then // Stage 2 is disabled return (fault, ipa); if AArch32.IPAIsOutOfRange(walkparams, ipa.paddress.address<39:0>) then fault.statuscode = Fault_Translation; fault.level = 1; return (fault, AddressDescriptor UNKNOWN); TTWState walkstate; (fault, walkstate) = AArch32.S2Walk(fault, walkparams, accdesc, ipa); if fault.statuscode != Fault_None then return (fault, AddressDescriptor UNKNOWN); if AArch32.S2HasAlignmentFaultDueToMemType(accdesc, aligned, walkstate.memattrs) then fault.statuscode = Fault_Alignment; elsif AArch32.S2HasPermissionsFault(walkparams, walkstate.permissions, walkstate.memattrs.memtype, accdesc) then fault.statuscode = Fault_Permission; MemoryAttributes s2_memattrs; if ((accdesc.acctype == AccessType_TTW && walkstate.memattrs.memtype == MemType_Device) || (accdesc.acctype == AccessType_IFETCH && (walkstate.memattrs.memtype == MemType_Device || HCR2.ID == '1')) || (accdesc.acctype != AccessType_IFETCH && walkstate.memattrs.memtype == MemType_Normal && HCR2.CD == '1')) then // Treat memory attributes as Normal Non-Cacheable s2_memattrs = NormalNCMemAttr(); s2_memattrs.xs = walkstate.memattrs.xs; else s2_memattrs = walkstate.memattrs;
```

```
s2aarch64 = FALSE; memattrs = S2CombineS1MemAttrs(ipa.memattrs, s2_memattrs, s2aarch64); ipa_64 = ZeroExtend(ipa.paddress.address<39:0>, 64); // Output Address oa = StageOA(ipa_64, walkparams.d128, walkparams.tgx, walkstate); pa = CreateAddressDescriptor(ipa.vaddress, oa, memattrs, accdesc); return (fault, pa); J1.2.4.29 AArch32.SDStageOA // AArch32.SDStageOA() // =================== // Given the final walk state of a short-descriptor translation walk, // map the untranslated input address bits to the base output address FullAddress AArch32.SDStageOA(FullAddress baseaddress, bits(32) va, SDFType sdftype) constant integer tsize = SDFSize(sdftype); // Output Address FullAddress oa; oa.address = baseaddress.address<55:tsize> : va<tsize-1:0>; oa.paspace = baseaddress.paspace; return oa; J1.2.4.30 AArch32.TranslateAddress // AArch32.TranslateAddress() // ========================== // Main entry point for translating an address AddressDescriptor AArch32.TranslateAddress(bits(32) va, AccessDescriptor accdesc, boolean aligned, integer size) constant Regime regime = TranslationRegime(PSTATE.EL); if !RegimeUsingAArch32(regime) then return AArch64.TranslateAddress(ZeroExtend(va, 64), accdesc, aligned, size); AddressDescriptor result = AArch32.FullTranslate(va, accdesc, aligned); if !IsFault(result) && accdesc.acctype != AccessType_IFETCH then // For an instruction fetch, CheckDebug will be called // after the instruction is read from memory result.fault = AArch32.CheckDebug(va, accdesc, size); // Update virtual address for abort functions result.vaddress = ZeroExtend(va, 64); return result; J1.2.4.31 SDFSize granule size
```

```
// SDFSize() // ========= // Returns the short-descriptor format translation AddressSize SDFSize(SDFType sdftype) case sdftype of when SDFType_SmallPage return 12; when SDFType_LargePage return 16; when SDFType_Section return 20;
```

```
when SDFType_Supersection return 24; otherwise Unreachable();
```

## J1.2.4.32 AArch32.DecodeDescriptorTypeLD // AArch32.DecodeDescriptorTypeLD() // ================================ // Determine whether the long-descriptor is a page, block or table DescriptorType AArch32.DecodeDescriptorTypeLD(bits(64) descriptor, integer level) if descriptor&lt;1:0&gt; == '11' &amp;&amp; level == FINAL\_LEVEL then return DescriptorType\_Leaf; elsif descriptor&lt;1:0&gt; == '11' then return DescriptorType\_Table; elsif descriptor&lt;1:0&gt; == '01' &amp;&amp; level != FINAL\_LEVEL then return DescriptorType\_Leaf; else return DescriptorType\_Invalid; J1.2.4.33 AArch32.DecodeDescriptorTypeSD // AArch32.DecodeDescriptorTypeSD() // ================================ // Determine the type of the short-descriptor SDFType AArch32.DecodeDescriptorTypeSD(bits(32) descriptor, integer level) if level == 1 &amp;&amp; descriptor&lt;1:0&gt; == '01' then return SDFType\_Table; elsif level == 1 &amp;&amp; descriptor&lt;18,1&gt; == '01' then return SDFType\_Section; elsif level == 1 &amp;&amp; descriptor&lt;18,1&gt; == '11' then return SDFType\_Supersection; elsif level == 2 &amp;&amp; descriptor&lt;1:0&gt; == '01' then return SDFType\_LargePage; elsif level == 2 &amp;&amp; descriptor&lt;1:0&gt; == '1x' then return SDFType\_SmallPage; else return SDFType\_Invalid; J1.2.4.34 AArch32.S1IASize // AArch32.S1IASize() // ================== // Retrieve the number of bits containing the input address for stage 1 translation AddressSize AArch32.S1IASize(bits(3) txsz) return 32 UInt(txsz); J1.2.4.35 AArch32.S1WalkLD accdesc,

```
// AArch32.S1WalkLD() // ================== // Traverse stage 1 translation tables in long format to obtain the final descriptor (FaultRecord, TTWState) AArch32.S1WalkLD(FaultRecord fault_in, Regime regime, S1TTWParams walkparams, AccessDescriptor bits(32) va) FaultRecord fault = fault_in; bits(3) txsz; bits(64) ttbr;
```

```
bit epd; VARange varange; if regime == Regime_EL2 then ttbr = HTTBR; txsz = walkparams.t0sz; varange = VARange_LOWER; else varange = AArch32.GetVARange(va, walkparams.t0sz, walkparams.t1sz); bits(64) ttbr0; bits(64) ttbr1; TTBCR_Type ttbcr; if regime == Regime_EL30 then ttbcr = TTBCR_S; ttbr0 = TTBR0_S; ttbr1 = TTBR1_S; elsif HaveEL(EL3) && ELUsingAArch32(EL3) then ttbcr = TTBCR_NS; ttbr0 = TTBR0_NS; ttbr1 = TTBR1_NS; else ttbcr = TTBCR; ttbr0 = TTBR0; ttbr1 = TTBR1; assert ttbcr.EAE == '1'; if varange == VARange_LOWER then txsz = walkparams.t0sz; ttbr = ttbr0; epd = ttbcr.EPD0; else txsz = walkparams.t1sz; ttbr = ttbr1; epd = ttbcr.EPD1; if regime != Regime_EL2 && epd == '1' then fault.level = 1; fault.statuscode = Fault_Translation; return (fault, TTWState UNKNOWN); // Input Address size iasize = AArch32.S1IASize(txsz); granulebits = TGxGranuleBits(walkparams.tgx); stride = granulebits - 3; startlevel = FINAL_LEVEL - (((iasize-1) granulebits) DIV stride); levels = FINAL_LEVEL -startlevel; if !IsZero(ttbr<47:40>) then fault.statuscode = Fault_AddressSize; fault.level = 0; return (fault, TTWState UNKNOWN); FullAddress baseaddress; constant baselsb = (iasize - (levels*stride + granulebits)) + 3; baseaddress.paspace = if accdesc.ss == SS_Secure then PAS_Secure else PAS_NonSecure; baseaddress.address = ZeroExtend(ttbr<39:baselsb>:Zeros(baselsb), 56); TTWState walkstate; walkstate.baseaddress = baseaddress; walkstate.level = startlevel; walkstate.istable = TRUE; // In regimes that support global and non-global translations, translation // table entries from lookup levels other than the final level of lookup // are treated as being non-global walkstate.nG = if HasUnprivileged(regime) then '1' else '0'; walkstate.memattrs = WalkMemAttrs(walkparams.sh, walkparams.irgn, walkparams.orgn); walkstate.permissions.ap_table = '00';
```

```
walkstate.permissions.xn_table = '0'; walkstate.permissions.pxn_table = '0'; bits(64) descriptor; AddressDescriptor walkaddress; walkaddress.vaddress = ZeroExtend(va, 64); if !AArch32.S1DCacheEnabled(regime) then walkaddress.memattrs = NormalNCMemAttr(); walkaddress.memattrs.xs = walkstate.memattrs.xs; else walkaddress.memattrs = walkstate.memattrs; // Shareability value of stage 1 translation subject to stage 2 is IMPLEMENTATION DEFINED // to be either effective value or descriptor value if (regime == Regime_EL10 && AArch32.EL2Enabled(accdesc.ss) && (if ELStateUsingAArch32(EL2, accdesc.ss==SS_Secure) then HCR.VM else HCR_EL2.VM) == '1' && !(boolean IMPLEMENTATION_DEFINED "Apply effective shareability at stage 1")) then walkaddress.memattrs.shareability = walkstate.memattrs.shareability; else walkaddress.memattrs.shareability = EffectiveShareability(walkaddress.memattrs); DescriptorType desctype; integer msb_residual = iasize - 1; repeat fault.level = walkstate.level; constant indexlsb = (FINAL_LEVEL -walkstate.level)*stride + granulebits; constant indexmsb = msb_residual; constant bits(40) index = ZeroExtend(va<indexmsb:indexlsb>:'000', 40); walkaddress.paddress.address = walkstate.baseaddress.address OR ZeroExtend(index, 56); walkaddress.paddress.paspace = walkstate.baseaddress.paspace; constant boolean toplevel = walkstate.level == startlevel; constant AccessDescriptor walkaccess = CreateAccDescS1TTW(toplevel, varange, accdesc); // If there are two stages of translation, then the first stage table walk addresses // are themselves subject to translation if regime == Regime_EL10 && AArch32.EL2Enabled(accdesc.ss) then s2aligned = TRUE; (s2fault, s2walkaddress) = AArch32.S2Translate(fault, walkaddress, s2aligned, walkaccess); // Check for a fault on the stage 2 walk if s2fault.statuscode != Fault_None then return (s2fault, TTWState UNKNOWN); (fault, descriptor) = FetchDescriptor(walkparams.ee, s2walkaddress, walkaccess, fault, 64); else (fault, descriptor) = FetchDescriptor(walkparams.ee, walkaddress, walkaccess, fault, 64); if fault.statuscode != Fault_None then return (fault, TTWState UNKNOWN); desctype = AArch32.DecodeDescriptorTypeLD(descriptor, walkstate.level); case desctype of when DescriptorType_Table if !IsZero(descriptor<47:40>) then fault.statuscode = Fault_AddressSize; return (fault, TTWState UNKNOWN); walkstate.baseaddress.address = ZeroExtend(descriptor<39:12>:Zeros(12), 56); if walkstate.baseaddress.paspace == PAS_Secure && descriptor<63> == '1' then walkstate.baseaddress.paspace = PAS_NonSecure;
```

```
if walkparams.hpd == '0' then walkstate.permissions.xn_table = (walkstate.permissions.xn_table OR descriptor<60>); walkstate.permissions.ap_table = (walkstate.permissions.ap_table OR descriptor<62:61>); walkstate.permissions.pxn_table = (walkstate.permissions.pxn_table OR descriptor<59>); walkstate.level = walkstate.level + 1; msb_residual = indexlsb - 1; when DescriptorType_Invalid fault.statuscode = Fault_Translation; return (fault, TTWState UNKNOWN); when DescriptorType_Leaf walkstate.istable = FALSE; until desctype == DescriptorType_Leaf; // Check the output address is inside the supported range if !IsZero(descriptor<47:40>) then fault.statuscode = Fault_AddressSize; return (fault, TTWState UNKNOWN); // Check the access flag if descriptor<10> == '0' then fault.statuscode = Fault_AccessFlag; return (fault, TTWState UNKNOWN); walkstate.permissions.xn = descriptor<54>; walkstate.permissions.pxn = descriptor<53>; walkstate.permissions.ap = descriptor<7:6>:'1'; walkstate.contiguous = descriptor<52>; if regime == Regime_EL2 then // All EL2 regime accesses are treated as Global walkstate.nG = '0'; elsif accdesc.ss == SS_Secure && walkstate.baseaddress.paspace == PAS_NonSecure then // When a PE is using the Long-descriptor translation table format, // and is in Secure state, a translation must be treated as non-global, // regardless of the value of the nG bit, // if NSTable is set to 1 at any level of the translation table walk. walkstate.nG = '1'; else walkstate.nG = descriptor<11>; constant indexlsb = (FINAL_LEVEL -walkstate.level)*stride + granulebits; walkstate.baseaddress.address = ZeroExtend(descriptor<39:indexlsb>:Zeros(indexlsb), 56); if walkstate.baseaddress.paspace == PAS_Secure && descriptor<5> == '1' then walkstate.baseaddress.paspace = PAS_NonSecure; memattr = descriptor<4:2>; sh = descriptor<9:8>; attr = AArch32.MAIRAttr(UInt(memattr), walkparams.mair); s1aarch64 = FALSE; walkstate.memattrs = S1DecodeMemAttrs(attr, sh, s1aarch64); return (fault, walkstate);
```

## J1.2.4.36 AArch32.S1WalkSD

```
// AArch32.S1WalkSD() // ================== // Traverse stage 1 translation tables in short format to obtain the final descriptor (FaultRecord, TTWState) AArch32.S1WalkSD(FaultRecord fault_in, Regime regime,
```

```
AccessDescriptor accdesc, bits(32) va) FaultRecord fault = fault_in; SCTLR_Type sctlr; TTBCR_Type ttbcr; TTBR0_Type ttbr0; TTBR1_Type ttbr1; // Determine correct translation control registers to use. if regime == Regime_EL30 then sctlr = SCTLR_S; ttbcr = TTBCR_S; ttbr0 = TTBR0_S; ttbr1 = TTBR1_S; elsif HaveEL(EL3) && ELUsingAArch32(EL3) then sctlr = SCTLR_NS; ttbcr = TTBCR_NS; ttbr0 = TTBR0_NS; ttbr1 = TTBR1_NS; else sctlr = SCTLR; ttbcr = TTBCR; ttbr0 = TTBR0; ttbr1 = TTBR1; assert ttbcr.EAE == '0'; ee = sctlr.EE; afe = sctlr.AFE; tre = sctlr.TRE; constant integer ttbcr_n = UInt(ttbcr.N); constant VARange varange = (if ttbcr_n == 0 || IsZero(va<31:(32-ttbcr_n)>) then VARange_LOWER else VARange_UPPER); constant integer n = if varange == VARange_LOWER then ttbcr_n else 0; bits(32) ttb; bits(1) pd; bits(2) irgn; bits(2) rgn; bits(1) s; bits(1) nos; if varange == VARange_LOWER then ttb = ttbr0.TTB0:Zeros(7); pd = ttbcr.PD0; irgn = ttbr0.IRGN; rgn = ttbr0.RGN; s = ttbr0.S; nos = ttbr0.NOS; else ttb = ttbr1.TTB1:Zeros(7); pd = ttbcr.PD1; irgn = ttbr1.IRGN; rgn = ttbr1.RGN; s = ttbr1.S; nos = ttbr1.NOS; // Check if Translation table walk disabled for translations with this Base register. if pd == '1' then fault.level = 1; fault.statuscode = Fault_Translation; return (fault, TTWState UNKNOWN); FullAddress baseaddress; baseaddress.paspace = if accdesc.ss == SS_Secure then PAS_Secure else PAS_NonSecure; baseaddress.address = ZeroExtend(ttb<31:14-n>:Zeros(14-n), 56); constant integer startlevel = 1; TTWState walkstate; walkstate.baseaddress = baseaddress; // In regimes that support global and non-global translations, translation
```

```
// table entries from lookup levels other than the final level of lookup // are treated as being non-global. Translations in Short-Descriptor Format // always support global & non-global translations. walkstate.nG = '1'; walkstate.memattrs = WalkMemAttrs(s:nos, irgn, rgn); walkstate.level = startlevel; walkstate.istable = TRUE; bits(4) domain; bits(32) descriptor; AddressDescriptor walkaddress; walkaddress.vaddress = ZeroExtend(va, 64); if !AArch32.S1DCacheEnabled(regime) then walkaddress.memattrs = NormalNCMemAttr(); walkaddress.memattrs.xs = walkstate.memattrs.xs; else walkaddress.memattrs = walkstate.memattrs; // Shareability value of stage 1 translation subject to stage 2 is IMPLEMENTATION DEFINED // to be either effective value or descriptor value if (regime == Regime_EL10 && AArch32.EL2Enabled(accdesc.ss) && (if ELStateUsingAArch32(EL2, accdesc.ss==SS_Secure) then HCR.VM else HCR_EL2.VM) == '1' && !(boolean IMPLEMENTATION_DEFINED "Apply effective shareability at stage 1")) then walkaddress.memattrs.shareability = walkstate.memattrs.shareability; else walkaddress.memattrs.shareability = EffectiveShareability(walkaddress.memattrs); bit nG; bit ns; bit pxn; bits(3) ap; bits(3) tex; bit c; bit b; bit xn; repeat fault.level = walkstate.level; bits(32) index; if walkstate.level == 1 then index = ZeroExtend(va<31-n:20>:'00', 32); else index = ZeroExtend(va<19:12>:'00', 32); walkaddress.paddress.address = walkstate.baseaddress.address OR ZeroExtend(index, 56); walkaddress.paddress.paspace = walkstate.baseaddress.paspace; constant boolean toplevel = walkstate.level == startlevel; constant AccessDescriptor walkaccess = CreateAccDescS1TTW(toplevel, varange, accdesc); if regime == Regime_EL10 && AArch32.EL2Enabled(accdesc.ss) then s2aligned = TRUE; (s2fault, s2walkaddress) = AArch32.S2Translate(fault, walkaddress, s2aligned, walkaccess); if s2fault.statuscode != Fault_None then return (s2fault, TTWState UNKNOWN); (fault, descriptor) = FetchDescriptor(ee, s2walkaddress, walkaccess, fault, 32); else (fault, descriptor) = FetchDescriptor(ee, walkaddress, walkaccess, fault, 32); if fault.statuscode != Fault_None then return (fault, TTWState UNKNOWN);
```

```
walkstate.sdftype = AArch32.DecodeDescriptorTypeSD(descriptor, walkstate.level); case walkstate.sdftype of when SDFType_Invalid fault.domain = domain; fault.statuscode = Fault_Translation; return (fault, TTWState UNKNOWN); when SDFType_Table domain = descriptor<8:5>; ns = descriptor<3>; pxn = descriptor<2>; walkstate.baseaddress.address = ZeroExtend(descriptor<31:10>:Zeros(10), 56); walkstate.level = 2; when SDFType_SmallPage nG = descriptor<11>; s = descriptor<10>; ap = descriptor<9,5:4>; tex = descriptor<8:6>; c = descriptor<3>; b = descriptor<2>; xn = descriptor<0>; walkstate.baseaddress.address = ZeroExtend(descriptor<31:12>:Zeros(12), 56); walkstate.istable = FALSE; when SDFType_LargePage xn = descriptor<15>; tex = descriptor<14:12>; nG = descriptor<11>; s = descriptor<10>; ap = descriptor<9,5:4>; c = descriptor<3>; b = descriptor<2>; walkstate.baseaddress.address = ZeroExtend(descriptor<31:16>:Zeros(16), 56); walkstate.istable = FALSE; when SDFType_Section ns = descriptor<19>; nG = descriptor<17>; s = descriptor<16>; ap = descriptor<15,11:10>; tex = descriptor<14:12>; domain = descriptor<8:5>; xn = descriptor<4>; c = descriptor<3>; b = descriptor<2>; pxn = descriptor<0>; walkstate.baseaddress.address = ZeroExtend(descriptor<31:20>:Zeros(20), 56); walkstate.istable = FALSE; when SDFType_Supersection ns = descriptor<19>; nG = descriptor<17>; s = descriptor<16>; ap = descriptor<15,11:10>; tex = descriptor<14:12>;
```

```
xn = descriptor<4>; c = descriptor<3>; b = descriptor<2>; pxn = descriptor<0>; domain = '0000'; walkstate.baseaddress.address = ZeroExtend(descriptor<8:5,23:20,31:24>:Zeros(24), 56); walkstate.istable = FALSE; until walkstate.sdftype != SDFType_Table; if afe == '1' && ap<0> == '0' then fault.domain = domain; fault.statuscode = Fault_AccessFlag; return (fault, TTWState UNKNOWN); // Decode the TEX, C, B and S bits to produce target memory attributes if tre == '1' then walkstate.memattrs = AArch32.RemappedTEXDecode(regime, tex, c, b, s); elsif RemapRegsHaveResetValues() then walkstate.memattrs = AArch32.DefaultTEXDecode(tex, c, b, s); else walkstate.memattrs = MemoryAttributes IMPLEMENTATION_DEFINED; walkstate.permissions.ap = ap; walkstate.permissions.xn = xn; walkstate.permissions.pxn = pxn; walkstate.domain = domain; walkstate.nG = nG; if accdesc.ss == SS_Secure && ns == '0' then walkstate.baseaddress.paspace = PAS_Secure; else walkstate.baseaddress.paspace = PAS_NonSecure; return (fault, walkstate);
```

```
J1.2.4.37 AArch32.S2IASize // AArch32.S2IASize() // ================== // Retrieve the number of bits containing the input address for stage 2 translation AddressSize AArch32.S2IASize(bits(4) t0sz) return 32 SInt(t0sz); J1.2.4.38 AArch32.S2StartLevel 2 translation
```

```
// AArch32.S2StartLevel() // ====================== // Determine the initial lookup level when performing a stage // table walk integer AArch32.S2StartLevel(bits(2) sl0) return 2 UInt(sl0);
```

## J1.2.4.39 AArch32.S2Walk

```
// AArch32.S2Walk() // ================ // Traverse stage 2 translation tables in long format to obtain the final descriptor (FaultRecord, TTWState) AArch32.S2Walk(FaultRecord fault_in, S2TTWParams walkparams, AccessDescriptor accdesc, AddressDescriptor ipa) FaultRecord fault = fault_in; if walkparams.sl0 == '1x' || AArch32.S2InconsistentSL(walkparams) then fault.statuscode = Fault_Translation; fault.level = 1; return (fault, TTWState UNKNOWN); // Input Address size iasize = AArch32.S2IASize(walkparams.t0sz); startlevel = AArch32.S2StartLevel(walkparams.sl0); levels = FINAL_LEVEL -startlevel; granulebits = TGxGranuleBits(walkparams.tgx); stride = granulebits - 3; if !IsZero(VTTBR<47:40>) then fault.statuscode = Fault_AddressSize; fault.level = 0; return (fault, TTWState UNKNOWN); FullAddress baseaddress; constant baselsb = (iasize - (levels*stride + granulebits)) + 3; baseaddress.paspace = PAS_NonSecure; baseaddress.address = ZeroExtend(VTTBR<39:baselsb>:Zeros(baselsb), 56); TTWState walkstate; walkstate.baseaddress = baseaddress; walkstate.level = startlevel; walkstate.istable = TRUE; walkstate.memattrs = WalkMemAttrs(walkparams.sh, walkparams.irgn, walkparams.orgn); bits(64) descriptor; constant AccessDescriptor walkaccess = CreateAccDescS2TTW(accdesc); AddressDescriptor walkaddress; walkaddress.vaddress = ipa.vaddress; if HCR2.CD == '1' then walkaddress.memattrs = NormalNCMemAttr(); walkaddress.memattrs.xs = walkstate.memattrs.xs; else walkaddress.memattrs = walkstate.memattrs; walkaddress.memattrs.shareability = EffectiveShareability(walkaddress.memattrs); integer msb_residual = iasize - 1; DescriptorType desctype; repeat fault.level = walkstate.level; constant indexlsb = (FINAL_LEVEL -walkstate.level)*stride + granulebits; constant indexmsb = msb_residual; constant bits(40) index = ZeroExtend(ipa.paddress.address<indexmsb:indexlsb>:'000', 40); walkaddress.paddress.address = walkstate.baseaddress.address OR ZeroExtend(index, 56); walkaddress.paddress.paspace = walkstate.baseaddress.paspace; (fault, descriptor) = FetchDescriptor(walkparams.ee, walkaddress, walkaccess, fault, 64);
```

```
if fault.statuscode != Fault_None then return (fault, TTWState UNKNOWN); desctype = AArch32.DecodeDescriptorTypeLD(descriptor, walkstate.level); case desctype of when DescriptorType_Table if !IsZero(descriptor<47:40>) then fault.statuscode = Fault_AddressSize; return (fault, TTWState UNKNOWN); walkstate.baseaddress.address = ZeroExtend(descriptor<39:12>:Zeros(12), 56); walkstate.level = walkstate.level + 1; msb_residual = indexlsb - 1; when DescriptorType_Invalid fault.statuscode = Fault_Translation; return (fault, TTWState UNKNOWN); when DescriptorType_Leaf walkstate.istable = FALSE; until desctype == DescriptorType_Leaf; // Check the output address is inside the supported range if !IsZero(descriptor<47:40>) then fault.statuscode = Fault_AddressSize; return (fault, TTWState UNKNOWN); // Check the access flag if descriptor<10> == '0' then fault.statuscode = Fault_AccessFlag; return (fault, TTWState UNKNOWN); // Unpack the descriptor into address and upper and lower block attributes constant indexlsb = (FINAL_LEVEL -walkstate.level)*stride + granulebits; walkstate.baseaddress.address = ZeroExtend(descriptor<39:indexlsb>:Zeros(indexlsb), 56); walkstate.permissions.s2ap = descriptor<7:6>; walkstate.permissions.s2xn = descriptor<54>; if IsFeatureImplemented(FEAT_XNX) then walkstate.permissions.s2xnx = descriptor<53>; else walkstate.permissions.s2xnx = '0'; memattr = descriptor<5:2>; sh = descriptor<9:8>; s2aarch64 = FALSE; walkstate.memattrs = S2DecodeMemAttrs(memattr, sh, s2aarch64); walkstate.contiguous = descriptor<52>; return (fault, walkstate);
```

## J1.2.4.40 RemapRegsHaveResetValues

```
// RemapRegsHaveResetValues() // ========================== boolean RemapRegsHaveResetValues();
```

## J1.2.4.41 AArch32.GetS1TTWParams

```
// AArch32.GetS1TTWParams() // ======================== // Returns stage 1 translation table walk parameters from respective controlling // System registers. S1TTWParams AArch32.GetS1TTWParams(Regime regime, bits(32) va) S1TTWParams walkparams; case regime of when Regime_EL2 walkparams = AArch32.S1TTWParamsEL2(); when Regime_EL10 walkparams = AArch32.S1TTWParamsEL10(va); when Regime_EL30 walkparams = AArch32.S1TTWParamsEL30(va); return walkparams;
```

```
J1.2.4.42 AArch32.GetS2TTWParams // AArch32.GetS2TTWParams() // ======================== // Gather walk parameters for stage 2 translation S2TTWParams AArch32.GetS2TTWParams() S2TTWParams walkparams; walkparams.tgx = TGx_4KB; walkparams.s = VTCR.S; walkparams.t0sz = VTCR.T0SZ; walkparams.sl0 = VTCR.SL0; walkparams.irgn = VTCR.IRGN0; walkparams.orgn = VTCR.ORGN0; walkparams.sh = VTCR.SH0; walkparams.ee = HSCTLR.EE; walkparams.ptw = HCR.PTW; walkparams.vm = HCR.VM OR HCR.DC; // VTCR.S must match VTCR.T0SZ[3] if walkparams.s != walkparams.t0sz<3> then (-, walkparams.t0sz) = ConstrainUnpredictableBits(Unpredictable_RESVTCRS, 4); return walkparams; J1.2.4.43 AArch32.GetVARange // AArch32.GetVARange() // ==================== // Select the translation base address for stage 1 long-descriptor walks VARange AArch32.GetVARange(bits(32) va, bits(3) t0sz, bits(3) t1sz) // Lower range Input Address size constant AddressSize lo_iasize = AArch32.S1IASize(t0sz); // Upper range Input Address size constant AddressSize up_iasize = AArch32.S1IASize(t1sz); if t1sz == '000' && t0sz == '000' then return VARange_LOWER; elsif t1sz == '000' then return if IsZero(va<31:lo_iasize>) then VARange_LOWER else VARange_UPPER; elsif t0sz == '000' then return if IsOnes(va<31:up_iasize>) then VARange_UPPER else VARange_LOWER; elsif IsZero(va<31:lo_iasize>) then return VARange_LOWER;
```

```
elsif IsOnes(va<31:up_iasize>) then return VARange_UPPER; else // Will be reported as a Translation Fault return VARange UNKNOWN;
```

## J1.2.4.44 AArch32.S1DCacheEnabled

```
// AArch32.S1DCacheEnabled() // ========================= // Determine cacheability of stage 1 data accesses boolean AArch32.S1DCacheEnabled(Regime regime) case regime of when Regime_EL30 return SCTLR_S.C == '1'; when Regime_EL2 return HSCTLR.C == '1'; when Regime_EL10 return (if HaveEL(EL3) && ELUsingAArch32(EL3) then SCTLR_NS.C else SCTLR.C) == '1';
```

## J1.2.4.45 AArch32.S1ICacheEnabled

```
// AArch32.S1ICacheEnabled() // ========================= // Determine cacheability of stage 1 instruction fetches boolean AArch32.S1ICacheEnabled(Regime regime) case regime of when Regime_EL30 return SCTLR_S.I == '1'; when Regime_EL2 return HSCTLR.I == '1'; when Regime_EL10 return (if HaveEL(EL3) && ELUsingAArch32(EL3) then SCTLR_NS.I else SCTLR.I) == '1';
```

## J1.2.4.46 AArch32.S1TTWParamsEL10

```
// AArch32.S1TTWParamsEL10() // ========================= // Gather stage 1 translation table walk parameters for EL1&0 regime // (with EL2 enabled or disabled). S1TTWParams AArch32.S1TTWParamsEL10(bits(32) va) bits(64) mair; bit sif; TTBCR_Type ttbcr; TTBCR2_Type ttbcr2; SCTLR_Type sctlr; if ELUsingAArch32(EL3) then ttbcr = TTBCR_NS; ttbcr2 = TTBCR2_NS; sctlr = SCTLR_NS; mair = MAIR1_NS:MAIR0_NS; sif = SCR.SIF; else ttbcr = TTBCR; ttbcr2 = TTBCR2; sctlr = SCTLR; mair = MAIR1:MAIR0; sif = if HaveEL(EL3) then SCR_EL3.SIF else '0'; assert ttbcr.EAE == '1'; S1TTWParams walkparams;
```

```
walkparams.t0sz = ttbcr.T0SZ; walkparams.t1sz = ttbcr.T1SZ; walkparams.ee = sctlr.EE; walkparams.wxn = sctlr.WXN; walkparams.uwxn = sctlr.UWXN; walkparams.ntlsmd = if IsFeatureImplemented(FEAT_LSMAOC) then sctlr.nTLSMD else '1'; walkparams.mair = mair; walkparams.sif = sif; varange = AArch32.GetVARange(va, walkparams.t0sz, walkparams.t1sz); if varange == VARange_LOWER then walkparams.sh = ttbcr.SH0; walkparams.irgn = ttbcr.IRGN0; walkparams.orgn = ttbcr.ORGN0; walkparams.hpd = (if IsFeatureImplemented(FEAT_AA32HPD) then ttbcr.T2E AND ttbcr2.HPD0 else '0'); else walkparams.sh = ttbcr.SH1; walkparams.irgn = ttbcr.IRGN1; walkparams.orgn = ttbcr.ORGN1; walkparams.hpd = (if IsFeatureImplemented(FEAT_AA32HPD) then ttbcr.T2E AND ttbcr2.HPD1 else '0'); return walkparams;
```

## J1.2.4.47 AArch32.S1TTWParamsEL2

```
// AArch32.S1TTWParamsEL2() // ======================== // Gather stage 1 translation table walk parameters for EL2 regime S1TTWParams AArch32.S1TTWParamsEL2() S1TTWParams walkparams; walkparams.tgx = TGx_4KB; walkparams.t0sz = HTCR.T0SZ; walkparams.irgn = HTCR.IRGN0; walkparams.orgn = HTCR.ORGN0; walkparams.sh = HTCR.SH0; walkparams.hpd = if IsFeatureImplemented(FEAT_AA32HPD) then HTCR.HPD else '0'; walkparams.ee = HSCTLR.EE; walkparams.wxn = HSCTLR.WXN; if IsFeatureImplemented(FEAT_LSMAOC) then walkparams.ntlsmd = HSCTLR.nTLSMD; else walkparams.ntlsmd = '1'; walkparams.mair = HMAIR1:HMAIR0; return walkparams;
```

## J1.2.4.48 AArch32.S1TTWParamsEL30

```
// AArch32.S1TTWParamsEL30() // ========================= // Gather stage 1 translation table walk parameters for EL3&0 regime S1TTWParams AArch32.S1TTWParamsEL30(bits(32) va) assert TTBCR_S.EAE == '1'; S1TTWParams walkparams; walkparams.t0sz = TTBCR_S.T0SZ;
```

```
walkparams.t1sz = TTBCR_S.T1SZ; walkparams.ee = SCTLR_S.EE; walkparams.wxn = SCTLR_S.WXN; walkparams.uwxn = SCTLR_S.UWXN; walkparams.ntlsmd = if IsFeatureImplemented(FEAT_LSMAOC) then SCTLR_S.nTLSMD else '1'; walkparams.mair = MAIR1_S:MAIR0_S; walkparams.sif = SCR.SIF; varange = AArch32.GetVARange(va, walkparams.t0sz, walkparams.t1sz); if varange == VARange_LOWER then walkparams.sh = TTBCR_S.SH0; walkparams.irgn = TTBCR_S.IRGN0; walkparams.orgn = TTBCR_S.ORGN0; walkparams.hpd = (if IsFeatureImplemented(FEAT_AA32HPD) then TTBCR_S.T2E AND TTBCR2_S.HPD0 else '0'); else walkparams.sh = TTBCR_S.SH1; walkparams.irgn = TTBCR_S.IRGN1; walkparams.orgn = TTBCR_S.ORGN1; walkparams.hpd = (if IsFeatureImplemented(FEAT_AA32HPD) then TTBCR_S.T2E AND TTBCR2_S.HPD1 else '0'); return walkparams;
```