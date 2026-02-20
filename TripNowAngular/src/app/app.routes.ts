import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: '',
        loadComponent: () => import('./layouts/main-layout/main-layout').then((c => c.MainLayout)),
        title: "inicio",
        children: [
            {
                path: '',
                loadComponent: () => import("./features/inicio/inicio").then((c => c.Inicio)),
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
                path: 'autentificacion',
                loadComponent: () => import('./features/auth/autentificacion/autentificacion').then((c => c.Autentificacion)),
            },
            {
                path: 'sobre-nosotros',
                loadComponent: () => import('./features/sobre-nosotros/sobre-nosotros').then((c => c.SobreNosotros)),
            },
            {
                path: 'contacto',
                loadComponent: () => import('./features/contacto/contacto').then((c => c.Contacto)),
            },
            {
                path: 'resenias',
                loadComponent: () => import('./features/resenias/resenias').then((c => c.Resenias)),
            }


        ]

    }
];
