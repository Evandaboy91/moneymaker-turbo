// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title ZephyrLedger
/// @notice Meridian phase-2 checkpoint registry. Genesis params and canonical source are fixed at deploy; no claim logic, no token, no distribution.
contract ZephyrLedger {
    address public immutable registryTreasury;
    uint256 public immutable genesisBlock;
    uint256 public immutable genesisTimestamp;
    bytes32 public immutable domainSeparator;

    mapping(bytes32 => uint256) private _checkpoints;
    uint256 public totalCheckpoints;

    event CheckpointSet(bytes32 indexed id, uint256 value, uint256 totalCheckpoints);

    constructor() {
        registryTreasury = msg.sender;
        genesisBlock = block.number;
        genesisTimestamp = block.timestamp;
        domainSeparator = keccak256(
            abi.encodePacked(
                block.chainid,
                address(this),
                block.number,
                block.timestamp
            )
        );
    }

    function setCheckpoint(bytes32 id, uint256 value) external {
        require(msg.sender == registryTreasury, "Zephyr: only treasury");
        require(_checkpoints[id] == 0, "Zephyr: id already set");
        _checkpoints[id] = value;
        totalCheckpoints += 1;
        emit CheckpointSet(id, value, totalCheckpoints);
    }

    function getCheckpoint(bytes32 id) external view returns (uint256) {
        return _checkpoints[id];
    }

    function seal() external view returns (bytes32) {
        return keccak256(
            abi.encodePacked(
                domainSeparator,
                totalCheckpoints,
                genesisBlock,
                genesisTimestamp
            )
        );
    }
}






