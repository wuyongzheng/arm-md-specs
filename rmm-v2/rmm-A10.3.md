## A10.3 Planes memory management

- All Planes within a Realm have the same IPA size.
- If a given Protected IPA x is mapped to a given PA y in one Plane, x is not mapped to a different PA z in any other Plane within the Realm.

## A10.3.1 Auxiliary RTT

- A Realm which is configured to have an RTT tree per Plane has one primary RTT tree and (number of auxiliary Planes) auxiliary RTT trees .
- For a Realm which is configured to have an RTT tree per Plane, RTT trees are identified using a zero-based RTT tree index .

The RTT tree index of the primary RTT tree is zero.

- For a Realm which is configured to have an RTT tree per Plane, the mapping from Plane index to RTT tree index is as follows:

| Plane index   | RTT tree index   |
|---------------|------------------|
| 0             | 1                |
| 1             | 2                |
| . . .         | . . .            |
| n-2           | n-1              |
| n-1           | 0                |

For a Realm with no auxiliary Planes, n == 1 and therefore the index of the single Plane (0) maps to the index of the single RTT tree (0).

- Within Protected IPA space, the primary RTT tree and the auxiliary RTT trees are distinct. For a given Protected IPA, the set of RTTs traversed by a walk of any auxilary RTT tree is disjoint from the set of RTTs traversed by a walk of the primary RTT tree.


- Within Unprotected IPA space, below the RTT starting level, the primary RTT tree and the auxiliary RTT trees are shared. For a given Unprotected IPA, if a walk of any auxilary RTT tree progresses beyond the RTT starting level, then the set of RTTs traversed is identical to the set of RTTs traversed by a walk of the primary RTT tree.
- Within Protected IPA space, if a primary RTT entry is live and its state is not RTTE\_TABLE, then execution of RMI\_RTT\_AUX\_PROT\_MAP creates a mapping to the same output address in an auxiliary RTT.
- A Protected IPA is auxiliary-live if any of the entries identified by that IPA in auxiliary RTTs are live.
- Within Unprotected IPA space, if the state of a primary RTT entry at the RTT starting level is RTTE\_MAPPED\_NS or RTTE\_TABLE, then execution of RMI\_RTT\_AUX\_UNPROT\_MAP copies the primary RTT entry to the RTT starting level of an auxiliary RTT.
- Within Unprotected IPA space, if the state of an auxiliary RTT entry is RTTE\_TABLE then its output address is an RTT in the primary RTT tree.
- Within Unprotected IPA space, a primary RTT is auxiliary-referenced if it is pointed to by an auxiliary RTT entry whose state is RTTE\_TABLE.
- In a Realm which is configured to have an RTT tree per Plane, a given Unprotected IPA may be mapped to different output addresses in different Planes.

- The absence of a rule which states that a given Unprotected IPA must map to the same output address in different Planes avoids the need for the RMM to manage reference counts for NS Granules.
- If a Protected IPA is auxiliary-live then the corresponding entry in the primary RTT is live.

This invariant is preserved by blocking any actions which would make the primary RTT entry non-live, including the following:

- RMI\_RTT\_DATA\_UNMAP
- RMI\_RTT\_DEV\_UNMAP
- RMI\_RTT\_SET\_RIPAS
- If an IPA is auxiliary-live then its RIPAS cannot be changed.
- Specifying that RIPAS is invariant while an IPA is auxiliary-live avoids an implementation of RMI\_RTT\_SET\_RIPAS or RMI\_RTT\_DEV\_VALIDATE having to walk multiple auxiliary RTT trees.
- Folding of primary RTTs is independent of folding of auxiliary RTTs for the same IPA range.

See also:

- A5.6.8 RTTE liveness and RTT liveness
- B4.5.57 RMI\_RTT\_AUX\_CREATE command
- B4.5.58 RMI\_RTT\_AUX\_DESTROY command
- B4.5.59 RMI\_RTT\_AUX\_FOLD command
- B4.5.60 RMI\_RTT\_AUX\_PROT\_MAP command
- B4.5.61 RMI\_RTT\_AUX\_PROT\_UNMAP command
- B4.5.62 RMI\_RTT\_AUX\_UNPROT\_MAP command
- B4.5.63 RMI\_RTT\_AUX\_UNPROT\_UNMAP command
- B4.5.67 RMI\_RTT\_DATA\_UNMAP command
- B4.5.75 RMI\_RTT\_SET\_RIPAS command

