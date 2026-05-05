## C6.2.152 DSB

Data synchronization barrier

This instruction is a memory barrier that ensures the completion of memory accesses, see Data Synchronization Barrier.

This instruction is used by the aliases PSSBB and SSBB.

It has encodings from 2 classes: Memory barrier and Memory nXS barrier

## Memory barrier

<!-- image -->

## Encoding

```
DSB (<option>|#<imm>)
```

## Decode for this encoding

```
boolean nXS = FALSE; DSBAlias alias; case CRm of when '0000' alias = DSBAlias_SSBB; when '0100' alias = DSBAlias_PSSBB; otherwise alias = DSBAlias_DSB; MBReqDomain domain; case CRm<3:2> of when '00' domain = MBReqDomain_OuterShareable; when '01' domain = MBReqDomain_Nonshareable; when '10' domain = MBReqDomain_InnerShareable; when '11' domain = MBReqDomain_FullSystem; MBReqTypes types; case CRm<1:0> of when '00' types = MBReqTypes_All; domain = MBReqDomain_FullSystem; when '01' types = MBReqTypes_Reads; when '10' types = MBReqTypes_Writes; when '11' types = MBReqTypes_All;
```

## Memory nXS barrier

(FEAT\_XS)

<!-- image -->

## Encoding

DSB &lt;option&gt;nXS

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_XS) then EndOfDecode(Decode_UNDEF);
```

```
constant MBReqTypes types = MBReqTypes_All; boolean nXS = TRUE; constant DSBAlias alias = DSBAlias_DSB; MBReqDomain domain; case imm2 of when '00' domain = MBReqDomain_OuterShareable; when '01' domain = MBReqDomain_Nonshareable; when '10' domain = MBReqDomain_InnerShareable; when '11' domain = MBReqDomain_FullSystem;
```

## Assembler Symbols

## &lt;option&gt;

For the 'Memory barrier' variant: specifies the limitation on the barrier operation. Values are:

- SY Full system is the required shareability domain, reads and writes are the required access types, both before and after the barrier instruction. This option is referred to as the full system barrier. Encoded as CRm = 0b1111 .
- ST Full system is the required shareability domain, writes are the required access type, both before and after the barrier instruction. Encoded as CRm = 0b1110 .
- LD Full system is the required shareability domain, reads are the required access type before the barrier instruction, and reads and writes are the required access types after the barrier instruction. Encoded as CRm = 0b1101 .
- ISH Inner Shareable is the required shareability domain, reads and writes are the required access types, both before and after the barrier instruction. Encoded as CRm = 0b1011 .
- ISHST Inner Shareable is the required shareability domain, writes are the required access type, both before and after the barrier instruction. Encoded as CRm = 0b1010 .
- ISHLD Inner Shareable is the required shareability domain, reads are the required access type before the barrier instruction, and reads and writes are the required access types after the barrier instruction. Encoded as CRm = 0b1001 .
- NSH Non-shareable is the required shareability domain, reads and writes are the required access, both before and after the barrier instruction. Encoded as CRm = 0b0111 .
- NSHST Non-shareable is the required shareability domain, writes are the required access type, both before and after the barrier instruction. Encoded as CRm = 0b0110 .
- NSHLD Non-shareable is the required shareability domain, reads are the required access type before the barrier instruction, and reads and writes are the required access types after the barrier instruction. Encoded as CRm = 0b0101 .
- OSH Outer Shareable is the required shareability domain, reads and writes are the required access types, both before and after the barrier instruction. Encoded as CRm = 0b0011 .
- OSHST Outer Shareable is the required shareability domain, writes are the required access type, both before and after the barrier instruction. Encoded as CRm = 0b0010 .
- OSHLD Outer Shareable is the required shareability domain, reads are the required access type before the barrier instruction, and reads and writes are the required access types after the barrier instruction. Encoded as CRm = 0b0001 .

All other encodings of 'CRm' that are not listed, other than the values 0b0000 and 0b0100 , are reserved and can be encoded using the #&lt;imm&gt; syntax. All unsupported and reserved options must execute as a full system barrier operation, but software must not rely on this behavior. For more information on whether an access is before or after a barrier instruction, see Data Memory Barrier (DMB) or see Data Synchronization Barrier (DSB).

Note

The value 0b0000 is used to encode SSBB and the value 0b0100 is used to encode PSSBB .

|   CRm | <option>   |
|-------|------------|
|  0001 | OSHLD      |

## &lt;imm&gt;

Is a 4-bit unsigned immediate, in the range 0 to 15, encoded in the 'CRm' field.

## Alias Conditions

## Operation

| CRm   | <option>   |
|-------|------------|
| 0010  | OSHST      |
| 0011  | OSH        |
| 0101  | NSHLD      |
| 0110  | NSHST      |
| 0111  | NSH        |
| 1001  | ISHLD      |
| 1010  | ISHST      |
| 1011  | ISH        |
| 1x00  | RESERVED   |
| 1101  | LD         |
| 1110  | ST         |
| 1111  | SY         |

For the 'Memory nXS barrier' variant: specifies the limitation on the barrier operation. Values are:

- SY Full system is the required shareability domain, reads and writes are the required access types, both before and after the barrier instruction. This option is referred to as the full system barrier. Encoded as imm2 = 0b11 .
- ISH Inner Shareable is the required shareability domain, reads and writes are the required access types, both before and after the barrier instruction. Encoded as imm2 = 0b10 .
- NSH Non-shareable is the required shareability domain, reads and writes are the required access, both before and after the barrier instruction. Encoded as imm2 = 0b01 .
- OSH Outer Shareable is the required shareability domain, reads and writes are the required access types, both before and after the barrier instruction. Encoded as imm2 = 0b00 .

|   imm2 | <option>   |
|--------|------------|
|     00 | OSH        |
|     01 | NSH        |
|     10 | ISH        |
|     11 | SY         |

| Alias   | Is preferred when   |
|---------|---------------------|
| PSSBB   | CRm == '0100'       |
| SSBB    | CRm == '0000'       |

```
case alias of when DSBAlias_SSBB SpeculativeStoreBypassBarrierToVA(); when DSBAlias_PSSBB SpeculativeStoreBypassBarrierToPA(); when DSBAlias_DSB if !nXS && IsFeatureImplemented(FEAT_XS) then nXS = PSTATE.EL IN {EL0, EL1} && IsHCRXEL2Enabled() && HCRX_EL2.FnXS == '1'; DataSynchronizationBarrier(domain, types, nXS); otherwise Unreachable();
```
