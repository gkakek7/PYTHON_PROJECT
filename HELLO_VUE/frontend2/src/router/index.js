import { createRouter, createWebHistory } from 'vue-router'

// 연결할 각 컴포넌트 import (src/views폴더 아래 컴포넌트들 생성해둠)
import AaView	from '../views/AaView'
import BbView	from '../views/BbView'
import CcView	from '../views/CcView'

// 라우터 설계
const routes = [
    { path: '/', component:AaView},
    { path: '/1', component:BbView},
    { path: '/2', component:CcView}
]

// 라우터 생성
const router = createRouter({
    history: createWebHistory(),
    routes
});

// 라우터 추출 (main.js에서 import)
export {router}