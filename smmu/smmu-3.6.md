## 3.6 Structure and queue ownership

Arm expects that the Non-secure Stream table, Command queue, Event queue and PRI queue are controlled by the most privileged Non-secure system software.

If present, Arm expects that the Secure Stream table, Secure Command queue and Secure Event queue are controlled by Secure software. For example, these would be controlled by software in EL3 if a separation in control between Secure EL1 and EL3 is required.

Arm expects that the stage 2 translation tables indicated by all STEs are controlled by a hypervisor.

The ownership of stage 1 CDs and translation tables depends on the configuration in use. If pointed to by a Secure STE, they are controlled by Secure software (one of EL3, S-EL2, or S-EL1). If pointed to by a Non-secure STE, they are controlled by Non-secure software (either NS-EL2 or NS-EL1). If pointed to by a Realm STE, they are controlled by Realm software (either Realm-EL2 or Realm-EL1).

Note: For example, the context might be one of the following:

- Used by a bare-metal OS, which controls the descriptor and translation tables and is addressed by PA.
- Used internally by a hypervisor, which controls the descriptor and translation tables and is addressed by PA.
- Used by a guest, in which case Arm expects that the CD and translation tables are controlled by the guest, and addressed by IPA.

Note: When a hypervisor is used in a given Security state, Arm expects that the Event queue for that Security state is managed by the hypervisor, which forwards events into guest VMs as appropriate. StreamIDs might be mapped from physical to virtual equivalents during this process.

In virtualized scenarios, Arm expects a hypervisor to:

- Convert guest STEs into physical SMMU STEs, controlling permissions and features as required.

Note: The physical StreamIDs might be hidden from the guest, which would be given virtual StreamIDs, so a mapping between virtual and physical StreamIDs must be maintained.

- Read and interpret commands from the guest Command queue. These might result in commands being issued to the SMMU or invalidation of internal shadowed data structures.
- Consume new entries from the PRI and Event queues, mapping from host StreamIDs to guest, and deliver appropriate entries to guest Event and PRI queues.