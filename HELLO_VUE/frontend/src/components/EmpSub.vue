<template>


	<table border="1px">
		<thead>
			<tr>
				<td>사번</td>
				<td>이름</td>
				<td>성별</td>
				<td>주소</td>
			</tr>
		</thead>
		<tbody>
			<tr v-for="d in state.data" :key="d.e_id">
				<td @click="detail(d.e_id)">{{ d.e_id }}</td>
				<td>{{ d.e_name }}</td>
				<td>{{ d.sex }}</td>
				<td>{{ d.addr }}</td>
			</tr>
		</tbody>

	</table>

	<table border="1px">
		<tr>
			<td>사번</td>
			<td><input type="text" id="e_id" /></td>
		</tr>
		<tr>
			<td>이름</td>
			<td><input type="text" id="e_name" /></td>
		</tr>
		<tr>
			<td>성별</td>
			<td><input type="text" id="sex" /></td>
		</tr>
		<tr>
			<td>주소</td>
			<td><input type="text" id="addr" /></td>
		</tr>

		<tr>
			<td colspan="2"><input type="button" value="추가" @click="add()" />
				<input type="button" value="수정" @click="edit()" /> <input
				type="button" value="삭제" @click="del()" /></td>
		</tr>
	</table>

</template>

<script>

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
</script>

<style lang="scss" scoped>
</style>
