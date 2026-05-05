## C6.2.150 DMB

## Data memory barrier

This instruction is a memory barrier that ensures the ordering of observations of memory accesses, see Data Memory Barrier.

<!-- image -->

## Encoding

```
DMB (<option>|#<imm>)
```

## Decode for this encoding

```
MBReqDomain domain; MBReqTypes types; case CRm<3:2> of when '00' domain = MBReqDomain_OuterShareable; when '01' domain = MBReqDomain_Nonshareable; when '10' domain = MBReqDomain_InnerShareable; when '11' domain = MBReqDomain_FullSystem; case CRm<1:0> of when '00' types = MBReqTypes_All; domain when '01' types = MBReqTypes_Reads; when '10' types = MBReqTypes_Writes; when '11' types = MBReqTypes_All;
```

## Assembler Symbols

## &lt;option&gt;

Specifies the limitation on the barrier operation. Values are:

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

```
= MBReqDomain_FullSystem;
```

OSHLD Outer Shareable is the required shareability domain, reads are the required access type before the barrier instruction, and reads and writes are the required access types after the barrier instruction. Encoded as CRm = 0b0001 .

All other encodings of 'CRm' that are not listed are reserved and can be encoded using the #&lt;imm&gt; syntax. All unsupported and reserved options must execute as a full system barrier operation, but software must not rely on this behavior. For more information on whether an access is before or after a barrier instruction, see Data Memory Barrier (DMB) or see Data Synchronization Barrier (DSB).

| CRm   | <option>   |
|-------|------------|
| 0001  | OSHLD      |
| 0010  | OSHST      |
| 0011  | OSH        |
| 0101  | NSHLD      |
| 0110  | NSHST      |
| 0111  | NSH        |
| xx00  | RESERVED   |
| 1001  | ISHLD      |
| 1010  | ISHST      |
| 1011  | ISH        |
| 1101  | LD         |
| 1110  | ST         |
| 1111  | SY         |

## &lt;imm&gt;

Is a 4-bit unsigned immediate, in the range 0 to 15, encoded in the 'CRm' field.

## Operation

DataMemoryBarrier(domain, types);
