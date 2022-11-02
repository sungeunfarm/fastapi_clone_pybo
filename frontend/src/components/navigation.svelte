<script>
    import {link} from 'svelte-spa-router'
    import {page} from '../lib/store'
</script>

<!-- 네비게이션 -->

<nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
    <div class="container-fluid">
        <a href="/" class="navbar-brand" use:link on:click="{()=>{$page = 0}}">Pybo</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a use:link href="/user-create" class="nav-link">회원가입</a>
                </li>
                <li class="nav-item">
                    <a use:link class="nav-link" href="/user-login">로그인</a>
                </li>
            </ul>
        </div>
    </div>
</nav>