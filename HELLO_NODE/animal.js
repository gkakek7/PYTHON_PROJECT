class Animal {
	constructor() {
		console.log('construtor');
		this.name = "";
	}
	named(name) {
		return this.name = name
	}
}
module.exports = Animal;

if (require.main === module) {
	var ani = new Animal();
	ani.named("멍멍이");
	console.log(ani.name)
}
