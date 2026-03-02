## B4.5.74 RMI\_RTT\_READ\_ENTRY command

Reads an entry from a primary RTT.

See also:

- A5.6 Realm Translation Table

## B4.5.74.1 Interface

## B4.5.74.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                              |
|--------|------------|--------|---------|------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000161                    |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm        |
| ipa    | X2         | 63:0   | Address | Realm Address for which to read the RTTE |
| level  | X3         | 63:0   | Int64   | RTT level at which to read the RTTE      |

## B4.5.74.1.2 Context

The RMI\_RTT\_READ\_ENTRY command operates on the following context.

| Name   | Type Value                             | Before   | Description                      |
|--------|----------------------------------------|----------|----------------------------------|
| realm  | RmmRealm RealmAt(rd)                   | false    | Realm                            |
| walk   | RmmRttWalkResult RttWalk(              | false    | RTT walk result                  |
| rtte   | RmmRttEntry RttDescriptorDecode( desc, | false    | RTT entry value returned to Host |


## B4.5.74.1.3 Output values

| Name       | Register   | Bits   | Type             | Description                       |
|------------|------------|--------|------------------|-----------------------------------|
| result     | X0         | 63:0   | RmiResult        | Command result                    |
| walk_level | X1         | 63:0   | UInt64           | RTT level reached by the RTT walk |
| state      | X2         | 7:0    | RmiRttEntryState | State of RTTE reached by the walk |
| desc       | X3         | 63:0   | Bits64           | RTTE descriptor                   |
| ripas      | X4         | 7:0    | RmiRipas         | RIPAS of RTTE reached by the walk |

The following unused bits of RMI\_RTT\_READ\_ENTRY output values MBZ: X2[63:8], X4[63:8].

The layout and encoding of fields in the desc output value match 'Attribute fields in stage 2 VMSAv8-64 Block and Page descriptors' in Arm Architecture Reference Manual for A-Profile architecture [3].

See also:

- Arm Architecture Reference Manual for A-Profile architecture [3]
- A5.6.12 Memory attributes

## B4.5.74.2 Failure conditions

```
ID Condition rd_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT rd_bound pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT level_bound pre: !RttLevelIsValid(realm, level) post: result.status == RMI_ERROR_INPUT ipa_align pre: !AddrIsRttLevelAligned(ipa, level) post: result.status == RMI_ERROR_INPUT ipa_bound pre: UInt(ipa) >= (2 ^ realm.ipa_width) post: result.status == RMI_ERROR_INPUT
```

B4.5.74.2.1 Failure condition ordering The RMI\_RTT\_READ\_ENTRY command does not have any failure condition orderings. B4.5.74.3 Success conditions ID Condition walk\_level post: walk\_level == walk.level state post: state == RttEntryStateToRmi(walk.rtte.state) state\_invalid pre: (walk.rtte.state == RTTE\_VOID || walk.rtte.state == RTTE\_UNMAPPED\_NS) post: (rtte.attr\_unprot == Zeros{3}() &amp;&amp; rtte.s2ap\_indirect.base\_index == S2AP\_NO\_ACCESS &amp;&amp; rtte.s2ap\_indirect.overlay\_index == 0 &amp;&amp; rtte.s2ap\_direct.read == RMM\_FALSE &amp;&amp; rtte.s2ap\_direct.write == RMM\_FALSE &amp;&amp; rtte.addr == Zeros{ADDRESS\_WIDTH}()) state\_prot pre: (walk.rtte.state == RTTE\_DATA || walk.rtte.state == RTTE\_NARCH\_DEV || walk.rtte.state == RTTE\_ARCH\_DEV || walk.rtte.state == RTTE\_TABLE) post: (rtte.attr\_unprot == Zeros{3}() &amp;&amp; rtte.s2ap\_indirect.base\_index == S2AP\_NO\_ACCESS &amp;&amp; rtte.s2ap\_indirect.overlay\_index == 0 &amp;&amp; rtte.s2ap\_direct.read == RMM\_FALSE &amp;&amp; rtte.s2ap\_direct.write == RMM\_FALSE &amp;&amp; rtte.addr == walk.rtte.addr)

## ID

## Condition

```
state_unprot pre: walk.rtte.state == RTTE_MAPPED_NS post: (rtte.attr_unprot == walk.rtte.attr_unprot && rtte.s2ap_indirect.base_index == walk.rtte.s2ap_indirect.base_index && rtte.s2ap_indirect.overlay_index == 0 && rtte.s2ap_direct.read == walk.rtte.s2ap_direct.read && rtte.s2ap_direct.write == walk.rtte.s2ap_direct.write && rtte.addr == walk.rtte.addr) state_io pre: walk.rtte.state == RTTE_NARCH_DEV post: (rtte.attr_unprot == Zeros{3}() && rtte.s2ap_indirect.base_index == S2AP_NO_ACCESS && rtte.s2ap_indirect.overlay_index == 0 && rtte.s2ap_direct.read == RMM_FALSE && rtte.s2ap_direct.write == RMM_FALSE && rtte.addr == walk.rtte.addr) state_vsmmu pre: walk.rtte.state == RTTE_ARCH_DEV post: (rtte.attr_unprot == Zeros{3}() && rtte.s2ap_indirect.base_index == S2AP_NO_ACCESS && rtte.s2ap_indirect.overlay_index == 0 && rtte.s2ap_direct.read == RMM_FALSE && rtte.s2ap_direct.write == RMM_FALSE && rtte.addr == walk.rtte.addr) ripas_prot pre: (walk.rtte.state == RTTE_VOID || walk.rtte.state == RTTE_DATA) post: ripas == RipasToRmi(walk.rtte.ripas) ripas_unprot pre: (walk.rtte.state == RTTE_UNMAPPED_NS || walk.rtte.state == RTTE_MAPPED_NS) post: ripas == RMI_RIPAS_EMPTY
```

## B4.5.74.4 Footprint

The RMI\_RTT\_READ\_ENTRY command does not have any footprint.