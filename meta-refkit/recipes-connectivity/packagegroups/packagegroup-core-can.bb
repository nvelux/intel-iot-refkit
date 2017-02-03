SUMMARY = "IoT Reference OS Kit Connectivity package groups"
LICENSE = "MIT"
PR = "r1"

inherit packagegroup

SUMMARY_${PN} = "IoT Reference OS Kit CAN stack"
RDEPENDS_${PN} = "\
    can-utils \
    can-init-scripts \
    "
