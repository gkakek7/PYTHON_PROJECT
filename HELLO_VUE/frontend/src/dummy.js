
import { reactive } from "vue";
import axios from "axios";

export default {
	setup() {
		const state = reactive({
			data: [],
		});


		const del = () => {
			var e_id = document.querySelector("#e_id").value;

			axios.post("/api/emp_delete", { e_id }).then((res) => {
				console.log("emp_delete", res.data);
				state.data = res.data;
				document.querySelector("#e_id").value = "";
				document.querySelector("#e_name").value = "";
				document.querySelector("#sex").value = "";
				document.querySelector("#addr").value = "";
			});
		};


		const add = () => {
			var e_name = document.querySelector("#e_name").value;
			var sex = document.querySelector("#sex").value;
			var addr = document.querySelector("#addr").value;

			axios.post("/api/emp_insert", { e_name, sex, addr }).then((res) => {
				console.log("emp_insert", res.data);
				state.data = res.data;
				document.querySelector("#e_id").value = "";
				document.querySelector("#e_name").value = "";
				document.querySelector("#sex").value = "";
				document.querySelector("#addr").value = "";

			});
		};

		const edit = () => {
			var e_id = document.querySelector("#e_id").value;
			var e_name = document.querySelector("#e_name").value;
			var sex = document.querySelector("#sex").value;
			var addr = document.querySelector("#addr").value;

			axios.post("/api/emp_update", { e_id, e_name, sex, addr }).then((res) => {
				console.log("emp_update", res.data);
				state.data = res.data;
				document.querySelector("#e_id").value = "";
				document.querySelector("#e_name").value = "";
				document.querySelector("#sex").value = "";
				document.querySelector("#addr").value = "";
			});
		};

		const detail = (e_id) => {
			axios.post("/api/emp_select", { e_id }).then((res) => {
				console.log("emp_select", res.data);
				document.querySelector("#e_id").value = res.data[0].e_id;
				document.querySelector("#e_name").value = res.data[0].e_name;
				document.querySelector("#sex").value = res.data[0].sex;
				document.querySelector("#addr").value = res.data[0].addr;
			});
		};

		axios.get("/api/emp_selects").then((res) => {
			console.log("emp_selects", res);
			state.data = res.data;
		});

		return { state, detail, add, edit, del };
	}
};
