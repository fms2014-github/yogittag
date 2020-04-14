<template>
    <div>
        <b-table stacked :items="items"></b-table>
    </div>
</template>

<script>
export default {
    props: {
        items: {
            type: Array,
            default: function () {
                return [
                    {
                        Branch: null,
                        Area: null,
                        Tel: null,
                        Address: null,
                    },
                ]
            },
        },
    },
}
</script>
