## 8.2 Miscellaneous

An external abort detected while accessing the PRI queue, for example when writing a record, activates the SMMU\_GERROR.PRIQ\_ABT\_ERR Global Error. If PRIQ\_ABT\_ERR becomes active, one or more PRI records might have been lost. The behavior of PRIQ\_ABT\_ERR relates to entries written to the PRI queue as the behavior of EVENTQ\_ABT\_ERR relates to entries written to the Event queue, as described in section 7.2.2 Event queue access external abort . It is IMPLEMENTATION DEFINED whether an external abort that is triggered by a write to the PRI queue is synchronous or asynchronous. When the write of a PRI queue entry results in a synchronous external abort, an automatic PRG Response with ResponseCode == 0b1111 is generated for the associated PPR. When the write of a PRI queue entry results in an asynchronous external abort, one or more queue entries might have been lost and no automatic response is generated for the PPRs that are associated with these entries.

An implementation is permitted to read any address within the bounds of the PRI queue when the queue is enabled (that is, when the effective value of SMMU\_CR0.PRIQEN == 1). In addition to writes of new records to the queue, such reads might also lead to an external abort.

A PPR received from a Secure stream is discarded, is not recorded into the PRI queue and results in an automatic Response Message having ResponseCode == 0b1111 .

If an active GERROR.PRIQ\_ABT\_ERR error condition exists, or if the effective value of SMMU\_CR0.PRIQEN == 0 (SMMU\_CR0.SMMUEN == 0 implies PRIQEN == 0) all of the following apply:

- No entries are written to the PRI queue.
- All incoming PPRs cause an automatic PRG Response having ResponseCode == 0b1111 ('Response Failure') and the messages are discarded.

Note: Incoming PRI Page Requests are not affected by SMMU\_CR0.ATSCHK or STE.EATS configuration.

The SMMU does not generate responses to Stop Marker messages.

Automatically-generated PRG responses have the following properties:

- Same StreamID as the PPR that triggered the response so that the message is returned to the originating RequesterID.
- Same Page Request Group Index as the PPR that triggered the response.
- Response Code depends on the cause of auto-generated response, see this section and sections 8.1 PRI queue overflow and 8.3 PRG Response Message codes .
- No PASID prefix is used on responses that were auto-generated because the effective value of PRIQEN == 0 or PRIQ\_ABT\_ERR occurred.
- A PASID prefix is used if all of the following are true:
- -The response was auto-generated because of PRI queue overflow.
- -The SMMU supports substreams.
- -SMMU\_IDR3.PPS == 1, or SMMU\_IDR3.PPS == 0 and STE.PPAR == 1.
- -The response will not have ResponseCode == 0b1111 .
- -The PPR that triggered the auto-response had a PASID prefix.
- If a PASID prefix is used, its PASID value matches that of the PPR that triggered the response.