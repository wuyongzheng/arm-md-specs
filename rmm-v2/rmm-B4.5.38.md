## B4.5.38 RMI\_PSCI\_COMPLETE command

Completes a pending PSCI command which was called with an MPIDR argument, by providing the corresponding REC.

## See also:

- A4.3.7 REC exit due to PSCI
- B6.3.1 PSCI\_AFFINITY\_INFO command
- B6.3.3 PSCI\_CPU\_ON command
- D1.4 PSCI flows

## B4.5.38.1 Interface

## B4.5.38.1.1 Input values

| Name            | Register   | Bits   | Type           | Description                |
|-----------------|------------|--------|----------------|----------------------------|
| fid             | X0         | 63:0   | UInt64         | FID, value 0xC4000164      |
| calling_rec_ptr | X1         | 63:0   | Address        | PA of the calling REC      |
| target_rec_ptr  | X2         | 63:0   | Address        | PA of the target REC       |
| status          | X3         | 63:0   | PsciReturnCode | Status of the PSCI request |

## B4.5.38.1.2 Context

The RMI\_PSCI\_COMPLETE command operates on the following context.

| Name        | Type   | Value                  | Before   | Description   |
|-------------|--------|------------------------|----------|---------------|
| calling_rec | RmmRec | RecAt(calling_rec_ptr) | false    | Calling REC   |
| target_rec  | RmmRec | RecAt(target_rec_ptr)  | false    | Target REC    |


## B4.5.38.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.38.2 Failure conditions

Condition

ID

| alias         | pre:       | calling_rec_ptr == target_rec_ptr                              |
|---------------|------------|----------------------------------------------------------------|
| calling_align | pre:       | !AddrIsRmiGranuleAligned(calling_rec_ptr)                      |
| calling_bound | pre: post: | !PaIsTracked(calling_rec_ptr) result.status == RMI_ERROR_INPUT |

## ID

## Condition

```
calling_state pre: GranuleAt(calling_rec_ptr).state != GRAN_REC post: result.status == RMI_ERROR_INPUT target_align pre: !AddrIsRmiGranuleAligned(target_rec_ptr) post: result.status == RMI_ERROR_INPUT target_bound pre: !PaIsTracked(target_rec_ptr) post: result.status == RMI_ERROR_INPUT target_state pre: GranuleAt(target_rec_ptr).state != GRAN_REC post: result.status == RMI_ERROR_INPUT pending pre: calling_rec.pending != REC_PENDING_PSCI post: result.status == RMI_ERROR_INPUT owner pre: target_rec.owner != calling_rec.owner post: result.status == RMI_ERROR_INPUT target pre: target_rec.mpidr != calling_rec.gprs[[1]] post: result.status == RMI_ERROR_INPUT status pre: !PsciReturnCodePermitted( calling_rec, target_rec, status) post: result.status == RMI_ERROR_INPUT
```

```
pending post: calling_rec.pending == REC_PENDING_NONE on_already pre: (status == PSCI_SUCCESS && calling_rec.gprs[[0]] == && target_rec.flags.runnable == RUNNABLE) post: (calling_rec.gprs[[0]] == PsciReturnCodeEncode(PSCI_ALREADY_ON))
```

B4.5.38.2.1 Failure condition ordering The RMI\_PSCI\_COMPLETE command does not have any failure condition orderings. B4.5.38.3 Success conditions ID Condition FID\_PSCI\_CPU\_ON

ID

## Condition

```
on_success pre: (status == PSCI_SUCCESS && calling_rec.gprs[[0]] == FID_PSCI_CPU_ON && target_rec.flags.runnable != RUNNABLE) post: (target_rec.gprs[[0]] == calling_rec.gprs[[3]] && target_rec.gprs[[1]] == Zeros{64}() && target_rec.gprs[[2]] == Zeros{64}() && target_rec.gprs[[3]] == Zeros{64}() && target_rec.gprs[[4]] == Zeros{64}() && target_rec.gprs[[5]] == Zeros{64}() && target_rec.gprs[[6]] == Zeros{64}() && target_rec.gprs[[7]] == Zeros{64}() && target_rec.gprs[[8]] == Zeros{64}() && target_rec.gprs[[9]] == Zeros{64}() && target_rec.gprs[[10]] == Zeros{64}() && target_rec.gprs[[11]] == Zeros{64}() && target_rec.gprs[[12]] == Zeros{64}() && target_rec.gprs[[13]] == Zeros{64}() && target_rec.gprs[[14]] == Zeros{64}() && target_rec.gprs[[15]] == Zeros{64}() && target_rec.gprs[[16]] == Zeros{64}() && target_rec.gprs[[17]] == Zeros{64}() && target_rec.gprs[[18]] == Zeros{64}() && target_rec.gprs[[19]] == Zeros{64}() && target_rec.gprs[[20]] == Zeros{64}() && target_rec.gprs[[21]] == Zeros{64}() && target_rec.gprs[[22]] == Zeros{64}() && target_rec.gprs[[23]] == Zeros{64}() && target_rec.gprs[[24]] == Zeros{64}() && target_rec.gprs[[25]] == Zeros{64}() && target_rec.gprs[[26]] == Zeros{64}() && target_rec.gprs[[27]] == Zeros{64}() && target_rec.gprs[[28]] == Zeros{64}() && target_rec.gprs[[29]] == Zeros{64}() && target_rec.gprs[[30]] == Zeros{64}() && target_rec.gprs[[31]] == Zeros{64}() && target_rec.pc == calling_rec.gprs[[2]] && target_rec.flags.runnable == RUNNABLE && calling_rec.gprs[[0]] == PsciReturnCodeEncode(PSCI_SUCCESS)) affinity_on pre: (status == PSCI_SUCCESS && calling_rec.gprs[[0]] == FID_PSCI_AFFINITY_INFO && target_rec.flags.runnable == RUNNABLE) post: (calling_rec.gprs[[0]] == PsciReturnCodeEncode(PSCI_SUCCESS)) affinity_off pre: (status == PSCI_SUCCESS && calling_rec.gprs[[0]] == FID_PSCI_AFFINITY_INFO && target_rec.flags.runnable != RUNNABLE) post: (calling_rec.gprs[[0]] == PsciReturnCodeEncode(PSCI_OFF)) status pre: status != PSCI_SUCCESS post: (calling_rec.gprs[[0]] == PsciReturnCodeEncode(status)) args post: (calling_rec.gprs[[1]] == Zeros{64}() && calling_rec.gprs[[2]] == Zeros{64}() && calling_rec.gprs[[3]] == Zeros{64}())
```

## B4.5.38.4 Footprint

| ID           | Value               |
|--------------|---------------------|
| target_flags | target_rec.flags    |
| target_gprs  | target_rec.gprs     |
| target_pc    | target_rec.pc       |
| calling_pend | calling_rec.pending |
| calling_gprs | calling_rec.gprs    |

<!-- image -->