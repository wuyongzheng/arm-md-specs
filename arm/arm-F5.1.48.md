## F5.1.48 DSB

Data Synchronization Barrier is a memory barrier that ensures the completion of memory accesses, see Data Synchronization Barrier (DSB).

An AArch32 DSB instruction does not require the completion of any AArch64 TLB maintenance instructions, regardless of the nXS qualifier, appearing in program order before the AArch32 DSB.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

DSB{&lt;c&gt;}{&lt;q&gt;} {&lt;option&gt;}

## Decode for this encoding

// No additional decoding required

T1

<!-- image -->

## Encoding

DSB{&lt;c&gt;}{&lt;q&gt;} {&lt;option&gt;}

## Decode for this encoding

// No additional decoding required

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

Listing F5-34

Listing F5-35

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. Must be AL or omitted.

For the 'T1' variant: see Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;option&gt;

Specifies an optional limitation on the barrier operation. Values are:

- SY Full system is the required shareability domain, reads and writes are the required access types, both before and after the barrier instruction. Can be omitted. This option is referred to as the full system barrier. Encoded as option = 0b1111 .
- ST Full system is the required shareability domain, writes are the required access type, both before and after the barrier instruction. SYST is a synonym for ST . Encoded as option = 0b1110 .
- LD Full system is the required shareability domain, reads are the required access type before the barrier instruction, and reads and writes are the required access types after the barrier instruction. Encoded as option = 0b1101 .
- ISH Inner Shareable is the required shareability domain, reads and writes are the required access types, both before and after the barrier instruction. Encoded as option = 0b1011 .
- ISHST Inner Shareable is the required shareability domain, writes are the required access type, both before and after the barrier instruction. Encoded as option = 0b1010 .
- ISHLD Inner Shareable is the required shareability domain, reads are the required access type before the barrier instruction, and reads and writes are the required access types after the barrier instruction. Encoded as option = 0b1001 .
- NSH Non-shareable is the required shareability domain, reads and writes are the required access, both before and after the barrier instruction. Encoded as option = 0b0111 .
- NSHST Non-shareable is the required shareability domain, writes are the required access type both before and after the barrier instruction. Encoded as option = 0b0110 .
- NSHLD Non-shareable is the required shareability domain, reads are the required access type before the barrier instruction, and reads and writes are the required access types after the barrier instruction. Encoded as option = 0b0101 .
- OSH Outer Shareable is the required shareability domain, reads and writes are the required access types, both before and after the barrier instruction. Encoded as option = 0b0011 .
- OSHST Outer Shareable is the required shareability domain, writes are the required access type, both before and after the barrier instruction. Encoded as option = 0b0010 .
- OSHLD Outer Shareable is the required shareability domain, reads are the required access type before the barrier instruction, and reads and writes are the required access types after the barrier instruction. Encoded as option = 0b0001 .

For more information on whether an access is before or after a barrier instruction, see Data Synchronization Barrier (DSB). All other encodings of option are reserved, other than the values 0b0000 and 0b0100 . All unsupported and reserved options must execute as a full system DSB operation, but software must not rely on this behavior.

Note

The value 0b0000 is used to encode SSBB and the value 0b0100 is used to encode PSSBB.

The instruction supports the following alternative &lt;option&gt; values, but Arm recommends that software does not use these alternative values:

- SH as an alias for ISH .
- SHST as an alias for ISHST .
- UN as an alias for NSH .
- UNST as an alias for NSHST .

## Operation

if ConditionPassed() then

Listing F5-36

end

```
EncodingSpecificOperations(); boolean nXS; if IsFeatureImplemented(FEAT_XS) then nXS = (PSTATE.EL IN {EL0, EL1} && !ELUsingAArch32(EL2) && IsHCRXEL2Enabled() && HCRX_EL2.FnXS == '1'); else nXS = FALSE; end MBReqDomain domain; MBReqTypes types; case option of when '0001' domain = MBReqDomain_OuterShareable; types = MBReqTypes_Reads; when '0010' domain = MBReqDomain_OuterShareable; types = MBReqTypes_Writes; when '0011' domain = MBReqDomain_OuterShareable; types = MBReqTypes_All; when '0101' domain = MBReqDomain_Nonshareable; types = MBReqTypes_Reads; when '0110' domain = MBReqDomain_Nonshareable; types = MBReqTypes_Writes; when '0111' domain = MBReqDomain_Nonshareable; types = MBReqTypes_All; when '1001' domain = MBReqDomain_InnerShareable; types = MBReqTypes_Reads; when '1010' domain = MBReqDomain_InnerShareable; types = MBReqTypes_Writes; when '1011' domain = MBReqDomain_InnerShareable; types = MBReqTypes_All; when '1101' domain = MBReqDomain_FullSystem; types = MBReqTypes_Reads; when '1110' domain = MBReqDomain_FullSystem; types = MBReqTypes_Writes; otherwise assert option != '0x00'; domain = MBReqDomain_FullSystem; types = MBReqTypes_All; end if PSTATE.EL IN {EL0, EL1} && EL2Enabled() then if HCR.BSU == '11' then domain = MBReqDomain_FullSystem; end if HCR.BSU == '10' && domain != MBReqDomain_FullSystem then domain = MBReqDomain_OuterShareable; end if HCR.BSU == '01' && domain == MBReqDomain_Nonshareable then domain = MBReqDomain_InnerShareable; end end DataSynchronizationBarrier(domain, types, nXS);
```