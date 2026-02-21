## Chapter 8 Page request queue

The message format arriving on the PRI queue in response to an incoming PCIe PRI message closely follows the PCIe packet format. The field names have been generalized for consistency with terminology elsewhere in this specification. PRI messages are little-endian. The system must ensure that the mapping between StreamID and RequesterID or Root Complex is identical whether used in either incoming or outgoing directions for PRI, ATS or normal DMA traffic.

<!-- image -->

## · StreamID[31:0]

- -When used with ATS/PRI, StreamID[15:0] must equal PCIe RequesterID[15:0]. Bits StreamID[n:16] might indicate different Root Complex sources where more than 16 bits of StreamID are implemented.
- SSV: Substream valid
- -When 1, the Page Request was issued with a PASID TLP prefix.
- -When 0, the Page Request was not issued with a PASID. This value is also 0 when Substreams are not supported by the SMMU. When SSV == 0, the X and Priv bits are both 0.

- SubstreamID[19:0]
- -This value is UNKNOWN when SSV == 0.
- Page address[63:12]
- PRGIndex[8:0]
- Last, W, R, X, Priv: Last/Write/Read/eXecute/Privileged:
- -These bits encode requested page permissions
- -'Last' is set on the last request in a PRG
- -The PCIe 'Stop PASID' marker message delimits Page Request message groups as a request with LWR == 0b100 . Stop Markers have a PASID, that is, SSV == 1. A message that arrives without a PASID and that has LWR == 0b100 is not a Stop Marker, has SSV == 0, and is treated as a PRI Page Request.

Several related PRI Page Requests (PPRs) might arrive in batches, named Page Request Groups (PRGs). Several pages might be requested in a PRG and all arrive with the same PRGIndex value. The last page request in a PRG is marked by the Endpoint as Last == 1 and the PRI queue can be configured to send an interrupt when Last == 1 is received (see SMMU\_PRIQ\_IRQ\_CFG2. Member requests of a PRG are not guaranteed to be contiguous in the PRI queue as requests of more than one PRG might be interleaved. PPRs that are members of the PRG are not guaranteed to appear in the PRI queue in the order that they were issued from an endpoint, with the exception of the Last == 1 entry which is not re-ordered with respect to prior PPRs.

The SMMU is not required to track and verify that, for a given PRGIndex value, all entries received in a PRG have identical PASID TLP prefixes.

The CMD\_PRI\_RESP command causes a PRI response to be sent to an endpoint and takes a success or failure parameter to inform the endpoint of the overall status of the PRG. When Substreams (PASIDs in this context) are supported and this command is used with a valid SubstreamID (SSV == 1), a PASID tag is present on the response.

Note: Arm expects this command to be issued after all PPRs in a PRG have been processed, including the Last == 1 entry.

Note: The PRI queue does not overflow with correct software usage and endpoint credit management, because software grants credits to each device (using PCI configuration space) which sum to the amount of space in the PRI queue minus an allowance for any 'Stop PASID' markers that are required. The device can only issue as many outstanding PPRs as it has credits for.

The SMMU freely accepts incoming PRI messages and puts them in the PRI queue, if space is free and the queue is enabled and not in an error condition. If the queue is full a programming error (or protocol failure by PCIe endpoint) has occurred.

Note: A device is intended to always receive a response to a PRG, whether positive or negative.

Note: A CMD\_PRI\_RESP returns a credit to the Endpoint that could cause another PPR. This must be considered when calculating credit capability of a queue. If the number of credits granted to devices equals the queue capacity, a PPR must be consumed from the queue (freeing an entry) prior to issuing a CMD\_PRI\_RESP for that PPR.

The SMMU supports a maximum PRI queue size of 2 19 entries.

Note: When a guest VM manages a PRI queue for page request service from one or more devices assigned to that guest, it is up to the guest OS to allocate and size its local PRI queue. It will subsequently give credits to the devices to allow them to issue PPRs, using configuration space accesses. In this scenario, the hypervisor manages the actual SMMU PRI queue and the sum of the credits given to all clients of that queue must not be greater than the size of the queue. For safety, Arm expects that a hypervisor will trap the write of a credit value of a guest to a device, and substitute its own allocation if necessary. This would ensure that the total number of credits cannot exceed the PRI queue size, even if a guest OS requests a larger number of credits to be used. The hypervisor is also expected to choose an appropriate PRI queue size which will approximate the sum of credits reasonably expected to be used by all guest VMs using the PRI facilities of an SMMU.