## A10.3.2 Stage 2 Access Permissions within a multi-Plane Realm

This section describes how S2AP is controlled within a multi-Plane Realm.

## A10.3.2.1 Stage 2 Access Permissions within a multi-Plane Realm overview

- The S2AP which applies to an access from Pn to a Protected IPA is controlled by P0.


- The S2AP which applies to an access from Pn to a Protected IPA can be different for each Pn within the Realm.
- An access by Pn to a Protected IPA which violates S2AP causes a Plane exit taken to P0.
- The S2AP which applies to a Realm access to an Unprotected IPA is the same for all Planes within the Realm.
- A data access by Pn to an Unprotected IPA which violates S2AP causes a REC exit taken to the Host.
- An instruction fetch by Pn to an Unprotected IPA causes a Plane exit taken to P0.
- On a platform which implements FEAT\_S2PIE and FEAT\_S2POE, the RMM can utilise these architecture features to store per-Plane S2AP in a single RTT tree.

On a platform which does not implement these architecture features, a separate RTT tree is required for each Plane.

See also:

- A5.6.11 Stage 2 Access Permissions

## A10.3.2.2 Stage 2 Access Permissions for a Protected IPA within a multi-Plane Realm


The S2AP overlay index of a Protected IPA is between 0 and 14.


S2AP overlay index 15 is RESERVED.

At Realm activation, S2AP overlay indices 0 to 14 map to S2AP overlay value RW+puX for P0.

At Realm activation, S2AP overlay indices 0 to 14 map to S2AP overlay value NoAccess for all Planes other than P0.

For each S2AP overlay index there is an associated lock bit which applies to S2AP overlay values for Planes other than P0.

- If the lock bit is LOCKED then the S2AP overlay values for all Planes are immutable.
- If the lock bit is UNLOCKED then the S2AP overlay values for Planes other than P0 can be changed by P0.

At Realm activation, S2AP overlay index 0 is LOCKED.

At Realm activation, S2AP overlay indices 1 to 14 are UNLOCKED.

At Realm activation, the S2AP overlay index of all Protected IPAs is 0.

- The following table summarises the attributes of all S2AP overlay indices for Protected IPA space, at Realm activation.

| S2AP overlay index   | P0 S2AP overlay value   | Pn S2AP overlay values   | Lock status for Pn S2AP overlay values   |
|----------------------|-------------------------|--------------------------|------------------------------------------|
| 0                    | RW+puX                  | NoAccess                 | LOCKED                                   |
| 1 to 14              | RW+puX                  | NoAccess                 | UNLOCKED                                 |

The RSI\_MEM\_SET\_PERM\_INDEX command can be used by P0 to change the S2AP overlay index for a Protected IPA.

The RSI\_MEM\_SET\_PERM\_VALUE command can be used by P0 to change the mapping from a { Plane, S2AP overlay index } tuple to an S2AP overlay value.

## See also:

- Chapter A5 Realm memory management
- A10.3.1 Auxiliary RTT


- B5.4.11 RSI\_MEM\_SET\_PERM\_INDEX command
- B5.4.12 RSI\_MEM\_SET\_PERM\_VALUE command

## A10.3.2.3 Stage 2 Access Permissions change within a multi-Plane Realm

An S2AP change is a process via which the S2AP of a region of Protected IPA space is changed.

An S2AP change consists of actions taken both by P0 within the Realm and by the Host:

- P0 issues an S2AP change request by executing RSI\_MEM\_SET\_PERM\_INDEX.
- -The input values to this command include:
* The requested IPA range: [base, top)
* The requested S2AP overlay index
- A'handle', whose initial value is zero. Across successive calls to RSI\_MEM\_SET\_PERM\_INDEX,
* the handle is used by the RMM to store an IMPLEMENTATION DEFINED value which tracks progress of the request.
- -The RMM records these values in the REC, and then performs a REC exit due to S2AP change pending.
- In response, the Host executes zero or more RMI\_RTT\_SET\_S2AP commands.
- If the requested RIPAS value was not RIPAS\_EMPTY then at the next RMI\_REC\_ENTER the Host can optionally indicate that it rejects the S2AP change request.

The purpose of the handle is to record the progress of the S2AP change request across multiple RTT trees. For a

Realm which is configured to use a shared RTT tree, the RMM should return a handle value of zero.



