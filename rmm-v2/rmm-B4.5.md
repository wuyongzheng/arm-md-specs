## B4.5 RMI commands

The following table summarizes the FIDs of commands in the RMI interface.

| FID              | Command                       |
|------------------|-------------------------------|
| 0xC4000150       | RMI_VERSION                   |
| 0xC4000153       | RMI_RTT_DATA_MAP_INIT         |
| 0xC4000157       | RMI_REALM_ACTIVATE            |
| 0xC4000158       | RMI_REALM_CREATE              |
| 0xC4000159       | RMI_REALM_DESTROY             |
| 0xC400015A       | RMI_REC_CREATE                |
| 0xC400015B       | RMI_REC_DESTROY               |
| 0xC400015C       | RMI_REC_ENTER                 |
| 0xC400015D       | RMI_RTT_CREATE                |
| 0xC400015E       | RMI_RTT_DESTROY               |
| 0xC4000161       | RMI_RTT_READ_ENTRY            |
| 0xC4000163       | RMI_RTT_DEV_VALIDATE          |
 0xC4000164 | RMI_PSCI_COMPLETE             |
| 0xC4000165       | RMI_FEATURES                  |
| 0xC4000166       | RMI_RTT_FOLD                  |
| 0xC4000168       | RMI_RTT_INIT_RIPAS            |
| 0xC4000169       | RMI_RTT_SET_RIPAS             |
| 0xC400016A       | RMI_VSMMU_CREATE              |
| 0xC400016B       | RMI_VSMMU_DESTROY             |
| 0xC400016E       | RMI_RMM_CONFIG_SET            |
| 0xC400016F       | RMI_PSMMU_IRQ_NOTIFY          |
| 0xC4000170       | RMI_ATTEST_PLAT_TOKEN_REFRESH |
| 0xC4000174       | RMI_PDEV_ABORT                |
| 0xC4000175       | RMI_PDEV_COMMUNICATE          |
| 0xC4000176       | RMI_PDEV_CREATE               |
| 0xC4000177       | RMI_PDEV_DESTROY              |
| 0xC4000178       | RMI_PDEV_GET_STATE            |
| 0xC400017A       | RMI_PDEV_STREAM_KEY_REFRESH   |
| 0xC400017B       | RMI_PDEV_SET_PUBKEY           |
| 0xC400017C       | RMI_PDEV_STOP                 |
| 0xC400017D       | RMI_RTT_AUX_CREATE            |
| 0xC400017E       | RMI_RTT_AUX_DESTROY           |

| FID              | Command                       |
|------------------|-------------------------------|
| 0xC400017F       | RMI_RTT_AUX_FOLD              |
| 0xC4000185       | RMI_VDEV_ABORT                |
| 0xC4000186       | RMI_VDEV_COMMUNICATE          |
| 0xC4000187       | RMI_VDEV_CREATE               |
| 0xC4000188       | RMI_VDEV_DESTROY              |
| 0xC4000189       | RMI_VDEV_GET_STATE            |
| 0xC400018A       | RMI_VDEV_UNLOCK               |
| 0xC400018B       | RMI_RTT_SET_S2AP              |
| 0xC400018E       | RMI_VDEV_COMPLETE             |
| 0xC40001D0       | RMI_VDEV_GET_INTERFACE_REPORT |
| 0xC40001D1       | RMI_VDEV_GET_MEASUREMENTS     |
| 0xC40001D2       | RMI_VDEV_LOCK                 |
| 0xC40001D3       | RMI_VDEV_START                |
| 0xC40001D4       | RMI_VDEV_P2P_BIND             |
| 0xC40001D5       | RMI_VDEV_P2P_UNBIND           |
 0xC40001D6 | RMI_VSMMU_EVENT_NOTIFY        |
