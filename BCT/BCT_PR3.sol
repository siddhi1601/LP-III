pragma solidity ^0.4.19;

contract Bank {

    mapping(address => uint256)  balanceOf;   // balances, indexed by addresses

    function deposit(uint256 amount) public returns(uint){
        balanceOf[msg.sender] += amount;
        return balanceOf[msg.sender];     // adjust the account's balance
    }

    function withdraw(uint256 amount) public returns(uint) {
        balanceOf[msg.sender] -= amount;
        return balanceOf[msg.sender];
    }

    function getBalance() public view returns(uint){
        return balanceOf[msg.sender];
    }
}