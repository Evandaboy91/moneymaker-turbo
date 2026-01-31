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
