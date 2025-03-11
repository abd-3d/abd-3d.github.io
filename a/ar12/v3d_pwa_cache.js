const CACHE_PREFIX = 'v3d-app-cache';
const CACHE_HASH = 'e7ad4b0ded';
const CACHE_VERSION = 'v1';

const ASSETS = [
    'basis_transcoder.js',
    'basis_transcoder.wasm',
    'Bed_table.bin',
    'Bed_table.css',
    'Bed_table.gltf',
    'Bed_table.html',
    'Bed_table.js',
    'bfont.woff',
    'book_c.jpg',
    'edit_button.png',
    'index.html',
    'interior.png',
    'opentype.js',
    'prompt_move_around.png',
    'ready_button.png',
    'roughness.jpg',
    'v3d.js',
    'visual_logic.js',
    'WoodYellowish_diffuse_xtm copy.jpg',
    'WoodYellowish_DisplacementMap.jpg',
    'WoodYellowish_NormalMap.jpg',
    'media/android-chrome-192x192.png',
    'media/android-chrome-512x512.png',
    'media/apple-touch-icon.png',
    'media/ar.png',
    'media/ar.svg',
    'media/enter_AR_button.png',
    'media/explode.svg',
    'media/favicon-16x16.png',
    'media/favicon-32x32.png',
    'media/favicon-48x48.png',
    'media/fullscreen_close.svg',
    'media/fullscreen_open.svg',
    'media/hide_obj.svg',
    'media/info.png',
    'media/manifest.json',
    'media/safari-pinned-tab.svg',
    'media/screen.svg',
    'media/show_obj.svg',
    'media/unexplode.svg',
    'media/warning_AR_unavailable.png',
    'media/warning_could_not_enter_AR.png',
    'media/w_1.png',
    'media/w_2.png',
    'media/w_3.png',
    'media/w_4.png',
    'media/sound/pop.mp3',
    'media/sound/wood.wav',
];

const cacheName = () => {
    return `${CACHE_PREFIX}-${CACHE_HASH}-${CACHE_VERSION}`;
}

self.addEventListener('install', (event) => {
    event.waitUntil(caches.open(cacheName()).then(cache => {
        return cache.addAll(ASSETS);
    }));
});

const deleteCache = async (key) => {
    await caches.delete(key);
};

const deleteOldCaches = async () => {
    const cacheKeepList = [cacheName()];
    const keyList = await caches.keys();
    const cachesToDelete = keyList.filter((key) => {
        return (key.includes(CACHE_HASH) && !cacheKeepList.includes(key));
    });
    await Promise.all(cachesToDelete.map(deleteCache));
};

self.addEventListener('activate', (event) => {
    event.waitUntil(deleteOldCaches());
});

const handleCached = async (request) => {
    const responseFromCache = await caches.match(request);
    if (responseFromCache)
        return responseFromCache;
    return fetch(request);
};

self.addEventListener('fetch', (event) => {
    event.respondWith(handleCached(event.request));
});
