var Animal = require('./animal.js')

class Human extends Animal{
	constructor() {
        super();
		this.asset=0;
    }
	goldspoon(){
		this.asset=10000000000;
	}
}
module.exports = Human;