Rejection by the Host of an S2AP change request is intended to be used if the target IPA range extends beyond the agreed DRAM range for the Realm. In this situation, accepting the request may impose unplanned resource costs on the Host, by requiring allocation of additional RTTs.

The S2AP change process ensures that a Realm can always reliably determine the maximum S2AP which can be observed at the next access to any Protected IPA.

An S2AP change is applied by one or more calls to the RMI\_RTT\_SET\_S2AP command.

The order in which the S2AP of Planes and pages within the target IPA range are changed during execution of RSI\_MEM\_SET\_PERM\_INDEX is IMPLEMENTATION DEFINED.

If the input arguments of RSI\_MEM\_SET\_PERM\_INDEX are modified by the caller during the loop, it is IMPLEMENTATION DEFINED whether the S2AP of Planes and pages within the target IPA range are changed.

The P0 programming model for changing S2AP is to call RSI\_MEM\_SET\_PERM\_INDEX in a loop until progress reaches the top of the target IPA range, as shown in the following pseudocode:

```
handle,
```

```
int realm_set_s2ap(uint64_t base, uint64_t top, unsigned int index) { uint64_t new_base; RsiResponse response; uint64_t handle = 0, new_handle; int ret = RSI_SUCCESS; while (base != top) { ret = rsi_mem_set_perm_index(base, top, index, &new_base, &response, &new_handle); if (ret != RSI_SUCCESS) { return ret; } if (response == RSI_RESPONSE_REJECT) { return RSI_ERROR_INPUT; } base = new_base; handle = new_handle; } return RSI_SUCCESS; }
```

The Host programming model for handling an S2AP change request is to call RMI\_RTT\_SET\_S2AP in a loop until progress reaches the top of the target IPA range, as shown in the following pseudocode:

```
int host_set_s2ap(uint64_t base, uint64_t top) { uint64_t out_top, index, rtt_tree; int ret = RMI_SUCCESS; while (base != top) { ret = RMI_RTT_SET_S2AP(rd, rec, base, top, &out_top, &rtt_tree, &index); if (ret == RMI_ERROR_RTT || ret == RMI_ERROR_AUX_RTT) { create_rtt(ipa = out_top, level = index + 1, rtt_tree); continue;
```

```
Chapter A10. Planes A10.3. Planes memory management } else if (ret != RMI_SUCCESS) { break; } base = out_top; } return ret; }
```


On REC entry following a REC exit due to S2AP change, rec.s2ap\_response is set to the value of enter.flags.s2ap\_response .






If all of the following are true then the output value of RSI\_MEM\_SET\_PERM\_INDEX indicates 'Host rejected the request':

- rec.s2ap\_addr is not equal to rec.s2ap\_top .
- rec.s2ap\_response is REJECT.

Otherwise, the output value of RSI\_MEM\_SET\_PERM\_INDEX indicates 'Host accepted the request'.

See also:

· A4.3.11 REC exit due to S2AP change pending · B3.109 RecS2APResponseToRsi function · B4.5.51 RMI\_REC\_ENTER command · B4.5.76 RMI\_RTT\_SET\_S2AP command · B5.4.11 RSI\_MEM\_SET\_PERM\_INDEX command · D1.5.4 S2AP change flow A10.3.2.4 Stage 2 Access Permissions reset due to Host action Execution of RMI\_RTT\_DESTROY or RMI\_RTT\_AUX\_DESTROY sets the S2AP overlay index of the target RTTE to 0. The Host is permitted at any time to destroy an RTT. Destruction of an RTT causes the RMM to lose information about the S2AP for the IPA range described by that RTT. The S2AP are observable by the Realm only while the RIPAS is RIPAS\_RAM. Therefore, this specification defines the value to which the S2AP overlay index must be reset on a RIPAS transition to RIPAS\_RAM.

See also:

- A5.4 RIPAS change

## A10.3.2.5 Stage 2 Access Permissions reset due to Realm action

For a Realm which is configured to have an RTT tree per Plane, execute permission for Pn is dropped on transition to RIPAS\_DEV.

Following a transition from RIPAS\_DEV to RIPAS\_EMPTY, in order to ensure that a subsequent instruction fetch from Pn does not result in a permission fault, P0 must restore execute permission by executing RSI\_MEM\_SET\_PERM\_INDEX.

See also:

- B5.4.11 RSI\_MEM\_SET\_PERM\_INDEX command