| 0xC40001D7       | RMI_PSMMU_ACTIVATE            |
| 0xC40001D8       | RMI_PSMMU_DEACTIVATE          |
| 0xC40001DB       | RMI_PSMMU_ST_L2_CREATE        |
| 0xC40001DC       | RMI_PSMMU_ST_L2_DESTROY       |
| 0xC40001DD       | RMI_DPT_L0_CREATE             |
| 0xC40001DE       | RMI_DPT_L0_DESTROY            |
| 0xC40001DF       | RMI_DPT_L1_CREATE             |
| 0xC40001E0       | RMI_DPT_L1_DESTROY            |
| 0xC40001E1       | RMI_GRANULE_TRACKING_GET      |
| 0xC40001E3       | RMI_GRANULE_TRACKING_SET      |
| 0xC40001E4       | RMI_CMEM_ADD_PDEV             |
| 0xC40001E5       | RMI_CMEM_CREATE               |
| 0xC40001E6       | RMI_CMEM_DESTROY              |
| 0xC40001E7       | RMI_CMEM_POPULATE             |
| 0xC40001E8       | RMI_CMEM_REMOVE_PDEV          |
| 0xC40001E9       | RMI_CMEM_START                |
| 0xC40001EA       | RMI_CMEM_STOP                 |
| 0xC40001EB       | RMI_CMEM_UNPOPULATE           |
| 0xC40001EC       | RMI_RMM_CONFIG_GET            |

| FID              | Command                      |
|------------------|------------------------------|
| 0xC40001ED       | RMI_PDEV_MEC_REFRESH         |
| 0xC40001EE       | RMI_VSMMU_EVENT_COMPLETE     |
| 0xC40001F0       | RMI_PSMMU_EVENT_DISCARD      |
| 0xC40001F1       | RMI_GRANULE_RANGE_DELEGATE   |
| 0xC40001F2       | RMI_GRANULE_RANGE_UNDELEGATE |
| 0xC40001F3       | RMI_GPT_L1_CREATE            |
| 0xC40001F4       | RMI_GPT_L1_DESTROY           |
| 0xC40001F5       | RMI_RTT_DATA_MAP             |
| 0xC40001F6       | RMI_RTT_DATA_UNMAP           |
| 0xC40001F7       | RMI_RTT_DEV_MAP              |
| 0xC40001F8       | RMI_RTT_DEV_UNMAP            |
| 0xC40001F9       | RMI_RTT_ARCH_DEV_MAP         |
| 0xC40001FA       | RMI_RTT_ARCH_DEV_UNMAP       |
| 0xC40001FB       | RMI_RTT_UNPROT_MAP           |
| 0xC40001FC       | RMI_RTT_UNPROT_UNMAP         |
 0xC40001FD | RMI_RTT_AUX_PROT_MAP         |
| 0xC40001FE       | RMI_RTT_AUX_PROT_UNMAP       |
| 0xC40001FF       | RMI_RTT_AUX_UNPROT_MAP       |
| 0xC4000200       | RMI_RTT_AUX_UNPROT_UNMAP     |
| 0xC4000201       | RMI_REALM_TERMINATE          |
| 0xC4000202       | RMI_RMM_ACTIVATE             |
| 0xC4000203       | RMI_OP_CONTINUE              |
| 0xC4000204       | RMI_PDEV_STREAM_CONNECT      |
| 0xC4000205       | RMI_PDEV_STREAM_DISCONNECT   |
| 0xC4000206       | RMI_PDEV_STREAM_COMPLETE     |
| 0xC4000207       | RMI_PDEV_STREAM_KEY_PURGE    |
| 0xC4000208       | RMI_OP_MEM_DONATE            |
| 0xC4000209       | RMI_OP_MEM_RECLAIM           |
| 0xC400020A       | RMI_OP_CANCEL                |
| 0xC400020B       | RMI_VSMMU_FEATURES           |
| 0xC400020C       | RMI_VSMMU_CMD_GET            |
| 0xC400020D       | RMI_VSMMU_CMD_COMPLETE       |