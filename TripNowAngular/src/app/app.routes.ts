import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: '',
        loadComponent: () => import('./layouts/main-layout/main-layout').then((c => c.MainLayout)),
        title: "inicio",
        children: [
            {
                path: '',
                loadComponent: () => import("./features/inicio/inicio").then(c => c.Inicio),
            },
            {
                path: 'busquedas',
                loadComponent: () => import('./features/busquedas/busquedas').then((c => c.Busquedas)),
                title: "busquedas",
            },
            {
                path: 'perfil',
                loadComponent: () => import('./features/perfil/perfil').then((c => c.Perfil)),
                title: "perfil",
            },
            {
                path: 'reservas',
                loadComponent: () => import('./features/reservas/reservas').then((c => c.Reservas)),
                title: "reservas",
            },
            {
                path: 'notificaciones',
                loadComponent: () => import('./features/notificaciones/notificaciones').then((c => c.Notificaciones)),
                title: "notificaciones",
            },
            {
                path: 'login',
                loadComponent: () => import('./features/auth/login/login').then((c => c.Login)),
            },
            {
                path: 'register',
                loadComponent: () => import('./features/auth/register/register').then((c => c.Register)),
            }


        ]

    }
];
